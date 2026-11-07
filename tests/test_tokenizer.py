from api.engine.tokenizer import split_vietnamese_sentences, mask_protected_economics_terms
from api.engine.lexicon import (
    UNIFIED_ECONOMICS_TERMS,
    SINO_VIETNAMESE_ABSTRACT_SYLLABLES,
    RULE_METADATA,
)


def test_split_sentences_preserves_vietnamese_abbreviations_and_decimals():
    text = (
        "Theo PGS.TS. Nguyễn Văn A (2025), tại TP.HCM, biên lãi ròng đạt 3.45% "
        "và nợ xấu ở mức 1.200 tỷ đồng theo Thông tư 02/2023/TT-NHNN. "
        "Tuy nhiên, rủi ro thanh khoản vẫn hiện hữu."
    )
    sentences = split_vietnamese_sentences(text)
    assert len(sentences) == 2
    assert "PGS.TS. Nguyễn Văn A" in sentences[0]["text"]
    assert "3.45%" in sentences[0]["text"]
    assert sentences[1]["text"] == "Tuy nhiên, rủi ro thanh khoản vẫn hiện hữu."
    assert sentences[0]["word_count"] > 10
    assert sentences[0]["start"] == 0
    assert sentences[1]["end"] == len(text)


def test_masks_unified_8_field_economics_terms():
    sample = (
        "Doanh nghiệp áp dụng quản trị sản xuất tinh gọn, kiểm soát rủi ro có sai sót trọng yếu "
        "trên báo cáo tài chính hợp nhất và tối ưu tồn kho an toàn trong quản trị chuỗi cung ứng."
    )
    masked_text, spans = mask_protected_economics_terms(sample)
    matched = [s["term"].lower() for s in spans]
    assert "quản trị sản xuất tinh gọn" in matched
    assert "rủi ro có sai sót trọng yếu" in matched
    assert "báo cáo tài chính hợp nhất" in matched
    assert "tồn kho an toàn" in matched
    assert "quản trị chuỗi cung ứng" in matched
    assert len(masked_text) == len(sample)


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
    assert len(UNIFIED_ECONOMICS_TERMS) >= 80
    assert len(SINO_VIETNAMESE_ABSTRACT_SYLLABLES) >= 40
