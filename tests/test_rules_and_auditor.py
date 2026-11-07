import io
import json
from api.engine.rules import audit_paragraph
from api.engine.auditor import audit_document_sections, SAMPLE_THESIS_PAYLOAD
from api.audit import evaluate_audit_request


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


def test_audit_document_sections_and_serverless_evaluator():
    result = evaluate_audit_request(SAMPLE_THESIS_PAYLOAD)
    assert result["title"] == SAMPLE_THESIS_PAYLOAD["title"]
    assert len(result["sections"]) >= 4
    assert result["summary"]["totalFlags"] > 0
    assert "criticalCount" in result["summary"]
    assert "warningCount" in result["summary"]
    assert "suggestionCount" in result["summary"]
