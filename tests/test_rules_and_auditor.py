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


def test_clause_bounded_sino_vietnamese_never_bridges_across_punctuation():
    # Previously, commas and sentence-ending periods were stripped without resetting the syllable run counter,
    # causing false positives across commas ("cầu, giá trị, mức độ hoạt động") and periods ("hoạt động. Doanh").
    comma_and_period_text = (
        "Khảo sát đánh giá nhu cầu, giá trị, mức độ hoạt động. "
        "Doanh nghiệp tập trung kiểm soát chất lượng dịch vụ tại chi nhánh."
    )
    res = audit_paragraph(comma_and_period_text, 0)
    flagged_ids = [f["ruleId"] for f in res["flags"]]
    assert "LEX-VN-01" not in flagged_ids


def test_multi_match_collection_catches_all_occurrences_in_paragraph():
    multi_issue_para = (
        "Cụ thể, mô hình này đóng vai trò như là nền tảng cốt lõi (contentReference[oaicite:1]{index=1}). "
        "Tuy nhiên, quy trình kia cũng hoạt động như một công cụ hỗ trợ (contentReference[oaicite:2]{index=2}). "
        "Do đó, hệ thống mới giữ vị thế là trụ cột vận hành. "
        "Hơn nữa, việc áp dụng đã hoàn tất."
    )
    res = audit_paragraph(multi_issue_para, 0)
    for01_flags = [f for f in res["flags"] if f["ruleId"] == "FOR-01"]
    lex02_flags = [f for f in res["flags"] if f["ruleId"] == "LEX-02"]
    dis03_flags = [f for f in res["flags"] if f["ruleId"] == "DIS-03"]

    assert len(for01_flags) >= 2
    assert len(lex02_flags) >= 3
    assert len(dis03_flags) >= 4


def test_econometric_legal_and_outline_exemptions_prevent_false_positives():
    # 1. Econometric reporting paragraph (EFA, Cronbach's Alpha, OLS, hypothesis tests)
    econometric_para = (
        "Thang đo Sự hài lòng của khách hàng được cấu thành bởi 4 biến quan sát với hệ số Cronbach's Alpha đạt 0.845. "
        "Kết quả phân tích nhân tố khám phá EFA cho thấy tổng phương sai trích được giải thích bởi 5 nhân tố đạt 68,42% tại mức KMO = 0.812 (Sig. = 0.000). "
        "Trong mô hình hồi quy OLS, biến độc lập Chất lượng dịch vụ được đo lường bởi 5 thang đo thành phần và có tác động thuận chiều ở mức ý nghĩa thống kê 1%. "
        "Giả thuyết H1 được chấp nhận với hệ số hồi quy chuẩn hóa beta = 0.364 và VIF = 1.42."
    )
    eco_res = audit_paragraph(econometric_para, 0)
    eco_rules = [f["ruleId"] for f in eco_res["flags"]]
    assert "SYN-VN-03" not in eco_rules
    assert "RHY-01" not in eco_rules

    # 2. Thesis chapter outline paragraph in MỞ ĐẦU
    outline_para = (
        "Ngoài phần mở đầu, kết luận và danh mục tài liệu tham khảo, khóa luận được kết cấu thành 3 chương: "
        "Chương 1 trình bày cơ sở lý luận về chất lượng dịch vụ chăm sóc khách hàng tại ngân hàng thương mại. "
        "Chương 2 phân tích thực trạng chất lượng dịch vụ chăm sóc khách hàng tại Ngân hàng TMCP Đông Nam Á. "
        "Chương 3 đề xuất giải pháp nâng cao chất lượng dịch vụ chăm sóc khách hàng trong giai đoạn tới."
    )
    out_res = audit_paragraph(outline_para, 0)
    out_rules = [f["ruleId"] for f in out_res["flags"]]
    assert "RHY-01" not in out_rules
    assert "DIS-01" not in out_rules


def test_general_triad_detector_syn04_and_multi_field_synonym_cycling_lex04():
    triad_and_cycle_para = (
        "Trong quá trình vận hành, doanh nghiệp này đã triển khai kế hoạch, hoàn thiện cơ chế và kiểm soát hệ thống, "
        "đồng thời định hướng chiến lược, củng cố cấu trúc và thúc đẩy hiệu suất. "
        "Nhờ đó, đơn vị kinh doanh trên đã giúp pháp nhân thương mại này nâng cao thị phần."
    )
    res = audit_paragraph(triad_and_cycle_para, 0)
    rule_ids = [f["ruleId"] for f in res["flags"]]
    assert "SYN-04" in rule_ids
    assert "LEX-04" in rule_ids


def test_jaccard_echoic_conclusion_dis02_and_contextual_rewrite_suggestions():
    echoic_para = (
        "Việc nâng cao hiệu quả quản trị rủi ro tín dụng tại chi nhánh ngân hàng thương mại đòi hỏi sự kiểm soát chặt chẽ quy trình thẩm định hồ sơ vay vốn. "
        "Cán bộ tín dụng cần đối chiếu dòng tiền thực tế của khách hàng với lịch trả nợ định kỳ. "
        "Bộ phận quản lý rủi ro thực hiện rà soát độc lập các khoản vay có dấu hiệu suy giảm khả năng trả nợ. "
        "Tóm lại, việc nâng cao hiệu quả quản trị rủi ro tín dụng tại chi nhánh ngân hàng thương mại đòi hỏi sự kiểm soát chặt chẽ quy trình thẩm định."
    )
    res = audit_paragraph(echoic_para, 0)
    rule_ids = [f["ruleId"] for f in res["flags"]]
    assert "DIS-02" in rule_ids

    # Check contextual rewrite suggestion on SYN-VN-03 passive calque
    passive_para = "Quyết định phê duyệt hạn mức đã được thực hiện bởi hội đồng tín dụng trung ương."
    pas_res = audit_paragraph(passive_para, 0)
    syn_vn03_flags = [f for f in pas_res["flags"] if f["ruleId"] == "SYN-VN-03"]
    assert len(syn_vn03_flags) == 1
    assert "hội đồng tín dụng trung ương thực hiện" in syn_vn03_flags[0]["suggestion"].lower()


def test_cross_paragraph_discourse_pass_detects_multi_paragraph_arg01_syn01b_and_dis03():
    sections = [
        {
            "id": "sec-cross",
            "title": "Chương 3: Giải pháp",
            "isExcluded": False,
            "paragraphs": [
                "Thứ nhất, đơn vị cần rà soát lại quy trình phối hợp nội bộ giữa các phòng ban chức năng nhằm hạn chế tình trạng chồng chéo nghiệp vụ trong quá trình xử lý hồ sơ.",
                "Thứ hai, chi nhánh cần tăng cường công tác kiểm tra định kỳ đối với các bộ phận giao dịch trực tiếp nhằm phát hiện sớm những sai sót phát sinh trong quy trình vận hành.",
                "Thứ ba, ban lãnh đạo cần chú trọng hoàn thiện hệ thống đánh giá mức độ hoàn thành công việc của từng vị trí nhân sự nhằm khuyến khích tinh thần làm việc chủ động.",
            ],
        }
    ]
    res = audit_document_sections("Cross_Paragraph_Test.docx", sections)
    arg01_findings = [f for f in res["findings"] if f["ruleId"] == "ARG-01"]
    assert len(arg01_findings) == 3


def test_lex01b_ai_intensifier_vocab_density_and_syn03_four_variants():
    para = (
        "Trong bối cảnh chuyển đổi số đóng vai trò then chốt và có ý nghĩa quyết định, "
        "năng lực cạnh tranh là tài sản vô giá thúc đẩy sự phát triển vượt bậc của đơn vị. "
        "Mô hình quản trị mới không phải là một sự thay thế hình thức mà là bước tái cấu trúc nền tảng. "
        "Hệ thống đo lường tập trung vào hiệu suất thực chất chứ không phải các chỉ tiêu báo cáo bề nổi. "
        "Giải pháp này không đơn thuần là công cụ kiểm soát ngắn hạn mà còn mở ra dư địa tăng trưởng dài hạn."
    )
    res = audit_paragraph(para, 0)
    rule_ids = [f["ruleId"] for f in res["flags"]]
    assert "LEX-01" in rule_ids
    syn03_flags = [f for f in res["flags"] if f["ruleId"] == "SYN-03"]
    assert len(syn03_flags) >= 3


def test_prg02_b_c_meta_disclaimers_and_lex05_vague_hedging_density():
    para = (
        "Mặc dù báo cáo chưa công bố số liệu chi tiết theo từng phân khúc khách hàng, "
        "nhưng việc phân tích vẫn sử dụng khung đánh giá chuẩn nhằm phản ánh xu hướng vận hành tương đối ổn định. "
        "Kết quả khảo sát đạt mức tương đối khả quan và tạo ra những tác động nhất định đối với hiệu quả hoạt động."
    )
    res = audit_paragraph(para, 0)
    rule_ids = [f["ruleId"] for f in res["flags"]]
    assert "PRG-02" in rule_ids
    assert "LEX-05" in rule_ids


def test_syn_vn01_mid_clause_vi_vay_and_fmt01_explanatory_dashes():
    para = (
        "Cấu trúc vốn của doanh nghiệp vì vậy cần được điều chỉnh linh hoạt theo chu kỳ kinh doanh — "
        "đặc biệt là trong giai đoạn lãi suất biến động mạnh - nhằm giảm thiểu rủi ro thanh khoản."
    )
    res = audit_paragraph(para, 0)
    rule_ids = [f["ruleId"] for f in res["flags"]]
    assert "SYN-VN-01" in rule_ids
    assert "FMT-01" in rule_ids


def test_dis02_short_closing_echo_and_dis04_table_signposting():
    para_dis04 = (
        "Số liệu ở Bảng 2.4 không chỉ phản ánh quy mô nguồn vốn mà còn cho thấy ba xu hướng dịch chuyển rõ nét. "
        "Thứ nhất, tỷ trọng vốn huy động ngắn hạn tăng nhanh."
    )
    res_dis04 = audit_paragraph(para_dis04, 0)
    assert "DIS-04" in [f["ruleId"] for f in res_dis04["flags"]]

    para_dis02 = (
        "Tóm lại, những hạn chế trên đòi hỏi doanh nghiệp phải sớm đồng bộ hóa quy trình kiểm soát nội bộ. "
        "Đây là tiền đề quan trọng để nâng cao hiệu quả kinh doanh trong giai đoạn tới."
    )
    res_dis02 = audit_paragraph(para_dis02, 0)
    assert "DIS-02" in [f["ruleId"] for f in res_dis02["flags"]]


def test_cross_paragraph_dis02_dis04_lex04_lex05_and_fmt01():
    sections = [
        {
            "id": "sec-cross-extended",
            "title": "Chương 2: Phân tích thực trạng",
            "isExcluded": False,
            "paragraphs": [
                "Qua Bảng 2.1 có thể thấy tốc độ tăng trưởng doanh thu của doanh nghiệp này đạt mức tương đối cao — phản ánh nỗ lực mở rộng thị trường tương đối rõ nét.",
                "Qua Bảng 2.2 có thể thấy cơ cấu chi phí vận hành của đơn vị kinh doanh trên duy trì ở ngưỡng tương đối ổn định — giúp pháp nhân thương mại này bảo toàn biên lợi nhuận.",
                "Qua Bảng 2.3 có thể thấy hiệu suất sử dụng vốn của công ty tạo ra những tác động nhất định — củng cố nền tảng tài chính tương đối tốt.",
                "Tóm lại, bức tranh tài chính giai đoạn 2023-2025 cho thấy sự tăng trưởng ổn định và là cơ sở quan trọng để đề xuất các giải pháp ở chương sau.",
            ],
        }
    ]
    res = audit_document_sections("Cross_Paragraph_Extended.docx", sections)
    found_rules = {f["ruleId"] for f in res["findings"]}
    assert "DIS-04" in found_rules
    assert "DIS-02" in found_rules
    assert "LEX-04" in found_rules
    assert "LEX-05" in found_rules
    assert "FMT-01" in found_rules


def test_build_contextual_suggestion_covers_all_26_rules_with_quoted_evidence():
    from api.engine.lexicon import build_contextual_suggestion

    sample_evidence = "Mô hình này không phải là giải pháp tạm thời mà là chiến lược cốt lõi"
    for rule_id in RULE_METADATA:
        suggestion = build_contextual_suggestion(rule_id, sample_evidence)
        assert suggestion.strip(), f"Empty suggestion for {rule_id}"
        assert "«" in suggestion and "»" in suggestion, f"Missing quoted evidence in suggestion for {rule_id}"

