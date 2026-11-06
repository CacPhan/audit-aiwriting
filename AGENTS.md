# AGENTS.md — Quy tắc & Hướng dẫn Dành cho AI Agent

## Lưu ý quan trọng (BẮT BUỘC TUÂN THỦ)
- Sau mỗi lần hoàn thành thay đổi, bắt buộc phải tạo một Git commit tương ứng để thuận tiện cho việc truy vết và quay lại phiên bản trước đó.
- Sau mỗi lần thay đổi, bắt buộc phải chạy hoặc cập nhật các bài kiểm thử liên quan trước khi bàn giao cho người dùng, đảm bảo tất cả các bài kiểm thử và bước xác minh đều đạt yêu cầu.

---

## Bối cảnh Dự án & Tài liệu Thiết kế Đã Thống Nhất
Dự án **AI Writing Style Auditor** đã hoàn thành giai đoạn Nghiên cứu Knowledge Base, Thiết kế Kỹ thuật (Design Spec) và Kế hoạch Triển khai (Implementation Plan). Khi bắt đầu phiên làm việc mới, Agent cần đọc ngay các tài liệu sau (không hỏi lại các câu hỏi đã chốt):

1. **Tổng hợp bàn giao & các quyết định đã chốt của người dùng**: `HANDOFF_CONTEXT.md`
2. **Thiết kế kỹ thuật và thống nhất công nghệ/thuật toán (Approved Design Spec)**: `docs/superpowers/specs/2026-11-06-ai-writing-style-auditor-design.md`
3. **Kế hoạch triển khai chi tiết 4 Tasks (Implementation Plan)**: `docs/superpowers/plans/2026-11-06-ai-writing-style-auditor-plan.md`
4. **Cơ sở tri thức & Bộ máy quy tắc 26 dấu hiệu văn phong AI**:
   - `knowledge_base/ai_writing_rules_engine.json`
   - `knowledge_base/ai_writing_signs_kb.json`
   - Các hồ sơ phân tích chuyên sâu từ `knowledge_base/00_TAXONOMY_AND_INTERACTION_MAP.md` đến `knowledge_base/06_EVALUATION_AND_TESTING_FRAMEWORK.md`
