"""
Section-Level & Document-Level Academic Writing Auditor + Sample Economics Thesis Payload.
Includes Cross-Paragraph Discourse Auditing (ARG-01 multi-paragraph ordinal uniformity,
SYN-01b paragraph-initial syntactic isomorphism, DIS-03 cross-paragraph connective chains,
section-wide BCR calculation) and Length-Weighted Prose Score Aggregation.
"""

import math
import re
from typing import Any, Dict, List, Optional, Tuple
from api.engine.lexicon import RULE_METADATA, UNIFIED_ECONOMICS_TERMS
from api.engine.rules import _make_flag, audit_paragraph
from api.engine.tokenizer import has_academic_citation, has_quantitative_evidence


SAMPLE_THESIS_PAYLOAD: Dict[str, Any] = {
    "title": "Ban_thao_luan_van_Kinh_te_Tai_chinh_Chuoi_cung_ung.docx",
    "sections": [
        {
            "id": "sec-1",
            "title": "Chương 1: Cơ sở lý luận và Tổng quan nghiên cứu",
            "shortTitle": "Chương 1: Cơ sở lý luận",
            "sectionLabel": "Chương 1 · Mục 1.1 – 1.2",
            "isExcluded": False,
            "paragraphs": [
                (
                    "Trong bối cảnh toàn cầu hóa và cuộc cách mạng công nghiệp diễn ra mạnh mẽ hiện nay, "
                    "hoạt động tối ưu hóa chuỗi cung ứng lạnh kết hợp với quản trị vốn lưu động ròng "
                    "đóng vai trò như một chất xúc tác then chốt và mang tính bước ngoặt lịch sử "
                    "đối với năng lực cạnh tranh của các doanh nghiệp sản xuất và phân phối."
                ),
                (
                    "Việc đồng bộ dữ liệu hàng tồn kho theo thời gian thực giúp doanh nghiệp chủ động điều phối nguồn lực, "
                    "qua đó góp phần nâng cao hiệu suất sử dụng tài sản, tối ưu hóa chi phí giao dịch và thúc đẩy giá trị bền vững cho cổ đông."
                ),
            ],
        },
        {
            "id": "sec-2",
            "title": "Chương 2: Phương pháp nghiên cứu và Dữ liệu",
            "shortTitle": "Chương 2: Phương pháp nghiên cứu",
            "sectionLabel": "Chương 2 · Mục 2.1 – 2.2",
            "isExcluded": False,
            "paragraphs": [
                (
                    "Khi đánh giá tác động của đòn bẩy tài chính và tỷ lệ an toàn vốn tối thiểu lên tỷ suất sinh lời trên tổng tài sản, "
                    "việc các quyết định phân bổ ngân sách được thực hiện bởi bộ phận kế toán quản trị đã được chứng minh là có sự ảnh hưởng đáng kể "
                    "tới khả năng kiểm soát chi phí đại diện trong doanh nghiệp."
                ),
            ],
        },
        {
            "id": "sec-3",
            "title": "Chương 3: Kết quả phân tích và Thảo luận",
            "shortTitle": "Chương 3: Kết quả và Thảo luận",
            "sectionLabel": "Chương 3 · Mục 3.1 – 3.2",
            "isExcluded": False,
            "paragraphs": [
                (
                    "Kết quả ước lượng trên dữ liệu bảng cho thấy thời gian lưu kho trung bình giảm có ý nghĩa thống kê ở mức 1%. "
                    "Theo tổng hợp mới nhất (Nguyen & Tran, 2024, doi:10.1016/j.jcorpfin.2024.999999 — contentReference[oaicite:0]{index=0}), "
                    "việc tích hợp hệ thống dự báo nhu cầu giúp giảm 18,4% lượng hàng tồn kho chậm luân chuyển."
                ),
                (
                    "Đây không chỉ là một giải pháp vận hành đơn thuần mà còn là một tuyên ngôn chiến lược toàn diện "
                    "giúp doanh nghiệp duy trì thanh khoản hệ thống ổn định trong giai đoạn biến động lãi suất."
                ),
            ],
        },
        {
            "id": "sec-4",
            "title": "Chương 4: Kết luận và Khuyến nghị quản trị",
            "shortTitle": "Chương 4: Kết luận và Khuyến nghị",
            "sectionLabel": "Chương 4 · Mục 4.1 – 4.2",
            "isExcluded": False,
            "paragraphs": [
                (
                    "Tóm lại, có thể khẳng định chắc chắn rằng sự kết hợp hài hòa giữa quản trị nguồn nhân lực, tiếp thị kỹ thuật số "
                    "và quản trị sản xuất tinh gọn chính là chìa khóa vàng mở ra cánh cửa thành công rực rỡ cho mọi doanh nghiệp trong kỷ nguyên mới."
                ),
            ],
        },
    ],
}

# Cross-paragraph discourse regexes
_ORDINAL_PARA_OPENER_RE = re.compile(
    r"^(?:Thứ\s+(?:nhất|hai|ba|tư|năm)|(?:Một|Hai|Ba|Bốn|Năm)\s+là)\s*[,:]",
    re.IGNORECASE | re.UNICODE,
)

_PARA_FRAME_OPENER_RE = re.compile(
    r"^(?:Thông\s+qua\s+việc|Bằng\s+việc|Bằng\s+cách|Dựa\s+trên|Trên\s+cơ\s+sở|Về\s+mặt|Về\s+phương\s+diện|Xét\s+về|Xét\s+trên\s+phương\s+diện|Đối\s+với|Trong\s+bối\s+cảnh|Trước\s+những|Cùng\s+với\s+sự)\s+[^,]{3,60},",
    re.IGNORECASE | re.UNICODE,
)

_PARA_CONNECTIVE_OPENER_RE = re.compile(
    r"^(?:Hơn\s+nữa|Bên\s+cạnh\s+đó|Ngoài\s+ra|Thêm\s+vào\s+đó|Đồng\s+thời|Mặt\s+khác|Không\s+những\s+vậy|Tuy\s+nhiên|Do\s+đó|Vì\s+vậy)\s*,",
    re.IGNORECASE | re.UNICODE,
)


def _append_cross_para_flag(
    p_res: Dict[str, Any],
    rule_id: str,
    start: int,
    end: int,
    custom_suggestion: Optional[str] = None,
) -> None:
    """Safely appends a cross-paragraph flag to a paragraph result and updates its score."""
    for existing in p_res["flags"]:
        if existing["ruleId"] == rule_id and not (
            end <= existing["start"] or start >= existing["end"]
        ):
            return
    flag_index = len(p_res["flags"]) + 1
    new_flg = _make_flag(
        rule_id=rule_id,
        para_index=p_res["index"],
        flag_index=flag_index,
        start=start,
        end=end,
        full_text=p_res["text"],
        sentence_text=p_res["text"][start:end],
        custom_suggestion=custom_suggestion,
    )
    p_res["flags"].append(new_flg)
    weights = {"critical": 35, "warning": 18, "suggestion": 12}
    p_res["aiStyleScore"] = min(100, p_res["aiStyleScore"] + weights.get(new_flg["severity"], 12))


def _run_cross_paragraph_discourse_pass(para_results: List[Dict[str, Any]]) -> None:
    """
    Executes multi-paragraph discourse analysis across a section's paragraphs:
    1. Cross-paragraph ARG-01: 3+ paragraphs starting with 'Thứ nhất / Thứ hai / Thứ ba'
       with uniform word counts (CV < 0.22) and low empirical evidence.
    2. Cross-paragraph SYN-01 (SYN-01b): 3+ consecutive paragraphs opening with the same
       adverbial/prepositional template frame.
    3. Cross-paragraph DIS-03: 3+ consecutive paragraphs opening with mechanical connectives.
    4. Section-level BCR (Boxed Closure Rate) aggregation across multi-sentence prose paragraphs.
    """
    n_paras = len(para_results)
    if n_paras < 2:
        return

    # 1. Cross-paragraph ARG-01 (Ordinal Paragraph Sequences)
    ordinal_indices: List[int] = []
    for idx, p_res in enumerate(para_results):
        if _ORDINAL_PARA_OPENER_RE.match(p_res["text"].strip()):
            ordinal_indices.append(idx)

    if len(ordinal_indices) >= 3:
        lengths = [para_results[i]["wordCount"] for i in ordinal_indices if para_results[i]["wordCount"] > 0]
        if len(lengths) >= 3:
            mean_l = sum(lengths) / len(lengths)
            std_l = math.sqrt(sum((l - mean_l) ** 2 for l in lengths) / len(lengths))
            cv_para = (std_l / mean_l) if mean_l > 0 else 1.0
            emp_count = sum(
                1
                for i in ordinal_indices
                if has_quantitative_evidence(para_results[i]["text"])
                or has_academic_citation(para_results[i]["text"])
            )
            if cv_para < 0.22 and emp_count < (len(ordinal_indices) / 2.0):
                for i in ordinal_indices:
                    txt = para_results[i]["text"]
                    m_ord = _ORDINAL_PARA_OPENER_RE.match(txt.strip())
                    e_pos = m_ord.end() if m_ord else min(40, len(txt))
                    _append_cross_para_flag(
                        para_results[i],
                        "ARG-01",
                        0,
                        e_pos,
                        custom_suggestion=(
                            "Các đoạn luận điểm 'Thứ nhất / Thứ hai / Thứ ba' đang có độ dài quá đồng đều "
                            "và thiếu số liệu thực nghiệm; hãy bổ sung dẫn chứng định lượng cho luận điểm trọng tâm."
                        ),
                    )

    # 2. Cross-paragraph SYN-01b (3+ consecutive paragraphs opening with adverbial frames)
    run_frame: List[Tuple[int, re.Match]] = []
    for idx, p_res in enumerate(para_results):
        m_fr = _PARA_FRAME_OPENER_RE.match(p_res["text"])
        if m_fr:
            run_frame.append((idx, m_fr))
        else:
            if len(run_frame) >= 3:
                for p_i, match_obj in run_frame:
                    _append_cross_para_flag(
                        para_results[p_i],
                        "SYN-01",
                        match_obj.start(),
                        match_obj.end(),
                        custom_suggestion=(
                            "Ba đoạn văn liên tiếp đều mở đầu bằng cùng một khuôn trạng ngữ; "
                            "hãy đảo chủ ngữ kinh tế hoặc số liệu thực tế lên đầu đoạn."
                        ),
                    )
            run_frame = []
    if len(run_frame) >= 3:
        for p_i, match_obj in run_frame:
            _append_cross_para_flag(
                para_results[p_i],
                "SYN-01",
                match_obj.start(),
                match_obj.end(),
            )

    # 3. Cross-paragraph DIS-03 (3+ consecutive paragraphs opening with mechanical connectives)
    run_conn: List[Tuple[int, re.Match]] = []
    for idx, p_res in enumerate(para_results):
        m_cn = _PARA_CONNECTIVE_OPENER_RE.match(p_res["text"])
        if m_cn:
            run_conn.append((idx, m_cn))
        else:
            if len(run_conn) >= 3:
                for p_i, match_obj in run_conn:
                    _append_cross_para_flag(
                        para_results[p_i],
                        "DIS-03",
                        match_obj.start(),
                        match_obj.end(),
                    )
            run_conn = []
    if len(run_conn) >= 3:
        for p_i, match_obj in run_conn:
            _append_cross_para_flag(
                para_results[p_i],
                "DIS-03",
                match_obj.start(),
                match_obj.end(),
            )

    # 4. Section-level BCR (Boxed Closure Rate) across multi-sentence prose paragraphs
    multi_sent_paras = [p for p in para_results if p["sentenceCount"] >= 3]
    if len(multi_sent_paras) >= 3:
        boxed_count = sum(1 for p in multi_sent_paras if p["metrics"].get("bcr", 0.0) >= 1.0)
        section_bcr = round(boxed_count / len(multi_sent_paras), 4)
        for p in multi_sent_paras:
            if p["metrics"].get("bcr", 0.0) > 0:
                p["metrics"]["bcr"] = max(p["metrics"]["bcr"], section_bcr)


def _compute_section_score(para_results: List[Dict[str, Any]]) -> int:
    """
    Computes length-weighted section AI Style Score (0-100), ignoring short non-prose
    fragments (< 10 words, such as stray labels or captions) when genuine prose paragraphs exist.
    """
    if not para_results:
        return 0

    prose_paras = [p for p in para_results if p["wordCount"] >= 10]
    target_paras = prose_paras if prose_paras else para_results

    total_w = sum(max(1, p["wordCount"]) for p in target_paras)
    if total_w <= 0:
        return 0

    weighted_sum = sum(p["aiStyleScore"] * max(1, p["wordCount"]) for p in target_paras)
    return min(100, round(weighted_sum / total_w))


def audit_document_sections(title: str, sections: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Audits all non-excluded sections of a thesis/manuscript and aggregates
    findings, severity counts, and document-level statistics.
    """
    safe_title = str(title).strip() if title else "Ban_thao_hoc_thuat.docx"
    audited_sections: List[Dict[str, Any]] = []
    all_flags: List[Dict[str, Any]] = []
    total_words = 0
    total_sentences = 0
    protected_terms_set = set()
    global_finding_seq = 1

    if not isinstance(sections, list):
        sections = []

    for sec_idx, raw_sec in enumerate(sections):
        sec = raw_sec if isinstance(raw_sec, dict) else {}
        sec_id = str(sec.get("id") or f"sec-{sec_idx + 1}")
        sec_title = str(sec.get("title") or f"Chương {sec_idx + 1}")
        short_title = (
            str(sec.get("shortTitle"))
            if sec.get("shortTitle")
            else (sec_title.split(":")[0].strip() if ":" in sec_title else sec_title)
        )
        section_label = str(sec.get("sectionLabel") or f"Phần {sec_idx + 1} · Bản thảo")
        parent_heading = str(sec.get("parentHeading") or "").strip()
        is_excluded = bool(sec.get("isExcluded", False))
        raw_paragraphs_input = sec.get("paragraphs")
        raw_paragraphs: List[str] = (
            [str(p) for p in raw_paragraphs_input if p is not None and str(p).strip()]
            if isinstance(raw_paragraphs_input, list)
            else (
                [str(raw_paragraphs_input)]
                if isinstance(raw_paragraphs_input, str) and raw_paragraphs_input.strip()
                else []
            )
        )

        if is_excluded:
            audited_sections.append(
                {
                    "id": sec_id,
                    "chapterNumber": sec_idx + 1,
                    "title": sec_title,
                    "shortTitle": short_title,
                    "sectionLabel": section_label,
                    "parentHeading": parent_heading,
                    "isExcluded": True,
                    "wordCount": sum(len(p.split()) for p in raw_paragraphs),
                    "flagCount": 0,
                    "aiStyleScore": 0,
                    "paragraphs": [
                        {
                            "index": p_i,
                            "text": p_txt,
                            "wordCount": len(p_txt.split()),
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
                        for p_i, p_txt in enumerate(raw_paragraphs)
                    ],
                }
            )
            continue

        para_results: List[Dict[str, Any]] = []
        sec_flags: List[Dict[str, Any]] = []
        sec_words = 0

        for p_idx, p_text in enumerate(raw_paragraphs):
            p_res = audit_paragraph(p_text, p_idx)
            sec_words += p_res["wordCount"]
            total_words += p_res["wordCount"]
            total_sentences += p_res["sentenceCount"]
            for term in p_res["protectedTerms"]:
                protected_terms_set.add(term)
            para_results.append(p_res)

        # Execute Cross-Paragraph Discourse Pass on the section's paragraphs
        _run_cross_paragraph_discourse_pass(para_results)

        # Collect all paragraph flags and assign globally unique finding IDs for UI navigation
        for p_idx, p_res in enumerate(para_results):
            for flg in p_res["flags"]:
                flg["id"] = f"f{global_finding_seq}"
                flg["sectionId"] = sec_id
                flg["chapterNumber"] = sec_idx + 1
                flg["chapterTitle"] = sec_title
                flg["paragraphIndex"] = p_idx
                flg["status"] = "pending"
                global_finding_seq += 1
                sec_flags.append(flg)
                all_flags.append(flg)

        sec_score = _compute_section_score(para_results)

        audited_sections.append(
            {
                "id": sec_id,
                "chapterNumber": sec_idx + 1,
                "title": sec_title,
                "shortTitle": short_title,
                "sectionLabel": section_label,
                "parentHeading": parent_heading,
                "isExcluded": False,
                "wordCount": sec_words,
                "flagCount": len(sec_flags),
                "aiStyleScore": sec_score,
                "paragraphs": para_results,
            }
        )

    critical_count = sum(1 for f in all_flags if f["severity"] == "critical")
    warning_count = sum(1 for f in all_flags if f["severity"] == "warning")
    suggestion_count = sum(1 for f in all_flags if f["severity"] == "suggestion")

    active_sections = [s for s in audited_sections if not s["isExcluded"]]
    non_empty_active = [s for s in active_sections if s["wordCount"] > 0 and len(s["paragraphs"]) > 0]
    if non_empty_active:
        total_active_w = sum(max(1, s["wordCount"]) for s in non_empty_active)
        overall_score = round(
            sum(s["aiStyleScore"] * max(1, s["wordCount"]) for s in non_empty_active) / total_active_w
        )
    else:
        overall_score = 0

    return {
        "title": safe_title,
        "sections": audited_sections,
        "findings": all_flags,
        "summary": {
            "totalWords": total_words,
            "totalSentences": total_sentences,
            "totalSections": len(audited_sections),
            "auditedSections": len(active_sections),
            "totalFlags": len(all_flags),
            "criticalCount": critical_count,
            "warningCount": warning_count,
            "suggestionCount": suggestion_count,
            "overallAiStyleScore": overall_score,
            "protectedTermsMatched": sorted(list(protected_terms_set)),
            "lexiconSize": len(UNIFIED_ECONOMICS_TERMS),
            "totalRulesCount": len(RULE_METADATA),
        },
    }
