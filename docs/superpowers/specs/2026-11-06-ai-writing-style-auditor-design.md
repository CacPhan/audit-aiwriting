# THIẾT KẾ KỸ THUẬT ĐÃ PHÊ DUYỆT (APPROVED DESIGN SPEC): AI WRITING STYLE AUDITOR
**Hệ thống Kiểm toán Văn phong Học thuật Khối ngành Kinh tế – Kinh doanh – Tài chính – Ngân hàng – Kế Kiểm – Vận hành**
- **Ngày phê duyệt**: 2026-11-06
- **Trạng thái**: Đã phê duyệt (Approved by User)
- **Mục tiêu triển khai**: GitHub Repository $\rightarrow$ Import trực tiếp lên **Vercel (`vercel.app`)**

---

## 1. Mục đích, Đối tượng và Giá trị Cốt lõi (Intent & The Why)
- **Người dùng mục tiêu**: Sinh viên đại học và học viên cao học thuộc **toàn bộ khối ngành Kinh tế – Kinh doanh hợp nhất** (bao gồm: *Quản trị kinh doanh, Quản trị nhân sự, Logistics & Hậu cần, Marketing, Tài chính – Ngân hàng, Kế toán – Kiểm toán, Quản trị sản xuất & Vận hành, Kinh tế học*).
- **Trải nghiệm không cần chọn chuyên ngành**: Hệ thống **hợp nhất toàn bộ từ điển thuật ngữ và quy tắc của cả 8 chuyên ngành Kinh tế** vào một bộ máy duy nhất — sinh viên tải luận văn lên là kiểm toán ngay lập tức mà không cần phải chọn dropdown chuyên ngành.
- **Chiến lược sản phẩm (Audit-First MVP & Monetization Hook)**:
  - **Phiên bản hiện tại (Core Audit System)**: Tập trung hoàn thiện 100% luồng **Kiểm toán Văn phong (Audit)** cho file luận văn `.docx` dài 70–90+ trang (hoặc văn bản dán trực tiếp): Bóc tách mục lục Chương/Mục, chạy thuật toán 26 quy tắc, tô sáng chính xác câu/cụm từ mắc lỗi trên giao diện đọc kiểm toán, giải thích chi tiết cơ sở ngôn ngữ học, chấm điểm mức độ biểu hiện thực tế ($CV_L, ISI, OPR, SVCI, SICD, BCR$), hướng dẫn công thức sửa cụ thể cho từng lỗi và **Xuất Báo cáo Kiểm toán (Audit Report HTML/In PDF/JSON)**.
  - **Định hướng Tính năng Trả phí (Pro Tier Hook)**: Tính năng *"Sửa trực tiếp trên Web kèm Chấm điểm Real-time & Xuất file `.docx` giữ nguyên định dạng"* được thiết kế sẵn điểm chạm giao diện (nút khóa `[PRO] Chỉnh sửa trực tiếp & Xuất .docx`) để sẵn sàng mở khóa thu phí ở giai đoạn thương mại hóa tiếp theo.

---

## 2. Mục tiêu, Phi mục tiêu và Phản mục tiêu (Goals, Non-Goals & Anti-Goals)
### 2.1. Mục tiêu (Goals)
- **G1 — Tương thích 100% với Vercel (`vercel.app`)**: Cấu trúc dự án chuẩn Vite/React TypeScript kết hợp Vercel Python Serverless Function (`/api/audit.py`, dung lượng $< 5\text{MB}$, không phụ thuộc thư viện nặng quá 250MB) và bộ máy quy tắc đồng nhất (`src/engine/`), đẩy lên GitHub và import vào Vercel là hoạt động ngay.
- **G2 — Đọc và Kiểm toán mượt mà luận văn `.docx` 70–90+ trang**: Tự động giải nén và phân tích file `.docx` (25.000–45.000+ chữ) thành cây cấu trúc Chương / Mục (`Chương 1`, `1.1`, `1.2`...), tự động nhận diện và lọc bỏ phần *Mục lục, Danh mục chữ viết tắt, Tài liệu tham khảo* để không báo lỗi nhầm.
- **G3 — Phát hiện, Tô sáng, Chấm điểm Toán học & Giải thích Minh bạch 26 Dấu hiệu**:
  - Phân tích theo 5 Nhóm Kiểm toán (`RHY` Nhịp văn, `SYN` Cú pháp, `VN-NAT` Bản ngữ Tiếng Việt, `DIS` Đoạn văn đóng hộp & Từ nối, `ARG & FOR` Lập luận & Dấu vết AI).
  - Hiển thị rõ lý do vì sao bị gắn cờ, trích dẫn quy tắc ngôn ngữ học và đưa ra hướng dẫn sửa cụ thể cho sinh viên.
- **G4 — Hợp nhất Từ điển Bảo vệ Thuật ngữ 8 Chuyên ngành Kinh tế**: Bảo vệ hơn **600+ cụm thuật ngữ chuyên môn** thuộc *Quản trị, Nhân sự, Logistics/Hậu cần, Marketing, Ngân hàng, Tài chính, Kế toán – Kiểm toán, Quản trị sản xuất* khỏi bị nhận diện nhầm là lỗi tắc nghẽn Hán–Việt hay sáo ngữ AI.
- **G5 — Xuất Báo cáo Kiểm toán Chuyên nghiệp (Audit Report)**: Hỗ trợ xem, tải xuống bản báo cáo HTML độc lập và chế độ **In / Lưu PDF chuẩn học thuật** (gồm Điểm tổng thể, Biểu đồ 5 trụ cột văn phong, Bảng điểm theo từng Chương/Mục, Chỉ số định lượng $CV_L, OPR, SVCI, SICD$, và Danh sách chi tiết từng câu cần sửa kèm hướng dẫn).

### 2.2. Phi mục tiêu trong Giai đoạn Hiện tại (Non-Goals)
- Chưa mở khóa trình soạn thảo trực tiếp (Live Editor) và xuất file `.docx` đã sửa (được giữ làm tính năng **Pro / Trả phí** hiển thị dưới dạng khóa nâng cấp trên UI).
- Không bắt người dùng chọn chuyên ngành trước khi kiểm toán.

---

## 3. Kiến trúc Hệ thống trên Vercel (System Architecture)

```mermaid
flowchart TD
    A["Sinh viên tải file Luận văn .docx (70-90+ trang)\nhoặc dán văn bản mẫu"] --> B["Docx Parser & Chapter Tree Builder\n(Tách Chương 1..5, Mục 1.1..3.4 & Lọc bỏ Mục lục/TLTK)"]
    B --> C["Bộ Máy Kiểm Toán 26 Quy Tắc (Rule-Based Auditor)\n+ Từ điển Hợp nhất 8 Ngành Kinh tế (600+ thuật ngữ)"]
    C <--> D["Vercel Python Serverless API (/api/audit)\n& Client-Side High-Speed Batch Engine"]
    C --> E["Giao diện Kiểm toán 3 Cột (Audit Studio)\n- Cột 1: Cây Chương/Mục & Điểm từng phần\n- Cột 2: Văn bản Tô sáng theo 5 nhóm màu\n- Cột 3: Chi tiết Lỗi, Công thức Toán học & Hướng dẫn sửa"]
    E --> F["Xuất Báo Cáo Kiểm Toán (Audit Report)\nIn PDF trực tiếp / Tải file HTML & JSON"]
    E -.-> G["[PRO Feature Gate]\nNút 'Chỉnh sửa trực tiếp & Xuất .docx' (Tính năng trả phí)"]
```

---

## 4. Bộ Từ điển Hợp nhất 8 Chuyên ngành Kinh tế (Unified Economics Terminology Shield)

Bộ từ điển hợp nhất (`UNIFIED_ECONOMICS_LEXICON`) tự động bảo vệ các thuật ngữ chuyên ngành thuộc 8 lĩnh vực khi tính toán mật độ Hán–Việt (`LEX-VN-01`), lặp thuật ngữ (`LEX-04`) và danh hóa (`SYN-VN-03`):
1. **Tài chính – Ngân hàng**: *biên lãi ròng (NIM), tỷ lệ nợ xấu (NPL), tỷ lệ an toàn vốn (CAR), dự phòng rủi ro tín dụng, thanh khoản hệ thống, thị trường liên ngân hàng, lãi suất điều hành, chính sách tiền tệ, tỷ giá hối đoái, cấu trúc vốn, đòn bẩy tài chính, dòng tiền chiết khấu (DCF), giá trị hiện tại ròng (NPV), tỷ suất sinh lời nội bộ (IRR), tiền gửi không kỳ hạn (CASA), phân phối bảo hiểm qua ngân hàng (Bancassurance)...*
2. **Kế toán – Kiểm toán**: *báo cáo tài chính hợp nhất, bảng cân đối kế toán, báo cáo kết quả hoạt động kinh doanh, báo cáo lưu chuyển tiền tệ, chuẩn mực kế toán Việt Nam (VAS), chuẩn mực báo cáo tài chính quốc tế (IFRS), kiểm soát nội bộ, rủi ro có sai sót trọng yếu, bằng chứng kiểm toán, ý kiến kiểm toán chấp nhận toàn phần, khấu hao tài sản cố định, khoản phải thu, hàng tồn kho, giá vốn hàng bán, chi phí trả trước...*
3. **Quản trị sản xuất & Vận hành**: *quản trị sản xuất tinh gọn (Lean Manufacturing), hoạch định nguồn lực doanh nghiệp (ERP), quản lý chất lượng toàn diện (TQM), bảo trì năng suất toàn diện (TPM), cân bằng chuyền, định mức nguyên vật liệu (BOM), năng lực sản xuất, điểm hòa vốn, thời gian chu kỳ (cycle time), tỷ lệ phế phẩm, kiểm soát chất lượng bằng thống kê (SPC), sản xuất tức thời (Just-in-Time / JIT)...*
4. **Logistics & Hậu cần**: *quản trị chuỗi cung ứng, tồn kho an toàn (safety stock), thời gian chờ (lead time), vận tải đa phương thức, trung tâm phân phối, kho ngoại quan, dịch vụ logistics bên thứ ba (3PL), truy xuất nguồn gốc, chi phí lưu kho, thông quan hàng hóa, luồng hàng hải, vận đơn đường biển (Bill of Lading)...*
5. **Quản trị kinh doanh, Nhân sự & Marketing**: *lợi thế cạnh tranh, chuỗi giá trị, năng lực cốt lõi, quản trị chiến lược, đánh giá thực hiện công việc (KPI/OKR), thu hút và giữ chân nhân tài, đãi ngộ toàn diện, phân khúc thị trường, định vị thương hiệu, hành vi người tiêu dùng, truyền thông marketing tích hợp (IMC), trải nghiệm khách hàng...*
