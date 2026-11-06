# AI Writing Style Auditor Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Xây dựng ứng dụng web **AI Writing Style Auditor** triển khai trên Vercel (`vercel.app`), cho phép sinh viên và học viên cao học khối ngành Kinh tế (Quản trị, Nhân sự, Logistics, Marketing, Ngân hàng, Tài chính, Kế toán – Kiểm toán, Quản trị sản xuất) tải lên luận văn `.docx` dài 70–90+ trang để kiểm toán, tô sáng, chấm điểm toán học và giải thích chi tiết 26 dấu hiệu văn phong AI theo thuật toán quy tắc, kèm xuất Báo cáo Kiểm toán (HTML/PDF/JSON) và cổng khóa tính năng trả phí (Pro Live Editor).

**Architecture:** Ứng dụng sử dụng Vite + React + TypeScript + Tailwind CSS kết hợp Vercel Python Serverless API (`/api/audit.py`) và bộ máy kiểm toán quy tắc đồng nhất (`src/engine/`). Luận văn `.docx` 70–90+ trang được bóc tách thành cây cấu trúc Chương/Mục (tự động lọc bỏ Mục lục và Tài liệu tham khảo), bảo vệ thuật ngữ chuyên ngành bằng từ điển hợp nhất 8 chuyên ngành Kinh tế, chấm điểm định lượng ($CV_L, ISI, OPR, SVCI, SICD, BCR$) và hiển thị trên giao diện Audit Studio 3 cột.

**Tech Stack:** React 18, TypeScript, Vite, Tailwind CSS, Vitest (testing), Mammoth.js (`.docx` parsing), Lucide React (icons), Python 3.11 (`http.server` / Vercel Serverless Handler cho `/api/audit.py`).

**Spec:** `docs/superpowers/specs/2026-11-06-ai-writing-style-auditor-design.md`

## Global Constraints

- **Vercel Compatibility:** Tổng dung lượng thư mục `api/` và thư viện Python phải $< 10\text{MB}$ (không dùng PyTorch/underthesea nặng quá 250MB của Vercel Serverless).
- **No Major Selection Dropdown:** Hợp nhất toàn bộ 8 chuyên ngành (*Quản trị kinh doanh, Nhân sự, Logistics/Hậu cần, Marketing, Ngân hàng, Tài chính, Kế toán – Kiểm toán, Quản trị sản xuất*) vào một bộ từ điển bảo vệ thuật ngữ tự động (`UNIFIED_ECONOMICS_LEXICON`).
- **Audit-First Scope & Pro Gate:** Phiên bản hiện tại chỉ mở tính năng Kiểm toán (Audit) và Xuất Báo cáo Kiểm toán; tính năng *"Chỉnh sửa trực tiếp trên web kèm chấm điểm real-time & Xuất file `.docx`"* được đặt sau cổng tính năng trả phí (`ProUpgradeModal`).
- **Large Thesis Performance:** Phải phân tách tài liệu `.docx` 70–90+ trang theo từng Chương/Mục để render theo mục đang chọn, đảm bảo không treo DOM khi tải tài liệu $> 30.000$ chữ.
- **True Mathematical Metrics:** Điểm số phải tính từ công thức định lượng thực tế ($CV_L, ISI, OPR, SVCI, SICD, BCR$) dựa trên `knowledge_base/06_EVALUATION_AND_TESTING_FRAMEWORK.md`.

## Review Focus

1. **Chữ viết tắt và số thập phân tiếng Việt trong luận văn Kinh tế:** Các cụm như `TP.HCM`, `TS. Nguyễn Văn A`, `PGS.TS.`, `Thông tư 02/2023/TT-NHNN`, `14.5%`, `1.250 tỷ đồng` không được làm bộ tách câu (`splitSentences`) cắt nhầm thành câu ngắn 1–2 chữ gây sai lệch chỉ số $CV_L$ (`RHY-01`).
2. **Bảo vệ thuật ngữ 8 chuyên ngành Kinh tế khỏi báo nhầm `LEX-VN-01`:** Các câu chứa thuật ngữ dài như *"báo cáo tài chính hợp nhất"*, *"rủi ro có sai sót trọng yếu"*, *"quản trị chuỗi cung ứng"*, *"tỷ lệ an toàn vốn tối thiểu"* không được bị tính là chuỗi tắc nghẽn âm tiết Hán–Việt trừu tượng.
3. **Tự động loại trừ Mục lục và Danh mục Tài liệu tham khảo:** Khi tải file `.docx` luận văn 80 trang, phần *Danh mục tài liệu tham khảo* (chứa hàng trăm dòng tên tác giả, năm, DOI, link) phải được tự động đánh dấu `isExcluded: true` để không bị báo lỗi `RHY-01` hoặc `SYN-01`.
4. **Đoạn văn ngắn dưới 4 câu:** Chỉ số biến thiên độ dài câu $CV_L$ (`RHY-01`) và đoạn văn đóng hộp 4 bước (`DIS-01`) chỉ kích hoạt trên các đoạn văn có $\ge 4$ câu để tránh dương tính giả trên các đoạn dẫn nhập 1–2 câu.
5. **Tài liệu `.docx` không dùng thẻ Heading chuẩn của Word:** Nhiều sinh viên in đậm dòng chữ `"CHƯƠNG 1: CƠ SỞ LÝ LUẬN"` bằng thẻ `<p><strong>` thay vì Heading 1; bộ phân tích cấu trúc (`extractSectionsFromHtml`) phải nhận diện được cả thẻ `<h1>..<h3>` lẫn đoạn văn ngắn bắt đầu bằng `CHƯƠNG [1-9]/I..V`, `PHẦN MỞ ĐẦU`, `KẾT LUẬN`, `TÀI LIỆU THAM KHẢO`, hoặc `1.1.`, `2.1.`.

---

## File Structure

- `package.json`, `tsconfig.json`, `vite.config.ts`, `tailwind.config.js`, `postcss.config.js`, `index.html`, `vercel.json`: Cấu hình ứng dụng web Vite + React + TypeScript + Vitest và định tuyến Vercel.
- `src/types/auditor.ts`: Định nghĩa toàn bộ kiểu dữ liệu TypeScript cho hệ thống kiểm toán.
- `src/engine/economicsLexicon.ts`: Từ điển hợp nhất 8 chuyên ngành Kinh tế (`UNIFIED_ECONOMICS_LEXICON`), từ điển âm tiết Hán–Việt trừu tượng và danh mục quy tắc 26 dấu hiệu.
- `src/engine/sentenceTokenizer.ts`: Bộ tách đoạn, tách câu tiếng Việt (xử lý viết tắt học hàm học vị, số liệu) và bộ đếm âm tiết/che mặt nạ thuật ngữ Kinh tế.
- `src/engine/ruleEvaluators.ts`: Thuật toán kiểm toán 26 dấu hiệu (`RHY`, `SYN`, `VN-NAT`, `DIS`, `ARG & FOR`) và tính toán 6 chỉ số định lượng ($CV_L, ISI, OPR, SVCI, SICD, BCR$).
- `src/engine/documentParser.ts`: Bộ đọc file `.docx` (qua `mammoth`), phân tách cây Chương/Mục (kể cả khi sinh viên không dùng Heading chuẩn) và tự động lọc Mục lục / Tài liệu tham khảo.
- `src/engine/documentAuditor.ts`: Bộ điều phối kiểm toán toàn văn bản, tính điểm trọng số theo đoạn/chương/toàn bài và cung cấp dữ liệu luận văn mẫu ngành Kinh tế.
- `api/audit.py`: Vercel Python Serverless Function nhận payload văn bản và trả về kết quả kiểm toán JSON đồng nhất.
- `src/utils/reportExporter.ts`: Bộ xuất Báo cáo Kiểm toán ra file HTML độc lập, JSON và giao diện In PDF chuẩn học thuật.
- `src/components/HeaderBar.tsx`, `src/components/ChapterSidebar.tsx`, `src/components/AuditDocumentViewer.tsx`, `src/components/DiagnosticInspector.tsx`, `src/components/ProUpgradeModal.tsx`, `src/App.tsx`: Hệ thống giao diện Audit Studio 3 cột và cổng khóa tính năng trả phí Pro.

---

### Task 1: Project Scaffolding, Types & Unified 8-Field Economics Lexicon

**Files:**
- Create: `package.json`
- Create: `tsconfig.json`
- Create: `vite.config.ts`
- Create: `tailwind.config.js`
- Create: `postcss.config.js`
- Create: `index.html`
- Create: `vercel.json`
- Create: `src/types/auditor.ts`
- Create: `src/engine/economicsLexicon.ts`
- Create: `src/engine/sentenceTokenizer.ts`
- Test: `src/engine/__tests__/sentenceTokenizer.test.ts`

**Interfaces:**
- Produces:
  - `src/types/auditor.ts`: `AuditTier`, `SeverityLevel`, `SpanFlag`, `ParagraphMetrics`, `ParagraphAudit`, `SectionAudit`, `DocumentAuditResult`, `RuleDefinition`
  - `src/engine/economicsLexicon.ts`: `UNIFIED_ECONOMICS_TERMS: string[]`, `SINO_VIETNAMESE_ABSTRACT_WORDS: Set<string>`, `RULE_DEFINITIONS: Record<string, RuleDefinition>`
  - `src/engine/sentenceTokenizer.ts`:
    - `splitVietnameseSentences(paragraphText: string): { text: string; start: number; end: number; wordCount: number }[]`
    - `maskProtectedEconomicsTerms(text: string): { maskedText: string; protectedSpans: { term: string; start: number; end: number }[] }`

- [ ] **Step 1: Initialize project configuration files and install dependencies**

Create `package.json`, `tsconfig.json`, `vite.config.ts`, `tailwind.config.js`, `postcss.config.js`, `index.html`, `vercel.json` and run `npm install` with React 18, Lucide-React, Mammoth, Tailwind, TypeScript, and Vitest.

- [ ] **Step 2: Write the failing test in `src/engine/__tests__/sentenceTokenizer.test.ts`**

```typescript
import { describe, it, expect } from 'vitest';
import { splitVietnameseSentences, maskProtectedEconomicsTerms } from '../sentenceTokenizer';

describe('sentenceTokenizer & Economics Lexicon Shield', () => {
  it('does not split sentences on Vietnamese academic titles, abbreviations, or decimals', () => {
    const text = 'Theo PGS.TS. Nguyễn Văn A (2025), tại TP.HCM, biên lãi ròng đạt 3.45% và nợ xấu ở mức 1.200 tỷ đồng. Tuy nhiên, rủi ro thanh khoản vẫn hiện hữu.';
    const sentences = splitVietnameseSentences(text);
    expect(sentences).toHaveLength(2);
    expect(sentences[0].text).toContain('PGS.TS. Nguyễn Văn A');
    expect(sentences[0].text).toContain('3.45%');
    expect(sentences[1].text).toBe('Tuy nhiên, rủi ro thanh khoản vẫn hiện hữu.');
  });

  it('masks protected terms across all 8 Economics sub-fields (Banking, Accounting, Logistics, Production, HRM, Marketing)', () => {
    const sample = 'Doanh nghiệp áp dụng quản trị sản xuất tinh gọn, kiểm soát rủi ro có sai sót trọng yếu trên báo cáo tài chính hợp nhất và tối ưu tồn kho an toàn trong quản trị chuỗi cung ứng.';
    const { protectedSpans } = maskProtectedEconomicsTerms(sample);
    const matchedTerms = protectedSpans.map(s => s.term.toLowerCase());
    expect(matchedTerms).toContain('quản trị sản xuất tinh gọn');
    expect(matchedTerms).toContain('rủi ro có sai sót trọng yếu');
    expect(matchedTerms).toContain('báo cáo tài chính hợp nhất');
    expect(matchedTerms).toContain('tồn kho an toàn');
    expect(matchedTerms).toContain('quản trị chuỗi cung ứng');
  });
});
```

- [ ] **Step 3: Run test to verify it fails**

Run: `npx vitest run src/engine/__tests__/sentenceTokenizer.test.ts`
Expected: FAIL (modules `../sentenceTokenizer` not found)

- [ ] **Step 4: Implement `src/types/auditor.ts`, `src/engine/economicsLexicon.ts`, and `src/engine/sentenceTokenizer.ts`**

Implement full TypeScript interfaces in `src/types/auditor.ts`, the 8-subfield unified lexicon + 26 rule definitions in `src/engine/economicsLexicon.ts`, and the abbreviation-safe Vietnamese sentence tokenizer + longest-match economics term masker in `src/engine/sentenceTokenizer.ts`.

- [ ] **Step 5: Run test to verify it passes**

Run: `npx vitest run src/engine/__tests__/sentenceTokenizer.test.ts`
Expected: PASS (2 passed)

---

### Task 2: Deterministic 26-Sign Rule Engine & Mathematical Metrics Calculator

**Files:**
- Create: `src/engine/ruleEvaluators.ts`
- Test: `src/engine/__tests__/ruleEvaluators.test.ts`

**Interfaces:**
- Consumes: `src/types/auditor.ts`, `src/engine/economicsLexicon.ts`, `src/engine/sentenceTokenizer.ts`
- Produces:
  - `src/engine/ruleEvaluators.ts`:
    - `auditParagraph(paragraphText: string, paragraphIndex: number): ParagraphAudit`
    - `calculateCoefficientOfVariation(lengths: number[]): { cv: number; mean: number; stdDev: number; spread: number }`

- [ ] **Step 1: Write the failing test in `src/engine/__tests__/ruleEvaluators.test.ts`**

```typescript
import { describe, it, expect } from 'vitest';
import { auditParagraph } from '../ruleEvaluators';

describe('26-Sign Rule Evaluators & Mathematical Metrics', () => {
  it('detects RHY-01 (Low Burstiness), DIS-01/02/03 (Boxed Paragraph & Connectives), and SYN-02 (Trailing Superficial Clause)', () => {
    const aiParagraph =
      'Trong bối cảnh biên lãi ròng thu hẹp, việc đa dạng hóa nguồn thu ngoài lãi đóng vai trò then chốt đối với các ngân hàng. ' +
      'Cụ thể, các hoạt động dịch vụ thanh toán và kinh doanh ngoại hối đã mang lại nguồn thu ổn định, giúp giảm sự phụ thuộc vào tín dụng. ' +
      'Tuy nhiên, mảng phân phối bảo hiểm qua ngân hàng lại đang đối mặt với nhiều thách thức lớn về niềm tin của khách hàng. ' +
      'Do đó, các tổ chức tín dụng cần tái cấu trúc danh mục dịch vụ một cách toàn diện để đảm bảo sự phát triển bền vững.';

    const result = auditParagraph(aiParagraph, 0);
    const ruleIds = result.flags.map(f => f.ruleId);

    expect(result.metrics.cvLength).toBeLessThan(0.18);
    expect(ruleIds).toContain('RHY-01');
    expect(ruleIds).toContain('DIS-01');
    expect(ruleIds).toContain('DIS-03');
    expect(ruleIds).toContain('ARG-02');
    expect(result.aiStyleScore).toBeGreaterThan(55);
  });

  it('detects SYN-01 (Syntactic Isomorphism) across 3 consecutive 3-part sentences', () => {
    const isomorphicText =
      'Trong bối cảnh cạnh tranh gay gắt hiện nay, các ngân hàng thương mại đang đẩy mạnh quá trình số hóa dịch vụ, qua đó nâng cao trải nghiệm cho khách hàng cá nhân. ' +
      'Trước những biến động khó lường của vĩ mô, nhiều tổ chức tín dụng cũng chủ động thắt chặt khẩu vị rủi ro, từ đó đảm bảo sự an toàn cho toàn bộ hệ thống. ' +
      'Thông qua việc ứng dụng trí tuệ nhân tạo, quy trình thẩm định tín dụng đã được rút ngắn đáng kể, góp phần tối ưu hóa chi phí vận hành của doanh nghiệp.';

    const result = auditParagraph(isomorphicText, 0);
    const ruleIds = result.flags.map(f => f.ruleId);
    expect(ruleIds).toContain('SYN-01');
    expect(ruleIds).toContain('SYN-02');
  });

  it('detects SYN-VN-01 (Zero-anaphora deficit), SYN-VN-02 (Topic-Comment loss), SYN-VN-03 (Passive/Nominalization), and LEX-VN-01 (Sino-Vietnamese congestion)', () => {
    const calqueText =
      'Đối với vấn đề rủi ro thanh khoản, nó thường được các ngân hàng nhỏ xử lý thông qua việc thực hiện quy trình chuyển đổi mô hình quản trị rủi ro tập trung của họ. ' +
      'Điều này giúp bảo vệ lợi nhuận của mình.';

    const result = auditParagraph(calqueText, 0);
    const ruleIds = result.flags.map(f => f.ruleId);
    expect(ruleIds).toContain('SYN-VN-01');
    expect(ruleIds).toContain('SYN-VN-02');
    expect(ruleIds).toContain('SYN-VN-03');
    expect(ruleIds).toContain('LEX-VN-01');
  });

  it('does NOT trigger RHY-01 on short 2-sentence paragraphs and does NOT falsely flag protected Accounting/Logistics terms as LEX-VN-01', () => {
    const cleanHumanParagraph =
      'Khi kiểm toán báo cáo tài chính hợp nhất năm 2025, kiểm toán viên đánh giá rủi ro có sai sót trọng yếu nằm ở khoản mục hàng tồn kho và dự phòng phải thu khó đòi. ' +
      'Nhờ đối chiếu trực tiếp vận đơn đường biển với sổ cái kho ngoại quan, đoàn kiểm toán đã phát hiện chênh lệch 14,2 tỷ đồng ghi nhận sai kỳ kế toán.';

    const result = auditParagraph(cleanHumanParagraph, 0);
    const ruleIds = result.flags.map(f => f.ruleId);
    expect(ruleIds).not.toContain('RHY-01');
    expect(ruleIds).not.toContain('LEX-VN-01');
    expect(result.aiStyleScore).toBeLessThan(20);
  });
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `npx vitest run src/engine/__tests__/ruleEvaluators.test.ts`
Expected: FAIL (`../ruleEvaluators` not found)

- [ ] **Step 3: Implement `src/engine/ruleEvaluators.ts`**

Implement the complete 26-rule detection engine and mathematical metrics ($CV_L, ISI, OPR, SVCI, SICD, BCR$) with exact character span offsets (`start`, `end`), matched excerpt, detailed Vietnamese diagnostic explanation, and rule-based transformation guidance.

- [ ] **Step 4: Run test to verify it passes**

Run: `npx vitest run src/engine/__tests__/ruleEvaluators.test.ts`
Expected: PASS (4 passed)

---

### Task 3: Large `.docx` Thesis Structure Parser, Section Filter & Document Auditor

**Files:**
- Create: `src/engine/documentParser.ts`
- Create: `src/engine/documentAuditor.ts`
- Create: `api/audit.py`
- Test: `src/engine/__tests__/documentAuditor.test.ts`

**Interfaces:**
- Consumes: `src/types/auditor.ts`, `src/engine/ruleEvaluators.ts`
- Produces:
  - `src/engine/documentParser.ts`:
    - `parseStructuredSectionsFromTextOrHtml(rawInput: string, isHtml?: boolean): { title: string; paragraphs: string[]; isExcludedByDefault: boolean }[]`
    - `parseDocxFileToSections(file: File): Promise<{ title: string; paragraphs: string[]; isExcludedByDefault: boolean }[]>`
  - `src/engine/documentAuditor.ts`:
    - `auditStructuredDocument(title: string, rawSections: { title: string; paragraphs: string[]; isExcludedByDefault: boolean }[]): DocumentAuditResult`
    - `recalculateDocumentTotals(doc: DocumentAuditResult): DocumentAuditResult`
    - `SAMPLE_ECONOMICS_THESIS_SECTIONS`: Bộ dữ liệu luận văn mẫu đa chuyên ngành Kinh tế (Ngân hàng, Logistics, Quản trị, Kế toán) để kiểm thử và demo ngay trên giao diện.

- [ ] **Step 1: Write the failing test in `src/engine/__tests__/documentAuditor.test.ts`**

```typescript
import { describe, it, expect } from 'vitest';
import { parseStructuredSectionsFromTextOrHtml } from '../documentParser';
import { auditStructuredDocument } from '../documentAuditor';

describe('Document Parser & Multi-Chapter Thesis Auditor', () => {
  it('splits thesis chapters even when headings are plain bold paragraphs (CHƯƠNG 1, 1.1) and auto-excludes References/TOC', () => {
    const rawThesis = [
      'MỤC LỤC',
      'Chương 1: Cơ sở lý luận ........................ 1',
      'CHƯƠNG 1: CƠ SỞ LÝ LUẬN VỀ QUẢN TRỊ CHUỖI CUNG ỨNG VÀ TÀI CHÍNH',
      'Trong bối cảnh toàn cầu hóa hiện nay, quản trị chuỗi cung ứng đóng vai trò là yếu tố then chốt của doanh nghiệp.',
      '1.1. Khái niệm và vai trò của tồn kho an toàn',
      'Đối với vấn đề tồn kho an toàn, nó thường được các doanh nghiệp sản xuất thực hiện thông qua việc dự trữ nguyên vật liệu.',
      'DANH MỤC TÀI LIỆU THAM KHẢO',
      '1. Nguyễn Văn A (2024), Quản trị học, NXB Kinh tế Quốc dân.',
      '2. Trần Thị B (2025), Kế toán kiểm toán nâng cao, NXB Tài chính.'
    ].join('\n\n');

    const sections = parseStructuredSectionsFromTextOrHtml(rawThesis, false);
    expect(sections.length).toBeGreaterThanOrEqual(4);

    const tocSection = sections.find(s => s.title.toUpperCase().includes('MỤC LỤC'));
    const refSection = sections.find(s => s.title.toUpperCase().includes('TÀI LIỆU THAM KHẢO'));
    expect(tocSection?.isExcludedByDefault).toBe(true);
    expect(refSection?.isExcludedByDefault).toBe(true);

    const auditResult = auditStructuredDocument('Luận văn Thạc sĩ Kinh tế mẫu', sections);
    expect(auditResult.overallScore).toBeGreaterThan(0);
    // Excluded sections must not contribute flags to total active flags
    const refAudit = auditResult.sections.find(s => s.title.toUpperCase().includes('TÀI LIỆU THAM KHẢO'));
    expect(refAudit?.isExcluded).toBe(true);
  });
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `npx vitest run src/engine/__tests__/documentAuditor.test.ts`
Expected: FAIL (`../documentParser` not found)

- [ ] **Step 3: Implement `src/engine/documentParser.ts`, `src/engine/documentAuditor.ts`, and `api/audit.py`**

Implement the heading-aware & regex-fallback chapter splitter, automatic TOC/Reference detector, cross-paragraph macro-argumentation checks (`ARG-01` equal paragraph length distribution, `ARG-04` Challenges & Future Prospects section check), document score aggregator, and Vercel Python serverless endpoint `api/audit.py`.

- [ ] **Step 4: Run test to verify it passes**

Run: `npx vitest run src/engine/__tests__/documentAuditor.test.ts`
Expected: PASS

---

### Task 4: Audit Studio 3-Column UI, Report Exporter & Pro Feature Gate

**Files:**
- Create: `src/utils/reportExporter.ts`
- Create: `src/components/HeaderBar.tsx`
- Create: `src/components/ChapterSidebar.tsx`
- Create: `src/components/AuditDocumentViewer.tsx`
- Create: `src/components/DiagnosticInspector.tsx`
- Create: `src/components/ProUpgradeModal.tsx`
- Create: `src/App.tsx`
- Create: `src/main.tsx`
- Create: `src/index.css`
- Test: `src/utils/__tests__/reportExporter.test.ts`

**Interfaces:**
- Consumes: `src/types/auditor.ts`, `src/engine/documentParser.ts`, `src/engine/documentAuditor.ts`
- Produces:
  - `src/utils/reportExporter.ts`: `generateStandaloneHtmlReport(audit: DocumentAuditResult): string`
  - Complete interactive React Web App in `src/App.tsx`

- [ ] **Step 1: Write the failing test in `src/utils/__tests__/reportExporter.test.ts`**

```typescript
import { describe, it, expect } from 'vitest';
import { auditStructuredDocument, SAMPLE_ECONOMICS_THESIS_SECTIONS } from '../../engine/documentAuditor';
import { generateStandaloneHtmlReport } from '../reportExporter';

describe('Audit Report Exporter', () => {
  it('generates a complete standalone HTML Audit Certificate containing overall score, 5-tier breakdown, and flagged excerpts', () => {
    const doc = auditStructuredDocument('Luận văn Kinh tế mẫu', SAMPLE_ECONOMICS_THESIS_SECTIONS);
    const html = generateStandaloneHtmlReport(doc);
    expect(html).toContain('<!DOCTYPE html>');
    expect(html).toContain('BÁO CÁO KIỂM TOÁN VĂN PHONG HỌC THUẬT');
    expect(html).toContain(String(doc.overallScore));
    expect(html).toContain('SYN-01');
  });
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `npx vitest run src/utils/__tests__/reportExporter.test.ts`
Expected: FAIL (`../reportExporter` not found)

- [ ] **Step 3: Implement `src/utils/reportExporter.ts` and the 3-Column React Audit Studio Components**

Implement `reportExporter.ts`, `HeaderBar.tsx`, `ChapterSidebar.tsx`, `AuditDocumentViewer.tsx` (with non-overlapping span highlighter, tier filtering, and paragraph metric badges), `DiagnosticInspector.tsx` (with detailed rule rationale, quantitative formula display, before/after examples, and Pro Live-Edit hook), `ProUpgradeModal.tsx`, and `App.tsx`.

- [ ] **Step 4: Run all unit tests and production build verification**

Run: `npx vitest run && npm run build`
Expected: All test suites PASS and `vite build` succeeds with zero TypeScript or bundler errors.
