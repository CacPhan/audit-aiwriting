"""
Single-Source 26-Sign Python Rule Engine & 6 Quantitative Metrics Calculator
(CV_L, ISI, OPR, SVCI, SICD, BCR).
Upgraded with Multi-Match Collection (re.finditer), Clause-Bounded Sino-Vietnamese Analysis,
Clause-Vector Syntactic Isomorphism, Jaccard Echoic Conclusion Detection,
General Triadic Coordination Detection, Econometric/Legal Context Exemptions,
and Contextual Editorial Rewrite Suggestions.
"""

import math
import re
import unicodedata
from typing import Any, Dict, List, Optional, Tuple
from api.engine.lexicon import (
    RULE_METADATA,
    SINO_VIETNAMESE_ABSTRACT_SYLLABLES,
    SYNONYM_CYCLE_GROUPS,
    build_contextual_suggestion,
)
from api.engine.tokenizer import (
    count_vietnamese_words,
    extract_words,
    has_academic_citation,
    has_quantitative_evidence,
    is_econometric_or_statistical_sentence,
    is_legal_citation_sentence,
    is_thesis_outline_paragraph,
    mask_protected_economics_terms,
    split_into_clauses,
    split_vietnamese_sentences,
)

# Stopwords for Jaccard content-word overlap calculation (DIS-02)
_VIETNAMESE_STOPWORDS = {
    "và", "của", "các", "những", "trong", "cho", "với", "được", "là", "có", "để", "tại",
    "về", "từ", "đến", "như", "khi", "một", "này", "đó", "trên", "theo", "do", "bởi",
    "sự", "việc", "quá", "trình", "hoạt", "động", "cũng", "đã", "đang", "sẽ", "cần",
    "phải", "rằng", "thì", "mà", "nhưng", "hay", "hoặc", "nếu", "vì", "nên", "qua",
    "nhằm", "góp", "phần", "giúp", "tạo", "ra", "lên", "xuống", "vào", "hơn", "nhất",
    "rất", "khá", "nhiều", "ít", "mọi", "tất", "cả", "cùng", "đều", "chỉ", "tóm", "lại",
    "nhìn", "chung", "vậy", "thể", "nói", "thấy", "điều", "chính",
}

# Legitimate econometric / statistical / legal passive verbs exempted from SYN-VN-03
_LEGITIMATE_ACADEMIC_PASSIVE_VERBS = re.compile(
    r"^(?:cấu\s+thành|giải\s+thích|đo\s+lường|đại\s+diện|ước\s+lượng|kiểm\s+định|phản\s+ánh|quy\s+định|ban\s+hành|bảo\s+đảm|đảm\s+bảo|chi\s+phối|tính\s+toán|xác\s+định)$",
    re.IGNORECASE | re.UNICODE,
)


def _find_sentence_containing(sentences: List[Dict[str, Any]], start: int, end: int) -> str:
    """Finds the sentence text containing the character span [start, end]."""
    for s in sentences:
        if s["start"] <= start and end <= s["end"] + 2:
            return s["text"]
        if not (end <= s["start"] or start >= s["end"]):
            return s["text"]
    return ""


def _make_flag(
    rule_id: str,
    para_index: int,
    flag_index: int,
    start: int,
    end: int,
    full_text: str,
    sentence_text: str = "",
    custom_suggestion: Optional[str] = None,
    custom_title: Optional[str] = None,
    custom_reason: Optional[str] = None,
) -> Dict[str, Any]:
    meta = RULE_METADATA[rule_id]
    safe_start = max(0, min(start, len(full_text)))
    safe_end = max(safe_start, min(end, len(full_text)))
    excerpt = full_text[safe_start:safe_end].strip()
    if not excerpt:
        excerpt = full_text[: min(140, len(full_text))].strip()

    suggestion = (
        custom_suggestion
        if custom_suggestion
        else build_contextual_suggestion(rule_id, excerpt, sentence_text)
    )

    return {
        "id": f"p{para_index}-f{flag_index}",
        "ruleId": rule_id,
        "ruleName": meta["name"],
        "category": meta["category"],
        "priorityStage": meta["priority_stage"],
        "severity": meta["severity"],
        "severityLabel": meta["severityLabel"],
        "title": custom_title or meta["userTitle"],
        "excerpt": f'"{excerpt}"',
        "matchedText": excerpt,
        "reason": custom_reason or meta["userReason"],
        "suggestion": suggestion,
        "start": safe_start,
        "end": safe_end,
    }


def _find_sino_vietnamese_chains(
    masked_text: str, min_run: int = 7
) -> List[Tuple[int, int, int]]:
    """
    Finds ALL contiguous runs of Sino-Vietnamese abstract syllables (>= min_run syllables)
    outside masked 8-field Economics terms ('§').
    CRITICAL INVARIANT: Immediately resets cur_run = 0 if ANY punctuation character
    (',', '.', ';', ':', '—', '–', '()', etc.) appears between two tokens, preventing
    false-positive bridging across clauses or sentences!
    """
    token_iter = list(re.finditer(r"[^\s.,;:!?()\[\]{}'\"“”‘’—–/\\]+", masked_text))
    chains: List[Tuple[int, int, int]] = []

    cur_run = 0
    cur_start = 0
    cur_end = 0
    prev_end = -1

    for tok_match in token_iter:
        tok_str = tok_match.group(0).lower()

        # Check if punctuation occurred between previous token and current token
        if prev_end != -1:
            between = masked_text[prev_end : tok_match.start()]
            if between.strip() != "":
                # Clause or sentence boundary encountered -> close current chain and reset
                if cur_run >= min_run:
                    chains.append((cur_start, cur_end, cur_run))
                cur_run = 0

        if "§" in tok_str:
            if cur_run >= min_run:
                chains.append((cur_start, cur_end, cur_run))
            cur_run = 0
            prev_end = tok_match.end()
            continue

        if tok_str in SINO_VIETNAMESE_ABSTRACT_SYLLABLES:
            if cur_run == 0:
                cur_start = tok_match.start()
            cur_run += 1
            cur_end = tok_match.end()
        else:
            if cur_run >= min_run:
                chains.append((cur_start, cur_end, cur_run))
            cur_run = 0

        prev_end = tok_match.end()

    if cur_run >= min_run:
        chains.append((cur_start, cur_end, cur_run))

    return chains


def _find_max_sino_vietnamese_run(
    masked_text: str, original_text: str = ""
) -> Tuple[int, Optional[Tuple[int, int]]]:
    """
    Calculates SVCI (longest contiguous clause-bounded run of Sino-Vietnamese abstract syllables
    outside masked 8-field Economics terms).
    """
    chains = _find_sino_vietnamese_chains(masked_text, min_run=1)
    if not chains:
        return 0, None
    best = max(chains, key=lambda item: item[2])
    return best[2], (best[0], best[1])


def _compute_content_word_jaccard(sent_a: str, sent_b: str) -> float:
    """Computes Jaccard similarity of content words (excluding Vietnamese stopwords) between two sentences."""
    words_a = {
        w
        for w in extract_words(sent_a)
        if len(w) >= 2 and w not in _VIETNAMESE_STOPWORDS and not w.isdigit()
    }
    words_b = {
        w
        for w in extract_words(sent_b)
        if len(w) >= 2 and w not in _VIETNAMESE_STOPWORDS and not w.isdigit()
    }
    if len(words_a) < 4 or len(words_b) < 4:
        return 0.0
    intersection = words_a.intersection(words_b)
    union = words_a.union(words_b)
    return len(intersection) / len(union) if union else 0.0


def audit_paragraph(text: str, index: int = 0) -> Dict[str, Any]:
    """
    Audits a single paragraph against all 26 AI writing signs and computes
    the 6 quantitative metrics: CV_L, ISI, OPR, SVCI, SICD, BCR.
    """
    if not text or not text.strip():
        return {
            "index": index,
            "text": text or "",
            "wordCount": 0,
            "sentenceCount": 0,
            "metrics": {
                "cvLength": 0.0,
                "deltaLength": 0,
                "isi": 0.0,
                "opr": 0.0,
                "svci": 0,
                "sicd": 0.0,
                "bcr": 0.0,
            },
            "flags": [],
            "protectedTerms": [],
            "aiStyleScore": 0,
        }

    text = unicodedata.normalize("NFC", text)
    sentences = split_vietnamese_sentences(text)
    masked_text, protected_spans = mask_protected_economics_terms(text)
    total_words = max(1, count_vietnamese_words(text))
    n_sent = len(sentences)

    is_outline_para = is_thesis_outline_paragraph(text)
    econometric_sent_count = sum(
        1 for s in sentences if is_econometric_or_statistical_sentence(s["text"])
    )
    is_heavily_econometric_para = (
        n_sent > 0 and (econometric_sent_count / n_sent) >= 0.5
    )

    flags: List[Dict[str, Any]] = []
    flag_counter = 1

    def add_flag(
        rule_id: str,
        start: int,
        end: int,
        custom_suggestion: Optional[str] = None,
        custom_title: Optional[str] = None,
        custom_reason: Optional[str] = None,
    ) -> None:
        nonlocal flag_counter
        s_idx = max(0, min(start, len(text)))
        e_idx = max(s_idx, min(end, len(text)))
        if e_idx <= s_idx:
            return
        # Avoid overlapping spans for the same ruleId while allowing multiple distinct matches per paragraph
        for existing in flags:
            if existing["ruleId"] == rule_id and not (
                e_idx <= existing["start"] or s_idx >= existing["end"]
            ):
                return
        sent_ctx = _find_sentence_containing(sentences, s_idx, e_idx)
        flags.append(
            _make_flag(
                rule_id,
                index,
                flag_counter,
                s_idx,
                e_idx,
                text,
                sentence_text=sent_ctx,
                custom_suggestion=custom_suggestion,
                custom_title=custom_title,
                custom_reason=custom_reason,
            )
        )
        flag_counter += 1

    # -------------------------------------------------------------------------
    # METRIC 1 & RHY-01: Sentence Length Coefficient of Variation (CV_L)
    # Only evaluated when paragraph has >= 4 sentences and is not a thesis outline / econometric table summary
    # -------------------------------------------------------------------------
    lengths = [s["word_count"] for s in sentences if s["word_count"] > 0]
    if len(lengths) >= 4:
        mean_l = sum(lengths) / len(lengths)
        variance_l = sum((l - mean_l) ** 2 for l in lengths) / len(lengths)
        std_l = math.sqrt(variance_l)
        cv_length = round(std_l / mean_l, 4) if mean_l > 0 else 0.0
        delta_length = max(lengths) - min(lengths)

        if not is_outline_para and not is_heavily_econometric_para:
            if cv_length < 0.18 or delta_length < 8:
                add_flag(
                    "RHY-01",
                    sentences[0]["start"],
                    sentences[-1]["end"],
                    custom_suggestion=(
                        "Gộp 2 câu có quan hệ nhân quả hoặc tương phản thành câu phức (dùng dấu hai chấm ':' "
                        "hoặc cặp từ 'trong khi... thì...') và rút gọn câu mở đoạn thành câu đơn ngắn gọn."
                    ),
                )
    else:
        if len(lengths) >= 2:
            mean_l = sum(lengths) / len(lengths)
            std_l = math.sqrt(sum((l - mean_l) ** 2 for l in lengths) / len(lengths))
            cv_length = round(std_l / mean_l, 4) if mean_l > 0 else 0.35
            delta_length = max(lengths) - min(lengths)
        else:
            cv_length = 0.35
            delta_length = 0

    # -------------------------------------------------------------------------
    # P0: FOR-01 (Forensic Artifacts, Leaked Citation Tags, Hallucinated DOIs) — Multi-match
    # -------------------------------------------------------------------------
    for_patterns = [
        r"\([^)]*contentReference\[oaicite[^\)]*\)",
        r":?contentReference\[oaicite[^\]]*\](?:\{index=\d+\})?",
        r"\boaicite:\d+\b",
        r"\bturn\d+(?:search|view|news)\d+\b",
        r"\[span_\d+\]",
        r"grok_card",
        r"utm_source=chatgpt(?:\.com)?",
        r"\[attached_file:[^\]]+\]",
        r":::writing",
        r"Chắc chắn rồi!\s*Dưới đây là[^.!?\n]*[.!?]?",
        r"Dưới đây là (?:phần trình bày|bản phân tích|nội dung chi tiết)[^.!?\n]*[.!?]?",
        r"Hy vọng (?:thông tin|phần trình bày|bài viết) này (?:sẽ )?(?:hữu ích|giúp ích)[^.!?\n]*[.!?]?",
        r"Nếu bạn cần (?:chỉnh sửa|bổ sung|mở rộng)[^.!?\n]*hãy cho tôi biết[^.!?\n]*[.!?]?",
        r"\[(?:Điền|Chèn|Thêm|Tên) [^\]]{2,45}\]",
        r"\((?:Nguyễn Văn A|Trần Văn B|Author Name|Tác giả),?\s*(?:202X|20XX|19XX|YYYY)\)",
        r"doi:\s*10\.\d{4,9}/[^\s)]*(?:9999\d*|xyz123|test)",
    ]
    for pat in for_patterns:
        for m in re.finditer(pat, text, re.IGNORECASE):
            add_flag("FOR-01", m.start(), m.end())

    # -------------------------------------------------------------------------
    # FMT-01: Mechanical Formatting (Inline bold bullet headers, excessive em-dashes, markdown bold, emojis)
    # -------------------------------------------------------------------------
    for m in re.finditer(r"(?:^|\n)\s*[-*•]\s*(?:\*\*[^*]+\*\*|[A-ZÀ-Ỹ][^:\n]{2,35})\s*:", text):
        add_flag("FMT-01", m.start(), m.end())

    if text.count("—") >= 2:
        for m in re.finditer(r"\s*—\s*", text):
            add_flag("FMT-01", max(0, m.start() - 12), min(len(text), m.end() + 25))

    for m in re.finditer(r"\*\*[^*\n]{2,60}\*\*|[📌💡🚀✅🔹✨📊🔥🎯🌟]", text):
        add_flag("FMT-01", m.start(), m.end())

    # -------------------------------------------------------------------------
    # METRIC 5 & DIS-01, DIS-02, DIS-03, DIS-04: Discourse & Paragraph Framing
    # -------------------------------------------------------------------------
    connective_openers = (
        r"^(?:Cụ thể|Tuy nhiên|Do đó|Hơn nữa|Thêm vào đó|Bên cạnh đó|"
        r"Ngoài ra|Đáng chú ý là|Thật vậy|Ngược lại|Vì vậy|Như vậy|Mặt khác|Đồng thời|Không những vậy|Chính vì vậy)\s*,"
    )
    conn_matches = []
    for s in sentences:
        m = re.match(connective_openers, s["text"], re.IGNORECASE)
        if m:
            conn_matches.append((s, m))

    sicd = round(len(conn_matches) / max(1, n_sent), 4)
    if len(conn_matches) >= 2 and sicd > 0.25:
        # Highlight ALL mechanical sentence-initial connectives in the paragraph
        for s_item, m_item in conn_matches:
            add_flag(
                "DIS-03",
                s_item["start"],
                s_item["start"] + m_item.end(),
            )

    # DIS-01: 4-step Boxed Paragraph ([Topic] -> [Cụ thể,] -> [Tuy nhiên,] -> [Do đó,/Như vậy,/Tóm lại,])
    bcr = 0.0
    if n_sent >= 4 and not is_outline_para:
        s1_txt = sentences[1]["text"]
        s2_txt = sentences[2]["text"]
        s_last = sentences[-1]
        has_elab = bool(re.match(r"^(?:Cụ thể|Thực tế|Theo đó|Trước hết)\s*,", s1_txt, re.IGNORECASE))
        has_pivot = bool(re.match(r"^(?:Tuy nhiên|Song|Mặt khác|Ngược lại|Bên cạnh đó)\s*,", s2_txt, re.IGNORECASE))
        has_box_close = bool(
            re.match(
                r"^(?:Do đó|Như vậy|Tóm lại|Nhìn chung|Vì vậy|Chính vì vậy|Có thể nói|Từ đó cho thấy|Qua đó cho thấy)\s*,?",
                s_last["text"],
                re.IGNORECASE,
            )
            or re.search(
                r"(?:để đảm bảo sự phát triển bền vững|phát triển bền vững trong tương lai|điều này khẳng định tầm quan trọng của|qua đó tạo nền tảng vững chắc cho)",
                s_last["text"],
                re.IGNORECASE,
            )
        )
        if (
            (has_elab and has_pivot and has_box_close)
            or (len(conn_matches) >= 3 and has_box_close)
            or bool(
                re.match(
                    r"^(?:Tóm lại|Nhìn chung|Có thể nói|Từ đó cho thấy|Tựu trung lại)\s*,",
                    s_last["text"],
                    re.IGNORECASE,
                )
            )
        ):
            bcr = 1.0
            add_flag("DIS-01", s_last["start"], s_last["end"])

    # DIS-02: Redundant / Echoic summary sentence (Regex + Jaccard Content-Word Overlap)
    dis02_re = re.compile(
        r"(?:Tóm lại,\s*có thể khẳng định(?: chắc chắn)? rằng[^.!?]+[.!?]?|"
        r"(?:Tóm lại|Nhìn chung|Như vậy(?:,\s*qua đó có thể thấy)?|Có thể nói|Chính vì vậy)\s*,?[^.!?]*(?:chìa khóa vàng|thành công rực rỡ|kỷ nguyên mới|phát triển bền vững|mở ra hướng đi mới|khẳng định vị thế vững chắc)[^.!?]*[.!?]?)",
        re.IGNORECASE,
    )
    for m in dis02_re.finditer(text):
        bcr = 1.0
        add_flag("DIS-02", m.start(), m.end())

    if n_sent >= 4 and not is_outline_para:
        first_s = sentences[0]
        last_s = sentences[-1]
        if re.match(
            r"^(?:Tóm lại|Nhìn chung|Như vậy|Có thể nói|Qua đó có thể thấy|Tựu trung lại)\b",
            last_s["text"],
            re.IGNORECASE,
        ) and not has_quantitative_evidence(last_s["text"]):
            overlap = _compute_content_word_jaccard(first_s["text"], last_s["text"])
            if overlap >= 0.40:
                bcr = 1.0
                add_flag("DIS-02", last_s["start"], last_s["end"])

    # DIS-04: Header-echo definition opener & robotic meta-discourse signposting
    dis04_re = re.compile(
        r"(?:^[^,.]{3,60}\s+(?:là một tập hợp các|đề cập đến quá trình|được định nghĩa như là một khái niệm)\b"
        r"|Sau khi đã (?:phân tích|tìm hiểu|làm rõ)[^,]{3,65},\s*(?:tiếp theo chúng ta sẽ|phần tiếp theo sẽ|chúng ta hãy cùng)"
        r"|Như đã (?:đề cập|trình bày) ở (?:phần )?trên,\s*(?:phần này sẽ|tiếp theo sẽ|chúng ta sẽ))",
        re.IGNORECASE,
    )
    for m in dis04_re.finditer(text):
        add_flag("DIS-04", m.start(), m.end())

    # -------------------------------------------------------------------------
    # METRIC 2 & SYN-01, SYN-02, SYN-03, SYN-04: Syntactic Patterns
    # -------------------------------------------------------------------------
    adv_opener_re = re.compile(
        r"^(?:Trong bối cảnh|Trước những|Thông qua việc|Bằng việc|Bằng cách|Dựa trên(?: việc| cơ sở)?|Trên cơ sở|Trên phương diện|Xét về(?: mặt| phương diện)?|Về mặt|Về phương diện|Đối với|Nhằm hướng tới)\b[^,]{3,65},",
        re.IGNORECASE,
    )
    tail_clause_re = re.compile(
        r",\s*(?:(?:qua đó|từ đó|nhờ đó|theo đó)\s+(?:góp phần|giúp|tạo điều kiện|tạo tiền đề|thúc đẩy|nâng cao|khẳng định|mở ra|đảm bảo|củng cố|tối ưu hóa)|góp phần\s+(?:quan trọng\s+)?(?:vào việc|nâng cao|thúc đẩy|tối ưu hóa|đảm bảo|củng cố|hoàn thiện)|điều này phản ánh|mở ra triển vọng|tạo tiền đề vững chắc)\s+[^.!?]+[.!?]?",
        re.IGNORECASE,
    )

    opener_indices: List[int] = []
    tail_indices: List[int] = []
    both_indices: List[int] = []

    for s_idx, s in enumerate(sentences):
        has_adv = bool(adv_opener_re.search(s["text"]))
        tail_matches = list(tail_clause_re.finditer(s["text"]))
        if has_adv:
            opener_indices.append(s_idx)
        if tail_matches:
            tail_indices.append(s_idx)
            for tm in tail_matches:
                add_flag(
                    "SYN-02",
                    s["start"] + tm.start() + 2,
                    s["start"] + tm.end(),
                )
        if has_adv and tail_matches:
            both_indices.append(s_idx)

    isomorphic_idx_set = set(both_indices)
    if len(opener_indices) >= 2:
        isomorphic_idx_set.update(opener_indices)
    if len(tail_indices) >= 3:
        isomorphic_idx_set.update(tail_indices)

    # Clause-Vector Isomorphism: >= 3 consecutive sentences with identical clause count >= 3 and <15% length variance
    if n_sent >= 3 and not is_outline_para and not is_heavily_econometric_para:
        clause_counts = [len(split_into_clauses(s["text"])) for s in sentences]
        for i in range(n_sent - 2):
            if clause_counts[i] == clause_counts[i + 1] == clause_counts[i + 2] and clause_counts[i] >= 3:
                w0, w1, w2 = sentences[i]["word_count"], sentences[i + 1]["word_count"], sentences[i + 2]["word_count"]
                mean_w = (w0 + w1 + w2) / 3.0
                if mean_w >= 18 and max(abs(w0 - mean_w), abs(w1 - mean_w), abs(w2 - mean_w)) / mean_w < 0.15:
                    isomorphic_idx_set.update([i, i + 1, i + 2])

    isi = round(len(isomorphic_idx_set) / max(1, n_sent), 4)
    if len(isomorphic_idx_set) >= 2:
        sorted_iso = sorted(isomorphic_idx_set)
        add_flag(
            "SYN-01",
            sentences[sorted_iso[0]]["start"],
            sentences[sorted_iso[-1]]["end"],
        )

    # SYN-03: Negative Parallelism ("không chỉ... mà còn...", "không đơn thuần là... mà là...") & False Ranges ("Từ A đến B, từ C đến D")
    syn03_re = re.compile(
        r"(?:(?:Đây\s+)?(?:không\s+chỉ\s+(?:là\s+)?[^.!?]{3,80}\s+mà\s+còn\s+(?:là\s+)?[^.!?]{3,80}|"
        r"không\s+đơn\s+thuần\s+là\s+[^.!?]{3,60}\s+mà\s+(?:còn\s+)?là\s+[^.!?]{3,60}|"
        r"thay\s+vì\s+chỉ\s+đơn\s+thuần\s+(?:là\s+)?[^,.;!?]{3,60})|"
        r"\bTừ\s+[^,.;]{3,35}\s+đến\s+[^,.;]{3,35},\s*(?:từ\s+[^,.;]{3,35}\s+đến\s+[^,.;]{3,35}|tất\s+cả\s+đều|mọi\s+khía\s+cạnh\s+đều))",
        re.IGNORECASE,
    )
    for m in syn03_re.finditer(text):
        add_flag("SYN-03", m.start(), m.end())

    # SYN-04: Mechanical Rule of Three (Explicit triads + General Syllable-Balanced Triadic Coordination Detector)
    syn04_re = re.compile(
        r"(?:đồng bộ,\s*toàn diện\s+và\s+hiệu quả|"
        r"đồng bộ,\s*hài hòa\s+và\s+bền vững|"
        r"chặt chẽ,\s*linh hoạt\s+và\s+hiệu quả|"
        r"kịp thời,\s*chính xác\s+và\s+minh bạch|"
        r"toàn diện,\s*sâu sắc\s+và\s+triệt để|"
        r"(?:qua đó\s+)?(?:góp phần\s+)?(?:nâng cao|tăng cường|xây dựng)\s+[^,.]+,\s*(?:tối ưu hóa|củng cố|hoàn thiện)\s+[^,.]+\s+và\s+(?:thúc đẩy|phát triển|đảm bảo)\s+[^.!?]+)",
        re.IGNORECASE,
    )
    for m in syn04_re.finditer(text):
        add_flag("SYN-04", m.start(), m.end())

    general_triad_re = re.compile(
        r"\b([a-zà-ỹ]+(?:\s+[a-zà-ỹ]+){1,3}),\s*([a-zà-ỹ]+(?:\s+[a-zà-ỹ]+){1,3})\s+(?:và|cũng\s+như|lẫn)\s+([a-zà-ỹ]+(?:\s+[a-zà-ỹ]+){1,3})\b",
        re.IGNORECASE | re.UNICODE,
    )
    abstract_triads: List[Tuple[int, int]] = []
    for m in general_triad_re.finditer(masked_text):
        if "§" in m.group(0):
            continue
        w1, w2, w3 = extract_words(m.group(1)), extract_words(m.group(2)), extract_words(m.group(3))
        if 2 <= len(w1) <= 4 and 2 <= len(w2) <= 4 and 2 <= len(w3) <= 4:
            sv_cnt = sum(1 for w in (w1 + w2 + w3) if w in SINO_VIETNAMESE_ABSTRACT_SYLLABLES)
            if sv_cnt >= 5:
                abstract_triads.append((m.start(), m.end()))
    if len(abstract_triads) >= 2:
        for t_s, t_e in abstract_triads:
            add_flag("SYN-04", t_s, t_e)

    # -------------------------------------------------------------------------
    # METRIC 3 & SYN-VN-01, SYN-VN-02, SYN-VN-03: Vietnamese Native Syntax
    # -------------------------------------------------------------------------
    opr_matches = list(
        re.finditer(
            r"\b(?:khi nó|nó thường|nó đã|nó có thể|nó cũng|điều này|việc này|của họ|của nó|của mình)\b|,\s*nó\s+",
            text,
            re.IGNORECASE,
        )
    )
    opr = round((len(opr_matches) / total_words) * 100, 2)
    for m in opr_matches:
        add_flag("SYN-VN-01", m.start(), m.end())

    # SYN-VN-02: Topic-Comment loss ("Đối với vấn đề X, nó thường được...")
    syn_vn02_re = re.compile(
        r"(?:Đối với vấn đề|Liên quan đến khía cạnh|Xét trên phương diện)\s+[^,]+,\s*(?:nó\s+)?(?:thường\s+)?(?:được|bị)?",
        re.IGNORECASE,
    )
    for m in syn_vn02_re.finditer(text):
        add_flag("SYN-VN-02", m.start(), m.end())

    # SYN-VN-03: Passive calque & foreign nominalization (with Econometric & Legal Exemption Filter!)
    syn_vn03_explicit_re = re.compile(
        r"(?:việc\s+[^,.]{3,65}\s+được\s+thực\s+hiện\s+bởi\s+[^,.]{3,50}(?:\s+đã\s+được\s+chứng\s+minh\s+là\s+có\s+sự\s+ảnh\s+hưởng\s+đáng\s+kể)?|"
        r"thông qua việc thực hiện quy trình[^,.]{3,60}|"
        r"\b(?:sự|việc)\s+(?:chuyển biến|triển khai|thực hiện|tối ưu hóa|hoàn thiện)\s+của\s+[^,.;!?()]{3,35})",
        re.IGNORECASE,
    )
    for m in syn_vn03_explicit_re.finditer(text):
        masked_slice = masked_text[m.start() : m.end()]
        # Skip only if the entire matched phrase is a protected economics term (e.g., "sự hài lòng của khách hàng")
        if masked_slice.replace(" ", "").strip("§") != "":
            add_flag("SYN-VN-03", m.start(), m.end())

    syn_vn03_passive_re = re.compile(
        r"\b(?:được|bị)\s+([a-zA-ZÀ-ỹ]+(?:\s+[a-zA-ZÀ-ỹ]+){0,2})\s+bởi\s+([^,.;!?()]{3,35})",
        re.IGNORECASE,
    )
    for m in syn_vn03_passive_re.finditer(text):
        verb_phrase = m.group(1).strip()
        sent_ctx = _find_sentence_containing(sentences, m.start(), m.end())
        if _LEGITIMATE_ACADEMIC_PASSIVE_VERBS.match(verb_phrase):
            continue
        if is_econometric_or_statistical_sentence(sent_ctx) or is_legal_citation_sentence(sent_ctx):
            continue
        add_flag("SYN-VN-03", m.start(), m.end())

    # -------------------------------------------------------------------------
    # METRIC 4 & LEX-VN-01, LEX-01..05: Lexical & Sino-Vietnamese Congestion
    # -------------------------------------------------------------------------
    sv_chains = _find_sino_vietnamese_chains(masked_text, min_run=7)
    svci, sv_span = _find_max_sino_vietnamese_run(masked_text, text)

    nominal_chain_re = re.compile(
        r"(?:thực hiện quy trình chuyển đổi mô hình quản trị[^,.]{0,40}|"
        r"thực hiện việc tiết giảm|triển khai sự tái cấu trúc|quá trình tối ưu hóa hiệu suất|"
        r"(?:việc|sự|quá trình)\s+(?:triển khai|thực hiện|tối ưu hóa|hoàn thiện|tăng cường)\s+(?:đồng bộ\s+|toàn diện\s+)?(?:các\s+)?(?:giải pháp|cơ chế|chính sách|quy trình|phương thức|chiến lược|hệ thống)\s+(?:vận hành|quản trị|kiểm soát|phát triển|tích hợp|chuyển đổi)(?:\s+[a-zA-ZÀ-ỹ]+){1,4})",
        re.IGNORECASE,
    )
    for m in nominal_chain_re.finditer(text):
        masked_slice = masked_text[m.start() : m.end()]
        if masked_slice.replace(" ", "").strip("§") != "":
            svci = max(svci, 8)
            add_flag("LEX-VN-01", m.start(), m.end())

    for sv_s, sv_e, _ in sv_chains:
        sent_ctx = _find_sentence_containing(sentences, sv_s, sv_e)
        if not is_legal_citation_sentence(sent_ctx):
            add_flag("LEX-VN-01", sv_s, sv_e)

    # LEX-01: AI Vocabulary & Clichés
    lex01_re = re.compile(
        r"(?:đóng vai trò (?:như một chất xúc tác )?(?:vô cùng )?(?:then chốt|sống còn|quyết định)(?:\s+và\s+mang\s+tính\s+bước\s+ngoặt\s+lịch\s+sử)?|"
        r"bức tranh toàn cảnh|tấm thảm đa sắc|điều hướng qua những thách thức|"
        r"tích hợp một cách liền mạch|sự giao thoa phức tạp|bối cảnh không ngừng biến đổi|"
        r"nuôi dưỡng sự đổi mới|góc nhìn đa chiều|khai phá tiềm năng|kiến tạo hệ sinh thái|"
        r"đòn bẩy chiến lược|không thể phủ nhận rằng)",
        re.IGNORECASE,
    )
    for m in lex01_re.finditer(text):
        add_flag("LEX-01", m.start(), m.end())

    # LEX-02: Copula Avoidance
    lex02_re = re.compile(
        r"(?:đóng vai trò như là|đóng vai trò là|đứng như một|hoạt động như một|giữ vị thế là|tự hào có|nổi bật với|phục vụ như một)",
        re.IGNORECASE,
    )
    for m in lex02_re.finditer(text):
        add_flag("LEX-02", m.start(), m.end())

    # LEX-03: Promotional Puffery & Figurative Clichés
    lex03_re = re.compile(
        r"(?:mang tính bước ngoặt lịch sử|bước ngoặt lịch sử|minh chứng sống động cho|"
        r"tiên phong mang tính đột phá|sự kết hợp hoàn hảo giữa|chìa khóa vàng(?:\s+mở ra cánh cửa thành công rực rỡ)?|"
        r"cam kết không ngừng nghỉ|bề dày lịch sử phong phú|luồng gió mới|kim chỉ nam|"
        r"cơn địa chấn|mảnh đất màu mỡ|bệ phóng vững chắc|cú hích mạnh mẽ)",
        re.IGNORECASE,
    )
    for m in lex03_re.finditer(text):
        add_flag("LEX-03", m.start(), m.end())

    # LEX-04: Artificial Synonym Cycling across 7 Economics Entity Groups
    for grp in SYNONYM_CYCLE_GROUPS:
        found = [re.search(r"\b" + p + r"\b", text, re.IGNORECASE) for p in grp]
        found = [m for m in found if m is not None]
        # Bank group triggers at >= 2 when explicit demonstratives ("này/trên/định chế tài chính") are cycled
        min_cycle = 2 if grp is SYNONYM_CYCLE_GROUPS[0] and any("định chế" in m.group(0).lower() or "nhà băng" in m.group(0).lower() for m in found) else 3
        if len(found) >= min_cycle:
            found.sort(key=lambda m: m.start())
            add_flag("LEX-04", found[0].start(), found[-1].end())

    # LEX-05: Vague Association & Inflation
    lex05_re = re.compile(
        r"(?:gắn liền với các hoạt động|có mối liên hệ mật thiết với|"
        r"được ghi nhận trong mối tương quan với|xoay quanh các lĩnh vực liên quan đến|"
        r"vô cùng (?:quan trọng|to lớn|cấp thiết|sâu sắc)|cực kỳ (?:quan trọng|hiệu quả|ấn tượng)|"
        r"tăng trưởng vượt bậc|bước tiến vượt bậc|thành công rực rỡ)",
        re.IGNORECASE,
    )
    for m in lex05_re.finditer(text):
        add_flag("LEX-05", m.start(), m.end())

    # -------------------------------------------------------------------------
    # ARG-01..04 & PRG-01..02: Argumentation & Epistemic Stance
    # -------------------------------------------------------------------------
    # ARG-01: Flat Epistemic Weight ("Thứ nhất,... Thứ hai,... Thứ ba,..." without numbers)
    if (
        re.search(r"(?:Thứ nhất|Một là)\s*,.*(?:Thứ hai|Hai là)\s*,.*(?:Thứ ba|Ba là)\s*,", text, re.IGNORECASE | re.DOTALL)
        and not has_quantitative_evidence(text)
    ):
        add_flag("ARG-01", 0, len(text))

    # ARG-02: Pendulum Hedging ("Tuy nhiên... thách thức... Do đó... toàn diện / hài hòa ... bền vững" or "Mặc dù không thể phủ nhận... song cũng cần nhìn nhận...")
    arg02_re = re.compile(
        r"(?:Tuy nhiên\s*,[^.!?]*(?:thách thức|hạn chế|rủi ro)[^.!?]*\.\s*"
        r"(?:Do đó|Vì vậy|Như vậy)\s*,[^.!?]*(?:toàn diện|đồng bộ|hài hòa|cân bằng|phát triển bền vững)[^.!?]*[.!?]?|"
        r"Mặc dù không thể phủ nhận[^,]{5,80},\s*(?:song|nhưng)\s+cũng cần\s+(?:nhìn nhận|thừa nhận|lưu ý)[^.!?]*[.!?]?|"
        r"Một mặt\s+[^,]{5,70},\s*mặt khác\s+[^.!?]{5,80}(?:đòi hỏi sự cân nhắc|cần được xem xét hài hòa)[^.!?]*[.!?]?)",
        re.IGNORECASE,
    )
    for m in arg02_re.finditer(text):
        add_flag("ARG-02", m.start(), m.end())

    # ARG-03: Macro-significance / Broad Context Inflation
    arg03_re = re.compile(
        r"(?:Trong bối cảnh (?:toàn cầu hóa|hội nhập kinh tế|chuyển đổi số|cách mạng công nghiệp)[^,]{0,65},|"
        r"Trước những biến động không ngừng của[^,]{4,55},|"
        r"Cùng với sự phát triển mạnh mẽ của[^,]{4,55},|"
        r"phản ánh xu hướng rộng lớn hơn|để lại dấu ấn không phai mờ|đặt nền móng cho)",
        re.IGNORECASE,
    )
    for m in arg03_re.finditer(text):
        add_flag("ARG-03", m.start(), m.end())

    # ARG-04: Formulaic Challenges & Prospects / Hollow Policy Slogans
    arg04_re = re.compile(
        r"(?:Mặc dù đạt được\s+[^,]+,\s*[^,]+\s+vẫn đối mặt với nhiều thách thức|"
        r"Thách thức và Triển vọng tương lai|"
        r"Cần tăng cường (?:hơn nữa )?(?:sự |công tác )?phối hợp đồng bộ[^.!?]{0,60}|"
        r"Đẩy mạnh (?:việc )?ứng dụng công nghệ thông tin và chuyển đổi số một cách toàn diện[^.!?]{0,50})",
        re.IGNORECASE,
    )
    for m in arg04_re.finditer(text):
        add_flag("ARG-04", m.start(), m.end())

    # PRG-01: Weasel Attribution ("Theo các chuyên gia cho rằng...") & Vague Unquantified Claims
    prg01_weasel_re = re.compile(
        r"(?:Theo\s+)?(?:các chuyên gia(?:\s+kinh tế)? cho rằng|nhiều nhà quan sát nhận định|"
        r"các nghiên cứu(?: trước đây)? chỉ ra rằng|giới phân tích nhận định rằng|thực tế đã chứng minh rằng|"
        r"sự đưa tin độc lập từ các cơ quan truyền thông|các ấn phẩm thương mại chuyên ngành)",
        re.IGNORECASE,
    )
    for m in prg01_weasel_re.finditer(text):
        sent_ctx = _find_sentence_containing(sentences, m.start(), m.end())
        # Always flag ungrammatical calque "Theo các chuyên gia cho rằng" or when sentence lacks academic citation
        if "theo các chuyên gia cho rằng" in m.group(0).lower() or not has_academic_citation(sent_ctx):
            add_flag("PRG-01", m.start(), m.end())

    # PRG-02: Didactic Hedging & Disclaimer
    prg02_re = re.compile(
        r"(?:điều quan trọng cần lưu ý là|cần phải nhớ rằng|"
        r"mặc dù chi tiết cụ thể không được công bố rộng rãi|không ngoa khi nói rằng)",
        re.IGNORECASE,
    )
    for m in prg02_re.finditer(text):
        add_flag("PRG-02", m.start(), m.end())

    # -------------------------------------------------------------------------
    # Calculate composite intensity score (0..100) combining rule severity weights
    # and continuous quantitative metric penalties
    # -------------------------------------------------------------------------
    if not flags:
        ai_style_score = 0
    else:
        weights = {"critical": 35, "warning": 18, "suggestion": 12}
        raw_score = sum(weights.get(f["severity"], 12) for f in flags)
        # Continuous bonus from quantitative metrics when flags exist
        metric_bonus = 0.0
        if len(lengths) >= 4 and cv_length < 0.22:
            metric_bonus += 10.0 * ((0.22 - cv_length) / 0.22)
        if isi > 0.30:
            metric_bonus += min(8.0, 12.0 * isi)
        if sicd > 0.35:
            metric_bonus += min(6.0, 10.0 * sicd)
        ai_style_score = min(100, round(raw_score + metric_bonus))

    return {
        "index": index,
        "text": text,
        "wordCount": total_words,
        "sentenceCount": n_sent,
        "metrics": {
            "cvLength": cv_length,
            "deltaLength": delta_length,
            "isi": isi,
            "opr": opr,
            "svci": svci,
            "sicd": sicd,
            "bcr": bcr,
        },
        "flags": flags,
        "protectedTerms": [p["term"] for p in protected_spans],
        "aiStyleScore": ai_style_score,
    }
