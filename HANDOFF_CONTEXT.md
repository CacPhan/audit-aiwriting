# BẢN BÀN GIAO BỐI CẢNH DỰ ÁN (PROJECT HANDOFF CONTEXT)
**Dự án:** AI Writing Style Auditor (Hệ thống Kiểm toán Văn phong Học thuật Khối ngành Kinh tế)
**Cập nhật lần cuối:** 2026-11-07
**Trạng thái hiện tại:** Đã hoàn thành 100% Nghiên cứu Knowledge Base + Đã phê duyệt Thiết kế Kỹ thuật (Design Spec) + Đã lập xong Kế hoạch Triển khai Code (Implementation Plan). **Sẵn sàng bắt đầu code từ Task 1.**

---

## 1. Tóm tắt Mục tiêu & Các Quyết định Đã Chốt của Chủ Dự Án (Không hỏi lại)

1. **Bản chất sản phẩm**:
   - Không phải là công cụ AI Content Detector phán xét "% AI" cảm tính.
   - Là **Hệ thống Kiểm toán Văn phong Học thuật dựa trên Thuật toán Quy tắc (Rule-Based Style Auditor)**: Quét văn bản theo 26 tiêu chí văn phong AI, tô sáng chính xác câu/đoạn vi phạm, giải thích rõ cơ sở ngôn ngữ học, tính toán các chỉ số toán học thực tế ($CV_L, ISI, OPR, SVCI, SICD, BCR$) và hướng dẫn công thức sửa.
2. **Đối tượng người dùng & Ngành học mục tiêu**:
   - Sinh viên đại học và học viên cao học làm khóa luận, luận văn thạc sĩ, nghiên cứu khoa học (file Word `.docx` dài **70–90+ trang**, tương đương 25.000–45.000 chữ).
   - **Hợp nhất tự động 8 chuyên ngành Kinh tế** (*Quản trị kinh doanh, Quản trị nhân sự, Logistics & Hậu cần, Marketing, Ngân hàng, Tài chính, Kế toán – Kiểm toán, Quản trị sản xuất*) vào một bộ từ điển bảo vệ thuật ngữ duy nhất (`UNIFIED_ECONOMICS_LEXICON`). **KHÔNG bắt người dùng chọn dropdown chuyên ngành trước khi audit.**
3. **Phạm vi Phiên bản hiện tại (Audit-First MVP) & Mô hình Thu phí (Pro Hook)**:
   - **Làm ngay trong phiên bản này**: Toàn bộ luồng **Audit (Kiểm toán)** cho file `.docx` 70–90+ trang (và dán văn bản), tách cây Chương/Mục, tự động loại trừ Mục lục/Tài liệu tham khảo, hiển thị giao diện Kiểm toán 3 cột, và **Xuất Báo cáo Kiểm toán (Audit Report định dạng HTML độc lập / In PDF / JSON)**.
   - **Giữ làm tính năng Trả phí (Pro Feature Gate)**: Tính năng *"Sửa trực tiếp trên web kèm chấm điểm real-time & Xuất file `.docx` giữ nguyên định dạng"* được đặt sau nút/modal khóa **`[PRO]`** (`ProUpgradeModal`) để phục vụ thu phí thương mại.
4. **Nền tảng triển khai (Deployment)**:
   - Đẩy lên GitHub và import trực tiếp lên **Vercel (`vercel.app`)**.
   - Sử dụng Vite + React + TypeScript + Tailwind CSS kết hợp Vercel Python Serverless API (`/api/audit.py` gọn nhẹ $< 5\text{MB}$, không dùng thư viện nặng quá giới hạn 250MB của Vercel) và bộ máy quy tắc đồng nhất (`src/engine/`).

---

## 2. Bản đồ Toàn bộ Tài liệu Đã Có trong Workspace (`g:\Antigravity\Thư mục mới`)

### A. Thiết kế Kỹ thuật & Kế hoạch Triển khai (ĐỌC ĐẦU TIÊN KHI BẮT ĐẦU PHIÊN MỚI)
1. **Bản Thiết kế Kỹ thuật đã phê duyệt (Approved Design Spec)**:
   - Đường dẫn: `docs/superpowers/specs/2026-11-06-ai-writing-style-auditor-design.md`
2. **Kế hoạch Triển khai Chi tiết 4 Tasks (Implementation Plan)**:
   - Đường dẫn: `docs/superpowers/plans/2026-11-06-ai-writing-style-auditor-plan.md`

### B. Cơ sở Tri thức Chuyên sâu 26 Dấu hiệu Văn phong AI (Knowledge Base)
1. `knowledge_base/00_TAXONOMY_AND_INTERACTION_MAP.md`: Bản đồ phân loại 26 dấu hiệu, tách bạch khái niệm, sơ đồ nhân quả và thứ tự ưu tiên `P0 -> P3`.
2. `knowledge_base/01_LEXICAL_PHRASEOLOGICAL_PROFILES.md`: Hồ sơ `LEX-01` đến `LEX-VN-01` (Từ vựng AI, né hệ từ *là/có*, ngôn ngữ PR, xoay vòng từ đồng nghĩa, tắc nghẽn âm tiết Hán–Việt).
3. `knowledge_base/02_SYNTACTIC_SENTENCE_PROFILES.md`: Hồ sơ `SYN-01` đến `SYN-VN-03` (Đẳng cấu cú pháp 3 nhịp, đuôi câu *qua đó/góp phần*, sóng đôi phủ định, quy tắc số 3, dư thừa đại từ *nó/họ/điều này*, mất cấu trúc Đề–Thuyết, bị động dịch máy *được/bị* & danh hóa *việc/sự*).
4. `knowledge_base/03_RHYTHM_PARAGRAPH_DISCOURSE_PROFILES.md`: Hồ sơ `RHY-01` đến `DIS-04` (Low Burstiness $CV_L < 0,18$, đoạn văn đóng hộp 4 bước, câu kết đoạn thừa, từ nối khung đầu câu).
5. `knowledge_base/04_ARGUMENTATION_EPISTEMIC_PROFILES.md`: Hồ sơ `ARG-01` đến `PRG-02` (Trọng số luận điểm phẳng, lập luận con lắc an toàn, phóng đại di sản, quy chiếu nguồn mơ hồ, rào đón giáo huấn).
6. `knowledge_base/05_FORMATTING_AND_FORENSIC_ARTIFACTS.md`: Hồ sơ `FMT-01` & `FOR-01` (Danh sách tiêu đề in đậm, Title Case, dấu gạch ngang dài, mã rò rỉ `oaicite`/`turn0search`, DOI/link ảo giác).
7. `knowledge_base/06_EVALUATION_AND_TESTING_FRAMEWORK.md`: Công thức toán học cho 6 chỉ số định lượng ($CV_L, ISI, OPR, SVCI, SICD, BCR$) và danh mục tài liệu tham khảo đã xác minh.
8. `knowledge_base/ai_writing_signs_kb.json` & `knowledge_base/ai_writing_rules_engine.json`: Dữ liệu JSON cấu trúc máy cho toàn bộ 26 dấu hiệu và quy tắc quyết định.

---

## 3. Hướng dẫn Hành động Ngay cho AI Agent ở Phiên Mới

Khi người dùng bắt đầu phiên làm việc mới:
1. Đọc file này (`HANDOFF_CONTEXT.md`), sau đó đọc `docs/superpowers/specs/2026-11-06-ai-writing-style-auditor-design.md` và `docs/superpowers/plans/2026-11-06-ai-writing-style-auditor-plan.md`.
2. Tham chiếu `knowledge_base/ai_writing_rules_engine.json` để lấy đầy đủ bộ từ khóa kích hoạt và quy tắc của 26 dấu hiệu.
3. Thực thi lần lượt **Task 1 $\rightarrow$ Task 2 $\rightarrow$ Task 3 $\rightarrow$ Task 4** trong `docs/superpowers/plans/2026-11-06-ai-writing-style-auditor-plan.md` theo đúng quy trình TDD (viết test, chạy test, viết code, chạy build).
