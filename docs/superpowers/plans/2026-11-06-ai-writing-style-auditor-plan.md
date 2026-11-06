# AI Writing Style Auditor Implementation Plan (Phương án B: Python Backend trên Vercel)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Xây dựng ứng dụng web **AI Writing Style Auditor** triển khai trên Vercel (`vercel.app`) theo **Phương án (b) — Single-Source Python Audit Engine trên Vercel**, cho phép sinh viên và học viên cao học khối ngành Kinh tế (Quản trị, Nhân sự, Logistics, Marketing, Ngân hàng, Tài chính, Kế toán – Kiểm toán, Quản trị sản xuất) tải lên luận văn `.docx` dài 70–90+ trang để tách chương/mục, gửi từng chương xuống Backend Python (`/api/audit`) phân tích 26 dấu hiệu văn phong AI, hiển thị trên giao diện Audit Studio 3 cột và xuất Báo cáo Kiểm toán (HTML/PDF/JSON).

**Architecture:** Toàn bộ bộ máy kiểm toán 26 quy tắc, từ điển hợp nhất 8 chuyên ngành Kinh tế và xử lý NLP tiếng Việt được đặt duy nhất tại Backend Python (`api/engine/` & `api/audit.py`) chạy trên Vercel Python Serverless Function. Frontend (`src/`, React + TypeScript + Vite + Tailwind CSS) đảm nhiệm bóc tách file `.docx` 70–90+ trang thành từng Chương/Mục, gửi request theo từng chương xuống `/api/audit`, hiển thị kết quả tô sáng 3 cột, xuất Báo cáo Kiểm toán và hiển thị cổng khóa tính năng trả phí (`ProUpgradeModal`).

**Tech Stack:** Python 3.11+ (`pyvi` hoặc bộ tách từ từ điển nhẹ, `pytest`), React 18, TypeScript, Vite, Tailwind CSS, Vitest, Mammoth.js (`.docx` extraction), Lucide React.

**Spec:** `docs/superpowers/specs/2026-11-06-ai-writing-style-auditor-design.md`

## Global Constraints

- **Single-Source Python Rule Engine (Phương án b):** Toàn bộ 26 quy tắc kiểm toán và tính toán chỉ số toán học ($CV_L, ISI, OPR, SVCI, SICD, BCR$) chỉ viết một lần duy nhất bằng Python trong `api/engine/`, tuyệt đối không nhân bản logic quy tắc sang TypeScript.
- **Vercel Serverless Compatibility:** Gói phụ thuộc trong `requirements.txt` phải nhẹ ($< 50\text{MB}$), tuyệt đối không dùng PyTorch/underthesea vượt ngưỡng 250MB của Vercel. Khi kiểm toán file `.docx` 70–90+ trang, Frontend gửi theo từng Chương/Batch xuống `POST /api/audit` để mỗi request luôn $< 1\text{MB}$ và phản hồi nhanh.
- **No Major Selection Dropdown:** Hợp nhất toàn bộ 8 chuyên ngành Kinh tế (*Quản trị kinh doanh, Nhân sự, Logistics/Hậu cần, Marketing, Ngân hàng, Tài chính, Kế toán – Kiểm toán, Quản trị sản xuất*) vào một bộ từ điển bảo vệ thuật ngữ tự động (`UNIFIED_ECONOMICS_LEXICON` trong `api/engine/lexicon.py`).
- **Audit-First Scope & Pro Gate:** Phiên bản hiện tại chỉ mở tính năng Kiểm toán (Audit) và Xuất Báo cáo Kiểm toán; tính năng *"Chỉnh sửa trực tiếp trên web kèm chấm điểm real-time & Xuất file `.docx`"* được đặt sau cổng tính năng trả phí (`ProUpgradeModal`).
- **Mandatory Git Commit & Test Gate (`AGENTS.md`):** Sau mỗi task/thay đổi, bắt buộc phải chạy đầy đủ các bài kiểm thử liên quan (`pytest` cho Python và `vitest` cho Frontend) đảm bảo PASS 100%, sau đó tạo một Git commit tương ứng.

## Review Focus

1. **Chữ viết tắt và số thập phân tiếng Việt trong luận văn Kinh tế:** Bộ tách câu Python (`split_vietnamese_sentences` trong `api/engine/tokenizer.py`) không được cắt nhầm tại `TP.HCM`, `TS.`, `PGS.TS.`, `ThS.`, `TT-NHNN`, `NĐ-CP`, `14.5%`, `1.200 tỷ đồng`.
2. **Bảo vệ thuật ngữ 8 chuyên ngành Kinh tế khỏi báo nhầm `LEX-VN-01`:** Các cụm thuật ngữ chuyên ngành như *"báo cáo tài chính hợp nhất"*, *"rủi ro có sai sót trọng yếu"*, *"quản trị chuỗi cung ứng"*, *"quản trị sản xuất tinh gọn"*, *"tỷ lệ an toàn vốn tối thiểu"* phải được đánh dấu bảo vệ (`mask_protected_economics_terms`) trước khi đếm chuỗi âm tiết Hán–Việt trừu tượng.
3. **Đoạn văn ngắn dưới 4 câu:** Chỉ số biến thiên chiều dài câu $CV_L$ (`RHY-01`) và đoạn văn đóng hộp 4 bước (`DIS-01`) chỉ kích hoạt trên các đoạn văn có $\ge 4$ câu.
4. **Tự động loại trừ Mục lục và Danh mục Tài liệu tham khảo:** Bộ tách chương từ file `.docx` (`src/utils/docxParser.ts`) phải nhận diện cả thẻ Heading lẫn đoạn văn in đậm bắt đầu bằng `CHƯƠNG 1..5`, `MỤC LỤC`, `DANH MỤC TÀI LIỆU THAM KHẢO` và tự động đánh dấu `isExcluded: true` cho Mục lục / Tài liệu tham khảo.
5. **Tương thích môi trường Dev Local & Vercel Production:** Trong quá trình phát triển local (`npm run dev`), Vite dev server phải cấu hình proxy `/api/audit` sang Python server local (hoặc middleware) để giao diện React gọi `fetch('/api/audit')` giống hệt như khi chạy trên `vercel.app`.

---

## File Structure

- `api/engine/__init__.py`: Package khởi tạo bộ máy kiểm toán Python.
- `api/engine/lexicon.py`: Từ điển hợp nhất 8 chuyên ngành Kinh tế (`UNIFIED_ECONOMICS_TERMS`), từ điển âm tiết Hán–Việt trừu tượng và metadata 26 quy tắc.
- `api/engine/tokenizer.py`: Bộ tách câu tiếng Việt chống cắt nhầm từ viết tắt/số thập phân, tách từ tiếng Việt và che mặt nạ bảo vệ thuật ngữ Kinh tế.
- `api/engine/rules.py`: Bộ máy kiểm toán 26 quy tắc (`RHY-01`, `SYN-01`..`04`, `SYN-VN-01`..`03`, `LEX-01`..`05`, `LEX-VN-01`, `DIS-01`..`04`, `ARG-01`..`04`, `PRG-01`..`02`, `FMT-01`, `FOR-01`) và tính toán 6 chỉ số định lượng ($CV_L, ISI, OPR, SVCI, SICD, BCR$).
- `api/engine/auditor.py`: Bộ điều phối kiểm toán cấp Chương/Mục và cấp Toàn tài liệu, kèm dữ liệu luận văn mẫu ngành Kinh tế.
- `api/audit.py`: Vercel Python Serverless Function (`BaseHTTPRequestHandler`) phục vụ endpoint `POST /api/audit` và `GET /api/audit` (trả về dữ liệu mẫu + danh mục quy tắc).
- `tests/test_python_engine.py`: Bộ unit test `pytest` kiểm증 toàn bộ bộ máy Python (`tokenizer.py`, `rules.py`, `auditor.py`, `audit.py`).
- `package.json`, `requirements.txt`, `vercel.json`, `vite.config.ts`, `tsconfig.json`, `tailwind.config.js`, `postcss.config.js`, `index.html`: Cấu hình toàn dự án.
- `src/types/auditor.ts`: Kiểu dữ liệu TypeScript khớp 1-1 với JSON response từ `api/audit.py`.
- `src/utils/docxParser.ts`: Bộ đọc file `.docx` 70–90+ trang trên trình duyệt, tách cây Chương/Mục, nhận diện Mục lục/Tài liệu tham khảo và gửi batch xuống `/api/audit`.
- `src/utils/reportExporter.ts`: Bộ xuất Báo cáo Kiểm toán ra HTML độc lập / In PDF / JSON.
- `src/components/HeaderBar.tsx`, `src/components/ChapterSidebar.tsx`, `src/components/AuditDocumentViewer.tsx`, `src/components/DiagnosticInspector.tsx`, `src/components/ProUpgradeModal.tsx`, `src/App.tsx`: Giao diện React Audit Studio 3 cột.

---

### Task 1: Python NLP Tokenizer & Unified 8-Field Economics Lexicon (`api/engine/lexicon.py` & `tokenizer.py`)

**Files:**
- Create: `requirements.txt`
- Create: `api/engine/__init__.py`
- Create: `api/engine/lexicon.py`
- Create: `api/engine/tokenizer.py`
- Test: `tests/test_tokenizer.py`

**Interfaces:**
- Produces:
  - `api/engine/lexicon.py`: `UNIFIED_ECONOMICS_TERMS: list[str]`, `SINO_VIETNAMESE_ABSTRACT_SYLLABLES: set[str]`, `RULE_METADATA: dict[str, dict]`
  - `api/engine/tokenizer.py`:
    - `split_vietnamese_sentences(text: str) -> list[dict]` (each dict: `{"text": str, "start": int, "end": int, "word_count": int}`)
    - `mask_protected_economics_terms(text: str) -> tuple[str, list[dict]]`

- [ ] **Step 1: Write the failing test in `tests/test_tokenizer.py`**

```python
from api.engine.tokenizer import split_vietnamese_sentences, mask_protected_economics_terms

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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_tokenizer.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'api'`

- [ ] **Step 3: Implement `requirements.txt`, `api/engine/__init__.py`, `api/engine/lexicon.py`, and `api/engine/tokenizer.py`**

Implement the unified 8-field Economics lexicon (`Quản trị, Nhân sự, Logistics, Marketing, Ngân hàng, Tài chính, Kế toán – Kiểm toán, Quản trị sản xuất`), 26 rule definitions, and the Vietnamese sentence splitter + longest-match economics term masker.

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_tokenizer.py -v`
Expected: PASS (2 passed)

- [ ] **Step 5: Commit**

```bash
git add requirements.txt api/engine/__init__.py api/engine/lexicon.py api/engine/tokenizer.py tests/test_tokenizer.py
git commit -m "feat(engine): add unified 8-field economics lexicon and Vietnamese sentence tokenizer"
```

---

### Task 2: Single-Source 26-Sign Python Rule Engine & Vercel Serverless API (`api/engine/rules.py`, `auditor.py`, `api/audit.py`)

**Files:**
- Create: `api/engine/rules.py`
- Create: `api/engine/auditor.py`
- Create: `api/audit.py`
- Test: `tests/test_rules_and_auditor.py`

**Interfaces:**
- Consumes: `api/engine/lexicon.py`, `api/engine/tokenizer.py`
- Produces:
  - `api/engine/rules.py`: `audit_paragraph(text: str, index: int) -> dict`
  - `api/engine/auditor.py`: `audit_document_sections(title: str, sections: list[dict]) -> dict`, `SAMPLE_THESIS_PAYLOAD: dict`
  - `api/audit.py`: Vercel Serverless `handler(BaseHTTPRequestHandler)` handling `POST /api/audit` and `GET /api/audit`

- [ ] **Step 1: Write the failing test in `tests/test_rules_and_auditor.py`**

```python
from api.engine.rules import audit_paragraph
from api.engine.auditor import audit_document_sections

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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_rules_and_auditor.py -v`
Expected: FAIL (`ModuleNotFoundError: No module named 'api.engine.rules'`)

- [ ] **Step 3: Implement `api/engine/rules.py`, `api/engine/auditor.py`, and `api/audit.py`**

Implement all 26 rule evaluators, mathematical metrics ($CV_L, ISI, OPR, SVCI, SICD, BCR$), section/document aggregation, and the Vercel HTTP handler in `api/audit.py`.

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest -v`
Expected: PASS (all tests in `tests/` pass)

- [ ] **Step 5: Commit**

```bash
git add api/engine/rules.py api/engine/auditor.py api/audit.py tests/test_rules_and_auditor.py
git commit -m "feat(api): implement 26-sign Python rule engine and Vercel serverless endpoint"
```

---

### Task 3: Frontend Scaffolding, Large `.docx` Chapter Parser & Report Exporter (`src/utils/`)

**Files:**
- Create: `package.json`
- Create: `tsconfig.json`
- Create: `vite.config.ts`
- Create: `tailwind.config.js`
- Create: `postcss.config.js`
- Create: `vercel.json`
- Create: `index.html`
- Create: `src/types/auditor.ts`
- Create: `src/utils/docxParser.ts`
- Create: `src/utils/reportExporter.ts`
- Test: `src/utils/__tests__/docxAndReport.test.ts`

**Interfaces:**
- Produces:
  - `src/utils/docxParser.ts`:
    - `splitRawTextOrHtmlIntoSections(content: string, isHtml?: boolean): { title: string; paragraphs: string[]; isExcluded: boolean }[]`
    - `extractSectionsFromDocx(file: File): Promise<{ title: string; paragraphs: string[]; isExcluded: boolean }[]>`
  - `src/utils/reportExporter.ts`:
    - `generateStandaloneHtmlReport(audit: DocumentAuditResult): string`

- [ ] **Step 1: Initialize frontend config files and write failing test in `src/utils/__tests__/docxAndReport.test.ts`**

```typescript
import { describe, it, expect } from 'vitest';
import { splitRawTextOrHtmlIntoSections } from '../docxParser';
import { generateStandaloneHtmlReport } from '../reportExporter';

describe('Thesis .docx Section Splitter & Audit Report Exporter', () => {
  it('splits plain or bold chapter headings (CHƯƠNG 1, 1.1) and auto-excludes MỤC LỤC and TÀI LIỆU THAM KHẢO', () => {
    const rawThesis = [
      'MỤC LỤC',
      'Chương 1: Cơ sở lý luận ........................ 1',
      'CHƯƠNG 1: CƠ SỞ LÝ LUẬN VỀ QUẢN TRỊ CHUỖI CUNG ỨNG',
      'Đoạn văn phân tích cơ sở lý luận về tồn kho an toàn và vận tải đa phương thức.',
      '1.1. Khái niệm quản trị sản xuất tinh gọn',
      'Đoạn văn phân tích hoạch định nguồn lực doanh nghiệp.',
      'DANH MỤC TÀI LIỆU THAM KHẢO',
      '1. Nguyễn Văn A (2024), Quản trị học, NXB Kinh tế Quốc dân.'
    ].join('\n\n');

    const sections = splitRawTextOrHtmlIntoSections(rawThesis, false);
    expect(sections.length).toBe(4);
    expect(sections[0].isExcluded).toBe(true);
    expect(sections[1].isExcluded).toBe(false);
    expect(sections[3].isExcluded).toBe(true);
  });
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `npx vitest run src/utils/__tests__/docxAndReport.test.ts`
Expected: FAIL (`../docxParser` not found)

- [ ] **Step 3: Implement `src/types/auditor.ts`, `src/utils/docxParser.ts`, `src/utils/reportExporter.ts`, and Vite Python API middleware**

Configure `vite.config.ts` so `/api/audit` invokes Python `api/audit.py` seamlessly during local development and `vercel.json` routes `/api/(.*)` to `api/audit.py` in production.

- [ ] **Step 4: Run test to verify it passes**

Run: `npx vitest run src/utils/__tests__/docxAndReport.test.ts`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add package.json tsconfig.json vite.config.ts tailwind.config.js postcss.config.js vercel.json index.html src/types/auditor.ts src/utils/
git commit -m "feat(frontend): add .docx chapter splitter, HTML/PDF report exporter, and Vercel routing"
```

---

### Task 4: 3-Column Audit Studio UI, End-to-End Integration & Pro Feature Gate (`src/components/` & `src/App.tsx`)

**Files:**
- Create: `src/index.css`
- Create: `src/main.tsx`
- Create: `src/components/HeaderBar.tsx`
- Create: `src/components/ChapterSidebar.tsx`
- Create: `src/components/AuditDocumentViewer.tsx`
- Create: `src/components/DiagnosticInspector.tsx`
- Create: `src/components/ProUpgradeModal.tsx`
- Create: `src/App.tsx`
- Test: `src/components/__tests__/AppIntegration.test.tsx`

- [ ] **Step 1: Write the failing test in `src/components/__tests__/AppIntegration.test.tsx`**

Verify that the 3-column layout renders the section tree, highlighted spans, rule inspector details, report export buttons, and opens `ProUpgradeModal` when clicking the `[PRO] Chỉnh sửa trực tiếp & Xuất .docx` button.

- [ ] **Step 2: Run test to verify it fails**

Run: `npx vitest run src/components/__tests__/AppIntegration.test.tsx`
Expected: FAIL

- [ ] **Step 3: Implement the 3-Column Audit Studio components and `src/App.tsx`**

Implement `HeaderBar.tsx`, `ChapterSidebar.tsx`, `AuditDocumentViewer.tsx`, `DiagnosticInspector.tsx`, `ProUpgradeModal.tsx`, and `App.tsx` (with chunked chapter-by-chapter progress bar when auditing 70–90+ page `.docx` files via `/api/audit`).

- [ ] **Step 4: Run all Python & Frontend tests and verify production build**

Run: `python -m pytest -v && npx vitest run && npm run build`
Expected: All `pytest` and `vitest` suites PASS; `vite build` succeeds cleanly.

- [ ] **Step 5: Commit**

```bash
git add src/
git commit -m "feat(ui): complete 3-column Audit Studio UI, batch .docx auditing, and Pro upgrade gate"
```
