"""
Section-Level & Document-Level Academic Writing Auditor + Sample Economics Thesis Payload.
"""

from typing import Any, Dict, List
from api.engine.lexicon import RULE_METADATA, UNIFIED_ECONOMICS_TERMS
from api.engine.rules import audit_paragraph


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


def audit_document_sections(title: str, sections: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Audits all non-excluded sections of a thesis/manuscript and aggregates
    findings, severity counts, and document-level statistics.
    """
    audited_sections: List[Dict[str, Any]] = []
    all_flags: List[Dict[str, Any]] = []
    total_words = 0
    total_sentences = 0
    protected_terms_set = set()
    global_finding_seq = 1

    for sec_idx, sec in enumerate(sections):
        sec_id = sec.get("id") or f"sec-{sec_idx + 1}"
        sec_title = sec.get("title") or f"Chương {sec_idx + 1}"
        short_title = sec.get("shortTitle") or sec_title.split(":")[0].strip() if ":" in sec_title else sec_title
        section_label = sec.get("sectionLabel") or f"Phần {sec_idx + 1} · Bản thảo"
        is_excluded = bool(sec.get("isExcluded", False))
        raw_paragraphs: List[str] = sec.get("paragraphs") or []

        if is_excluded:
            audited_sections.append(
                {
                    "id": sec_id,
                    "chapterNumber": sec_idx + 1,
                    "title": sec_title,
                    "shortTitle": short_title,
                    "sectionLabel": section_label,
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

            # Assign globally unique finding IDs for UI navigation
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

            para_results.append(p_res)

        sec_score = (
            round(sum(p["aiStyleScore"] for p in para_results) / len(para_results))
            if para_results
            else 0
        )

        audited_sections.append(
            {
                "id": sec_id,
                "chapterNumber": sec_idx + 1,
                "title": sec_title,
                "shortTitle": short_title,
                "sectionLabel": section_label,
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
    overall_score = (
        round(sum(s["aiStyleScore"] for s in active_sections) / len(active_sections))
        if active_sections
        else 0
    )

    return {
        "title": title,
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
