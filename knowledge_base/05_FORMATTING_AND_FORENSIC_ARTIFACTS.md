# HỒ SƠ NGHIÊN CỨU CHUYÊN SÂU — NHÓM 5: ĐỊNH DẠNG THỊ GIÁC, DẤU CÂU VÀ DẤU VẾT KỸ THUẬT / FORENSIC (`FMT` & `FOR`)
**(Giai đoạn 3, Giai đoạn 4, Đầu ra B & C — Hồ sơ `FMT-01` và `FOR-01`)**

---

## HỒ SƠ 25: `FMT-01` — ĐỊNH DẠNG THỊ GIÁC, BỐ CỤC DANH SÁCH VÀ DẤU CÂU CƠ HỌC (`WP:AILIST`, `WP:AIBOLD`, `WP:AIDASH`, `WP:AITITLECASE`)

### 1. Thông tin định danh
- **ID**: `FMT-01`
- **Tên dấu hiệu**: Hệ thống định dạng thị giác, danh sách tiêu đề in đậm, lạm dụng chữ đậm/viết hoa và biến thiên cực đoan của dấu câu (*Mechanical Visual Formatting, Inline-Header Lists, Typography & Punctuation Extremes*).
- **Nguồn gốc trong danh sách gốc**: Khối II — Mục *Style* (`WP:AITITLECASE`, `WP:AIBOLD`, `WP:AILIST`, *Heading errors*, `WP:AIEMOJI`, `WP:AITABLE`, `WP:AICURLY`) & Mục *Historical indicators* (`WP:AIDASH` — *Overuse of em dashes [2022–September 2026] & Subsequent punctuation flattening*).

### 2. Bước 1 — Định nghĩa vận hành, Phạm vi & Đơn vị quan sát
- **Cấp độ ngôn ngữ**: Đồ họa văn bản, Bố cục & Dấu câu ( Paratextual Typography, Layout & Punctuation).
- **Đơn vị quan sát**: Cấu trúc danh sách, thẻ tiêu đề (headings), thẻ nhấn mạnh (`**bold**`), và phân bố dấu câu trên toàn văn bản.
- **Định nghĩa vận hành**: Tập hợp các thói quen trình bày văn bản mang tính công thức do hệ thống hướng dẫn (system prompts) và huấn luyện RLHF tối ưu hóa cho khả năng "đọc lướt nhanh trên màn hình chat" (scannability), nhưng lại phá vỡ tính liền mạch của văn xuôi chuyên khảo, báo chí hoặc học thuật.

### 3. Bước 2 — Phân tích 6 biểu hiện con độc lập (Sub-manifestations)
1. **`FMT-01a` — Danh sách dọc có tiêu đề nội dòng in đậm kèm dấu hai chấm (`WP:AILIST` — *Inline-Header Vertical Lists*)**:
   - Công thức cố định:
     - `1. **[Cụm danh từ tiêu đề in đậm]**: [Một câu giải thích ngắn].`
     - `- **[Cụm danh từ tiêu đề in đậm]**: [Một câu giải thích ngắn].`
   - Ngay cả khi chỉ có 3 ý ngắn hoàn toàn có thể viết thành một câu văn xuôi mạch lạc, AI vẫn bẻ vụn thành danh sách gạch đầu dòng có tiêu đề in đậm và dấu hai chấm.
2. **`FMT-01b` — Lạm dụng in đậm cơ học kiểu "Key Takeaways" (`WP:AIBOLD`)**:
   - In đậm hàng loạt cụm danh từ hoặc thuật ngữ ngay giữa dòng văn xuôi (mỗi câu có 2–3 cụm **in đậm**) như thể đang làm slide thuyết trình hoặc tài liệu ôn thi.
3. **`FMT-01c` — Hai thái cực của Dấu gạch ngang dài (`WP:AIDASH`) và Sự phẳng hóa dấu câu (Punctuation Flattening)**:
   - **Thái cực 1 (2022 – tháng 09/2026)**: Lạm dụng dấu gạch ngang dài (`—` em dash, thường có khoảng trắng hai bên ` — `) ở mọi vị trí mà người viết bình thường dùng dấu phẩy, dấu ngoặc đơn hoặc dấu hai chấm để tạo nhịp nhấn kịch tính kiểu copywriting (`"không phải là X — mà là Y"`).
   - **Thái cực 2 (Từ tháng 09/2026 trở đi — Phản ứng ngược do Hard-coding)**: Do làn sóng nhận diện AI qua dấu `—`, các nhà phát triển mô hình (như GPT-5.1, GPT-6) đã ép cứng (hard-code/penalize) mô hình không được dùng dấu `—`. Hệ quả phụ ngoài ý muốn (unintended side effect) là mô hình **không dám dùng bất kỳ dấu câu thay thế giàu sắc thái nào khác** (như dấu chấm phẩy `;`, dấu hai chấm `:`, dấu ngoặc đơn `()`), khiến toàn bộ văn bản chỉ còn độc nhất dấu phẩy (`,`) và dấu chấm (`.`) với mật độ cao bất thường `[Cấp B]` (*The Economist, July 2026; Edwards, 2025/2026*).
4. **`FMT-01d` — Viết hoa chữ cái đầu mọi từ trong tiêu đề (`WP:AITITLECASE` — *Title Case in Headings*)**:
   - Trong tiếng Anh, AI luôn viết hoa tất cả các từ chính trong tiêu đề mục (`Impact of Technology and Digitalization`). Khi áp dụng sang tiếng Việt, một số mô hình hoặc bản dịch giữ thói quen viết hoa kiểu Title Case (`Tác Động Của Công Nghệ Và Chuyển Đổi Số`) — **vi phạm trực tiếp quy tắc chính tả tiếng Việt chuẩn** (chỉ viết hoa chữ cái đầu âm tiết thứ nhất của câu/tiêu đề và danh từ riêng).
5. **`FMT-01e` — Lỗi cấu trúc cây tiêu đề (*Heading Hierarchy Errors*) & Bảng biểu vụn (`WP:AITABLE`)**:
   - Đặt lại tiêu đề bài viết làm dòng Heading 1 đầu tiên; nhảy cóc cấp độ tiêu đề; tạo các tiêu đề cha rỗng (chỉ chứa tiêu đề con ngay bên dưới mà không có câu dẫn nhập); hoặc kẻ bảng Markdown cho những dữ liệu chỉ có 2–3 dòng đơn giản (`WP:AITABLE`) và gắn Emoji vào đầu tiêu đề/bullet (`✨ Giới thiệu`, `🚀 Kết luận` — `WP:AIEMOJI`).
6. **`FMT-01f` — Dấu ngoặc kép/nháy đơn cong không nhất quán (`WP:AICURLY`)**:
   - Một số mô hình (ChatGPT, DeepSeek) mặc định sinh dấu ngoặc kép cong (`“...”`, `’`) hoặc pha trộn cả dấu cong và dấu thẳng (`"..."`) trong cùng một đoạn văn bản thuần (plain text/code editor) nơi bàn phím người dùng mặc định gõ dấu thẳng (trong khi Gemini và Claude mặc định dùng dấu thẳng).

### 4. Bước 3 — Cơ chế hình thành & Bằng chứng khoa học
- **Cơ chế hình thành**:
  - Như tài liệu Wikipedia đã trích dẫn trực tiếp từ **System Prompt của Claude 3.5 Sonnet (11/2024)** (*cite_note-sonnetprompt-34*): Các chatbot được lập trình ở tầng hệ thống để ưu tiên định dạng Markdown rõ ràng, dùng tiêu đề, danh sách và chữ đậm. Hơn nữa, trong đánh giá RLHF, người chấm điểm thường đọc lướt trong vài giây nên chấm điểm cao hơn cho các câu trả lời có bullet in đậm và bảng biểu bắt mắt (*formatting bias in human preference data*) `[Cấp B]`.
  - Nghiên cứu của **Russell et al. (2025)** chứng minh `Title Case` trong tiêu đề và `Inline-header vertical lists` là những đặc trưng thị giác có tần suất cao đột biến trong văn bản LLM `[Cấp B]`.

### 5. Bước 4 — Phân tích đặc điểm chuyên sâu trong Tiếng Việt
- **Về chính tả tiêu đề (`FMT-01d`)**: Theo Quy định chính tả tiếng Việt (và Nghị định 30/2020/NĐ-CP về công tác văn thư cũng như quy chuẩn xuất bản Việt Nam), tiêu đề mục trong văn bản tiếng Việt chỉ viết hoa chữ cái đầu của âm tiết đầu tiên và các danh từ riêng (Sentence case). Việc viết hoa `Chiến Lược Quản Trị Rủi Ro Tín Dụng Trong Kỷ Nguyên Số` là lỗi giao thoa hình thức từ tiếng Anh.
- **Về chuyển hóa danh sách thành văn xuôi (`FMT-01a`)**: Trong văn phong học thuật, nghị luận và báo chí chuyên sâu tiếng Việt, việc lạm dụng gạch đầu dòng `- **A**: ... - **B**: ...` ở mọi mục làm đứt gãy mạch lập luận (người viết không cần xây dựng quan hệ nhân quả hay chuyển tiếp giữa A và B vì đã có dấu bullet ngăn cách).
- **Về hệ thống dấu câu tiếng Việt (`FMT-01c`)**: Tiếng Việt viết hiện đại sử dụng rất hiệu quả **dấu hai chấm (`:`)** để mở rộng/giải thích trực tiếp (thay cho từ *"Cụ thể là"*), và **dấu chấm phẩy (`;`)** để ngăn cách các vế trong câu ghép dài có nhiều tầng phẩy. Việc AI thời kỳ đầu lạm dụng ` — ` và thời kỳ cuối 2026 chỉ dùng `,` và `.` đều làm nghèo nàn nhịp ngắt câu tiếng Việt.

### 6. Bước 5 – Bước 8 — Ví dụ Đối chiếu & Quy tắc Humanize
- **Ví dụ A (Dương tính rõ ràng — `FMT-01a` + `FMT-01b` + `FMT-01d`)**:
  > ### **Các Yếu Tố Ảnh Hưởng Đến Lãi Suất Ngân Hàng**
  > Lãi suất ngân hàng chịu sự tác động của nhiều **nhân tố vĩ mô** và **nội tại**:
  > - **Chính sách tiền tệ**: Ngân hàng Nhà nước điều chỉnh **lãi suất điều hành** để kiểm soát lạm phát.
  > - **Cung cầu vốn trên thị trường**: Khi nhu cầu vay vốn tăng cao, **lãi suất huy động** và cho vay sẽ tăng theo.
  > - **Mức độ rủi ro tín dụng**: Các khoản vay có **rủi ro cao** thường đi kèm mức lãi suất lớn hơn.
- **Ví dụ C (Hợp lệ — Tài liệu kỹ thuật / Hướng dẫn sử dụng / Tóm tắt điều khoản hợp đồng)**:
  > Trong tài liệu API Documentation, README phần mềm, hoặc phụ lục thông số kỹ thuật, cấu trúc `- **Tên tham số**: Mô tả` và bảng biểu là quy chuẩn tối ưu bắt buộc phải giữ nguyên.
- **Ví dụ D (Cặp Trước / Sau khi Humanize sang văn xuôi phân tích)**:
  - **Sau khi Humanize**:
    > ### **Các yếu tố chi phối mặt bằng lãi suất ngân hàng**
    > Mặt bằng lãi suất thương mại trước hết chịu sự dẫn dắt từ các mức lãi suất điều hành của Ngân hàng Nhà nước nhằm mục tiêu kiểm soát lạm phát. Trên nền định hướng đó, lãi suất thực tế tại từng ngân hàng sẽ biến động theo độ căng thẳng của cung – cầu vốn trên thị trường liên ngân hàng và mức bù rủi ro tín dụng của từng phân khúc khách hàng.
- **Quy tắc ra quyết định khi Humanize**:
  1. **Quy tắc Thể loại (Genre Check)**: Nếu văn bản mục tiêu là *Slide, Ghi chú nhanh, Tài liệu kỹ thuật (Docs/README), Cẩm nang hướng dẫn từng bước* $\rightarrow$ **Giữ nguyên danh sách và bảng biểu**. Nếu văn bản mục tiêu là *Bài báo khoa học, Tiểu luận, Báo cáo phân tích chuyên sâu, Bài viết bách khoa, Bài bình luận báo chí* $\rightarrow$ **Chuyển hóa tối thiểu 70% các danh sách `- **Tiêu đề**: Mô tả` ngắn thành đoạn văn xuôi có liên kết nhân quả – chính phụ**.
  2. **Quy tắc Chính tả Tiêu đề Tiếng Việt**: Tự động chuyển toàn bộ tiêu đề mục kiểu `Title Case` sang `Sentence case` chuẩn tiếng Việt.
  3. **Quy tắc Dấu câu Cân bằng**: Thay thế các dấu gạch ngang dài ` — ` sáo rỗng bằng dấu phẩy, dấu ngoặc đơn hoặc dấu hai chấm; đồng thời chủ động khôi phục dấu hai chấm (`:`) và dấu chấm phẩy (`;`) ở các câu phức phân tích để phá vỡ sự phẳng hóa dấu câu của các mô hình cuối 2026.

---

## HỒ SƠ 26: `FOR-01` — DẤU VẾT KỸ THUẬT, GIAO TIẾP HỘI THOẠI THỪA VÀ NGUỒN TRÍCH DẪN ẢO GIÁC (`WP:COLLABCOMM`, `WP:OAICITE`, `WP:AIFICTREF`)

### 1. Thông tin định danh
- **ID**: `FOR-01`
- **Tên dấu hiệu**: Dấu vết kỹ thuật nội bộ (Internal Markup Bugs), giao tiếp hội thoại của chatbot bị dán nhầm, mẫu điền khuyết (Placeholders) và nguồn trích dẫn ảo giác (*Forensic Artifacts, Meta-Conversational Leakage & Hallucinated Citations*).
- **Nguồn gốc trong danh sách gốc**: Khối II — *Communication intended for the user* (`WP:CERTAINLY`, `WP:COLLABCOMM`, `WP:AIPLACEHOLDER`), *Markup* (`WP:AIMARKDOWN`, `WP:OAICITE`, `WP:STARTSPAN`, `WP:GROKCARD`, DeepSeek `【†】`, Perplexity `attached_file`, `:::writing`), *Citations* (`WP:AIFICTREF`, `utm_source=`), *Comment & Edit summaries* (`WP:AICOMMENT`, `WP:AISUMMARY`), *Historical* (`WP:AICUTOFF`, *Prompt refusal*, *Abrupt cut offs*).

### 2. Bước 1 — Định nghĩa vận hành, Phạm vi & Đơn vị quan sát
- **Cấp độ**: Ngoại ngôn ngữ & Kỹ thuật pháp chứng văn bản (Extrinsic Forensic & Metadata level).
- **Định nghĩa vận hành**: Tập hợp các dấu hiệu **không thuộc về phong cách viết hay tư duy ngôn ngữ**, mà là các phần dư thừa của giao diện hội thoại, lỗi cú pháp xuất dữ liệu của nền tảng LLM (ChatGPT, Gemini, Claude, Grok, DeepSeek, Perplexity) hoặc các tham chiếu thư mục bị bịa đặt (hallucinated references). Trong đó, một số dấu vết (như `oaicite`, `turn0search0`, `【85†L261-269】`, câu mở đầu *"Chắc chắn rồi! Dưới đây là bài viết..."*) là **bằng chứng khẳng định tuyệt đối (unambiguous / deterministic proof – G15)** về sự can thiệp của LLM `[Cấp A/B]`.

### 3. Bước 2 — Phân loại chi tiết 5 nhóm dấu vết kỹ thuật & biểu hiện tiếng Việt
1. **`FOR-01a` — Rò rỉ giao tiếp hội thoại & Lời từ chối/Giới hạn kiến thức (`WP:COLLABCOMM`, `WP:AICUTOFF`, *Prompt Refusal*)**:
   - Câu mở đầu/kết thúc hội thoại bị người dùng copy-paste nguyên xi vào văn bản:
     - Tiếng Anh: *"Certainly! Here is a...", "I hope this helps!", "Let me know if you would like a more detailed breakdown", "As of my last knowledge update...", "As an AI language model..."*.
     - Tiếng Việt: *"**Chắc chắn rồi! Dưới đây là** bài viết/bản phân tích..."*, *"**Hy vọng những thông tin trên hữu ích với bạn!** Hãy cho tôi biết nếu bạn cần chỉnh sửa thêm..."*, *"**Tính đến lần cập nhật kiến thức cuối cùng của tôi**..."*, *"**Là một mô hình ngôn ngữ AI**, tôi không thể..."*.
   - Ghi chú hướng dẫn nộp bài trong thẻ bình luận HTML (`<!-- Xóa phần này trước khi gửi... -->`).
2. **`FOR-01b` — Mẫu điền khuyết (Placeholders) bị bỏ quên (`WP:AIPLACEHOLDER`)**:
   - Các khe trống trong ngoặc vuông hoặc ngoặc đơn chưa được điền: `"[Tên doanh nghiệp/ngân hàng của bạn]"`, `"[Chèn số liệu quý IV tại đây]"`, `"(Thêm đường dẫn website nếu có)"`, ngày truy cập giả `"2025-xx-xx"`.
3. **`FOR-01c` — Rò rỉ mã định dạng & truy xuất nội bộ theo từng hãng AI (`WP:OAICITE`, `WP:STARTSPAN`, `WP:GROKCARD`)**:
   - **OpenAI / ChatGPT**: `:contentReference[oaicite:0]{index=0}`, `oai_citation`, chuỗi Unicode vùng sử dụng riêng (PUA) kèm `citeturn0search0`, `turn0news0`, `turn0image0`, hoặc JSON cuối câu `({"attribution":{"attributableIndex":"0-1"}})`.
   - **Google Gemini**: `[cite: 1]`, `[cite: 3, 12]`, hoặc lỗi thẻ span `[span_1](start_span)...[span_1](end_span)`.
   - **xAI Grok**: Thẻ XML `grok_card`, `grok_render_citation_card_json`.
   - **DeepSeek**: Dấu ngoặc thấu kính kèm ký hiệu dao găm `【85†L261-269】`.
   - **Perplexity AI**: `[attached_file:1]`, `[web:1]`, URL chứa bucket `ppl-ai-file-upload`.
   - **Khối mã chưa phân loại (từ tháng 6/2026)**: `:::writing{variant="document" id="12345"} ... :::`.
   - **Tham số theo dõi nguồn trong URL (`utm_source=`)**: Đường dẫn trích dẫn có đuôi `?utm_source=chatgpt.com`, `?utm_source=openai`, `?utm_source=copilot.com`, hoặc `?referrer=grok.com`. *(Lưu ý quan trọng: Tham số này chứng minh người viết dùng công cụ tìm kiếm của AI để lấy link, nhưng chưa chắc toàn bộ văn bản do AI viết nếu người dùng chỉ dùng AI để tìm nguồn).*
4. **`FOR-01d` — Nguồn trích dẫn ảo giác & Sai lệch kiểm chứng thư mục (`WP:AIFICTREF`)**:
   - **Link chết hàng loạt ngay khi mới tạo**: Nhiều URL trả về lỗi 404 và chưa từng tồn tại trên Internet Archive (Wayback Machine).
   - **DOI và ISBN không hợp lệ hoặc "Râu ông nọ cắm cằm bà kia"**: Mã ISBN sai số kiểm tra (checksum); mã DOI có thật và đúng cú pháp (ví dụ `10.1109/PROC.1974.9547`) nhưng khi bấm vào lại dẫn đến một bài báo hoàn toàn khác không liên quan, hoặc gán cho tác giả đã qua đời trước thời điểm xuất bản 30 năm.
   - **Trích dẫn sách chung chung không có số trang hoặc số trang không chứa nội dung**: Trích dẫn một cuốn giáo trình nổi tiếng (như *Kinh tế học vĩ mô* của Mankiw hay sách của Dorf & Svoboda) để chứng minh một nhận định hẹp nhưng không ghi số trang, hoặc ghi `tr. 12` nhưng trang 12 hoàn toàn không nhắc đến khái niệm đó.
5. **`FOR-01e` — Giọng văn "Tự báo cáo quy trình biên tập" (`WP:AISUMMARY`, `WP:AICOMMENT`)**:
   - Khi người dùng yêu cầu AI viết lời giải trình hoặc tóm tắt chỉnh sửa, AI luôn dùng công thức tự cam kết quy trình: *"Đã chỉnh sửa đoạn văn để đảm bảo tính trung lập, khách quan và rõ ràng trong khi **vẫn giữ nguyên (preserving/retaining)** ý nghĩa gốc và các chi tiết kỹ thuật"*, hoặc giọng văn nhân viên chăm sóc khách hàng (*"Tôi hoàn toàn hiểu mối quan ngại của bạn... Nếu có bất kỳ vấn đề cụ thể nào cần giải quyết, xin vui lòng chỉ rõ..."*).

### 4. Bước 3 – Bước 8 — Quy tắc xử lý trong Công cụ Kiểm tra & Humanization Engine
- **Nguyên tắc tối thượng đối với `FOR-01`**:
  1. **Tự động quét và Cắt bỏ tuyệt đối (Deterministic Regex Sanitization)**: Công cụ phải chạy bộ lọc Regex ở **Giai đoạn P0 (trước mọi bước biên tập ngôn ngữ)** để phát hiện và xóa sạch các mã rò rỉ (`oaicite`, `turn0search`, `[span_...]`, `【...†...】`, `:::writing`, `?utm_source=chatgpt.com`) và các câu giao tiếp hội thoại đầu/cuối bài.
  2. **Cảnh báo Đỏ về Toàn vẹn Học thuật (Academic Integrity Red Flag)**: Khi phát hiện placeholder (`[Điền vào đây]`, `2025-xx-xx`) hoặc trích dẫn thiếu số trang / nghi ngờ DOI ảo giác (`FOR-01d`), công cụ **TUYỆT ĐỐI KHÔNG ĐƯỢC tự chế biến số liệu hay sửa mã DOI cho đẹp**, mà phải xuất cảnh báo bắt buộc tác giả kiểm tra đối chiếu nguồn gốc.
