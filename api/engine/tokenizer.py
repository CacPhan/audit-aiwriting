"""
Vietnamese Sentence Splitter & Unified 8-Field Economics Term Masker.
Designed for lightweight Vercel Serverless execution (<5MB, zero heavy NLP dependencies).
"""

import re
from typing import Dict, List, Tuple, Any
from api.engine.lexicon import UNIFIED_ECONOMICS_TERMS

# Common Vietnamese & academic abbreviations that contain periods and must NOT split sentences
_ABBREVIATION_PATTERNS = [
    r"PGS\.TS\.",
    r"GS\.TS\.",
    r"PGS\.",
    r"GS\.",
    r"TS\.",
    r"ThS\.",
    r"CN\.",
    r"KS\.",
    r"BS\.",
    r"DS\.",
    r"TP\.HCM",
    r"Tp\.HCM",
    r"TP\.",
    r"Tp\.",
    r"TW\.",
    r"TƯ\.",
    r"NXB\.",
    r"Nxb\.",
    r"Stt\.",
    r"STT\.",
    r"tr\.",
    r"Tr\.",
    r"tập\.",
    r"v\.v\.",
    r"et\s+al\.",
    r"e\.g\.",
    r"i\.e\.",
    r"vs\.",
    r"Dr\.",
    r"Prof\.",
    r"Mr\.",
    r"Ms\.",
    r"Mrs\.",
    r"Fig\.",
    r"Eq\.",
    r"No\.",
    r"Vol\.",
    r"pp\.",
]

_ABBREV_REGEX = re.compile(
    r"(" + "|".join(_ABBREVIATION_PATTERNS) + r")",
    re.IGNORECASE,
)

# Decimal / thousand separator dots inside numbers: e.g. 3.45%, 1.200
_NUMBER_DOT_REGEX = re.compile(r"(?<=\d)\.(?=\d)")

# DOI or URL patterns containing periods
_URL_OR_DOI_REGEX = re.compile(
    r"(?:doi:\s*10\.\d{4,9}/[-._;()/:A-Za-z0-9]+|https?://[^\s)]+|utm_source=[A-Za-z0-9._-]+)",
    re.IGNORECASE,
)

# Section numbering at the start of text or after newline: e.g., "1.1.", "2.3.1."
_SECTION_NUM_REGEX = re.compile(r"(?:^|(?<=\s))\d+(?:\.\d+)+\.")

_DOT_PLACEHOLDER = "\uE000"


def count_vietnamese_words(text: str) -> int:
    """Counts Vietnamese syllables/tokens (separated by whitespace, stripping punctuation-only tokens)."""
    tokens = [
        tok.strip(".,;:!?()[]{}'\"“”‘’—–-")
        for tok in text.strip().split()
    ]
    return sum(1 for t in tokens if t)


def split_vietnamese_sentences(text: str) -> List[Dict[str, Any]]:
    """
    Splits Vietnamese academic prose into sentences with character offsets and word counts,
    preserving academic titles (PGS.TS., TS., ThS.), geographic names (TP.HCM),
    legal codes (02/2023/TT-NHNN), DOIs, and decimal/thousand numbers (3.45%, 1.200).
    """
    if not text or not text.strip():
        return []

    working = list(text)

    def _mask_dots_in_match(match: re.Match) -> None:
        for idx in range(match.start(), match.end()):
            if working[idx] == ".":
                working[idx] = _DOT_PLACEHOLDER

    # 1. Protect URLs and DOIs
    for m in _URL_OR_DOI_REGEX.finditer(text):
        _mask_dots_in_match(m)

    # 2. Protect known Vietnamese and academic abbreviations
    for m in _ABBREV_REGEX.finditer(text):
        _mask_dots_in_match(m)

    # 3. Protect section numbers like 1.1. or 2.1.
    for m in _SECTION_NUM_REGEX.finditer(text):
        _mask_dots_in_match(m)

    # 4. Protect single-letter initials like "Nguyễn Văn A." when followed by "(" or lowercase
    for m in re.finditer(r"\b[A-ZĐ]\.(?=\s*[\(,a-zà-ỹ])", text):
        _mask_dots_in_match(m)

    # 5. Protect dots between digits (e.g., 3.45%, 1.200)
    for m in re.finditer(r"(?<=\d)\.(?=\d)", text):
        _mask_dots_in_match(m)

    masked_str = "".join(working)

    # Split on sentence-ending punctuation (. ! ? …) followed by whitespace or end of string
    # Keep track of exact character spans in original `text`
    sentences: List[Dict[str, Any]] = []
    boundary_pattern = re.compile(r"[.!?…]+[\"”’)\]]*(?=\s+|$)")

    last_idx = 0
    for match in boundary_pattern.finditer(masked_str):
        end_idx = match.end()
        raw_slice = text[last_idx:end_idx]
        # Trim leading whitespace while adjusting start offset
        leading_ws = len(raw_slice) - len(raw_slice.lstrip())
        start_offset = last_idx + leading_ws
        trimmed = text[start_offset:end_idx].rstrip()
        if trimmed:
            actual_end = start_offset + len(trimmed)
            sentences.append(
                {
                    "text": trimmed,
                    "start": start_offset,
                    "end": actual_end,
                    "word_count": count_vietnamese_words(trimmed),
                }
            )
        last_idx = end_idx

    # Remaining tail if text did not end with punctuation
    if last_idx < len(text):
        tail_slice = text[last_idx:]
        leading_ws = len(tail_slice) - len(tail_slice.lstrip())
        start_offset = last_idx + leading_ws
        trimmed = text[start_offset:].rstrip()
        if trimmed:
            actual_end = start_offset + len(trimmed)
            sentences.append(
                {
                    "text": trimmed,
                    "start": start_offset,
                    "end": actual_end,
                    "word_count": count_vietnamese_words(trimmed),
                }
            )

    return sentences


def mask_protected_economics_terms(text: str) -> Tuple[str, List[Dict[str, Any]]]:
    """
    Finds and masks all 8-field Economics technical terms using longest-match-first
    so they are never falsely penalized as Sino-Vietnamese abstract bloat (LEX-VN-01)
    or nominalization bloat (SYN-VN-03).

    Returns:
      - masked_text: string of identical length where matched characters (except spaces)
        are replaced with '§'
      - spans: list of dicts {"term": str, "canonical": str, "start": int, "end": int}
    """
    if not text:
        return "", []

    chars = list(text)
    occupied = [False] * len(text)
    spans: List[Dict[str, Any]] = []

    lower_text = text.lower()

    for canonical in UNIFIED_ECONOMICS_TERMS:
        pattern = re.compile(
            r"(?<![a-zA-ZÀ-ỹ0-9_])" + re.escape(canonical) + r"(?![a-zA-ZÀ-ỹ0-9_])",
            re.IGNORECASE,
        )
        for m in pattern.finditer(lower_text):
            s, e = m.start(), m.end()
            if any(occupied[s:e]):
                continue
            for i in range(s, e):
                occupied[i] = True
                if not chars[i].isspace():
                    chars[i] = "§"
            spans.append(
                {
                    "term": text[s:e],
                    "canonical": canonical,
                    "start": s,
                    "end": e,
                }
            )

    spans.sort(key=lambda item: item["start"])
    return "".join(chars), spans
