# AI Style Auditor (Audit AI Writing)

> **Hệ thống Kiểm toán Văn phong Học thuật & Rà soát Lối viết Máy móc dành cho Luận văn, Khóa luận (.docx)**

AI Style Auditor là giải pháp kiểm toán văn phong học thuật chuyên sâu chạy trên nền web. Ứng dụng cho phép tải trực tiếp tệp Microsoft Word (`.docx`), tự động nhận diện cây cấu trúc Chương/Mục, bóc tách và phân tích các dấu hiệu văn phong máy móc theo 3 mức độ trực quan: **Cần sửa ngay**, **Nên sửa**, và **Gợi ý biên tập**, kèm chế độ xem tô sáng dạng Turnitin Feedback Studio và xuất báo cáo kiểm toán đa định dạng.

---

## 🌟 Tính Năng Nổi Bật

- **Bóc tách file `.docx` trực tiếp trên trình duyệt**: Giữ nguyên tiêu đề Heading, định dạng đậm/nghiêng, tự động loại trừ Bìa, Lời cam đoan, Mục lục và Danh mục tài liệu tham khảo.
- **Bộ máy kiểm toán Python Serverless**: Chạy nhẹ nhàng dưới 5MB trên Vercel hoặc local, xử lý văn bản tiếng Việt với độ chính xác cao, tự động nhận diện và bảo vệ thuật ngữ chuyên môn.
- **Giao diện SaaS 3 Cột Hiện đại**:
  - *Cột Trái (25%)*: Cây cấu trúc Chương/Mục & bộ lọc mức độ phát hiện.
  - *Cột Giữa (50%)*: Trình đọc bản thảo với 2 chế độ xem: **Soát lỗi tập trung** và **Turnitin Feedback Studio** (tô màu theo dải tần số).
  - *Cột Phải (25%)*: Bảng chẩn đoán chi tiết với bằng chứng, nguyên nhân và công thức viết lại học thuật.
- **Xuất Báo Cáo Chuyên Nghiệp**:
  - In ấn / Lưu PDF sạch sẽ (tự động xử lý ngắt trang và chống trang trắng).
  - Tải về tệp HTML độc lập hoặc dữ liệu JSON.
- **Hỗ trợ Dark Mode / Light Mode**: Tối ưu thị giác khi đọc bản thảo dài.

---

## 🚀 Hướng Dẫn Chạy Local (Dành Cho Người Dùng Mới)

Dự án được thiết kế để bất kỳ ai tải về hoặc clone đều có thể khởi chạy dễ dàng chỉ với **2 lệnh**:

### Yêu Cầu Môi Trường
- **Node.js**: Phiên bản 18.0 trở lên ([Tải tại đây](https://nodejs.org/))
- **Python**: Phiên bản 3.10 trở lên ([Tải tại đây](https://www.python.org/))

### Các Bước Cài Đặt & Chạy

1. **Clone hoặc Giải nén thư mục dự án**:
   ```bash
   git clone https://github.com/CacPhan/audit-aiwriting.git
   cd audit-aiwriting
   ```

2. **Cài đặt các gói phụ thuộc (Dependencies)**:
   ```bash
   npm install
   ```

3. **Khởi chạy ứng dụng**:
   ```bash
   npm run dev
   ```

4. **Mở trình duyệt**:
   - Truy cập vào địa chỉ: `http://localhost:5173`
   - *Lưu ý*: Máy chủ phát triển Vite đã tích hợp sẵn cầu nối middleware tự động gọi backend Python (`api/audit.py`), bạn **không cần cài thêm server ngoài**.

### Chạy Kiểm Thử Tự Động (Optional)

- Kiểm thử Frontend & Trình bóc tách `.docx`:
  ```bash
  npm test
  ```
- Kiểm thử Bộ máy Quy tắc Python:
  ```bash
  python -m pytest
  ```

---

## ☁️ Hướng Dẫn Triển Khai Lên Vercel (Deploy to Vercel)

Dự án đã được cấu hình tối ưu sẵn sàng 100% cho Vercel (`vercel.json`, `api/audit.py` chuẩn Serverless Handler):

1. Đăng nhập vào [Vercel](https://vercel.com).
2. Nhấn **Add New Project** $\rightarrow$ chọn Repository **`audit-aiwriting`**.
3. Tại phần **Project Name**, bạn có thể đặt tên là `checkai` (để nhận domain `checkai.vercel.app`).
4. Nhấn **Deploy**.
5. Sau khoảng 1 phút, trang web sẽ chính thức hoạt động online với đầy đủ cả Frontend React và Python Serverless Function.

---

## 📂 Cấu Trúc Dự Án

```
├── api/                        # Backend Python Serverless Function
│   ├── audit.py                # Handler HTTP /api/audit (cho Vercel & local bridge)
│   └── engine/                 # Bộ máy quy tắc & xử lý ngôn ngữ học thuật
│       ├── auditor.py          # Bộ điều phối phân tích văn bản
│       ├── lexicon.py          # Từ điển bảo vệ thuật ngữ chuyên môn
│       ├── rules.py            # 26 quy tắc nhận diện văn phong AI
│       └── tokenizer.py        # Bộ tách câu tiếng Việt & che mặt nạ
├── src/                        # Frontend React + TypeScript + Tailwind CSS
│   ├── components/             # Các component giao diện (Header, Sidebar, Viewer...)
│   ├── utils/                  # docxParser (mammoth) & reportExporter
│   ├── App.tsx                 # Điều phối 3 màn hình (Home, Workspace, Insights)
│   └── main.tsx
├── tests/                      # Bộ kiểm thử tự động (pytest & vitest)
│   ├── fixtures/               # Các file .docx mẫu phục vụ kiểm thử
│   ├── test_rules_and_auditor.py
│   └── test_tokenizer.py
├── package.json                # Cấu hình scripts & dependencies frontend
├── requirements.txt            # Phụ thuộc Python (pytest)
├── vercel.json                 # Cấu hình rewrite & routing trên Vercel
└── vite.config.ts              # Cấu hình Vite & middleware Python cục bộ
```

---

## 📄 Bản Quyền & Giấy Phép

Dự án được phát triển nhằm mục đích hỗ trợ học thuật, rà soát tính tự nhiên và nâng cao chất lượng văn phong nghiên cứu khoa học.
