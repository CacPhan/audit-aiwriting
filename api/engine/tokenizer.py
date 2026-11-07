"""
Vietnamese Sentence & Clause Splitter, Unified 8-Field Economics Term Masker,
and Academic / Econometric / Legal Context Classifiers.
Supports both NFC and NFD decomposed Vietnamese Unicode transparently.
"""

import re
import unicodedata
from typing import Any, Dict, List, Tuple
from api.engine.lexicon import UNIFIED_ECONOMICS_TERMS

# Common Vietnamese & academic abbreviations (including spaced forms like "PGS. TS.")
_ABBREVIATION_PATTERNS = [
    r"(?:PGS|GS)\.\s*TS\.",
    r"(?:ThS|TS|PGS|GS)\.\s*(?:BS|DS|KTS|NCS)\.",
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
    r"KTS\.",
    r"NCS\.",
    r"TP\.HCM",
    r"Tp\.HCM",
    r"(?:TP|Tp)\.\s*(?:Hồ\s+Chí\s+Minh|Hà\s+Nội|Đà\s+Nẵng|Hải\s+Phòng|Cần\s+Thơ|Huế|Nha\s+Trang|Vũng\s+Tàu|Biên\s+Hòa|Thủ\s+Đức)",
    r"TP\.",
    r"Tp\.",
    r"TW\.",
    r"TƯ\.",
    r"T\.Ư",
    r"NXB\.",
    r"Nxb\.",
    r"Stt\.",
    r"STT\.",
    r"tr\.",
    r"Tr\.",
    r"tập\.",
    r"Tập\.",
    r"Ch\.",
    r"Đ\.",
    r"Kh\.",
    r"Sig\.",
    r"Std\.",
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
    re.IGNORECASE | re.UNICODE,
)

# DOI or URL patterns containing periods
_URL_OR_DOI_REGEX = re.compile(
    r"(?:doi:\s*10\.\d{4,9}/[-._;()/:A-Za-z0-9]+|https?://[^\s)]+|utm_source=[A-Za-z0-9._-]+)",
    re.IGNORECASE,
)

# Section numbering at the start of text or after newline/space: e.g., "1.1.", "2.3.1."
_SECTION_NUM_REGEX = re.compile(r"(?:^|(?<=\s))\d+(?:\.\d+)+\.")

_DOT_PLACEHOLDER = "\uE000"

WORD_TOKEN_REGEX = re.compile(r"[^\s.,;:!?()\[\]{}'\"“”‘’—–/\\]+")

# Academic citation regex: (Nguyen & Tran, 2024), (Parasuraman và cộng sự, 1988), Theo X (2022), [12]
ACADEMIC_CITATION_REGEX = re.compile(
    r"(?:"
    r"\([A-ZÀ-Ỹ][^()\d]{1,60},?\s*(?:19|20)\d{2}[a-z]?(?:\s*[;,]\s*[^()]{1,60})*\)"
    r"|\b[A-ZÀ-Ỹ][a-zà-ỹ]+(?:\s+[A-ZÀ-Ỹa-zà-ỹ&]+){0,5}\s+(?:và\s+cộng\s+sự\s+|et\s+al\.?\s*)?\((?:19|20)\d{2}[a-z]?\)"
    r"|\[\d{1,3}(?:\s*[,–-]\s*\d{1,3})*\]"
    r")",
    re.UNICODE,
)

# Quantitative evidence regex: %, currency, econometric statistics, dates/tables
QUANTITATIVE_EVIDENCE_REGEX = re.compile(
    r"(?:"
    r"\b\d+(?:[.,]\d+)?\s*(?:%|phần\s+trăm|điểm\s+phần\s+trăm|bps|tỷ|triệu|nghìn|ngàn|đồng|VNĐ|VND|USD|lần|năm|tháng|quý|ngày|giờ|người|khách\s+hàng|nhân\s+viên|doanh\s+nghiệp|chi\s+nhánh|mẫu|quan\s+sát|biến|nhân\s+tố)\b"
    r"|\b(?:β|beta|p-value|p|Sig\.?|R2|R²|Adjusted\s+R2|t-stat|F-stat|VIF|KMO|Cronbach(?:'s)?\s+Alpha|Eigenvalue|AVE|CR)\s*(?:=|<|>|≤|≥|đạt|bằng|là)\s*[-+]?\d+(?:[.,]\d+)?"
    r"|\b(?:Quý\s+(?:I|II|III|IV|1|2|3|4)|giai\s+đoạn\s+20\d{2}\s*[-–]\s*20\d{2}|năm\s+20\d{2})\b"
    r"|\b(?:Bảng|Hình|Biểu\s+đồ|Sơ\s+đồ)\s+\d+(?:[.,]\d+)?"
    r")",
    re.IGNORECASE | re.UNICODE,
)

# Econometric / Statistical reporting regex (SPSS, AMOS, SmartPLS, Stata, EViews)
ECONOMETRIC_REPORTING_REGEX = re.compile(
    r"(?:"
    r"\b(?:Cronbach(?:'s)?\s+Alpha|hệ\s+số\s+KMO|kiểm\s+định\s+Bartlett|phân\s+tích\s+nhân\s+tố\s+(?:khám\s+phá|khẳng\s+định)|EFA|CFA|SEM|OLS|FEM|REM|GMM|Hausman|Breusch-Pagan|White|Durbin-Watson|đa\s+cộng\s+tuyến|VIF|phương\s+sai\s+trích|tương\s+quan\s+biến\s+tổng|hệ\s+số\s+tải\s+nhân\s+tố|Factor\s+Loading|Eigenvalue)\b"
    r"|\b(?:Giả\s+thuyết\s+H\d+|biến\s+(?:phụ\s+thuộc|độc\s+lập|quan\s+sát|kiểm\s+soát|trung\s+gian|điều\s+tiết)|mức\s+ý\s+nghĩa\s+thống\s+kê\s+\d+%?|p-value\s*[<>=]|Sig\.\s*[<>=])\b"
    r"|\bđược\s+(?:cấu\s+thành|giải\s+thích|đo\s+lường|đại\s+diện|ước\s+lượng|kiểm\s+định)\s+bởi\s+(?:\d+\s+)?(?:biến|nhân\s+tố|thang\s+đo|mô\s+hình|phương\s+pháp)\b"
    r")",
    re.IGNORECASE | re.UNICODE,
)

# Legal & Regulatory citation regex
LEGAL_CITATION_REGEX = re.compile(
    r"\b(?:Theo\s+|Căn\s+cứ\s+|Tại\s+|Quy\s+định\s+tại\s+)?"
    r"(?:Điều\s+\d+|Khoản\s+\d+|Điểm\s+[a-zđ]\b|Luật\s+(?:Các\s+tổ\s+chức\s+tín\s+dụng|Doanh\s+nghiệp|Kế\s+toán|Kiểm\s+toán|Chứng\s+khoán|Đầu\s+tư|Thương\s+mại|Lao\s+động|Bảo\s+hiểm|Thuế)"
    r"|Nghị\s+định\s+(?:số\s+)?\d+\/\d{4}\/NĐ-CP"
    r"|Thông\s+tư\s+(?:số\s+)?\d+\/\d{4}\/TT-[A-ZĐ]+"
    r"|Quyết\s+định\s+(?:số\s+)?\d+\/\d{4}\/QĐ-[A-ZĐ]+"
    r"|Chuẩn\s+mực\s+(?:kế\s+toán|kiểm\s+toán|báo\s+cáo\s+tài\s+chính)\s+(?:Việt\s+Nam\s+|quốc\s+tế\s+)?(?:VAS|VSA|IAS|IFRS|Basel\s+(?:I|II|III)))",
    re.IGNORECASE | re.UNICODE,
)

# Thesis structure outline paragraph regex (in MỞ ĐẦU)
THESIS_OUTLINE_PARAGRAPH_REGEX = re.compile(
    r"(?:kết\s+cấu\s+của\s+(?:khóa\s+luận|luận\s+văn|đề\s+tài|báo\s+cáo|chuyên\s+đề)|ngoài\s+phần\s+mở\s+đầu[\s\S]{0,80}(?:gồm|chia\s+làm|kết\s+cấu\s+thành)\s+\d+\s+(?:chương|phần))"
    r"|(?:\bChương\s+1\b[\s\S]{10,350}\bChương\s+2\b[\s\S]{10,350}\bChương\s+3\b)",
    re.IGNORECASE | re.UNICODE,
)


def count_vietnamese_words(text: str) -> int:
    """Counts Vietnamese syllables/tokens (separated by whitespace, stripping punctuation-only tokens)."""
    norm = unicodedata.normalize("NFC", text or "")
    tokens = [
        tok.strip(".,;:!?()[]{}'\"“”‘’—–-")
        for tok in norm.strip().split()
    ]
    return sum(1 for t in tokens if t)


def extract_words(text: str) -> List[str]:
    """Extracts lowercase word tokens for lexical overlap and triad analysis."""
    if not text:
        return []
    norm = unicodedata.normalize("NFC", text)
    return [w.lower() for w in WORD_TOKEN_REGEX.findall(norm)]


def split_vietnamese_sentences(text: str) -> List[Dict[str, Any]]:
    """
    Splits Vietnamese academic prose into sentences with character offsets and word counts,
    preserving academic titles (PGS.TS., PGS. TS., TS., ThS.), geographic names (TP.HCM, Tp. Hà Nội),
    legal codes (02/2023/TT-NHNN, NĐ-CP), DOIs, and decimal/thousand numbers (3.45%, 14,5%, 1.200).
    """
    if not text or not text.strip():
        return []

    text = unicodedata.normalize("NFC", text)
    working = list(text)

    def _mask_dots_in_match(match: re.Match) -> None:
        for idx in range(match.start(), match.end()):
            if working[idx] == ".":
                working[idx] = _DOT_PLACEHOLDER

    # 1. Protect URLs and DOIs
    for m in _URL_OR_DOI_REGEX.finditer(text):
        _mask_dots_in_match(m)

    # 2. Protect known Vietnamese and academic abbreviations (including spaced forms)
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

    sentences: List[Dict[str, Any]] = []
    boundary_pattern = re.compile(r"[.!?…]+[\"”’)\]]*(?=\s+|$)")

    last_idx = 0
    for match in boundary_pattern.finditer(masked_str):
        end_idx = match.end()
        raw_slice = text[last_idx:end_idx]
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


def split_into_clauses(sentence_text: str, base_offset: int = 0) -> List[Dict[str, Any]]:
    """
    Splits a sentence into clauses at top-level commas, semicolons, colons, and em/en-dashes
    (ignoring commas inside parentheses or decimal numbers like 14,5%).
    Used for Clause-Vector Syntactic Isomorphism (SYN-01) and Clause-Bounded Analysis.
    """
    if not sentence_text or not sentence_text.strip():
        return []

    clauses: List[Dict[str, Any]] = []
    paren_depth = 0
    last_pos = 0
    n = len(sentence_text)

    for i, ch in enumerate(sentence_text):
        if ch in "([“":
            paren_depth += 1
        elif ch in ")]”":
            paren_depth = max(0, paren_depth - 1)
        elif paren_depth == 0 and ch in ",;:—–":
            is_decimal_comma = (
                ch == ","
                and i > 0
                and i + 1 < n
                and sentence_text[i - 1].isdigit()
                and sentence_text[i + 1].isdigit()
            )
            if not is_decimal_comma:
                raw_clause = sentence_text[last_pos:i]
                stripped = raw_clause.strip()
                if stripped:
                    lead = len(raw_clause) - len(raw_clause.lstrip())
                    c_start = base_offset + last_pos + lead
                    c_end = c_start + len(stripped)
                    wc = count_vietnamese_words(stripped)
                    if wc > 0:
                        clauses.append(
                            {
                                "text": stripped,
                                "start": c_start,
                                "end": c_end,
                                "word_count": wc,
                            }
                        )
                last_pos = i + 1

    if last_pos < n:
        raw_tail = sentence_text[last_pos:]
        stripped_tail = raw_tail.strip(" .!?…")
        if stripped_tail:
            lead = len(raw_tail) - len(raw_tail.lstrip())
            c_start = base_offset + last_pos + lead
            c_end = c_start + len(stripped_tail)
            wc = count_vietnamese_words(stripped_tail)
            if wc > 0:
                clauses.append(
                    {
                        "text": stripped_tail,
                        "start": c_start,
                        "end": c_end,
                        "word_count": wc,
                    }
                )

    return clauses


def mask_protected_economics_terms(text: str) -> Tuple[str, List[Dict[str, Any]]]:
    """
    Finds and masks all 8-field Economics & Econometric technical terms using longest-match-first
    so they are never falsely penalized as Sino-Vietnamese abstract bloat (LEX-VN-01)
    or nominalization bloat (SYN-VN-03).
    """
    if not text:
        return "", []

    text = unicodedata.normalize("NFC", text)
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


def has_academic_citation(text: str) -> bool:
    """Checks if a sentence or paragraph contains a formal academic citation (Author, Year) or [Number]."""
    if not text:
        return False
    return bool(ACADEMIC_CITATION_REGEX.search(unicodedata.normalize("NFC", text)))


def has_quantitative_evidence(text: str) -> bool:
    """Checks if a sentence or paragraph contains empirical numbers, %, currency, or econometric coefficients."""
    if not text:
        return False
    return bool(QUANTITATIVE_EVIDENCE_REGEX.search(unicodedata.normalize("NFC", text)))


def is_econometric_or_statistical_sentence(text: str) -> bool:
    """Checks if a sentence reports econometric/statistical test results (EFA, CFA, SEM, OLS, FEM, REM, GMM)."""
    if not text:
        return False
    return bool(ECONOMETRIC_REPORTING_REGEX.search(unicodedata.normalize("NFC", text)))


def is_legal_citation_sentence(text: str) -> bool:
    """Checks if a sentence directly cites a Vietnamese legal statute, decree, circular, or accounting standard."""
    if not text:
        return False
    return bool(LEGAL_CITATION_REGEX.search(unicodedata.normalize("NFC", text)))


def is_thesis_outline_paragraph(text: str) -> bool:
    """Checks if a paragraph is the standard thesis chapter outline summary in the Introduction."""
    if not text:
        return False
    return bool(THESIS_OUTLINE_PARAGRAPH_REGEX.search(unicodedata.normalize("NFC", text)))
