# AGENTS.md — Quy tắc & Hướng dẫn Dành cho AI Agent

## Lưu ý quan trọng
- Sau mỗi lần hoàn thành thay đổi, bắt buộc phải tạo một Git commit tương ứng để thuận tiện cho việc truy vết và quay lại phiên bản trước đó.
- Sau mỗi lần thay đổi, bắt buộc phải chạy hoặc cập nhật các bài kiểm thử liên quan trước khi bàn giao cho người dùng, đảm bảo tất cả các bài kiểm thử và bước xác minh đều đạt yêu cầu.

---

## Bối cảnh Dự án & Kiến trúc Kỹ thuật Đã Chốt (Phương án b)
Dự án **AI Writing Style Auditor** (Hệ thống Kiểm toán Văn phong Học thuật Khối ngành Kinh tế cho khóa luận/luận văn `.docx` 70–90+ trang) đã hoàn thành giai đoạn Nghiên cứu Knowledge Base, Thiết kế Kỹ thuật (Design Spec) và Kế hoạch Triển khai (Implementation Plan).

- **Kiến trúc đã chốt (Phương án b — Single-Source Python Backend Engine trên Vercel)**:
  - **Backend (`api/engine/` & `api/audit.py`)**: Toàn bộ 26 quy tắc kiểm toán và 6 chỉ số định lượng ($CV_L, ISI, OPR, SVCI, SICD, BCR$) được viết **duy nhất 1 lần bằng Python** (`api/engine/`) và chạy trên Vercel Python Serverless Function (`POST /api/audit`, gọn nhẹ $< 5\text{MB}$).
  - **Frontend (`src/`)**: Vite + React + TypeScript + Tailwind CSS đảm nhiệm đọc file `.docx` (`mammoth` + DOMParser), chia cây Chương/Mục, gửi sang `/api/audit`, hiển thị giao diện Kiểm toán 3 cột, xuất Báo cáo Kiểm toán (HTML/Print-to-PDF/JSON), và hiển thị `ProUpgradeModal` cho tính năng trả phí (Sửa trực tiếp trên web kèm chấm điểm real-time & Xuất `.docx`).
  - **Hợp nhất 8 chuyên ngành Kinh tế**: Tự động bảo vệ thuật ngữ của 8 ngành (*Quản trị kinh doanh, Quản trị nhân sự, Logistics & Hậu cần, Marketing, Ngân hàng, Tài chính, Kế toán – Kiểm toán, Quản trị sản xuất*) trong `UNIFIED_ECONOMICS_LEXICON` mà không bắt người dùng chọn dropdown chuyên ngành.

## Bản đồ Tài liệu Bắt buộc Đọc Khi Bắt đầu Phiên Mới
1. **Tổng hợp bàn giao & các quyết định đã chốt của người dùng**: `HANDOFF_CONTEXT.md`
2. **Thiết kế kỹ thuật và thống nhất công nghệ/thuật toán (Approved Design Spec)**: `docs/superpowers/specs/2026-11-06-ai-writing-style-auditor-design.md`
3. **Kế hoạch triển khai chi tiết 4 Tasks (Implementation Plan)**: `docs/superpowers/plans/2026-11-06-ai-writing-style-auditor-plan.md`
4. **Cơ sở tri thức & Bộ máy quy tắc 26 dấu hiệu văn phong AI**:
   - Tài liệu gốc đầy đủ: `Sign of AI Writing.md` (`knowledge_base/source/Sign_of_AI_Writing_Full_Original.md`)
   - Dữ liệu JSON quy tắc & tri thức: `knowledge_base/ai_writing_rules_engine.json`, `knowledge_base/ai_writing_signs_kb.json`
   - Hồ sơ phân tích chuyên sâu: `knowledge_base/00_TAXONOMY_AND_INTERACTION_MAP.md` đến `knowledge_base/06_EVALUATION_AND_TESTING_FRAMEWORK.md`
