# TÀI LIỆU BÀN GIAO TOÀN DIỆN CHO PHIÊN XỬ LÝ BACKEND (BACKEND HANDOFF SPECIFICATION)
## Dự án: AI Writing Style Auditor — Khối ngành Kinh tế (Bản nâng cấp Deep-Recall Zero-Miss 26 Quy tắc)

> **Mục tiêu phiên Backend**: Triển khai trực tiếp và triệt để toàn bộ kế hoạch nâng cấp Engine Python (`api/engine/`), mở rộng bộ từ điển (`lexicon.py`), nâng cấp regex & thuật toán nhận diện 26 quy tắc (`rules.py`), bổ sung kiểm toán liên đoạn (`auditor.py`), lọc nhiễu bảng biểu (`docxParser.ts`), và chạy test thực chiến trên 6 khóa luận tốt nghiệp thực tế đảm bảo **tuyệt đối không bỏ sót bất kỳ dấu hiệu AI-writing nào** (cả văn phong hoa mỹ lẫn ngụy trang học thuật trung tính).

---

## MỤC LỤC TỔNG QUAN
1. [Bối cảnh & Kiến trúc Hệ thống](#1-bối-cảnh--kiến-trúc-hệ-thống)
2. [Chẩn đoán Thực chứng từ 6 Khóa luận Thật (Empirical Gap Analysis)](#2-chẩn-đoán-thực-chứng-từ-6-khóa-luận-thật)
3. [Bản đồ Cơ sở Tri thức: 26 Quy tắc, 6 Chỉ số & Từ điển Kinh tế](#3-bản-đồ-cơ-sở-tri-thức)
4. [Đặc tả Kỹ thuật Chi tiết: Phương án Nâng cấp Từng File](#4-đặc-tả-kỹ-thuật-chi-tiết)
5. [Kế hoạch Triển khai 4 Bước (Step-by-Step Implementation)](#5-kế-hoạch-triển-khai-4-bước)
6. [Tiêu chuẩn Kiểm thử & Xác minh (Verification Checklist)](#6-tiêu-chuẩn-kiểm-thử--xác-minh)
7. [Prompt Khởi động Dành riêng cho Phiên Backend](#7-prompt-khởi-động-cho-phiên-backend)

---

## 1. BỐI CẢNH & KIẾN TRÚC HỆ THỐNG

### 1.1. Kiến trúc Đã chốt (Phương án b — Single-Source Python Engine)
- **Engine cốt lõi (Backend)**: Đặt tại `api/engine/` chạy trên Vercel Serverless Function qua `api/audit.py`.
  - [`api/engine/lexicon.py`](file:///g:/Antigravity/Th%C6%B0%20mu%CC%A3c%20m%C6%A1%CC%81i/api/engine/lexicon.py): Từ điển bảo vệ 8 chuyên ngành kinh tế (`UNIFIED_ECONOMICS_LEXICON`), các tập từ khóa AI, và bộ sinh gợi ý sửa lỗi động `build_contextual_suggestion()`.
  - [`api/engine/tokenizer.py`](file:///g:/Antigravity/Th%C6%B0%20mu%CC%A3c%20m%C6%A1%CC%81i/api/engine/tokenizer.py): Tách câu tiếng Việt, chuẩn hóa âm tiết, đếm âm tiết Hán-Việt, tính toán các chỉ số thống kê.
  - [`api/engine/rules.py`](file:///g:/Antigravity/Th%C6%B0%20mu%CC%A3c%20m%C6%A1%CC%81i/api/engine/rules.py): Triển khai thuật toán kiểm toán 26 quy tắc ở cấp độ đoạn văn (`ParagraphAuditor`).
  - [`api/engine/auditor.py`](file:///g:/Antigravity/Th%C6%B0%20mu%CC%A3c%20m%C6%A1%CC%81i/api/engine/auditor.py): Kiểm toán cấp tiểu mục/chương/tài liệu (`DocumentAuditor`), tính toán 6 chỉ số định lượng ($CV_L, ISI, OPR, SVCI, SICD, BCR$), và kiểm toán liên đoạn (Cross-Paragraph Discourse).
  - [`api/audit.py`](file:///g:/Antigravity/Th%C6%B0%20mu%CC%A3c%20m%C6%A1%CC%81i/api/audit.py): FastAPI endpoint tiếp nhận payload `{ document: DocumentModel }`, gọi `DocumentAuditor`, và trả về kết quả audit dạng JSON.
- **Frontend**: Vite + React + TypeScript + Tailwind CSS (`src/`).
  - [`src/utils/docxParser.ts`](file:///g:/Antigravity/Th%C6%B0%20mu%CC%A3c%20m%C6%A1%CC%81i/src/utils/docxParser.ts): Đọc file `.docx` bằng `mammoth`, parse HTML sang DOM, chia cây Chương/Mục, gửi sang `/api/audit`.

### 1.2. Vấn đề Hiện tại Cần Khắc phục Triệt để
Trong đợt test thực tế, hệ thống chỉ kích hoạt được 10–12 quy tắc (`RHY-01`, `DIS-03`, `SYN-04`, `SYN-VN-01`, `DIS-01`, `SYN-01`, `SYN-02`, `ARG-03`, `LEX-01`...). **Có tới 14 quy tắc bị "đóng băng" hoặc bỏ sót nghiêm trọng** do:
1. Regex quá hẹp, khớp chuỗi cố định thay vì khớp mẫu ngữ pháp (grammar patterns).
2. Điều kiện kích hoạt quá khắt khe (đòi $\ge 4$ câu trong 1 đoạn, hoặc $\ge 2$ lần xuất hiện trong cùng 1 câu).
3. Bỏ sót hoàn toàn văn phong **"Stealth Academic AI"** (Claude 3.5/4 & GPT-5 khi người dùng prompt *"viết văn phong học thuật trung tính, không dùng từ sáo rỗng"*).
4. Nhiễu bảng biểu từ file `.docx` làm loãng mật độ và số lượng đoạn văn.

---

## 2. CHẨN ĐOÁN THỰC CHỨNG TỪ 6 KHÓA LUẬN THẬT

Dữ liệu kiểm thử thực tế gồm 6 khóa luận tốt nghiệp thuộc ĐH Kinh tế Quốc dân (NEU) và các trường kinh tế:
1. **GKM Homes** (`media_1794045100630_459f1169.docx`): Quản trị tinh gọn 5S MIV.
2. **Viettel Software - VTIT** (`media_1794047484437_13910211.docx`): Quản trị tri thức B2B.
3. **E-COM WOW** (`media_1794047484454_0c4ad99e.docx`): Tạo động lực lao động.
4. **Karve Meilleur** (`media_1794047484451_ac9ee515.doc`): Quản trị thương hiệu.
5. **Nội thất An Cường** (`media_1794047484451_0171bd7e.docx`): Marketing Mix 4P.
6. **Hecatech** (`media_1794047484440_ace55a9e.docx`): Đánh giá thực hiện công việc.

### 2.1. Thế hệ AI 1: AI Khuếch đại Hoa mỹ (Classic GPT-4/GPT-4o)
- **Biểu hiện**: Sáo ngữ định danh, ẩn dụ sáo rỗng học thuật, PR doanh nghiệp dày đặc:
  - *"bứt phá mạnh mẽ", "nhảy vọt phi mã", "vươn ra biển lớn", "nút thắt cổ chai", "kim chỉ nam xuyên suốt", "bệ phóng vững chắc", "tảng băng chìm", "cát cứ tri thức", "thành tựu rực rỡ", "năng lực thực chiến đỉnh cao", "tài sản trí tuệ vô giá", "kho tàng tri thức đồ sộ"*.
- **Vì sao Engine cũ bỏ sót**: `LEX-01`, `LEX-02`, `LEX-03` chỉ có 8–14 cụm từ cứng, thiếu **Bộ đếm cụm mật độ từ vựng khuếch đại (Density Cluster Counter)**.

### 2.2. Thế hệ AI 2: AI Ngụy trang Học thuật Trung tính (Claude 3.5/4 & GPT-5)
Khi sinh viên cấm AI dùng từ hoa mỹ, AI chuyển sang các dấu vân tay cú pháp & diễn ngôn sau:
1. **Biến thể Sóng đôi phủ định (`SYN-03` — `WP:AIPARALLEL`)**:
   - `không phải (chỉ) (là) [X], mà (còn) (là) [Y]`: Xuất hiện **>30 lần** trong *Karve Meilleur* (*"không phải là hoạt động marketing bổ sung mà là chiến lược tăng trưởng cốt lõi"*, *"không phải bản dịch máy móc mà là..."*).
   - `[X] chứ không (chỉ) (phải) (là) [Y]`: Xuất hiện **>40 lần** trong *Hecatech* (*"xét về bản chất đây là một đơn vị kinh doanh chứ không phải một dự án"*, *"là chi phí học việc chứ không phải chi phí bán hàng"*).
   - *Engine cũ chỉ bắt `không chỉ... mà còn...` nên bỏ sót 100% hai cấu trúc này!*
2. **Lạm dụng từ rào đón mức độ mơ hồ (`LEX-05` — Hedging Qualifier Inflation)**:
   - Dùng từ `"tương đối"` (*tương đối nhanh, tương đối đầy đủ, tương đối tích cực, tương đối hợp lý*) và `"nhất định"` (*những kết quả nhất định, một số hạn chế nhất định*) từ **45–60 lần/bài** (2–4 lần trong 1 đoạn).
   - *Engine cũ không có bộ đếm từ rào đón mơ hồ này.*
3. **Rào đón miễn trừ trách nhiệm phương pháp luận & khan hiếm dữ liệu (`PRG-02b` & `PRG-02c` — `WP:AIDISCLAIMER`)**:
   - `PRG-02b` (Tự thú nhận giới hạn prompt): *"Trong phạm vi dữ liệu nghiên cứu, chưa có tài liệu cho thấy doanh nghiệp đã..."*, *"Dữ liệu hiện có mới cho thấy...; để khẳng định quan hệ nhân quả cần thêm dữ liệu..."*.
   - `PRG-02c` (Rào đón cách hiểu chỉ số): *"Khóa luận không sử dụng Maslow để... mà chỉ coi đây là khung tham chiếu..."*, *"không tính trực tiếp khoảng chênh lệch giữa hai loại điểm vì hai loại điểm phản ánh hai khía cạnh khác nhau"*, *"không dùng sự thay đổi của chỉ tiêu này để khẳng định trực tiếp quan hệ nhân quả"*.
   - *Engine cũ chỉ có 4 cụm `điều quan trọng cần lưu ý là`, bỏ sót 100% `PRG-02b` và `PRG-02c`!*
4. **Cấu trúc dịch máy chèn `"vì vậy"` giữa Chủ ngữ và Vị ngữ (`SYN-VN-01` / `SYN-VN-02`)**:
   - Dịch nguyên vị trí của tiếng Anh `Subject therefore Verb`: *"Mục tiêu vì vậy tăng nhanh hơn..."*, *"Doanh nghiệp vì vậy cần làm rõ..."*, *"Chuẩn giao cho người lao động vì vậy phải thay đổi..."*.
5. **Đoạn kết tiểu mục tổng kết thừa (`DIS-02` Cross-Paragraph Echoic Subsection Closure)**:
   - Cuối mỗi tiểu mục, AI tạo một đoạn 1–3 câu bắt đầu bằng *"Như vậy,..."*, *"Nhìn chung,..."*, *"Tóm lại,..."*, *"Có thể thấy,..."* rồi kết bằng *"Đây là cơ sở để tiếp tục xem xét / đề xuất giải pháp ở phần tiếp theo / Chương 3"*.
   - *Engine cũ đòi `n_sent >= 4` nên bỏ sót toàn bộ các đoạn kết 1–3 câu này!*
6. **Mở đầu đoạn định danh & bình luận bảng rập khuôn (`DIS-04` & `SYN-01`)**:
   - *Karve Meilleur*: 10 đoạn liên tiếp mở đầu bằng `[Danh động từ X] là hạng mục/bước/công cụ trọng tâm/cốt lõi...`.
   - *Hecatech*: 18 đoạn liên tiếp sau bảng mở đầu bằng `"Bảng trên cho thấy ba/bốn điểm. Thứ nhất,... Thứ hai,..."`.
7. **Quỹ đạo con lắc 3 pha (`ARG-02`)**:
   - Đoạn văn 3 pha: `[Nêu ưu điểm] -> Tuy nhiên, [nêu hạn chế / chưa đồng đều / chưa rõ ràng] -> Do đó / Vì vậy / Đây là cơ sở để [cần tiếp tục hoàn thiện / rà soát / cân bằng]`.
   - *Engine cũ đòi từ khóa cứng `toàn diện|đồng bộ|hài hòa|bền vững` ở câu cuối nên bỏ sót >30 đoạn.*
8. **Dấu gạch ngang / gạch nối giải thích kiểu tiếng Anh (`FMT-01`)**:
   - Dùng ` — ` hoặc ` - ` chèn mệnh đề giải thích giữa câu văn xuôi ở 20+ đoạn trong bài *Karve Meilleur* và *An Cường*.

---

## 3. BẢN ĐỒ CƠ SỞ TRI THỨC (TAXONOMY & METRICS)

### 3.1. Danh mục 26 Quy tắc (Chia theo 6 Nhóm)
1. **Nhóm Từ vựng (Lexical & Phraseological)**:
   - `LEX-01`: Sáo ngữ định danh & Mật độ từ vựng khuếch đại AI.
   - `LEX-02`: Né tránh hệ từ trực diện (`"là"`, `"có"`).
   - `LEX-03`: Ngôn ngữ phóng đại, tự tán dương (Corporate/Academic Puffery).
   - `LEX-04`: Xoay vòng từ đồng nghĩa thanh lịch giả tạo (Elegant Variation).
   - `LEX-05`: Động từ liên kết mơ hồ & Lạm dụng từ rào đón mức độ (`tương đối`, `nhất định`).
   - `LEX-VN-01`: Lạm dụng âm tiết Hán-Việt & Chuỗi danh hóa chồng chất.
2. **Nhóm Cú pháp (Syntactic & Sentence Structure)**:
   - `SYN-01`: Nhịp câu đều đặn đơn điệu, đẳng cấu cú pháp liên tiếp.
   - `SYN-02`: Đuôi câu phân từ / tổng kết giả tạo (`góp phần...`, `tạo tiền đề...`).
   - `SYN-03`: Cấu trúc sóng đôi phủ định (Negative Parallelism — 4 biến thể).
   - `SYN-04`: Bộ ba cấu trúc (Rule of Three — bộ ba tính từ, động từ, danh từ).
   - `SYN-VN-01`: Lạm dụng đại từ, danh từ chỉ định đầu câu, `"vì vậy"` chen giữa S-V.
   - `SYN-VN-02`: Cấu trúc Đề–Thuyết dịch máy (`Đối với...`, `Về mặt...`).
   - `SYN-VN-03`: Cấu trúc bị động dịch máy & Danh hóa `Việc + V` làm chủ ngữ.
   - `RHY-01`: Nhịp điệu câu đều đều đơn điệu ($CV_L < 0.22$).
3. **Nhóm Đoạn văn & Diễn ngôn (Discourse & Cohesion)**:
   - `DIS-01`: Đoạn văn đóng khung 4 bước khép kín.
   - `DIS-02`: Đoạn kết tiểu mục vọng âm, tổng kết thừa (Echoic Closure).
   - `DIS-03`: Lạm dụng liên từ cơ học đầu câu liên tiếp.
   - `DIS-04`: Dẫn nhập siêu diễn ngôn & Định danh hạng mục rập khuôn.
4. **Nhóm Lập luận & Nhận thức luận (Argumentation & Epistemic)**:
   - `ARG-01`: Trọng số luận điểm phẳng, liệt kê cơ học thiếu bằng chứng định lượng.
   - `ARG-02`: Quỹ đạo con lắc lập luận giả tạo (Pendulum Hedging 3 pha).
   - `ARG-03`: Cấu trúc khuếch đại bối cảnh vĩ mô / mở màn đại cảnh.
   - `ARG-04`: Cấu trúc đối lập hời hợt, khuyến nghị khẩu hiệu chung chung.
5. **Nhóm Ngữ dụng & Nguồn lực (Pragmatics & Attributions)**:
   - `PRG-01`: Quy chiếu đám đông mơ hồ (Weasel Attribution) & Nhấn mạnh truyền thông.
   - `PRG-02`: Rào đón miễn trừ trách nhiệm (`PRG-02a` giáo huấn, `PRG-02b` khan hiếm nguồn, `PRG-02c` rào đón cách hiểu chỉ số).
6. **Nhóm Định dạng & Cấu trúc (Formatting & Document)**:
   - `FMT-01`: Định dạng cơ học, lạm dụng dấu gạch ngang giải thích ` — ` / ` - `.
   - `FOR-01`: Cấu trúc tài liệu rập khuôn cứng nhắc.

### 3.2. 6 Chỉ số Định lượng Bắt buộc
1. **$CV_L$ (Coefficient of Variation of Sentence Length)**: Hệ số biến thiên độ dài câu ($CV_L = \sigma_L / \mu_L$). Nếu $CV_L < 0.28 \rightarrow$ cảnh báo nhịp văn máy móc.
2. **$ISI$ (Inter-Sentence Uniformity Index)**: Chỉ số tương đồng độ dài giữa các câu kế tiếp.
3. **$OPR$ (Opening Pronoun/Conjunction Ratio)**: Tỷ lệ câu mở đầu bằng từ nối / đại từ.
4. **$SVCI$ (Syntactic Variation Coefficient Index)**: Độ đa dạng cấu trúc ngữ pháp.
5. **$SICD$ (Syllable-Level Intonation & Cadence Dispersion)**: Phân tán âm điệu âm tiết.
6. **$BCR$ (Burstiness & Complexity Ratio)**: Tỷ lệ đột biến và phức hợp của văn bản.

### 3.3. Từ điển Bảo vệ 8 Chuyên ngành Kinh tế (`UNIFIED_ECONOMICS_LEXICON`)
Phải giữ nguyên tắc **Zero False Positives** trên thuật ngữ kinh tế:
- Quản trị kinh doanh, Quản trị nhân sự, Logistics & Hậu cần, Marketing, Ngân hàng, Tài chính, Kế toán – Kiểm toán, Quản trị sản xuất.
- Khi match bất kỳ cụm từ nào, phải kiểm tra nếu cụm từ nằm trong tên riêng doanh nghiệp (Viettel, An Cường, GKM...) hoặc thuật ngữ chuyên ngành đã bảo vệ thì **bỏ qua không phạt**.

---

## 4. ĐẶC TẢ KỸ THUẬT CHI TIẾT (NÂNG CẤP TỪNG FILE)

### 4.1. [`api/engine/lexicon.py`](file:///g:/Antigravity/Th%C6%B0%20mu%CC%A3c%20m%C6%A1%CC%81i/api/engine/lexicon.py)

#### Nhiệm vụ 1: Bổ sung `AI_INTENSIFIER_VOCAB` cho `LEX-01b`
Tập hợp các từ vựng khuếch đại:
```python
AI_INTENSIFIER_VOCAB = {
    "then chốt", "cốt lõi", "toàn diện", "đồng bộ", "sâu sắc", "triệt để", "đột phá",
    "bền vững", "thiết yếu", "mạnh mẽ", "vượt bậc", "tối ưu", "sống còn", "cấp thiết",
    "khắt khe", "gắt gao", "bệ phóng", "kim chỉ nam", "nút thắt", "mắt xích", "trụ cột",
    "đòn bẩy", "khai phá", "kiến tạo", "tiền đề", "động lực", "hài hòa", "chuyên sâu"
}
```

#### Nhiệm vụ 2: Bổ sung `VAGUE_HEDGING_QUALIFIERS` cho `LEX-05`
Tập hợp các mẫu rào đón mơ hồ:
```python
VAGUE_HEDGING_PATTERNS = [
    r"\btương\s+đối\s+(?:nhanh|chậm|cao|thấp|tốt|xấu|đầy\s+đủ|rõ\s+ràng|hợp\s+lý|tích\s+cực|tiêu\s+cực|đồng\s+đều|chặt\s+chẽ|hiệu\s+quả|ổn\s+định)\b",
    r"\b(?:một\s+số|những)\s+[^,.!?]{2,30}?\s+nhất\s+định\b",
    r"\bở\s+mức\s+độ\s+nhất\s+định\b",
    r"\bphần\s+nào\s+(?:phản\s+ánh|thể\s+hiện|tác\s+động|ảnh\s+hưởng)\b"
]
```

#### Nhiệm vụ 3: Mở rộng `SYNONYM_CYCLE_GROUPS` (`LEX-04`) lên 12 nhóm
Thêm các nhóm thực thể:
- `["thương hiệu", "nhãn hàng", "tên tuổi", "nhà mốt"]`
- `["dự án", "gói thầu", "thương vụ", "hợp đồng"]`
- `["sản phẩm", "mặt hàng", "dòng sản phẩm", "giải pháp"]`
- `["người quản lý", "nhà lãnh đạo", "cấp trên", "đội ngũ quản trị"]`
- `["nền tảng", "sàn thương mại điện tử", "kênh trực tuyến", "hệ thống"]`

#### Nhiệm vụ 4: Cập nhật `build_contextual_suggestion()` cho cả 26/26 Rules
Mọi mã rule (`LEX-01` đến `FOR-01`) đều phải có nhánh sinh gợi ý sửa bài kèm cụm từ vi phạm `«clean_match»` và câu văn học thuật mẫu.

---

### 4.2. [`api/engine/rules.py`](file:///g:/Antigravity/Th%C6%B0%20mu%CC%A3c%20m%C6%A1%CC%81i/api/engine/rules.py)

#### 1. `LEX-01`: Gộp Regex cụm ẩn dụ + Bộ đếm mật độ từ vựng khuếch đại (`LEX-01b`)
- Regex mở rộng: `r"\b(?:kim\s+chỉ\s+nam(?:\s+xuyên\s+suốt)?|bệ\s+phóng(?:\s+vững\s+chắc)?|nút\s+thắt\s+cổ\s+chai|tảng\s+băng\s+chìm|mắt\s+xích\s+(?:then\s+chốt|trung\s+tâm)|trụ\s+cột\s+chiến\s+lược|đòn\s+bẩy\s+chiến\s+lược|khai\s+phá|kiến\s+tạo|bóc\s+tách\s+toàn\s+diện|lăng\s+kính|hệ\s+sinh\s+thái|luồng\s+sinh\s+khí\s+mới|chuyển\s+mình|bước\s+đệm|tiền\s+đề\s+quyết\s+định|cát\s+cứ\s+tri\s+thức)\b"`
- Thuật toán `LEX-01b`: Đếm số từ trong `AI_INTENSIFIER_VOCAB`. Nếu đoạn có $\ge 3$ từ (hoặc tỷ lệ $\ge 2.5\%$ tổng số từ), gắn cờ vào cụm từ xuất hiện đầu tiên.

#### 2. `LEX-02`: Né tránh Hệ từ Trực diện (`"là"`, `"có"`)
- Bắt mọi biến thể:
  - Nhánh thay `"là"`: `r"\b(?:đóng|giữ)\s+vai\s+trò\s+(?:như\s+)?(?:là\s+)?(?:một\s+)?(?:yếu\s+tố|nền\s+tảng|công\s+cụ|mắt\s+xích|trụ\s+cột|đòn\s+bẩy|hạt\s+nhân|thành\s+phần|bộ\s+phận|chìa\s+khóa|tiền\s+đề|động\s+lực|cầu\s+nối|thước\s+đo|minh\s+chứng)\b"`
  - `r"\bđược\s+(?:xem|coi|nhìn\s+nhận|đánh\s+giá|hiểu|định\s+nghĩa)\s+(?:như\s+)?là\s+một\b"`
  - `r"\b(?:đứng|hoạt\s+động)\s+như\s+một\b"`, `r"\bđại\s+diện\s+cho\s+một\b"`
  - Nhánh thay `"có"`: `r"\b(?:sở\s+hữu|tự\s+hào\s+có|nổi\s+bật\s+với|mang\s+trong\s+mình)\s+(?:những|các|một|hệ\s+thống|đội\s+ngũ|quy\s+mô|bề\s+dày|lợi\s+thế|ưu\s+điểm)\b"`

#### 3. `LEX-03`: Ngôn ngữ Tán dương Doanh nghiệp (Corporate Puffery)
- Bổ sung: `r"\b(?:vươn\s+mình\s+mạnh\s+mẽ|vươn\s+ra\s+biển\s+lớn|vươn\s+tầm\s+(?:quốc\s+tế|toàn\s+cầu|khu\s+vực)|bứt\s+phá\s+(?:mạnh\s+mẽ|ngoạn\s+mục|vượt\s+bậc|lớn\s+nhất)|nhảy\s+vọt\s+phi\s+mã|tăng\s+trưởng\s+(?:vô\s+cùng\s+)?ấn\s+tượng|thành\s+tựu\s+(?:kinh\s+doanh\s+)?rực\s+rỡ|năng\s+lực\s+thực\s+chiến\s+đỉnh\s+cao|tài\s+sản\s+(?:trí\s+tuệ\s+)?vô\s+giá|kho\s+tàng\s+tri\s+thức\s+.*?\s+đồ\s+sộ|đáng\s+tự\s+hào|sự\s+ưu\s+việt|tinh\s+hoa\s+quản\s+trị|cực\s+kỳ\s+(?:phong\s+phú|khốc\s+liệt|mạnh\s+mẽ))\b"`

#### 4. `LEX-04`: Giảm ngưỡng và bắt danh ngữ chỉ định đồng quy chiếu
- Bắt khi có $\ge 2$ biến thể từ nhóm đồng nghĩa xuất hiện trong cùng 1 đoạn kèm từ chỉ định (`này / đó / trên / nói trên / vừa nêu`).

#### 5. `LEX-05`: Động từ liên kết mơ hồ + Mật độ rào đón mơ hồ
- Bổ sung cụm: `r"\b(?:gắn\s+liền\s+với|có\s+mối\s+(?:liên\s+hệ|quan\s+hệ|tương\s+quan)\s+(?:mật\s+thiết|chặt\s+chẽ)\s+với|xoay\s+quanh\s+các|được\s+ghi\s+nhận\s+trong\s+mối\s+tương\s+quan|chịu\s+ảnh\s+hưởng\s+đồng\s+thời\s+bởi\s+nhiều\s+yếu\s+tố)\b"`
- Quét các mẫu trong `VAGUE_HEDGING_PATTERNS`. Nếu $\ge 2$ lần trong 1 đoạn $\rightarrow$ kích hoạt cờ `LEX-05`.

#### 6. `SYN-01`: Đẳng cấu Cú pháp trong Đoạn Phân tích Tiêu chí/Bảng biểu
- Bắt khi $\ge 2$ câu trong đoạn mở đầu bằng khung: `r"^(?:Tiêu\s+chí|Chỉ\s+tiêu|Yếu\s+tố|Khía\s+cạnh|Biến\s+quan\s+sát)\s+[^,]{2,40}\s+đạt\s+[\d.,]+\s+điểm"` hoặc `r"^(?:Về|Xét\s+về)\s+[^,]{2,35},\s*"` lặp lại liên tiếp.

#### 7. `SYN-02`: Đuôi câu Phân từ Tổng kết Giả tạo
- Bổ sung: `r",\s*(?:đồng\s+thời\s+)?(?:góp\s+phần|giúp|tạo\s+cơ\s+sở|tạo\s+điều\s+kiện|tạo\s+nền\s+tảng|tạo\s+tiền\s+đề|làm\s+cơ\s+sở|hướng\s+tới\s+việc)\s+(?:nâng\s+cao|cải\s+thiện|duy\s+trì|đảm\s+bảo|bảo\s+đảm|thúc\s+đẩy|tối\s+ưu\s+hóa|củng\s+cố|hoàn\s+thiện|hình\s+thành)\b[^.!?]+"`

#### 8. `SYN-03`: Sóng đôi Phủ định (Negative Parallelism — 4 Biến thể)
```python
SYN03_PATTERNS = [
    # Biến thể 1: không chỉ... mà còn...
    r"\bkhông\s+chỉ\s+[^.!?]{2,90}?\s+mà\s+còn\s+[^.!?]{3,90}",
    # Biến thể 2: không đơn thuần là... mà là...
    r"\bkhông\s+(?:đơn\s+thuần|dừng\s+lại|giới\s+hạn)\s+(?:ở|là)\s+[^.!?]{3,80}?\s+mà\s+(?:còn\s+)?(?:là|ở|hướng\s+tới|mở\s+rộng)\s+[^.!?]{3,80}",
    # Biến thể 3: không phải (chỉ) (là) X mà (còn) (là) Y (Rất dày đặc trong Karve Meilleur & An Cường)
    r"\bkhông\s+phải\s+(?:chỉ\s+)?(?:là\s+)?[^,.;!?]{3,80}?,?\s+mà\s+(?:còn\s+)?(?:là|phải\s+là|nằm\s+ở|ở)\s+[^.!?]{3,80}",
    # Biến thể 4: X chứ không (chỉ) (phải) (là) Y (Rất dày đặc trong Hecatech)
    r"\bchứ\s+không\s+(?:chỉ\s+)?(?:phải\s+)?(?:đơn\s+thuần\s+)?(?:là\s+)?[^,.;!?]{3,65}"
]
```

#### 9. `SYN-04`: Bộ ba Cấu trúc
- Bắt ngay từ lần xuất hiện đầu tiên nếu là bộ ba tính từ/động từ trừu tượng hoặc bộ ba song hành dài `[V1+N1], [V2+N2] và [V3+N3]` có tổng $\ge 6$ âm tiết Hán-Việt.

#### 10. `SYN-VN-01`: Lạm dụng Đại từ & `"vì vậy"` chen giữa Chủ–Vị
- Bổ sung nhận diện đại từ chỉ định đầu câu lặp lại: `r"^(?:Điều\s+này|Việc\s+này|Kết\s+quả\s+này|Thực\s+trạng\s+này|Diễn\s+biến\s+này)\s+(?:cho\s+thấy|phản\s+ánh|giúp|làm\s+cho|góp\s+phần)"`
- Bổ sung cấu trúc dịch can tiếng Anh: `r"\b[A-ZÀ-ỸĐ][a-zà-ỹ]+(?:\s+[a-zà-ỹ]+){1,6}\s+vì\s+vậy\s+(?:cần|phải|có\s+thể|sẽ|được|bị|không|luôn|thường|trở\s+nên|đòi\s+hỏi|tăng|giảm|thay\s+đổi|lệch)\b"`

#### 11. `SYN-VN-02`: Đề–Thuyết Dịch máy Mở rộng
- Regex: `r"(?:Đối\s+với|Liên\s+quan\s+đến|Xét\s+(?:về|trên)\s+(?:mặt|phương\s+diện|góc\s+độ|khía\s+cạnh)|Về\s+(?:mặt|phương\s+diện|phía|khía\s+cạnh)|Dưới\s+góc\s+(?:độ|nhìn)\s+(?:của)?)\s+[^,]{3,55},\s*(?:nó|chúng|điều\s+này|việc\s+này|hoạt\s+động\s+này|quá\s+trình\s+này|yếu\s+tố\s+này|tiêu\s+chí\s+này|chỉ\s+tiêu\s+này|kết\s+quả\s+này)?\s*(?:thường\s+|luôn\s+|cũng\s+|vẫn\s+)?(?:được|bị|đóng\s+vai\s+trò|giữ\s+vai\s+trò|chịu\s+ảnh\s+hưởng|có\s+ý\s+nghĩa)"`

#### 12. `SYN-VN-03`: Bị động & Danh hóa `Việc + V` làm chủ ngữ
- Bắt thêm: `r"^Việc\s+[a-zà-ỹ]+(?:\s+[a-zà-ỹ]+){3,12}\s+(?:giúp|làm\s+cho|khiến|góp\s+phần|tạo\s+điều\s+kiện|đóng\s+vai\s+trò|có\s+ý\s+nghĩa|là\s+cơ\s+sở|đã\s+và\s+đang)\b"` khi xuất hiện $\ge 2$ câu trong đoạn.

#### 13. `DIS-01`: Đoạn văn Đóng hộp Khép kín
- Bắt bất kỳ đoạn $\ge 3$ câu nào có: (Câu 1 nêu nhận định) + (Câu 2 chuyển ý/giải thích `Tuy nhiên/Bên cạnh đó/Cụ thể`) + (Câu cuối đóng hộp bằng `Vì vậy, / Do đó, / Như vậy, / Nhìn chung, / Tóm lại, / Qua đó, / Từ đó, / Đây là cơ sở để... / Đây là những nội dung cần...`).

#### 14. `DIS-02`: Đoạn kết Tiểu mục Rập khuôn
- Bỏ điều kiện cứng `n_sent >= 4`. Bắt mọi câu/đoạn kết mở đầu bằng `Như vậy, / Nhìn chung, / Tóm lại, / Có thể thấy, / Tổng hợp kết quả cho thấy,` HOẶC chứa vế kết:
  `r"(?:Đây\s+là\s+(?:cơ\s+sở|tiền\s+đề|căn\s+cứ)\s+(?:quan\s+trọng\s+)?để\s+tiếp\s+tục\s+(?:xem\s+xét|phân\s+tích|đề\s+xuất).*?(?:ở\s+phần\s+tiếp\s+theo|tại\s+Chương\s+\d)|Đây\s+là\s+những\s+(?:nội\s+dung|vấn\s+đề|hạn\s+chế)\s+.*?\s+cần\s+(?:ưu\s+tiên\s+)?(?:rà\s+soát|xem\s+xét|hoàn\s+thiện|khắc\s+phục)\s+trong\s+(?:thời\s+gian\s+tới|giai\s+đoạn\s+tiếp\s+theo))"`

#### 15. `DIS-04`: Dẫn nhập Đề cương & Định danh Đầu đoạn
- Bắt 3 nhánh:
  1. Khớp định nghĩa tiêu đề: `r"^[A-ZÀ-ỸĐ][^,.]{2,65}\s+(?:được\s+hiểu\s+là|có\s+thể\s+được\s+hiểu\s+là|được\s+định\s+nghĩa\s+là|là\s+quá\s+trình|là\s+hoạt\s+động|là\s+tập\s+hợp\s+các|là\s+một\s+trong\s+những)\b"`
  2. Dẫn nhập đề cương/bảng biểu: `r"(?:Trong\s+phạm\s+vi\s+(?:nghiên\s+cứu|khóa\s+luận)(?:\s+này)?,\s*[^.!?]+được\s+xem\s+xét|Bảng\s+(?:trên|dưới\s+đây|[\d.]+)\s+cho\s+thấy\s+(?:ba|bốn|hai|năm)\s+(?:điểm|điều|đặc\s+điểm))"`
  3. Định danh hạng mục đầu đoạn: `r"^[A-ZÀ-ỸĐ][^,.]{2,45}\s+là\s+(?:hạng\s+mục|bước|yếu\s+tố|công\s+cụ)\s+(?:trọng\s+tâm|cốt\s+lõi|bắt\s+buộc|quan\s+trọng)\b"`

#### 16. `ARG-02`: Quỹ đạo Con lắc Lập luận 3 Pha (Pendulum Hedging)
- Nhận diện 3 pha:
  - Pha 1: Nêu mặt tích cực / kết quả đã đạt được.
  - Pha 2: `Tuy nhiên / Song / Mặt khác / Bên cạnh những kết quả đạt được,` + từ chỉ hạn chế (`hạn chế, thách thức, khó khăn, chưa đồng đều, chưa rõ ràng, chưa đầy đủ, khoảng trống`).
  - Pha 3: `Do đó / Vì vậy / Đây là cơ sở để / Điều này đòi hỏi` + từ chỉ hành động hoàn thiện (`cần tiếp tục hoàn thiện, cần rà soát, cần đồng bộ, cần kết hợp hài hòa`).

#### 17. `ARG-03`: Khuếch đại Bối cảnh Vĩ mô
- Mở rộng độ dài mệnh đề trạng ngữ bối cảnh lên `[^.!?]{0,140}` để bắt các câu dài >80 ký tự trước dấu phẩy.
- Bổ sung: `r"\b(?:Trong\s+(?:kỷ\s+nguyên\s+kinh\s+tế\s+số|nền\s+kinh\s+tế\s+tri\s+thức\s+hiện\s+đại|thời\s+đại\s+công\s+nghệ\s+số)|phản\s+ánh\s+xu\s+hướng\s+rộng\s+lớn\s+hơn|để\s+lại\s+dấu\s+ấn|đặt\s+nền\s+móng\s+cho|mở\s+ra\s+kỷ\s+nguyên|khẳng\s+định\s+tầm\s+vóc)\b"`

#### 18. `ARG-04`: Khuyến nghị Khẩu hiệu Chung chung
- Bổ sung: `r"(?:Nếu\s+được\s+triển\s+khai\s+(?:đồng\s+bộ|phù\s+hợp)[^,]{0,60},\s*(?:hệ\s+thống\s+)?các\s+giải\s+pháp\s+(?:đề\s+xuất\s+)?có\s+thể\s+góp\s+phần\s+nâng\s+cao\s+[^.!?]+trong\s+(?:những\s+năm\s+tiếp\s+theo|thời\s+gian\s+tới|dài\s+hạn)|Mặc\s+dù\s+(?:đã\s+)?(?:đạt\s+được|ghi\s+nhận|có)\s+[^,]{5,90},\s*[^,]{3,60}\s+vẫn\s+(?:còn\s+)?(?:đối\s+mặt|tồn\s+tại|gặp\s+phải)\s+[^.!?]{5,90})"`

#### 19. `PRG-01`: Quy chiếu Đám đông & Độ phủ Truyền thông
- Bổ sung quy chiếu đám đông không trích dẫn: `r"\b(?:Theo\s+)?(?:các\s+chuyên\s+gia|nhiều\s+nhà\s+quan\s+sát|nhiều\s+nghiên\s+cứu|các\s+nghiên\s+cứu\s+trước\s+đây|giới\s+phân\s+tích|nhiều\s+học\s+giả|thực\s+tế\s+cho\s+thấy|thực\s+tiễn\s+cho\s+thấy)\s+(?:cho\s+rằng|nhận\s+định|chỉ\s+ra\s+rằng|khẳng\s+định\s+rằng)?\b"` khi trong câu không có `(Tác giả, Năm)` và không có số liệu.
- Bổ sung `PRG-01b` (Độ phủ truyền thông sáo rỗng trong *Karve Meilleur*): `r"\b(?:được\s+đưa\s+tin\s+bởi\s+[^.!?]+tạp\s+chí|được\s+đăng\s+tải\s+trên\s+các\s+ấn\s+phẩm|sự\s+đưa\s+tin\s+độc\s+lập\s+từ\s+các\s+cơ\s+quan\s+truyền\s+thông)\b"`

#### 20. `PRG-02`: Bổ sung Toàn diện 3 Nhánh `PRG-02a`, `PRG-02b`, `PRG-02c`
- `PRG-02a` (Giáo huấn): `r"\b(?:điều\s+quan\s+trọng\s+(?:cần\s+lưu\s+ý\s+)?là|cần\s+(?:phải\s+)?(?:lưu\s+ý|nhớ|nhấn\s+mạnh)\s+rằng|một\s+(?:điểm|lưu\s+ý|nguyên\s+tắc)\s+(?:quan\s+trọng\s+)?cần\s+(?:nhấn\s+mạnh|lưu\s+ý)\s+là)\b"`
- `PRG-02b` (Tự thú nhận giới hạn prompt): `r"\b(?:trong\s+phạm\s+vi\s+dữ\s+liệu\s+nghiên\s+cứu,\s*chưa\s+có\s+(?:tài\s+liệu|cơ\s+sở)\s+cho\s+thấy|mặc\s+dù\s+chi\s+tiết\s+cụ\s+thể\s+không\s+được\s+công\s+bố|dữ\s+liệu\s+hiện\s+có\s+mới\s+cho\s+thấy.*?để\s+khẳng\s+định\s+quan\s+hệ\s+nhân\s+quả\s+cần\s+thêm)\b"`
- `PRG-02c` (Rào đón miễn trừ cách hiểu chỉ số): `r"\b(?:(?:khóa\s+luận|nghiên\s+cứu)\s+(?:chỉ\s+)?sử\s+dụng\s+[^.!?]{3,50}\s+như\s+(?:một\s+|các\s+)?(?:khung\s+tham\s+chiếu|chỉ\s+báo\s+bổ\s+sung|cơ\s+sở\s+bổ\s+trợ).*?\s+(?:chứ\s+)?không\s+(?:coi|dùng|sử\s+dụng|đồng\s+nhất)|không\s+tính\s+trực\s+tiếp\s+(?:khoảng\s+)?chênh\s+lệch\s+giữa\s+hai\s+loại\s+điểm\s+vì\s+hai\s+loại\s+điểm\s+phản\s+ánh\s+hai\s+khía\s+cạnh\s+khác\s+nhau|không\s+dùng\s+sự\s+thay\s+đổi\s+của\s+chỉ\s+tiêu\s+này\s+để\s+khẳng\s+định\s+trực\s+tiếp\s+quan\s+hệ\s+nhân\s+quả)\b"`

#### 21. `FMT-01`: Dấu Gạch ngang & Gạch nối Giải thích
- Bắt dấu gạch ngang dài ` — ` chèn mệnh đề giải thích giữa câu: `r"\s+—\s+[a-zà-ỹ]"`
- Bắt gạch nối kiểu tiếng Anh: `r"\s+-\s+(?:tức\s+là|nghĩa\s+là|nơi\s+|con\s+số\s+|yếu\s+tố\s+|đây\s+là|một\s+trong\s+những|không\s+phải)\b"`

---

### 4.3. [`api/engine/auditor.py`](file:///g:/Antigravity/Th%C6%B0%20mu%CC%A3c%20m%C6%A1%CC%81i/api/engine/auditor.py) (Kiểm toán Liên Đoạn — Cross-Paragraph Discourse)

Bổ sung phương thức `_audit_cross_paragraph_patterns(self, section: SectionModel)` trong `DocumentAuditor`:
1. **Liên đoạn `DIS-02`**: Nếu đoạn văn cuối tiểu mục có $\le 3$ câu, mở đầu bằng `Như vậy / Nhìn chung / Tóm lại / Có thể thấy`, và có độ trùng lặp từ vựng nội dung với các đoạn trước trong mục $\ge 0.30$ mà không chứa số liệu mới $\rightarrow$ gán cờ `DIS-02`.
2. **Liên đoạn `DIS-04` & `SYN-01`**: Nếu $\ge 3$ đoạn văn trong mục có cùng một khuôn ngữ pháp mở đầu (ví dụ: `Tiêu chí [X] đạt...` hoặc `[Danh động từ] là bước...`) $\rightarrow$ gán cờ `DIS-04` / `SYN-01`.
3. **Liên đoạn `LEX-05`**: Nếu từ `"tương đối"` xuất hiện $\ge 5$ lần trong cùng 1 tiểu mục $\rightarrow$ phát cờ cảnh báo lạm dụng rào đón mơ hồ toàn mục.
4. **Liên đoạn `FMT-01`**: Nếu dấu ` — ` hoặc ` - ` giải thích xuất hiện ở $\ge 3$ đoạn trong mục $\rightarrow$ phạt định dạng cơ học cấp mục.

---

### 4.4. [`src/utils/docxParser.ts`](file:///g:/Antigravity/Th%C6%B0%20mu%CC%A3c%20m%C6%A1%CC%81i/src/utils/docxParser.ts) (Lọc Nhiễu Bảng biểu)

Trước khi bóc tách đoạn văn:
1. Bỏ qua các thẻ `<p>` nằm trong `<table>` (`el.closest('table') !== null`).
2. Bỏ qua các đoạn văn ngắn là chú thích nguồn hoặc tiêu đề hình/bảng:
   - `r"^(?:Nguồn|Source)\s*:"`
   - `r"^(?:Bảng|Hình|Sơ\s+đồ|Biểu\s+đồ)\s+\d+[\d.]*"`

---

## 5. KẾ HOẠCH TRIỂN KHAI 4 BƯỚC (STEP-BY-STEP ROADMAP)

### Bước 1: Mở rộng Từ điển & Gợi ý Sửa lỗi trong `lexicon.py`
- Khai báo `AI_INTENSIFIER_VOCAB`, `VAGUE_HEDGING_PATTERNS`, mở rộng `SYNONYM_CYCLE_GROUPS`.
- Cập nhật `build_contextual_suggestion()` đảm bảo đủ 26 rules có gợi ý sửa bài chi tiết.

### Bước 2: Nâng cấp Toàn bộ 26 Rules Cấp Đoạn văn trong `rules.py`
- Thay thế các regex hẹp bằng regex mở rộng theo đặc tả Phần 4.2.
- Triển khai thuật toán đếm mật độ từ vựng `LEX-01b` và `LEX-05`.
- Bổ sung 4 biến thể của `SYN-03` và các nhánh `PRG-02a/b/c`.

### Bước 3: Nâng cấp Kiểm toán Liên Đoạn trong `auditor.py`
- Bổ sung logic `_audit_cross_paragraph_patterns` kiểm tra `DIS-02`, `DIS-04`, `LEX-04`, `LEX-05`, `FMT-01`.
- Cập nhật logic gom cờ và tính điểm AI Probability của Section và Document.

### Bước 4: Lọc Nhiễu trong `docxParser.ts`, Cập nhật Test & Chạy Thực nghiệm trên 6 Khóa luận
- Cập nhật bộ lọc bảng biểu trong `src/utils/docxParser.ts`.
- Viết unit test trong `tests/test_rules_and_auditor.py` kiểm tra từng mẫu câu mới.
- Chạy script kiểm toán trên cả 6 khóa luận thật, xuất bảng đối chiếu số lượng phát hiện của từng rule để chứng minh zero-miss.

---

## 6. TIÊU CHUẨN KIỂM THỬ & XÁC MINH (VERIFICATION CHECKLIST)

1. **Unit Test Pass Rate**: Chạy `pytest` đạt 100% pass trên toàn bộ test suite.
2. **Zero False Positives**: Các văn bản luật kinh tế chuẩn, báo cáo tài chính chuẩn, và câu văn kinh tế lượng mẫu không bị phạt nhầm.
3. **6 Khóa luận Thật**:
   - Khóa luận *Karve Meilleur*: Bắt trúng $\ge 25$ cờ `SYN-03` (mẫu *"không phải là X mà là Y"*), $\ge 15$ cờ `FMT-01` và `PRG-01b`.
   - Khóa luận *Hecatech*: Bắt trúng $\ge 30$ cờ `SYN-03` (mẫu *"chứ không phải Y"*), $\ge 15$ cờ `SYN-VN-01` (mẫu *"vì vậy"* chen giữa S-V), và toàn bộ các đoạn mở đầu rập khuôn `DIS-04`.
   - Khóa luận *E-COM WOW* & *An Cường*: Bắt trúng các cờ `PRG-02b`, `PRG-02c`, `LEX-05` (mật độ *"tương đối"*), và `ARG-02` (quỹ đạo con lắc).
   - Khóa luận *Viettel Software* & *GKM Homes*: Bắt trọn toàn bộ các sáo ngữ `LEX-01`, `LEX-02`, `LEX-03`, `ARG-03`.

---

## 7. PROMPT KHỞI ĐỘNG DÀNH RIÊNG CHO PHIÊN BACKEND

*Sao chép toàn bộ nội dung bên dưới và dán vào phiên làm việc mới để bắt đầu ngay lập tức:*

```text
Chào AI, tôi đưa bạn vào phiên làm việc này với vai trò Chuyên gia Kiến trúc Backend & Security/Audit Engine cho dự án "AI Writing Style Auditor" (Khối ngành Kinh tế).

Toàn bộ bối cảnh, chẩn đoán thực chứng từ 6 khóa luận tốt nghiệp thực tế và kế hoạch kỹ thuật chi tiết đã được biên soạn đầy đủ tại file:
`file:///g:/Antigravity/Thư mục mới/BACKEND_HANDOFF_FULL_SPEC.md`
và kế hoạch tổng thể tại:
`file:///g:/Antigravity/Thư mục mới/docs/superpowers/plans/2026-11-07-full-26-rules-deep-recall-upgrade-plan.md`

NHIỆM VỤ CỦA BẠN TRONG PHIÊN NÀY:
Hãy đọc ngay file `BACKEND_HANDOFF_FULL_SPEC.md` và thực thi lần lượt 4 bước nâng cấp backend:
1. Nâng cấp `api/engine/lexicon.py`: Thêm `AI_INTENSIFIER_VOCAB`, `VAGUE_HEDGING_PATTERNS`, mở rộng 12 nhóm `SYNONYM_CYCLE_GROUPS`, và hoàn thiện hàm gợi ý `build_contextual_suggestion()` cho toàn bộ 26/26 rules.
2. Nâng cấp `api/engine/rules.py`: Triển khai đầy đủ các mẫu regex mở rộng, bộ đếm mật độ từ vựng khuếch đại (LEX-01b), 4 biến thể của SYN-03 (đặc biệt là 'không phải X mà là Y' và 'chứ không phải Y'), PRG-02b/c, LEX-02, LEX-05, SYN-VN-01 (vì vậy chen giữa S-V), DIS-02 (đoạn kết 1-3 câu), ARG-02 (con lắc 3 pha), FMT-01 (dấu gạch ngang giải thích)...
3. Nâng cấp `api/engine/auditor.py`: Bổ sung kiểm toán liên đoạn (Cross-Paragraph Discourse) cho DIS-02, DIS-04, LEX-04, LEX-05, FMT-01.
4. Lọc nhiễu bảng biểu trong `src/utils/docxParser.ts`, cập nhật bộ test trong `tests/test_rules_and_auditor.py` và chạy xác minh thực tế trên 6 file khóa luận mẫu.

QUY TẮC BẮT BUỘC:
- Tuyệt đối không xóa bỏ các cơ chế bảo vệ thuật ngữ 8 chuyên ngành kinh tế (`UNIFIED_ECONOMICS_LEXICON`).
- Giữ vững nguyên tắc Zero False Positives trên văn bản kinh tế lượng chuẩn.
- Sau khi code xong mỗi bước, chạy test và tạo Git commit tương ứng theo quy định tại AGENTS.md.
- Hãy bắt đầu từ Bước 1 ngay bây giờ!
```
