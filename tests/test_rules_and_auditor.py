import io
import json
import os
import time
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from api.engine.lexicon import RULE_METADATA
from api.engine.rules import audit_paragraph
from api.engine.auditor import audit_document_sections, SAMPLE_THESIS_PAYLOAD
from api.audit import evaluate_audit_request, handler


def _extract_paragraphs_from_docx_file(docx_path: Path, max_paragraphs: int = 120):
    """Lightweight helper using stdlib zipfile + xml to extract paragraphs from real .docx files."""
    with zipfile.ZipFile(docx_path, "r") as zf:
        xml_bytes = zf.read("word/document.xml")
    root = ET.fromstring(xml_bytes)
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    paragraphs = []
    for p in root.findall(".//w:p", ns):
        texts = [t.text for t in p.findall(".//w:t", ns) if t.text]
        line = "".join(texts).strip()
        if line:
            paragraphs.append(line)
            if len(paragraphs) >= max_paragraphs:
                break
    return paragraphs


def test_detects_low_burstiness_boxed_paragraph_and_pendulum_hedging():
    ai_para = (
        "Trong bối cảnh biên lãi ròng thu hẹp, việc đa dạng hóa nguồn thu ngoài lãi đóng vai trò then chốt đối với các ngân hàng. "
        "Cụ thể, các hoạt động dịch vụ thanh toán và kinh doanh ngoại hối đã mang lại nguồn thu ổn định, giúp giảm sự phụ thuộc vào tín dụng. "
        "Tuy nhiên, mảng phân phối bảo hiểm qua ngân hàng lại đang đối mặt với nhiều thách thức lớn về niềm tin của khách hàng. "
        "Do đó, các tổ chức tín dụng cần tái cấu trúc danh mục dịch vụ một cách toàn diện để đảm bảo sự phát triển bền vững."
    )
    res = audit_paragraph(ai_para, 0)
    rule_ids = [f["ruleId"] for f in res["flags"]]
    assert res["metrics"]["cvLength"] < 0.18
    assert "RHY-01" in rule_ids
    assert "DIS-01" in rule_ids
    assert "DIS-03" in rule_ids
    assert "ARG-02" in rule_ids
    assert res["aiStyleScore"] > 55


def test_rhy01_and_dis01_never_trigger_on_short_paragraphs_under_4_sentences():
    # Even if a 1, 2, or 3-sentence paragraph has identical sentence lengths and connective openers,
    # RHY-01 and DIS-01 must NEVER trigger when sentence count < 4.
    one_sent = "Cụ thể, ngân hàng thương mại đã điều chỉnh lãi suất huy động vốn trong quý đầu năm."
    two_sents = (
        "Cụ thể, ngân hàng thương mại đã điều chỉnh lãi suất huy động vốn. "
        "Tuy nhiên, chi phí huy động vốn đầu vào vẫn ở mức khá cao."
    )
    three_sents = (
        "Cụ thể, ngân hàng thương mại đã điều chỉnh lãi suất huy động vốn. "
        "Tuy nhiên, chi phí huy động vốn đầu vào vẫn ở mức khá cao. "
        "Do đó, biên lãi ròng cần được kiểm soát chặt để phát triển bền vững."
    )

    for idx, short_para in enumerate([one_sent, two_sents, three_sents], start=1):
        res = audit_paragraph(short_para, idx)
        assert res["sentenceCount"] == idx
        flagged_ids = [f["ruleId"] for f in res["flags"]]
        assert "RHY-01" not in flagged_ids, f"RHY-01 falsely triggered on {idx}-sentence paragraph"
        assert "DIS-01" not in flagged_ids, f"DIS-01 falsely triggered on {idx}-sentence paragraph"


def test_all_26_rules_map_strictly_to_3_user_facing_severity_levels():
    valid_mappings = {
        "critical": "Cần sửa ngay",
        "warning": "Nên sửa",
        "suggestion": "Gợi ý",
    }
    assert len(RULE_METADATA) == 26
    for rule_id, meta in RULE_METADATA.items():
        sev = meta["severity"]
        label = meta["severityLabel"]
        assert sev in valid_mappings, f"Invalid severity '{sev}' in {rule_id}"
        assert label == valid_mappings[sev], f"Mismatched severityLabel '{label}' for {rule_id}"
        assert meta["userTitle"].strip()
        assert meta["userReason"].strip()
        assert meta["userSuggestion"].strip()


def test_detects_syntactic_isomorphism_and_trailing_clauses():
    iso_para = (
        "Trong bối cảnh cạnh tranh gay gắt hiện nay, các ngân hàng thương mại đang đẩy mạnh quá trình số hóa dịch vụ, qua đó nâng cao trải nghiệm cho khách hàng cá nhân. "
        "Trước những biến động khó lường của vĩ mô, nhiều tổ chức tín dụng cũng chủ động thắt chặt khẩu vị rủi ro, từ đó đảm bảo sự an toàn cho toàn bộ hệ thống. "
        "Thông qua việc ứng dụng trí tuệ nhân tạo, quy trình thẩm định tín dụng đã được rút ngắn đáng kể, góp phần tối ưu hóa chi phí vận hành của doanh nghiệp."
    )
    res = audit_paragraph(iso_para, 0)
    rule_ids = [f["ruleId"] for f in res["flags"]]
    assert "SYN-01" in rule_ids
    assert "SYN-02" in rule_ids


def test_detects_vietnamese_native_calques_and_sino_vietnamese_congestion():
    calque_para = (
        "Đối với vấn đề rủi ro thanh khoản, nó thường được các ngân hàng nhỏ xử lý thông qua việc thực hiện quy trình chuyển đổi mô hình quản trị rủi ro tập trung của họ. "
        "Điều này giúp bảo vệ lợi nhuận của mình."
    )
    res = audit_paragraph(calque_para, 0)
    rule_ids = [f["ruleId"] for f in res["flags"]]
    assert "SYN-VN-01" in rule_ids
    assert "SYN-VN-02" in rule_ids
    assert "SYN-VN-03" in rule_ids
    assert "LEX-VN-01" in rule_ids


def test_protects_clean_economics_prose_and_short_paragraphs():
    clean_para = (
        "Khi kiểm toán báo cáo tài chính hợp nhất năm 2025, kiểm toán viên đánh giá rủi ro có sai sót trọng yếu nằm ở khoản mục hàng tồn kho và dự phòng phải thu khó đòi. "
        "Nhờ đối chiếu trực tiếp vận đơn đường biển với sổ cái kho ngoại quan, đoàn kiểm toán đã phát hiện chênh lệch 14,2 tỷ đồng ghi nhận sai kỳ kế toán."
    )
    res = audit_paragraph(clean_para, 0)
    rule_ids = [f["ruleId"] for f in res["flags"]]
    assert "RHY-01" not in rule_ids
    assert "LEX-VN-01" not in rule_ids
    assert res["aiStyleScore"] < 20


def test_detects_forensic_artifacts_and_additional_signs():
    forensic_para = (
        "Chắc chắn rồi! Dưới đây là phân tích: Theo các chuyên gia cho rằng (Nguyen & Tran, 2024, "
        "doi:10.1016/j.jcorpfin.2024.999999 — contentReference[oaicite:0]{index=0}), "
        "điều quan trọng cần lưu ý là mô hình này đóng vai trò như là một bước ngoặt lịch sử, "
        "không chỉ là một giải pháp vận hành đơn thuần mà còn là một tuyên ngôn chiến lược, "
        "gắn liền với các hoạt động kinh doanh đồng bộ, toàn diện và hiệu quả."
    )
    res = audit_paragraph(forensic_para, 0)
    rule_ids = [f["ruleId"] for f in res["flags"]]
    assert "FOR-01" in rule_ids
    assert "PRG-01" in rule_ids
    assert "PRG-02" in rule_ids
    assert "LEX-02" in rule_ids
    assert "LEX-03" in rule_ids
    assert "LEX-05" in rule_ids
    assert "SYN-03" in rule_ids
    assert "SYN-04" in rule_ids


def test_audit_endpoint_handles_empty_missing_and_malformed_payloads_safely():
    # 1. Empty dict falls back to sample payload safely
    fallback_res = evaluate_audit_request({})
    assert len(fallback_res["sections"]) == 4

    # 2. Explicit empty sections list returns 0 sections and 0 findings without error
    empty_res = evaluate_audit_request({"title": "Empty_Doc.docx", "sections": []})
    assert empty_res["title"] == "Empty_Doc.docx"
    assert empty_res["sections"] == []
    assert empty_res["findings"] == []
    assert empty_res["summary"]["totalWords"] == 0
    assert empty_res["summary"]["totalFlags"] == 0

    # 3. Missing fields inside sections & empty/None paragraphs
    partial_res = evaluate_audit_request(
        {
            "title": "",
            "sections": [
                {},
                {"title": "MỤC LỤC", "isExcluded": True, "paragraphs": ["Chương 1 .... 1"]},
                {"title": "Chương 1", "paragraphs": ["", None, "   ", "Đoạn văn kiểm thử ngắn."]},
            ],
        }
    )
    assert partial_res["summary"]["totalSections"] == 3
    assert partial_res["summary"]["auditedSections"] == 2
    assert partial_res["sections"][1]["isExcluded"] is True


def test_audit_endpoint_processes_all_3_real_uploaded_theses_fast():
    fixtures_dir = Path(__file__).parent / "fixtures"
    docx_files = [
        fixtures_dir / "kltn_thai_son_11233561.docx",
        fixtures_dir / "kltn_ngoc_anh_11220218.docx",
        fixtures_dir / "bao_cao_phan_duy_cac_11233373.docx",
    ]
    for docx_path in docx_files:
        assert docx_path.exists(), f"Missing fixture {docx_path}"
        paragraphs = _extract_paragraphs_from_docx_file(docx_path, max_paragraphs=120)
        assert len(paragraphs) > 30

        payload = {
            "title": docx_path.name,
            "sections": [
                {
                    "id": "sec-cover",
                    "title": "Trang bìa & Mục lục",
                    "isExcluded": True,
                    "paragraphs": paragraphs[:15],
                },
                {
                    "id": "sec-ch1",
                    "title": "Chương 1: Cơ sở lý luận",
                    "isExcluded": False,
                    "paragraphs": paragraphs[15:65],
                },
                {
                    "id": "sec-ch2",
                    "title": "Chương 2: Thực trạng hoạt động",
                    "isExcluded": False,
                    "paragraphs": paragraphs[65:120],
                },
            ],
        }

        t0 = time.perf_counter()
        result = evaluate_audit_request(payload)
        elapsed = time.perf_counter() - t0

        assert elapsed < 1.5, f"Audit took too long ({elapsed:.2f}s) for {docx_path.name}"
        assert result["title"] == docx_path.name
        assert result["summary"]["totalSections"] == 3
        assert result["summary"]["auditedSections"] == 2
        assert result["summary"]["totalWords"] > 500
        assert len(result["summary"]["protectedTermsMatched"]) > 0


def test_requirements_txt_is_lightweight_for_vercel_serverless_limit():
    req_path = Path(__file__).resolve().parent.parent / "requirements.txt"
    assert req_path.exists()
    content = req_path.read_text(encoding="utf-8").lower()
    forbidden_heavy_libs = [
        "torch",
        "tensorflow",
        "transformers",
        "spacy",
        "scipy",
        "pandas",
        "scikit-learn",
        "underthesea",
        "pyvi",
        "nltk",
        "flair",
    ]
    for lib in forbidden_heavy_libs:
        assert lib not in content, f"Heavy dependency '{lib}' found in requirements.txt"
