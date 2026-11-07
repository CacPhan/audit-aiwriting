import unicodedata
from api.engine.tokenizer import (
    split_vietnamese_sentences,
    mask_protected_economics_terms,
    count_vietnamese_words,
)
from api.engine.lexicon import (
    UNIFIED_ECONOMICS_TERMS,
    SINO_VIETNAMESE_ABSTRACT_SYLLABLES,
    RULE_METADATA,
)
from api.engine.rules import audit_paragraph


def test_split_sentences_preserves_vietnamese_abbreviations_and_decimals():
    text = (
        "Theo PGS.TS. Nguyễn Văn A, TS. Trần Thị B và ThS. Lê Văn C (2025), tại TP.HCM, "
        "biên lãi ròng đạt 3.45%, tăng trưởng tín dụng đạt 14,5% và nợ xấu ở mức 1.200 tỷ đồng "
        "theo Thông tư 02/2023/TT-NHNN cùng Nghị định 65/2022/NĐ-CP. "
        "Tuy nhiên, rủi ro thanh khoản vẫn hiện hữu tại một số chi nhánh."
    )
    sentences = split_vietnamese_sentences(text)
    assert len(sentences) == 2
    assert "PGS.TS. Nguyễn Văn A" in sentences[0]["text"]
    assert "TS. Trần Thị B" in sentences[0]["text"]
    assert "ThS. Lê Văn C" in sentences[0]["text"]
    assert "TP.HCM" in sentences[0]["text"]
    assert "3.45%" in sentences[0]["text"]
    assert "14,5%" in sentences[0]["text"]
    assert "1.200 tỷ đồng" in sentences[0]["text"]
    assert "02/2023/TT-NHNN" in sentences[0]["text"]
    assert "65/2022/NĐ-CP" in sentences[0]["text"]
    assert sentences[1]["text"] == "Tuy nhiên, rủi ro thanh khoản vẫn hiện hữu tại một số chi nhánh."
    assert sentences[0]["word_count"] > 20
    assert sentences[0]["start"] == 0
    assert sentences[1]["end"] == len(text)


def test_split_sentences_on_real_thesis_statistical_prose():
    # Excerpt from Agribank Nghe An report (Phan Duy Cac - 11233373) & SeABank thesis (Ngoc Anh - 11220218)
    real_excerpt = (
        "Tính đến 31/12/2024, tổng nguồn vốn huy động của Chi nhánh đạt 19.729 tỷ đồng, "
        "tăng 1.799,694 tỷ đồng (tương ứng 10,04%) so với năm 2023 theo định hướng tại NĐ-CP và TT-NHNN. "
        "Trong đó, tiền gửi dân cư chiếm 87,45% tổng nguồn vốn và tỷ lệ nợ xấu nội bảng được kiểm soát ở mức 0.48%."
    )
    sentences = split_vietnamese_sentences(real_excerpt)
    assert len(sentences) == 2
    assert "19.729 tỷ đồng" in sentences[0]["text"]
    assert "1.799,694 tỷ đồng" in sentences[0]["text"]
    assert "10,04%" in sentences[0]["text"]
    assert "87,45%" in sentences[1]["text"]
    assert "0.48%." in sentences[1]["text"]


def test_masks_unified_8_field_economics_terms_and_prevents_false_lex_vn_01():
    sample = (
        "Doanh nghiệp áp dụng quản trị sản xuất tinh gọn, kiểm soát rủi ro có sai sót trọng yếu "
        "trên báo cáo tài chính hợp nhất, kết hợp đào tạo và phát triển nguồn nhân lực, "
        "quản trị quan hệ khách hàng, kiểm soát tỷ lệ an toàn vốn tối thiểu "
        "và tối ưu tồn kho an toàn trong quản trị chuỗi cung ứng."
    )
    masked_text, spans = mask_protected_economics_terms(sample)
    matched = [s["term"].lower() for s in spans]
    assert "quản trị sản xuất tinh gọn" in matched
    assert "rủi ro có sai sót trọng yếu" in matched
    assert "báo cáo tài chính hợp nhất" in matched
    assert "đào tạo và phát triển nguồn nhân lực" in matched
    assert "quản trị quan hệ khách hàng" in matched
    assert "tỷ lệ an toàn vốn tối thiểu" in matched
    assert "tồn kho an toàn" in matched
    assert "quản trị chuỗi cung ứng" in matched
    assert len(masked_text) == len(sample)

    # Verify that auditing this dense economics sentence NEVER triggers LEX-VN-01
    audit_res = audit_paragraph(sample, 0)
    flagged_rules = [f["ruleId"] for f in audit_res["flags"]]
    assert "LEX-VN-01" not in flagged_rules


def test_handles_nfd_decomposed_vietnamese_unicode_transparently():
    nfc_text = (
        "Quản trị quan hệ khách hàng và đào tạo và phát triển nguồn nhân lực "
        "giúp ngân hàng thương mại cổ phần nâng cao năng lực cạnh tranh."
    )
    nfd_text = unicodedata.normalize("NFD", nfc_text)
    assert len(nfd_text) != len(nfc_text)

    _, spans_nfc = mask_protected_economics_terms(nfc_text)
    _, spans_nfd = mask_protected_economics_terms(nfd_text)
    assert [s["canonical"] for s in spans_nfc] == [s["canonical"] for s in spans_nfd]
    assert count_vietnamese_words(nfc_text) == count_vietnamese_words(nfd_text)


def test_lexicon_contains_all_26_standardized_rules_and_8_fields():
    assert len(RULE_METADATA) == 26
    expected_ids = {
        "LEX-01", "LEX-02", "LEX-03", "LEX-04", "LEX-05", "LEX-VN-01",
        "SYN-01", "SYN-02", "SYN-03", "SYN-04", "SYN-VN-01", "SYN-VN-02", "SYN-VN-03",
        "RHY-01",
        "DIS-01", "DIS-02", "DIS-03", "DIS-04",
        "ARG-01", "ARG-02", "ARG-03", "ARG-04",
        "PRG-01", "PRG-02",
        "FMT-01", "FOR-01",
    }
    assert set(RULE_METADATA.keys()) == expected_ids
    assert len(UNIFIED_ECONOMICS_TERMS) >= 95
    assert len(SINO_VIETNAMESE_ABSTRACT_SYLLABLES) >= 40
