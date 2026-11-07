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
4. **Kiến trúc Kỹ thuật & Nền tảng Triển khai (Phương án b — Single-Source Python Backend trên Vercel)**:
   - Đẩy lên GitHub và import trực tiếp lên **Vercel (`vercel.app`)**.
   - **Tầng Backend (`api/engine/` & `api/audit.py`)**: Bộ máy kiểm toán 26 quy tắc được viết **duy nhất 1 lần bằng Python** (`api/engine/lexicon.py`, `preprocessor.py`, `metrics.py`, `rule_scanner.py`, `scoring.py`) và chạy trên Vercel Python Serverless Function (`POST /api/audit`, gọn nhẹ $< 5\text{MB}$, tuyệt đối không dùng thư viện NLP nặng quá giới hạn 250MB của Vercel).
   - **Tầng Frontend (`src/`)**: Vite + React + TypeScript + Tailwind CSS đảm nhiệm bóc tách file `.docx` 70–90+ trang (`mammoth` + DOMParser), chia cây Chương/Mục, gửi sang `/api/audit`, hiển thị giao diện Kiểm toán 3 cột và xuất Báo cáo Audit.

---

## 2. Bản đồ Toàn bộ Tài liệu Đã Có trong Workspace (`g:\Antigravity\Thư mục mới`)

### A. Quy tắc Bắt buộc, Thiết kế Kỹ thuật & Kế hoạch Triển khai (ĐỌC ĐẦU TIÊN KHI BẮT ĐẦU PHIÊN MỚI)
1. **Quy tắc Làm việc Bắt buộc của Dự án (`AGENTS.md`)**:
   - Đường dẫn: `AGENTS.md` (Quy định bắt buộc về Git commit và chạy kiểm thử sau mỗi lần thay đổi).
2. **Bản Thiết kế Kỹ thuật đã phê duyệt (Approved Design Spec — Phương án b)**:
   - Đường dẫn: `docs/superpowers/specs/2026-11-06-ai-writing-style-auditor-design.md`
3. **Kế hoạch Triển khai Chi tiết 4 Tasks (Implementation Plan — Phương án b)**:
   - Đường dẫn: `docs/superpowers/plans/2026-11-06-ai-writing-style-auditor-plan.md`
4. **Bản Mẫu Giao diện Frontend Chuẩn (Approved Multi-Screen SaaS UI Prototype)**:
   - Đường dẫn: `ai-writing-style-auditor-ui.html` (Giao diện SaaS đa màn hình độc lập: **Screen 01 – Home** với khu vực Upload `.docx` trọng tâm & nút `START AUDIT`, **Screen 02 – Workspace** 3 cột có thể thu gọn hai bên, **Screen 03 – Insights** tổng quan thống kê, và **Report Preview Modal**; phân loại 3 mức độ trực quan *Cần sửa ngay / Nên sửa / Gợi ý* với kiểu gạch chân riêng; CTA `Upgrade Pro (Coming soon)`; ẩn toàn bộ thông số thuật toán/chuyên ngành nội bộ khỏi UI người dùng cuối nhưng giữ nguyên trong tầng Backend Python). Khi triển khai Task 3 & Task 4, hãy chuyển hóa trực tiếp cấu trúc màn hình và hệ thống CSS/Hiệu ứng từ file này sang các React Component trong `src/`.

### B. Cơ sở Tri thức Chuyên sâu 26 Dấu hiệu Văn phong AI (Knowledge Base)
0. `Sign of AI Writing.md` & `knowledge_base/source/Sign_of_AI_Writing_Full_Original.md`: Toàn văn tài liệu gốc ban đầu của chủ dự án (180 KB).
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
1. Đọc ngay `AGENTS.md`, `HANDOFF_CONTEXT.md`, `docs/superpowers/specs/2026-11-06-ai-writing-style-auditor-design.md` và `docs/superpowers/plans/2026-11-06-ai-writing-style-auditor-plan.md`.
2. Tham chiếu `knowledge_base/ai_writing_rules_engine.json` để lấy đầy đủ bộ từ khóa kích hoạt và quy tắc của 26 dấu hiệu.
3. Thực thi lần lượt **Task 1 $\rightarrow$ Task 2 $\rightarrow$ Task 3 $\rightarrow$ Task 4** trong `docs/superpowers/plans/2026-11-06-ai-writing-style-auditor-plan.md`, tuân thủ nghiêm ngặt 2 quy tắc bắt buộc trong `AGENTS.md` (chạy kiểm thử đầy đủ và tạo Git commit sau mỗi lần hoàn thành thay đổi).

