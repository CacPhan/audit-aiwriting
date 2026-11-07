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
    AI_INTENSIFIER_VOCAB,
    RULE_METADATA,
    SINO_VIETNAMESE_ABSTRACT_SYLLABLES,
    SYNONYM_CYCLE_GROUPS,
    VAGUE_HEDGING_PATTERNS,
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
    # FMT-01: Mechanical Formatting (Inline bold bullet headers, explanatory em-dashes & spaced hyphens, markdown bold, emojis)
    # -------------------------------------------------------------------------
    for m in re.finditer(r"(?:^|\n)\s*[-*•]\s*(?:\*\*[^*]+\*\*|[A-ZÀ-Ỹ][^:\n]{2,35})\s*:", text):
        add_flag("FMT-01", m.start(), m.end())

    for m in re.finditer(r"\s+—\s+[a-zà-ỹ]", text):
        add_flag("FMT-01", max(0, m.start() - 10), min(len(text), m.end() + 25))

    if text.count("—") >= 2:
        for m in re.finditer(r"\s*—\s*", text):
            add_flag("FMT-01", max(0, m.start() - 12), min(len(text), m.end() + 25))

    for m in re.finditer(
        r"\s+-\s+(?:tức\s+là|nghĩa\s+là|nơi\s+|con\s+số\s+|yếu\s+tố\s+|đây\s+là|một\s+trong\s+những|không\s+phải)\b",
        text,
        re.IGNORECASE,
    ):
        add_flag("FMT-01", max(0, m.start() - 10), min(len(text), m.end() + 20))

    for m in re.finditer(r"\*\*[^*\n]{2,60}\*\*|[📌💡🚀✅🔹✨📊🔥🎯🌟]", text):
        add_flag("FMT-01", m.start(), m.end())

    # -------------------------------------------------------------------------
    # METRIC 5 & DIS-01, DIS-02, DIS-03, DIS-04: Discourse & Paragraph Framing
    # -------------------------------------------------------------------------
    connective_openers = (
        r"^(?:Cụ thể|Tuy nhiên|Do đó|Hơn nữa|Thêm vào đó|Bên cạnh đó|"
        r"Ngoài ra|Đáng chú ý là|Thật vậy|Ngược lại|Vì vậy|Như vậy|Mặt khác|Đồng thời|Không những vậy|Chính vì vậy|Song song với đó)\s*,"
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

    # DIS-01: 4-step Boxed Paragraph ([Topic] -> [Cụ thể,/Thực tế,] -> [Tuy nhiên,/Bên cạnh đó,] -> [Do đó,/Như vậy,/Tóm lại,])
    # Strictly requires n_sent >= 4 per test_rhy01_and_dis01_never_trigger_on_short_paragraphs_under_4_sentences
    bcr = 0.0
    if n_sent >= 4 and not is_outline_para:
        s_last = sentences[-1]
        mid_texts = [s["text"] for s in sentences[1:-1]]
        has_mid_transition = any(
            re.match(
                r"^(?:Cụ thể|Thực tế|Theo đó|Trước hết|Tuy nhiên|Song|Mặt khác|Ngược lại|Bên cạnh đó|Trong khi đó|Đồng thời)\s*,",
                mt,
                re.IGNORECASE,
            )
            for mt in mid_texts
        )
        has_box_close = bool(
            re.match(
                r"^(?:Do đó|Như vậy|Tóm lại|Nhìn chung|Vì vậy|Chính vì vậy|Có thể nói|Từ đó cho thấy|Qua đó cho thấy|Tựu trung lại|Qua đó|Từ đó)\s*,?",
                s_last["text"],
                re.IGNORECASE,
            )
            or re.search(
                r"(?:để đảm bảo sự phát triển bền vững|phát triển bền vững trong tương lai|điều này khẳng định tầm quan trọng của|qua đó tạo nền tảng vững chắc cho|Đây là cơ sở để|Đây là những nội dung cần)",
                s_last["text"],
                re.IGNORECASE,
            )
        )
        if (
            (has_mid_transition and has_box_close)
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

    # DIS-02: Redundant / Echoic summary sentence or subsection closure (Works on 1-3 sentence closing paragraphs too!)
    dis02_re = re.compile(
        r"(?:Tóm lại,\s*có thể khẳng định(?: chắc chắn)? rằng[^.!?]+[.!?]?|"
        r"(?:Tóm lại|Nhìn chung|Như vậy(?:,\s*qua đó có thể thấy)?|Có thể nói|Có thể thấy|Chính vì vậy|Tổng hợp kết quả cho thấy|Từ những phân tích trên)\s*,?[^.!?]*(?:chìa khóa vàng|thành công rực rỡ|kỷ nguyên mới|phát triển bền vững|mở ra hướng đi mới|khẳng định vị thế vững chắc)[^.!?]*[.!?]?|"
        r"(?:Đây\s+là\s+(?:cơ\s+sở|tiền\s+đề|căn\s+cứ)\s+(?:quan\s+trọng\s+|thực\s+tiễn\s+)?để\s+(?:tiếp\s+tục\s+|khóa\s+luận\s+|tác\s+giả\s+)?(?:xem\s+xét|phân\s+tích|đề\s+xuất|xây\s+dựng|hoàn\s+thiện)[^.!?]*(?:ở\s+phần\s+tiếp\s+theo|tại\s+Chương\s+\d|trong\s+Chương\s+\d|ở\s+chương\s+sau)[^.!?]*[.!?]?|"
        r"Đây\s+là\s+những\s+(?:nội\s+dung|vấn\s+đề|hạn\s+chế|yếu\s+tố|điểm\s+nghẽn)\s+[^.!?]{0,60}?\s+cần\s+(?:được\s+)?(?:ưu\s+tiên\s+|tiếp\s+tục\s+)?(?:rà\s+soát|xem\s+xét|hoàn\s+thiện|khắc\s+phục|cải\s+thiện)\s+trong\s+(?:thời\s+gian\s+tới|giai\s+đoạn\s+tiếp\s+theo|tương\s+lai|Chương\s+\d)[^.!?]*[.!?]?))",
        re.IGNORECASE,
    )
    for m in dis02_re.finditer(text):
        bcr = 1.0
        add_flag("DIS-02", m.start(), m.end())

    # Short echoic closing paragraph (1-3 sentences) opening with "Như vậy, / Nhìn chung, / Tóm lại, / Có thể thấy, / Tổng hợp kết quả cho thấy,"
    if 1 <= n_sent <= 3 and not is_outline_para:
        first_s = sentences[0]
        if (
            re.match(
                r"^(?:Như\s+vậy|Nhìn\s+chung|Tóm\s+lại|Có\s+thể\s+thấy(?:\s+rằng)?|Tổng\s+hợp\s+(?:lại|kết\s+quả\s+cho\s+thấy)|Từ\s+những\s+phân\s+tích\s+trên)\s*,",
                first_s["text"],
                re.IGNORECASE,
            )
            and not has_quantitative_evidence(text)
        ):
            bcr = 1.0
            add_flag("DIS-02", first_s["start"], sentences[-1]["end"])

    if n_sent >= 4 and not is_outline_para:
        first_s = sentences[0]
        last_s = sentences[-1]
        if re.match(
            r"^(?:Tóm lại|Nhìn chung|Như vậy|Có thể nói|Có thể thấy|Qua đó có thể thấy|Tựu trung lại|Tổng hợp kết quả cho thấy)\b",
            last_s["text"],
            re.IGNORECASE,
        ) and not has_quantitative_evidence(last_s["text"]):
            overlap = _compute_content_word_jaccard(first_s["text"], last_s["text"])
            if overlap >= 0.35:
                bcr = 1.0
                add_flag("DIS-02", last_s["start"], last_s["end"])

    # DIS-04: Header-echo definition opener, robotic meta-discourse table/enumeration signposting & category labeling
    dis04_re = re.compile(
        r"(?:^[A-ZÀ-ỸĐ][^,.]{2,65}\s+(?:được\s+hiểu\s+là|có\s+thể\s+được\s+hiểu\s+là|được\s+định\s+nghĩa\s+(?:như\s+)?là|là\s+một\s+tập\s+hợp\s+các|đề\s+cập\s+đến\s+quá\s+trình)\b|"
        r"^[A-ZÀ-ỸĐ][^,.]{2,45}\s+là\s+(?:hạng\s+mục|bước|yếu\s+tố|công\s+cụ|khâu|nhiệm\s+vụ)\s+(?:chiến\s+lược\s+)?(?:dài\s+hạn\s+)?(?:trọng\s+tâm|cốt\s+lõi|bắt\s+buộc|quan\s+trọng(?:\s+nhất|\s+hàng\s+đầu)?|then\s+chốt)\b|"
        r"Trong\s+phạm\s+vi\s+(?:nghiên\s+cứu|khóa\s+luận|chuyên\s+đề)(?:\s+này)?,\s*[^.!?]+được\s+xem\s+xét\s+(?:qua|trên|theo|dưới)\b|"
        r"(?:Số\s+liệu[\s\S]{0,25}?Bảng|Bảng|Hồ\s+sơ|Phân\s+tích|Cách\s+phân\s+bổ|Sự\s+khác\s+biệt|Cách\s+làm|Sự\s+phụ\s+thuộc)[\s\S]{0,95}?(?:cho\s+thấy|dẫn\s+tới|tác\s+động\s+tới\s+[^.!?]{0,35}\s+theo|thể\s+hiện\s+đầy\s+đủ\s+[^.!?]{0,30}\s+ở)\s+(?:hai|ba|bốn|năm|sáu|\d+)\s+(?:điểm|điều|đặc\s+điểm|xu\s+hướng|nhận\s+định|hệ\s+quả|định\s+hướng|hướng|hạn\s+chế(?:\s+nổi\s+bật)?)[^.!?]*\.\s*(?:Thứ\s+nhất|Một\s+là)\b|"
        r"Để\s+đánh\s+giá\s+[^,]{5,60},\s*(?:tác\s+giả|nghiên\s+cứu|khóa\s+luận)\s+(?:tiến\s+hành\s+)?(?:khảo\s+sát|sử\s+dụng)\s+(?:năm|bốn|ba|\d+)\s+(?:biến\s+quan\s+sát|tiêu\s+chí|khía\s+cạnh)|"
        r"Sau khi đã (?:phân tích|tìm hiểu|làm rõ)[^,]{3,65},\s*(?:tiếp theo chúng ta sẽ|phần tiếp theo sẽ|chúng ta hãy cùng)|"
        r"Như đã (?:đề cập|trình bày) ở (?:phần )?trên,\s*(?:phần này sẽ|tiếp theo sẽ|chúng ta sẽ))",
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
    criterion_opener_re = re.compile(
        r"^(?:(?:Tiêu\s+chí|Chỉ\s+tiêu|Yếu\s+tố|Khía\s+cạnh|Biến\s+quan\s+sát|Nội\s+dung)\s+[^,]{2,45}\s+đạt\s+[\d.,]+\s*điểm|(?:Về|Xét\s+về)\s+[^,]{2,35},\s*)",
        re.IGNORECASE,
    )
    tail_clause_re = re.compile(
        r",\s*(?:(?:qua đó|từ đó|nhờ đó|theo đó)\s+(?:góp phần|giúp|tạo điều kiện|tạo tiền đề|tạo cơ sở|tạo nền tảng|thúc đẩy|nâng cao|khẳng định|mở ra|đảm bảo|củng cố|tối ưu hóa)|"
        r"(?:đồng\s+thời\s+)?(?:góp\s+phần|giúp|tạo\s+cơ\s+sở|tạo\s+điều\s+kiện|tạo\s+nền\s+tảng|tạo\s+tiền\s+đề|làm\s+cơ\s+sở|hướng\s+tới\s+việc)\s+(?:quan\s+trọng\s+)?(?:vào\s+việc\s+|cho\s+việc\s+)?(?:nâng\s+cao|cải\s+thiện|duy\s+trì|đảm\s+bảo|bảo\s+đảm|thúc\s+đẩy|tối\s+ưu\s+hóa|củng\s+cố|hoàn\s+thiện|hình\s+thành)\b|"
        r"điều này phản ánh|mở ra triển vọng|tạo tiền đề vững chắc)\s*[^.!?]+[.!?]?",
        re.IGNORECASE,
    )

    opener_indices: List[int] = []
    criterion_opener_indices: List[int] = []
    tail_indices: List[int] = []
    both_indices: List[int] = []

    for s_idx, s in enumerate(sentences):
        has_adv = bool(adv_opener_re.search(s["text"]))
        has_crit = bool(criterion_opener_re.search(s["text"]))
        tail_matches = list(tail_clause_re.finditer(s["text"]))
        if has_adv:
            opener_indices.append(s_idx)
        if has_crit:
            criterion_opener_indices.append(s_idx)
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
    if len(criterion_opener_indices) >= 2:
        isomorphic_idx_set.update(criterion_opener_indices)
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

    # SYN-03: Negative Parallelism (All 4 Variants + False Ranges)
    syn03_re = re.compile(
        r"(?:"
        # Variant 1: không chỉ... mà (còn)...
        r"\bkhông\s+chỉ\s+[^.!?]{2,95}?\s+mà\s+(?:còn\s+|trở\s+thành\s+|phải\s+là\s+|là\s+|về\s+)?[^.!?]{3,90}|"
        # Variant 2: không đơn thuần/dừng lại/giới hạn ở/là... mà (còn)...
        r"\bkhông\s+(?:đơn\s+thuần|dừng\s+lại|giới\s+hạn)\s+(?:ở|là)?\s*[^.!?]{3,85}?\s+mà\s+(?:còn\s+)?(?:là|ở|hướng\s+tới|mở\s+rộng|thực\s+sự)?\s*[^.!?]{3,85}|"
        # Variant 3: không phải (chỉ) (là) X mà (còn) (là / nâng cấp / phản ánh...) Y (Karve Meilleur & An Cường)
        r"\bkhông\s+phải\s+(?:chỉ\s+)?(?:đơn\s+thuần\s+)?(?:là\s+)?[^.;!?]{3,90}?,?\s+mà\s+(?:còn\s+)?(?:là|phải\s+là|nằm\s+ở|ở|cần\s+được|đòi\s+hỏi|hướng\s+tới|phản\s+ánh|nâng\s+cấp|tập\s+trung|dựa\s+trên)?\s*[^.!?]{3,85}|"
        # Variant 4: X chứ không (chỉ) (phải) (đơn thuần) (là) Y (Hecatech)
        r"\bchứ\s+không\s+(?:chỉ\s+)?(?:phải\s+)?(?:đơn\s+thuần\s+)?(?:dừng\s+lại\s+ở\s+)?(?:là\s+)?[^,.;!?]{3,70}|"
        # Variant 5: thay vì chỉ đơn thuần... / Từ A đến B, từ C đến D...
        r"\bthay\s+vì\s+chỉ\s+(?:đơn\s+thuần\s+|cung\s+cấp\s+|tập\s+trung\s+)?(?:là\s+)?[^,.;!?]{3,65}|"
        r"\bTừ\s+[^,.;]{3,35}\s+đến\s+[^,.;]{3,35},\s*(?:từ\s+[^,.;]{3,35}\s+đến\s+[^,.;]{3,35}|tất\s+cả\s+đều|mọi\s+khía\s+cạnh\s+đều)"
        r")",
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
        r"rõ ràng,\s*minh bạch\s+và\s+nhất quán|"
        r"khách quan,\s*công bằng\s+và\s+minh bạch|"
        r"(?:qua đó\s+)?(?:góp phần\s+)?(?:nâng cao|tăng cường|xây dựng|đảm bảo|củng cố|mở rộng)\s+[^,.]{2,45},\s*(?:tối ưu hóa|củng cố|hoàn thiện|cải thiện|duy trì|nâng cao)\s+[^,.]{2,45}\s+và\s+(?:thúc đẩy|phát triển|đảm bảo|gia tăng|tạo dựng)\s+[^.!?]{2,55})",
        re.IGNORECASE,
    )
    for m in syn04_re.finditer(text):
        add_flag("SYN-04", m.start(), m.end())

    general_triad_re = re.compile(
        r"\b([a-zà-ỹ]+(?:\s+[a-zà-ỹ]+){1,3}),\s*([a-zà-ỹ]+(?:\s+[a-zà-ỹ]+){1,3})\s+(?:và|cũng\s+như|lẫn)\s+([a-zà-ỹ]+(?:\s+[a-zà-ỹ]+){1,3})\b",
        re.IGNORECASE | re.UNICODE,
    )
    abstract_triads: List[Tuple[int, int, int]] = []
    for m in general_triad_re.finditer(masked_text):
        if "§" in m.group(0):
            continue
        w1, w2, w3 = extract_words(m.group(1)), extract_words(m.group(2)), extract_words(m.group(3))
        if 2 <= len(w1) <= 4 and 2 <= len(w2) <= 4 and 2 <= len(w3) <= 4:
            sv_cnt = sum(1 for w in (w1 + w2 + w3) if w in SINO_VIETNAMESE_ABSTRACT_SYLLABLES)
            if sv_cnt >= 5:
                abstract_triads.append((m.start(), m.end(), sv_cnt))
    for t_s, t_e, sv_cnt in abstract_triads:
        if sv_cnt >= 6 or len(abstract_triads) >= 2:
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
    # Mid-clause "Subject + vì vậy + Verb" English calque (Hecatech & E-COM WOW)
    vi_vay_calque_matches = list(
        re.finditer(
            r"\b[A-ZÀ-ỸĐ][a-zà-ỹ]+(?:\s+[a-zà-ỹ]+){1,6}\s+vì\s+vậy\s+(?:cần|phải|có\s+thể|sẽ|được|bị|không|luôn|thường|trở\s+nên|đòi\s+hỏi|tăng|giảm|thay\s+đổi|lệch|chịu|mang|đặt\s+ra)\b",
            text,
        )
    )
    # Repeated demonstrative sentence openers ("Điều này / Kết quả này / Thực trạng này cho thấy...")
    demo_opener_matches = []
    for s in sentences:
        m_dem = re.match(
            r"^(?:Điều\s+này|Việc\s+này|Kết\s+quả\s+này|Thực\s+trạng\s+này|Diễn\s+biến\s+này|Cách\s+tiếp\s+cận\s+này|Chính\s+sách\s+này)\s+(?:cho\s+thấy|phản\s+ánh|giúp|làm\s+cho|góp\s+phần|đòi\s+hỏi|đặt\s+ra)\b",
            s["text"],
            re.IGNORECASE,
        )
        if m_dem:
            demo_opener_matches.append((s["start"], s["start"] + m_dem.end()))

    total_syn_vn01_hits = len(opr_matches) + len(vi_vay_calque_matches)
    opr = round((total_syn_vn01_hits / total_words) * 100, 2)
    for m in opr_matches:
        add_flag("SYN-VN-01", m.start(), m.end())
    for m in vi_vay_calque_matches:
        add_flag("SYN-VN-01", m.start(), m.end())
    if len(demo_opener_matches) >= 2:
        for d_s, d_e in demo_opener_matches:
            add_flag("SYN-VN-01", d_s, d_e)

    # SYN-VN-02: Topic-Comment loss ("Đối với..., / Về mặt..., nó thường được...")
    syn_vn02_re = re.compile(
        r"(?:(?:Đối\s+với\s+vấn\s+đề|Liên\s+quan\s+đến\s+khía\s+cạnh|Xét\s+trên\s+phương\s+diện)\s+[^,]+,\s*(?:nó\s+)?(?:thường\s+)?(?:được|bị)?|"
        r"(?:Đối\s+với|Liên\s+quan\s+đến|Xét\s+(?:về|trên)\s+(?:mặt|phương\s+diện|góc\s+độ|khía\s+cạnh)|Về\s+(?:mặt|phương\s+diện|phía|khía\s+cạnh)|Dưới\s+góc\s+(?:độ|nhìn)\s+(?:của)?)\s+[^,]{3,55},\s*(?:nó|chúng|điều\s+này|việc\s+này|hoạt\s+động\s+này|quá\s+trình\s+này|yếu\s+tố\s+này|tiêu\s+chí\s+này|chỉ\s+tiêu\s+này|kết\s+quả\s+này)?\s*(?:thường\s+|luôn\s+|cũng\s+|vẫn\s+)?(?:được|bị|đóng\s+vai\s+trò|giữ\s+vai\s+trò|chịu\s+ảnh\s+hưởng|có\s+ý\s+nghĩa))",
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
        if masked_slice.replace(" ", "").strip("§") != "":
            add_flag("SYN-VN-03", m.start(), m.end())

    # Repeated "Việc + [V_phrase] + giúp/làm cho/khiến/góp phần..." sentence subjects (>= 2 sentences in paragraph)
    viec_subject_spans: List[Tuple[int, int]] = []
    for s in sentences:
        m_viec = re.match(
            r"^Việc\s+[a-zà-ỹ]+(?:\s+[a-zà-ỹ]+){3,12}\s+(?:giúp|làm\s+cho|khiến|góp\s+phần|tạo\s+điều\s+kiện|đóng\s+vai\s+trò|có\s+ý\s+nghĩa|là\s+cơ\s+sở|đã\s+và\s+đang)\b",
            s["text"],
            re.IGNORECASE,
        )
        if m_viec:
            viec_subject_spans.append((s["start"], s["start"] + m_viec.end()))
    if len(viec_subject_spans) >= 2:
        for v_s, v_e in viec_subject_spans:
            add_flag("SYN-VN-03", v_s, v_e)

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
        r"(?:việc|sự|quá\s+trình|hoạt\s+động|công\s+tác)\s+(?:triển\s+khai|thực\s+hiện|tối\s+ưu\s+hóa|hoàn\s+thiện|tăng\s+cường|đẩy\s+mạnh|xây\s+dựng)\s+(?:đồng\s+bộ\s+|toàn\s+diện\s+|thực\s+hiện\s+)?(?:các\s+|những\s+)?(?:hoạt\s+động|quy\s+trình|chính\s+sách|giải\s+pháp|hệ\s+thống|cơ\s+chế|nội\s+dung|công\s+tác|phương\s+thức|chiến\s+lược)\s+(?:vận\s+hành|quản\s+trị|kiểm\s+soát|phát\s+triển|tích\s+hợp|chuyển\s+đổi|đánh\s+giá)(?:\s+[a-zA-ZÀ-ỹ]+){1,4})",
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

    # LEX-01: AI Vocabulary & Clichés + LEX-01b Intensifier Density Cluster Counter
    lex01_re = re.compile(
        r"(?:đóng vai trò (?:như một chất xúc tác )?(?:vô cùng )?(?:then chốt|sống còn|quyết định)(?:\s+và\s+mang\s+tính\s+bước\s+ngoặt\s+lịch\s+sử)?|"
        r"bức tranh toàn cảnh|tấm thảm đa sắc|điều hướng qua những thách thức|"
        r"tích hợp một cách liền mạch|sự giao thoa phức tạp|bối cảnh không ngừng biến đổi|"
        r"nuôi dưỡng sự đổi mới|góc nhìn đa chiều|khai phá tiềm năng|kiến tạo hệ sinh thái|"
        r"đòn bẩy chiến lược|không thể phủ nhận rằng|"
        r"\b(?:kim\s+chỉ\s+nam(?:\s+xuyên\s+suốt)?|bệ\s+phóng(?:\s+vững\s+chắc)?|nút\s+thắt\s+cổ\s+chai|tảng\s+băng\s+chìm|mắt\s+xích\s+(?:then\s+chốt|trung\s+tâm|quan\s+trọng)|trụ\s+cột\s+chiến\s+lược|bóc\s+tách\s+toàn\s+diện|lăng\s+kính\s+đa\s+chiều|luồng\s+sinh\s+khí\s+mới|bước\s+đệm\s+vững\s+chắc|tiền\s+đề\s+quyết\s+định|cát\s+cứ\s+tri\s+thức)\b)",
        re.IGNORECASE,
    )
    for m in lex01_re.finditer(text):
        add_flag("LEX-01", m.start(), m.end())

    # LEX-01b: AI Intensifier Vocabulary Density Counter (outside protected economics terms)
    intensifier_pattern = re.compile(
        r"\b(?:" + "|".join(re.escape(w) for w in sorted(AI_INTENSIFIER_VOCAB, key=len, reverse=True)) + r")\b",
        re.IGNORECASE,
    )
    intensifier_hits = [
        m for m in intensifier_pattern.finditer(masked_text) if "§" not in m.group(0)
    ]
    if len(intensifier_hits) >= 4 or (
        total_words >= 35 and len(intensifier_hits) >= 3 and (len(intensifier_hits) / total_words) >= 0.045
    ):
        first_hit = intensifier_hits[0]
        add_flag("LEX-01", first_hit.start(), first_hit.end())

    # LEX-02: Copula Avoidance (Expanded "là" & "có" replacement patterns)
    lex02_re = re.compile(
        r"(?:\b(?:đóng|giữ)\s+vai\s+trò\s+(?:như\s+)?(?:là\s+)?(?:một\s+)?(?:yếu\s+tố|nền\s+tảng|công\s+cụ|mắt\s+xích|trụ\s+cột|đòn\s+bẩy|hạt\s+nhân|thành\s+phần|bộ\s+phận|chìa\s+khóa|tiền\s+đề|động\s+lực|cầu\s+nối|thước\s+đo|minh\s+chứng)\b|"
        r"\bđược\s+(?:xem|coi|nhìn\s+nhận|đánh\s+giá|hiểu|định\s+nghĩa)\s+(?:như\s+)?là\s+một\b|"
        r"\b(?:đóng\s+vai\s+trò\s+như\s+là|đóng\s+vai\s+trò\s+là|đứng\s+như\s+một|hoạt\s+động\s+như\s+một|giữ\s+vị\s+thế\s+là|phục\s+vụ\s+như\s+một|đại\s+diện\s+cho\s+một)\b|"
        r"\b(?:sở\s+hữu|tự\s+hào\s+có|nổi\s+bật\s+với|mang\s+trong\s+mình)\s+(?:những|các|một|hệ\s+thống|đội\s+ngũ|quy\s+mô|bề\s+dày|lợi\s+thế|ưu\s+điểm)\b|"
        r"\b(?:tự\s+hào\s+có|nổi\s+bật\s+với)\b)",
        re.IGNORECASE,
    )
    for m in lex02_re.finditer(text):
        add_flag("LEX-02", m.start(), m.end())

    # LEX-03: Promotional & Corporate Puffery
    lex03_re = re.compile(
        r"(?:mang tính bước ngoặt lịch sử|bước ngoặt lịch sử|minh chứng sống động cho|"
        r"tiên phong mang tính đột phá|sự kết hợp hoàn hảo giữa|chìa khóa vàng(?:\s+mở ra cánh cửa thành công rực rỡ)?|"
        r"cam kết không ngừng nghỉ|bề dày lịch sử phong phú|luồng gió mới|kim chỉ nam|"
        r"cơn địa chấn|mảnh đất màu mỡ|bệ phóng vững chắc|cú hích mạnh mẽ|"
        r"\b(?:vươn\s+mình\s+mạnh\s+mẽ|vươn\s+ra\s+biển\s+lớn|vươn\s+tầm\s+(?:quốc\s+tế|toàn\s+cầu|khu\s+vực|châu\s+lục)|bứt\s+phá\s+(?:mạnh\s+mẽ|ngoạn\s+mục|vượt\s+bậc|lớn\s+nhất)|nhảy\s+vọt\s+phi\s+mã|tăng\s+trưởng\s+(?:vô\s+cùng\s+)?ấn\s+tượng|thành\s+tựu\s+(?:kinh\s+doanh\s+)?rực\s+rỡ|năng\s+lực\s+thực\s+chiến\s+đỉnh\s+cao|tài\s+sản\s+(?:trí\s+tuệ\s+)?vô\s+giá|kho\s+tàng\s+tri\s+thức\s+[^,.!?]{0,25}?\s*đồ\s+sộ|đáng\s+tự\s+hào|sự\s+ưu\s+việt|tinh\s+hoa\s+quản\s+trị|cực\s+kỳ\s+(?:phong\s+phú|khốc\s+liệt|mạnh\s+mẽ))\b)",
        re.IGNORECASE,
    )
    for m in lex03_re.finditer(text):
        add_flag("LEX-03", m.start(), m.end())

    # LEX-04: Artificial Synonym Cycling across 12 Economics Entity Groups
    demonstrative_suffix_re = re.compile(r"\b(?:này|đó|trên|nói\s+trên|vừa\s+nêu)\b", re.IGNORECASE)
    for grp in SYNONYM_CYCLE_GROUPS:
        found = [re.search(r"\b" + p + r"\b", text, re.IGNORECASE) for p in grp]
        found = [m for m in found if m is not None]
        has_demo_or_stylized = any(
            demonstrative_suffix_re.search(m.group(0))
            or any(
                styl in m.group(0).lower()
                for styl in ["định chế", "nhà băng", "pháp nhân", "nhà mốt", "thương trường", "thượng đế", "tài sản con người"]
            )
            for m in found
        )
        min_cycle = 2 if has_demo_or_stylized else 3
        if len(found) >= min_cycle:
            found.sort(key=lambda m: m.start())
            add_flag("LEX-04", found[0].start(), found[-1].end())

    # LEX-05: Vague Association & Stealth AI Hedging Qualifier Inflation ("tương đối...", "nhất định")
    lex05_re = re.compile(
        r"(?:\b(?:gắn\s+liền\s+với(?:\s+các\s+hoạt\s+động)?|có\s+mối\s+(?:liên\s+hệ|quan\s+hệ|tương\s+quan)\s+(?:mật\s+thiết|chặt\s+chẽ)\s+với|xoay\s+quanh\s+các(?:\s+lĩnh\s+vực)?|được\s+ghi\s+nhận\s+trong\s+mối\s+tương\s+quan(?:\s+với)?|chịu\s+ảnh\s+hưởng\s+đồng\s+thời\s+bởi\s+nhiều\s+yếu\s+tố)\b|"
        r"vô cùng (?:quan trọng|to lớn|cấp thiết|sâu sắc)|cực kỳ (?:quan trọng|hiệu quả|ấn tượng)|"
        r"tăng trưởng vượt bậc|bước tiến vượt bậc|thành công rực rỡ)",
        re.IGNORECASE,
    )
    for m in lex05_re.finditer(text):
        add_flag("LEX-05", m.start(), m.end())

    hedging_matches: List[re.Match] = []
    for h_pat in VAGUE_HEDGING_PATTERNS:
        hedging_matches.extend(re.finditer(h_pat, text, re.IGNORECASE))
    if len(hedging_matches) >= 2:
        hedging_matches.sort(key=lambda m: m.start())
        for hm in hedging_matches:
            add_flag("LEX-05", hm.start(), hm.end())

    # -------------------------------------------------------------------------
    # ARG-01..04 & PRG-01..02: Argumentation & Epistemic Stance
    # -------------------------------------------------------------------------
    # ARG-01: Flat Epistemic Weight ("Thứ nhất,... Thứ hai,... Thứ ba,..." or "Trước hết,... Bên cạnh đó,... Ngoài ra,..." without numbers)
    if (
        re.search(
            r"(?:(?:Thứ nhất|Một là)\s*,.*(?:Thứ hai|Hai là)\s*,.*(?:Thứ ba|Ba là)\s*,|"
            r"Trước hết\s*,.*Bên cạnh đó\s*,.*(?:Ngoài ra|Đồng thời|Cuối cùng)\s*,)",
            text,
            re.IGNORECASE | re.DOTALL,
        )
        and not has_quantitative_evidence(text)
    ):
        add_flag("ARG-01", 0, len(text))

    # ARG-02: 3-Phase Pendulum Hedging ("Khen/Kết quả -> Tuy nhiên hạn chế/chưa đồng đều -> Do đó/Vì vậy/Đây là cơ sở cần hoàn thiện/rà soát" or 2-sentence "Tuy nhiên... vẫn cần tiếp tục hoàn thiện/chuẩn hóa")
    arg02_re = re.compile(
        r"(?:(?:Tuy\s+nhiên|Song|Mặt\s+khác|Bên\s+cạnh\s+những\s+(?:kết\s+quả|ưu\s+điểm|điểm\s+tích\s+cực)[^,]{0,40})\s*,[\s\S]{5,260}?(?:thách\s+thức|hạn\s+chế|rủi\s+ro|khó\s+khăn|chưa\s+đồng\s+đều|chưa\s+rõ(?:\s+ràng)?|chưa\s+đầy\s+đủ|chưa\s+thực\s+sự|chưa\s+được\s+tổ\s+chức|chưa\s+có\s+gói|khoảng\s+trống|bất\s+cập|phụ\s+thuộc)[\s\S]{0,180}?\.\s*"
        r"(?:Do\s+đó|Vì\s+vậy|Như\s+vậy|Chính\s+vì\s+vậy|Đây\s+là\s+(?:cơ\s+sở|nội\s+dung|những\s+nội\s+dung|vấn\s+đề)|Các\s+hạn\s+chế\s+trên\s+là\s+cơ\s+sở|Điều\s+này\s+(?:đòi\s+hỏi|đặt\s+ra\s+yêu\s+cầu|cho\s+thấy))[^.!?]*(?:toàn\s+diện|đồng\s+bộ|hài\s+hòa|cân\s+bằng|phát\s+triển\s+bền\s+vững|tiếp\s+tục\s+(?:hoàn\s+thiện|xem\s+xét|rà\s+soát)|cần\s+(?:được\s+)?(?:hoàn\s+thiện|rà\s+soát|xây\s+dựng|điều\s+chỉnh|cải\s+thiện|kết\s+hợp|quan\s+tâm))[^.!?]*[.!?]?|"
        r"\bTuy\s+nhiên\s*,\s*(?:công\s+ty|doanh\s+nghiệp|đơn\s+vị|chi\s+nhánh|hoạt\s+động\s+[^,]{3,35}|khả\s+năng\s+[^,]{3,40})\s+vẫn\s+(?:cần\s+tiếp\s+tục\s+(?:chuẩn\s+hóa|hoàn\s+thiện|rà\s+soát|cải\s+thiện)|là\s+những\s+nội\s+dung\s+cần\s+tiếp\s+tục\s+hoàn\s+thiện)[^.!?]*[.!?]?|"
        r"Mặc dù không thể phủ nhận[^,]{5,80},\s*(?:song|nhưng)\s+cũng cần\s+(?:nhìn nhận|thừa nhận|lưu ý)[^.!?]*[.!?]?|"
        r"Một mặt\s+[^,]{5,80},\s*mặt khác\s+[^.!?]{5,90}(?:đòi hỏi sự cân nhắc|cần được xem xét hài hòa|cần có sự kết hợp)[^.!?]*[.!?]?)",
        re.IGNORECASE,
    )
    for m in arg02_re.finditer(text):
        add_flag("ARG-02", m.start(), m.end())

    # ARG-03: Macro-significance / Broad Context Inflation (expanded up to 140 chars before comma)
    arg03_re = re.compile(
        r"(?:Trong\s+bối\s+cảnh\s+(?:toàn\s+cầu\s+hóa|hội\s+nhập\s+kinh\s+tế|chuyển\s+đổi\s+số|cách\s+mạng\s+công\s+nghiệp|cạnh\s+tranh\s+ngày\s+càng\s+gay\s+gắt|nền\s+kinh\s+tế)[^.!?]{0,140}?,|"
        r"Trong\s+(?:kỷ\s+nguyên\s+kinh\s+tế\s+số|nền\s+kinh\s+tế\s+tri\s+thức\s+hiện\s+đại|thời\s+đại\s+công\s+nghệ\s+số)[^.!?]{0,100}?,|"
        r"Trước\s+những\s+biến\s+động\s+không\s+ngừng\s+của[^,]{4,90},|"
        r"Cùng\s+với\s+sự\s+phát\s+triển\s+mạnh\s+mẽ\s+của[^,]{4,90},|"
        r"\b(?:phản\s+ánh\s+xu\s+hướng\s+rộng\s+lớn\s+hơn|để\s+lại\s+dấu\s+ấn(?:\s+không\s+phai\s+mờ)?|đặt\s+nền\s+móng\s+cho|mở\s+ra\s+kỷ\s+nguyên|khẳng\s+định\s+tầm\s+vóc)\b)",
        re.IGNORECASE,
    )
    for m in arg03_re.finditer(text):
        add_flag("ARG-03", m.start(), m.end())

    # ARG-04: Formulaic Challenges & Prospects / Hollow Policy Slogans
    arg04_re = re.compile(
        r"(?:Mặc\s+dù\s+(?:đã\s+)?[^,]{5,90},\s*[^,.!?]{3,75}\s+vẫn\s+(?:còn\s+)?(?:đối\s+mặt|tồn\s+tại|gặp\s+phải|phụ\s+thuộc\s+nhiều\s+vào|chưa\s+liên\s+kết\s+đầy\s+đủ)\s+[^.!?]{5,90}|"
        r"Nếu\s+được\s+triển\s+khai\s+(?:đồng\s+bộ|phù\s+hợp)[^,]{0,60},\s*(?:hệ\s+thống\s+)?các\s+giải\s+pháp\s+(?:đề\s+xuất\s+)?có\s+thể\s+góp\s+phần\s+nâng\s+cao\s+[^.!?]+trong\s+(?:những\s+năm\s+tiếp\s+theo|thời\s+gian\s+tới|dài\s+hạn)|"
        r"đề\s+xuất\s+hệ\s+thống\s+các\s+giải\s+pháp\s+hoàn\s+thiện\s+đồng\s+bộ\s+trên\s+\d+\s+trụ\s+cột|"
        r"Thách thức và Triển vọng tương lai|"
        r"Cần tăng cường (?:hơn nữa )?(?:sự |công tác )?phối hợp đồng bộ[^.!?]{0,60}|"
        r"Đẩy mạnh (?:việc )?ứng dụng công nghệ thông tin và chuyển đổi số một cách toàn diện[^.!?]{0,50})",
        re.IGNORECASE,
    )
    for m in arg04_re.finditer(text):
        add_flag("ARG-04", m.start(), m.end())

    # PRG-01: Weasel Attribution ("Theo các chuyên gia cho rằng...") & PRG-01b Media Coverage Clichés (Karve Meilleur)
    prg01_weasel_re = re.compile(
        r"\b(?:(?:Theo\s+)?(?:các\s+chuyên\s+gia(?:\s+kinh\s+tế)?|nhiều\s+nhà\s+quan\s+sát|nhiều\s+nghiên\s+cứu|các\s+nghiên\s+cứu\s+trước\s+đây|giới\s+phân\s+tích|nhiều\s+học\s+giả|thực\s+tế\s+cho\s+thấy|thực\s+tiễn\s+cho\s+thấy|thực\s+tế\s+đã\s+chứng\s+minh\s+rằng)\s*(?:cho\s+rằng|nhận\s+định(?:\s+rằng)?|chỉ\s+ra\s+rằng|khẳng\s+định\s+rằng)?|"
        r"được\s+đưa\s+tin\s+bởi\s+[^.!?]+tạp\s+chí|được\s+đăng\s+tải\s+trên\s+các\s+ấn\s+phẩm|sự\s+đưa\s+tin\s+độc\s+lập\s+từ\s+các\s+cơ\s+quan\s+truyền\s+thông|các\s+ấn\s+phẩm\s+thương\s+mại\s+chuyên\s+ngành)\b",
        re.IGNORECASE,
    )
    for m in prg01_weasel_re.finditer(text):
        sent_ctx = _find_sentence_containing(sentences, m.start(), m.end())
        matched_lower = m.group(0).lower()
        is_media_cliche = any(w in matched_lower for w in ["đưa tin", "ấn phẩm", "tạp chí"])
        if (
            "theo các chuyên gia cho rằng" in matched_lower
            or is_media_cliche
            or (not has_academic_citation(sent_ctx) and not has_quantitative_evidence(sent_ctx))
        ):
            add_flag("PRG-01", m.start(), m.end())

    # PRG-02: Comprehensive 3-Branch Disclaimers (PRG-02a Didactic, PRG-02b Data Scarcity, PRG-02c Methodological Hedging)
    prg02_re = re.compile(
        r"\b(?:"
        # PRG-02a: Didactic hedging
        r"điều\s+quan\s+trọng\s+(?:cần\s+lưu\s+ý\s+)?là|cần\s+(?:phải\s+)?(?:lưu\s+ý|nhớ|nhấn\s+mạnh)\s+rằng|một\s+(?:điểm|lưu\s+ý|nguyên\s+tắc)\s+(?:quan\s+trọng\s+)?cần\s+(?:nhấn\s+mạnh|lưu\s+ý)\s+là|không\s+ngoa\s+khi\s+nói\s+rằng|"
        # PRG-02b: Prompt data scarcity self-disclaimer (WP:AIDISCLAIMER)
        r"trong\s+phạm\s+vi\s+dữ\s+liệu\s+nghiên\s+cứu,\s*chưa\s+có\s+(?:tài\s+liệu|cơ\s+sở|thông\s+tin)\s+cho\s+thấy|(?:tài\s+liệu|báo\s+cáo)\s+(?:chưa|không)\s+(?:có|công\s+bố)\s+số\s+liệu\s+(?:riêng|chi\s+tiết)\s+(?:về|theo)|mặc\s+dù\s+chi\s+tiết\s+cụ\s+thể\s+không\s+được\s+công\s+bố(?:\s+rộng\s+rãi)?|dữ\s+liệu\s+hiện\s+có\s+mới\s+cho\s+thấy[^.!?]*?để\s+khẳng\s+định\s+quan\s+hệ\s+nhân\s+quả\s+cần\s+thêm|"
        # PRG-02c: Methodological & metric interpretation disclaimer (E-COM WOW, An Cường, Hecatech)
        r"(?:khóa\s+luận|nghiên\s+cứu|chuyên\s+đề|tác\s+giả)\s+(?:không\s+sử\s+dụng\s+[^.!?]{3,55}\s+để\s+[^.!?]{3,55}\s+mà\s+chỉ\s+coi\s+đây\s+là\s+khung\s+tham\s+chiếu|(?:chỉ\s+)?sử\s+dụng\s+[^.!?]{2,55}\s+như\s+(?:một\s+|các\s+)?(?:khung\s+tham\s+chiếu|chỉ\s+báo\s+bổ\s+sung|cơ\s+sở\s+bổ\s+trợ)[^.!?]*?(?:,\s*không\s+(?:coi|dùng|sử\s+dụng|đồng\s+nhất)|và\s+kết\s+hợp\s+với|và\s+không\s+dùng))|"
        r"hai\s+loại\s+điểm\s+không\s+được\s+sử\s+dụng\s+để\s+tính\s+một\s+khoảng\s+chênh\s+lệch|"
        r"đây\s+chỉ\s+là\s+các\s+chỉ\s+báo\s+gián\s+tiếp\s+và\s+không\s+được\s+sử\s+dụng\s+để\s+khẳng\s+định\s+trực\s+tiếp|"
        r"không\s+tính\s+trực\s+tiếp\s+(?:khoảng\s+)?chênh\s+lệch\s+giữa\s+hai\s+loại\s+điểm\s+vì\s+hai\s+loại\s+điểm\s+phản\s+ánh\s+hai\s+khía\s+cạnh\s+khác\s+nhau|"
        r"không\s+dùng\s+sự\s+thay\s+đổi\s+của\s+chỉ\s+tiêu\s+này\s+để\s+khẳng\s+định\s+trực\s+tiếp\s+quan\s+hệ\s+nhân\s+quả"
        r")\b",
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
