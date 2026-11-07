"""
Single-Source 26-Sign Python Rule Engine & 6 Quantitative Metrics Calculator
(CV_L, ISI, OPR, SVCI, SICD, BCR).
"""

import math
import re
from typing import Any, Dict, List, Optional, Tuple
from api.engine.lexicon import (
    RULE_METADATA,
    SINO_VIETNAMESE_ABSTRACT_SYLLABLES,
)
from api.engine.tokenizer import (
    count_vietnamese_words,
    mask_protected_economics_terms,
    split_vietnamese_sentences,
)


def _make_flag(
    rule_id: str,
    para_index: int,
    flag_index: int,
    start: int,
    end: int,
    full_text: str,
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
        "suggestion": custom_suggestion or meta["userSuggestion"],
        "start": safe_start,
        "end": safe_end,
    }


def _find_max_sino_vietnamese_run(masked_text: str, original_text: str) -> Tuple[int, Optional[Tuple[int, int]]]:
    """
    Calculates SVCI (longest contiguous run of Sino-Vietnamese abstract syllables
    outside masked 8-field Economics terms).
    """
    token_iter = list(re.finditer(r"[^\s.,;:!?()\[\]{}'\"“”‘’—–-]+", masked_text))
    max_run = 0
    best_span: Optional[Tuple[int, int]] = None

    cur_run = 0
    cur_start = 0
    cur_end = 0

    for tok_match in token_iter:
        tok_str = tok_match.group(0).lower()
        if "§" in tok_str:
            if cur_run > max_run:
                max_run = cur_run
                best_span = (cur_start, cur_end)
            cur_run = 0
            continue

        if tok_str in SINO_VIETNAMESE_ABSTRACT_SYLLABLES:
            if cur_run == 0:
                cur_start = tok_match.start()
            cur_run += 1
            cur_end = tok_match.end()
        else:
            if cur_run > max_run:
                max_run = cur_run
                best_span = (cur_start, cur_end)
            cur_run = 0

    if cur_run > max_run:
        max_run = cur_run
        best_span = (cur_start, cur_end)

    return max_run, best_span


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

    sentences = split_vietnamese_sentences(text)
    masked_text, protected_spans = mask_protected_economics_terms(text)
    total_words = max(1, count_vietnamese_words(text))
    n_sent = len(sentences)

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
        # Avoid duplicate ruleId on identical span
        for existing in flags:
            if existing["ruleId"] == rule_id and abs(existing["start"] - start) < 8:
                return
        flags.append(
            _make_flag(
                rule_id,
                index,
                flag_counter,
                start,
                end,
                text,
                custom_suggestion=custom_suggestion,
                custom_title=custom_title,
                custom_reason=custom_reason,
            )
        )
        flag_counter += 1

    # -------------------------------------------------------------------------
    # METRIC 1 & RHY-01: Sentence Length Coefficient of Variation (CV_L)
    # Only evaluated when paragraph has >= 4 sentences
    # -------------------------------------------------------------------------
    lengths = [s["word_count"] for s in sentences if s["word_count"] > 0]
    if len(lengths) >= 4:
        mean_l = sum(lengths) / len(lengths)
        variance_l = sum((l - mean_l) ** 2 for l in lengths) / len(lengths)
        std_l = math.sqrt(variance_l)
        cv_length = round(std_l / mean_l, 4) if mean_l > 0 else 0.0
        delta_length = max(lengths) - min(lengths)

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
    # P0: FOR-01 (Forensic Artifacts, Leaked Citation Tags, Hallucinated DOIs)
    # -------------------------------------------------------------------------
    for_patterns = [
        r"\([^)]*contentReference\[oaicite[^\)]*\)",
        r"contentReference\[oaicite[^\]]*\](?:\{index=\d+\})?",
        r"turn0search\d+",
        r"\[span_\d+\]",
        r"grok_card",
        r"utm_source=chatgpt\.com",
        r"\[attached_file:[^\]]+\]",
        r":::writing",
        r"Chắc chắn rồi!\s*Dưới đây là[^.!?\n]*[.!?]?",
        r"Hy vọng thông tin này hữu ích[^.!?\n]*[.!?]?",
        r"\[Điền [^\]]+ vào đây\]",
        r"doi:\s*10\.\d{4,9}/[^\s)]*9999\d*",
    ]
    for pat in for_patterns:
        for m in re.finditer(pat, text, re.IGNORECASE):
            add_flag("FOR-01", m.start(), m.end())
            break
        if any(f["ruleId"] == "FOR-01" for f in flags):
            break

    # -------------------------------------------------------------------------
    # FMT-01: Mechanical Formatting (Inline bold bullet headers, excessive em-dashes)
    # -------------------------------------------------------------------------
    fmt_match = re.search(r"(?:^|\n)\s*[-*•]\s*\*\*[^*]+\*\*\s*:", text)
    if fmt_match:
        add_flag("FMT-01", fmt_match.start(), fmt_match.end())
    elif text.count("—") >= 2:
        first_dash = text.find("—")
        add_flag("FMT-01", max(0, first_dash - 15), min(len(text), first_dash + 45))

    # -------------------------------------------------------------------------
    # METRIC 5 & DIS-01, DIS-02, DIS-03, DIS-04: Discourse & Paragraph Framing
    # -------------------------------------------------------------------------
    connective_openers = (
        r"^(?:Cụ thể|Tuy nhiên|Do đó|Hơn nữa|Thêm vào đó|Bên cạnh đó|"
        r"Ngoài ra|Đáng chú ý là|Thật vậy|Ngược lại|Vì vậy|Như vậy|Mặt khác)\s*,"
    )
    conn_matches = []
    for s in sentences:
        m = re.match(connective_openers, s["text"], re.IGNORECASE)
        if m:
            conn_matches.append((s, m))

    sicd = round(len(conn_matches) / max(1, n_sent), 4)
    if len(conn_matches) >= 2 and sicd > 0.25:
        first_s, first_m = conn_matches[0]
        add_flag(
            "DIS-03",
            first_s["start"],
            first_s["start"] + first_m.end(),
        )

    # DIS-01: 4-step Boxed Paragraph ([Topic] -> [Cụ thể,] -> [Tuy nhiên,] -> [Do đó,/Như vậy,])
    bcr = 0.0
    if n_sent >= 4:
        s1_txt = sentences[1]["text"]
        s2_txt = sentences[2]["text"]
        s_last = sentences[-1]
        has_elab = bool(re.match(r"^(?:Cụ thể|Thực tế|Theo đó|Trước hết)\s*,", s1_txt, re.IGNORECASE))
        has_pivot = bool(re.match(r"^(?:Tuy nhiên|Song|Mặt khác|Ngược lại|Bên cạnh đó)\s*,", s2_txt, re.IGNORECASE))
        has_box_close = bool(
            re.match(
                r"^(?:Do đó|Như vậy|Tóm lại|Vì vậy|Chính vì vậy)\s*,",
                s_last["text"],
                re.IGNORECASE,
            )
            or re.search(r"để đảm bảo sự phát triển bền vững|phát triển bền vững", s_last["text"], re.IGNORECASE)
        )
        if (has_elab and has_pivot and has_box_close) or (len(conn_matches) >= 3 and has_box_close):
            bcr = 1.0
            add_flag("DIS-01", s_last["start"], s_last["end"])

    # DIS-02: Redundant summary sentence
    dis02_match = re.search(
        r"(?:Tóm lại,\s*có thể khẳng định chắc chắn rằng[^.!?]+[.!?]?|"
        r"(?:Tóm lại|Nhìn chung|Như vậy,\s*qua đó có thể thấy|Chính vì vậy)\s*,[^.!?]*(?:chìa khóa vàng|thành công rực rỡ|kỷ nguyên mới|phát triển bền vững)[^.!?]*[.!?]?)",
        text,
        re.IGNORECASE,
    )
    if dis02_match:
        bcr = 1.0
        add_flag("DIS-02", dis02_match.start(), dis02_match.end())

    # DIS-04: Header-echo definition opener
    dis04_match = re.search(
        r"^[^,.]{3,60}\s+(?:là một tập hợp các|đề cập đến quá trình|được định nghĩa như là một khái niệm)\b",
        text.strip(),
        re.IGNORECASE,
    )
    if dis04_match:
        add_flag("DIS-04", dis04_match.start(), dis04_match.end())

    # -------------------------------------------------------------------------
    # METRIC 2 & SYN-01, SYN-02, SYN-03, SYN-04: Syntactic Patterns
    # -------------------------------------------------------------------------
    adv_opener_re = re.compile(
        r"^(?:Trong bối cảnh|Trước những|Thông qua việc|Trên phương diện|Về mặt|Đối với|Nhằm hướng tới)\b[^,]{3,65},",
        re.IGNORECASE,
    )
    tail_clause_re = re.compile(
        r",\s*(?:qua đó|từ đó|góp phần|điều này phản ánh|mở ra triển vọng|tạo tiền đề vững chắc)\s+[^.!?]+[.!?]?",
        re.IGNORECASE,
    )

    isomorphic_sentences = []
    for s in sentences:
        has_adv = bool(adv_opener_re.search(s["text"]))
        has_tail = bool(tail_clause_re.search(s["text"]))
        if has_adv and has_tail:
            isomorphic_sentences.append(s)
        if has_tail:
            tm = tail_clause_re.search(s["text"])
            if tm:
                add_flag(
                    "SYN-02",
                    s["start"] + tm.start() + 2,
                    s["start"] + tm.end(),
                )

    isi = round(len(isomorphic_sentences) / max(1, n_sent), 4)
    if len(isomorphic_sentences) >= 2:
        add_flag(
            "SYN-01",
            isomorphic_sentences[0]["start"],
            isomorphic_sentences[-1]["end"],
        )

    # SYN-03: Negative Parallelism ("không chỉ... mà còn...", "không đơn thuần là... mà là...")
    syn03_match = re.search(
        r"(?:Đây\s+)?(?:không\s+chỉ\s+(?:là\s+)?[^.!?]{3,80}\s+mà\s+còn\s+(?:là\s+)?[^.!?]{3,80}|"
        r"không\s+đơn\s+thuần\s+là\s+[^.!?]{3,60}\s+mà\s+(?:còn\s+)?là\s+[^.!?]{3,60})",
        text,
        re.IGNORECASE,
    )
    if syn03_match:
        add_flag("SYN-03", syn03_match.start(), syn03_match.end())

    # SYN-04: Mechanical Rule of Three
    syn04_match = re.search(
        r"(?:đồng bộ,\s*toàn diện\s+và\s+hiệu quả|"
        r"đồng bộ,\s*hài hòa\s+và\s+bền vững|"
        r"(?:qua đó\s+)?(?:góp phần\s+)?nâng cao\s+[^,.]+,\s*tối ưu hóa\s+[^,.]+\s+và\s+thúc đẩy\s+[^.!?]+)",
        text,
        re.IGNORECASE,
    )
    if syn04_match:
        add_flag("SYN-04", syn04_match.start(), syn04_match.end())

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
    if opr_matches:
        m0 = opr_matches[0]
        add_flag("SYN-VN-01", m0.start(), m0.end())

    # SYN-VN-02: Topic-Comment loss ("Đối với vấn đề X, nó thường được...")
    syn_vn02_match = re.search(
        r"(?:Đối với vấn đề|Liên quan đến khía cạnh|Xét trên phương diện)\s+[^,]+,\s*(?:nó\s+)?(?:thường\s+)?(?:được|bị)?",
        text,
        re.IGNORECASE,
    )
    if syn_vn02_match:
        add_flag("SYN-VN-02", syn_vn02_match.start(), syn_vn02_match.end())

    # SYN-VN-03: Passive calque & foreign nominalization
    syn_vn03_match = re.search(
        r"(?:việc\s+[^,.]{3,65}\s+được\s+thực\s+hiện\s+bởi\s+[^,.]{3,50}(?:\s+đã\s+được\s+chứng\s+minh\s+là\s+có\s+sự\s+ảnh\s+hưởng\s+đáng\s+kể)?|"
        r"thông qua việc thực hiện quy trình[^,.]{3,60}|"
        r"\b(?:được|bị)\s+[a-zA-ZÀ-ỹ\s]{2,30}\s+bởi\b)",
        text,
        re.IGNORECASE,
    )
    if syn_vn03_match:
        add_flag("SYN-VN-03", syn_vn03_match.start(), syn_vn03_match.end())

    # -------------------------------------------------------------------------
    # METRIC 4 & LEX-VN-01, LEX-01..05: Lexical & Sino-Vietnamese Congestion
    # -------------------------------------------------------------------------
    svci, sv_span = _find_max_sino_vietnamese_run(masked_text, text)
    nominal_chain_match = re.search(
        r"(?:thực hiện quy trình chuyển đổi mô hình quản trị[^,.]{0,40}|"
        r"thực hiện việc tiết giảm|triển khai sự tái cấu trúc|quá trình tối ưu hóa hiệu suất)",
        masked_text,
        re.IGNORECASE,
    )
    if nominal_chain_match:
        svci = max(svci, 8)
        add_flag("LEX-VN-01", nominal_chain_match.start(), nominal_chain_match.end())
    elif svci >= 7 and sv_span is not None:
        add_flag("LEX-VN-01", sv_span[0], sv_span[1])

    # LEX-01: AI Vocabulary & Clichés
    lex01_match = re.search(
        r"(?:đóng vai trò (?:như một chất xúc tác )?then chốt(?:\s+và\s+mang\s+tính\s+bước\s+ngoặt\s+lịch\s+sử)?|"
        r"bức tranh toàn cảnh|tấm thảm đa sắc|điều hướng qua những thách thức|"
        r"tích hợp một cách liền mạch|sự giao thoa phức tạp|bối cảnh không ngừng biến đổi|"
        r"nuôi dưỡng sự đổi mới)",
        text,
        re.IGNORECASE,
    )
    if lex01_match:
        add_flag("LEX-01", lex01_match.start(), lex01_match.end())

    # LEX-02: Copula Avoidance
    lex02_match = re.search(
        r"(?:đóng vai trò như là|đóng vai trò là|đứng như một|hoạt động như một|giữ vị thế là|tự hào có|nổi bật với)",
        text,
        re.IGNORECASE,
    )
    if lex02_match:
        add_flag("LEX-02", lex02_match.start(), lex02_match.end())

    # LEX-03: Promotional Puffery
    lex03_match = re.search(
        r"(?:mang tính bước ngoặt lịch sử|bước ngoặt lịch sử|minh chứng sống động cho|"
        r"tiên phong mang tính đột phá|sự kết hợp hoàn hảo giữa|chìa khóa vàng mở ra cánh cửa thành công rực rỡ|"
        r"cam kết không ngừng nghỉ|bề dày lịch sử phong phú)",
        text,
        re.IGNORECASE,
    )
    if lex03_match:
        add_flag("LEX-03", lex03_match.start(), lex03_match.end())

    # LEX-04: Artificial Synonym Cycling
    synonym_cycle_groups = [
        [r"ngân hàng này", r"tổ chức tín dụng này", r"định chế tài chính", r"nhà băng này"],
    ]
    for grp in synonym_cycle_groups:
        found = [re.search(p, text, re.IGNORECASE) for p in grp]
        found = [m for m in found if m is not None]
        if len(found) >= 2:
            add_flag("LEX-04", found[0].start(), found[-1].end())

    # LEX-05: Vague Association
    lex05_match = re.search(
        r"(?:gắn liền với các hoạt động|có mối liên hệ mật thiết với|"
        r"được ghi nhận trong mối tương quan với|xoay quanh các lĩnh vực liên quan đến)",
        text,
        re.IGNORECASE,
    )
    if lex05_match:
        add_flag("LEX-05", lex05_match.start(), lex05_match.end())

    # -------------------------------------------------------------------------
    # ARG-01..04 & PRG-01..02: Argumentation & Epistemic Stance
    # -------------------------------------------------------------------------
    # ARG-01: Flat Epistemic Weight ("Thứ nhất,... Thứ hai,... Thứ ba,..." without numbers)
    if (
        re.search(r"Thứ nhất\s*,.*Thứ hai\s*,.*Thứ ba\s*,", text, re.IGNORECASE | re.DOTALL)
        and not re.search(r"\d+\s*%", text)
    ):
        add_flag("ARG-01", 0, len(text))

    # ARG-02: Pendulum Hedging ("Tuy nhiên... thách thức... Do đó... toàn diện / hài hòa ... bền vững")
    arg02_match = re.search(
        r"Tuy nhiên\s*,[^.!?]*(?:thách thức|hạn chế|rủi ro)[^.!?]*\.\s*"
        r"(?:Do đó|Vì vậy|Như vậy)\s*,[^.!?]*(?:toàn diện|đồng bộ|hài hòa|cân bằng|phát triển bền vững)[^.!?]*[.!?]?",
        text,
        re.IGNORECASE,
    )
    if arg02_match:
        add_flag("ARG-02", arg02_match.start(), arg02_match.end())

    # ARG-03: Macro-significance / Broad Context Inflation
    arg03_match = re.search(
        r"(?:Trong bối cảnh toàn cầu hóa và cuộc cách mạng công nghiệp[^,]*,|"
        r"phản ánh xu hướng rộng lớn hơn|để lại dấu ấn không phai mờ|đặt nền móng cho)",
        text,
        re.IGNORECASE,
    )
    if arg03_match:
        add_flag("ARG-03", arg03_match.start(), arg03_match.end())

    # ARG-04: Formulaic Challenges & Prospects
    arg04_match = re.search(
        r"(?:Mặc dù đạt được\s+[^,]+,\s*[^,]+\s+vẫn đối mặt với nhiều thách thức|Thách thức và Triển vọng tương lai)",
        text,
        re.IGNORECASE,
    )
    if arg04_match:
        add_flag("ARG-04", arg04_match.start(), arg04_match.end())

    # PRG-01: Weasel Attribution
    prg01_match = re.search(
        r"(?:Theo\s+)?(?:các chuyên gia cho rằng|nhiều nhà quan sát nhận định|"
        r"sự đưa tin độc lập từ các cơ quan truyền thông|các ấn phẩm thương mại chuyên ngành)",
        text,
        re.IGNORECASE,
    )
    if prg01_match:
        add_flag("PRG-01", prg01_match.start(), prg01_match.end())

    # PRG-02: Didactic Hedging & Disclaimer
    prg02_match = re.search(
        r"(?:điều quan trọng cần lưu ý là|cần phải nhớ rằng|"
        r"mặc dù chi tiết cụ thể không được công bố rộng rãi)",
        text,
        re.IGNORECASE,
    )
    if prg02_match:
        add_flag("PRG-02", prg02_match.start(), prg02_match.end())

    # Calculate composite intensity score (0..100) for internal evaluation
    weights = {"critical": 35, "warning": 18, "suggestion": 12}
    raw_score = sum(weights.get(f["severity"], 12) for f in flags)
    ai_style_score = min(100, raw_score)

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
