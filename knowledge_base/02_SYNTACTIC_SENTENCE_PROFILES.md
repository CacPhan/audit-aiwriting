# HỒ SƠ NGHIÊN CỨU CHUYÊN SÂU — NHÓM 2: CÚ PHÁP, CẤU TRÚC CÂU VÀ ĐẶC THÙ BẢN NGỮ TIẾNG VIỆT (`SYN`)
**(Giai đoạn 3, Giai đoạn 4, Đầu ra B & C — Các hồ sơ `SYN-01` đến `SYN-VN-03`)**

---

## HỒ SƠ 7: `SYN-01` — HIỆN TƯỢNG "ĐẲNG CẤU CÚ PHÁP" LIÊN CÂU (*SYNTACTIC ISOMORPHISM*)

### 1. Thông tin định danh
- **ID**: `SYN-01`
- **Tên dấu hiệu**: Đẳng cấu cú pháp liên câu / Nhân bản cây cú pháp (*Inter-sentential Syntactic Isomorphism / Parse-Tree Cloning*).
- **Nguồn gốc trong danh sách gốc**: Khối I — Mục 2 (*Hiện tượng "Đẳng cấu cú pháp" [Syntactic Isomorphism – Khác từ nhưng trùng khuôn câu]*).

### 2. Bước 1 — Định nghĩa vận hành, Phạm vi & Đơn vị quan sát
- **Cấp độ ngôn ngữ**: Cú pháp liên câu (Inter-sentential syntactic level).
- **Đơn vị quan sát**: Chuỗi từ 2 đến 4 câu liền kề trong cùng một đoạn văn hoặc ở vị trí mở đầu các đoạn văn liên tiếp.
- **Định nghĩa vận hành**: Hiện tượng hai hoặc nhiều câu liên tiếp có từ vựng bề mặt hoàn toàn khác nhau (thậm chí không lặp lại bất kỳ danh từ hay động từ nào nhờ cơ chế `LEX-04`), nhưng **cấu trúc cây cú pháp thành tố (Constituency Parse Tree)** và **tỷ lệ độ dài giữa các mệnh đề** lại trùng khớp nhau một cách cơ học. Hai người phân tích độc lập xác định dương tính với `SYN-01` khi:
  1. Có $\ge 2$ câu liên tiếp chia sẻ cùng một khuôn mẫu chuỗi mệnh đề (ví dụ: `[Trạng ngữ mở đầu 6–9 chữ] + , + [Chủ ngữ + Vị ngữ + Tân ngữ 10–15 chữ] + , + [Mệnh đề phụ chỉ hệ quả 8–12 chữ]`), **VÀ**
  2. Việc lặp lại cấu trúc này không nhằm mục đích tu từ điệp cấu trúc (rhetorical parallelism/anaphora) có chủ đích, mà chỉ là sự trình bày các thông tin nối tiếp thông thường.
- **Phân biệt với hiện tượng gần nghĩa**:
  - Khác với **Phép điệp cấu trúc tu từ (Rhetorical Parallelism)**: Trong phép điệp tu từ của con người, người viết cố ý giữ lại một từ khóa/hư từ làm trục đối xứng để tạo cao trào cảm xúc hoặc nhấn mạnh sự tương phản. Ngược lại, trong `SYN-01` của AI, mô hình cố gắng *giấu* sự lặp lại bằng cách thay toàn bộ từ vựng (`Trong bối cảnh...` $\rightarrow$ `Trước những biến động...` $\rightarrow$ `Thông qua việc...`) nhưng lại giữ nguyên khung xương cú pháp.

### 3. Bước 2 — Phân tích các biểu hiện cụ thể (Sub-manifestations)
1. **`SYN-01a` — Khuôn câu 3 nhịp kinh điển của AI tiếng Việt (*The Canonical Tripartite AI Frame*)**:
   - Công thức: **`[Trạng ngữ bối cảnh/phương tiện], [Mệnh đề chính S-V-O], [Mệnh đề phụ chỉ kết quả/ý nghĩa].`**
   - Mở đầu nhịp 1 thường xoay vòng giữa: *"Trong bối cảnh X,"*, *"Trước những thách thức của Y,"*, *"Thông qua việc Z,"*, *"Nhờ vào sự phát triển của W,"*, *"Với mục tiêu K,"*.
   - Nhịp 3 thường xoay vòng giữa: *"..., qua đó nâng cao..."*, *"..., từ đó đảm bảo..."*, *"..., góp phần tối ưu hóa..."*, *"..., tạo tiền đề cho..."*.
2. **`SYN-01b` — Đẳng cấu câu mở đoạn xuyên suốt bài viết (*Paragraph-Initial Isomorphism*)**:
   - Mọi đoạn văn trong bài đều bắt đầu bằng một câu có cấu trúc giống hệt nhau: Đoạn 1 bắt đầu bằng *"Về mặt kinh tế, [S] + [V]..."*, Đoạn 2 bắt đầu bằng *"Trên phương diện xã hội, [S] + [V]..."*, Đoạn 3 bắt đầu bằng *"Xét từ góc độ môi trường, [S] + [V]..."*.
3. **`SYN-01c` — Đẳng cấu câu đối xứng nhị phân (*Binary Contrast Isomorphism*)**:
   - Lặp lại liên tiếp khuôn: *"Trong khi [A] tập trung vào [X], thì [B] lại hướng tới [Y]."* ở nhiều cặp câu liền kề.

### 4. Bước 3 — Cơ chế hình thành & Bằng chứng khoa học
- **Cơ chế hình thành**:
  1. **Sự kết hợp giữa Tự hồi quy theo khuôn (Structural Priming / In-Context Template Locking) và Phạt lặp từ vựng (Lexical Repetition Penalty)**: Khi LLM vừa sinh ra Câu 1 với một cấu trúc cú pháp có xác suất cao (high syntactic log-probability), cơ chế *self-attention* trong ngữ cảnh cục bộ bị "mồi" (syntactic priming) bởi chính cấu trúc cây cú pháp của Câu 1. Tuy nhiên, vì bộ giải mã phạt việc lặp lại các token từ vựng của Câu 1, mô hình giải bài toán tối ưu bằng cách **giữ nguyên khung cú pháp xác suất cao của Câu 1 nhưng thay thế các khe từ vựng (lexical slots) bằng các từ đồng nghĩa/tương đương chức năng** `[Cấp B/C]`.
  2. **Ảnh hưởng của dữ liệu tóm tắt báo chí và báo cáo tổng hợp**: Khuôn câu 3 nhịp (*Bối cảnh $\rightarrow$ Hành động $\rightarrow$ Ý nghĩa*) là khuôn câu nén thông tin an toàn nhất trong các bản tóm tắt (abstracts/executive summaries) mà mô hình được huấn luyện `[Cấp C]`.
- **Bằng chứng ủng hộ**:
  - **Reinhart et al. (2024/2025, PNAS)**: Phân tích sự biến thiên cấu trúc ngữ pháp và tu từ giữa LLM và con người, chứng minh rằng LLM có độ đa dạng cấu trúc cú pháp nội văn bản (intra-text syntactic variation) thấp hơn đáng kể so với người viết chuyên nghiệp và có xu hướng khóa chặt vào một số khuôn mệnh đề trạng ngữ – phân từ cố định `[Cấp B]`.
  - **Boghrati et al. / Nghiên cứu về Syntactic Alignment trong LLM (2023–2025)**: Chứng minh hiện tượng *structural persistence* (bám dính cấu trúc cú pháp) giữa các câu kế tiếp trong văn bản sinh tự hồi quy `[Cấp B]`.

### 5. Bước 4 — Phân tích đặc điểm chuyên sâu trong Tiếng Việt
- Trong văn xuôi nghị luận và khoa học tiếng Việt tự nhiên (Diệp Quang Ban, 2005; Trần Ngọc Thêm, 1999), cấu trúc câu giữa các câu liên tiếp biến đổi rất linh hoạt nhờ **sự chuyển hóa vai trò Đề – Thuyết**:
  - Nếu Câu 1 đã thiết lập khung bối cảnh (*"Trong bối cảnh cạnh tranh gay gắt hiện nay..."*), thì Câu 2 và Câu 3 của người Việt sẽ **kế thừa luôn khung bối cảnh đó** (không bao giờ mở lại một trạng ngữ bối cảnh 8 chữ mới ở đầu Câu 2 và Câu 3), mà đi thẳng vào phân tích chi tiết, nêu số liệu hoặc đảo phần Thuyết của Câu 1 thành phần Đề của Câu 2 (*liên kết móc xích*) `[Cấp C]`.
- Việc AI mở đầu 3 câu liên tiếp bằng 3 cụm trạng ngữ dài (*Trong bối cảnh... / Trước những biến động... / Thông qua việc...*) kèm 3 mệnh đề đuôi (*qua đó... / từ đó... / góp phần...*) tạo ra cảm giác mỗi câu là một khẩu hiệu độc lập, phá hủy tính liên kết dòng chảy của tiếng Việt.

### 6. Bước 5 — Mức độ đặc trưng và Khả năng chẩn đoán
- **Khả năng phân biệt**: **Rất cao (Một trong những dấu hiệu chẩn đoán mạnh nhất ở cấp độ đoạn văn)**. Người viết thật hiếm khi viết 3 câu liên tiếp có cấu trúc 3 nhịp đối xứng hoàn hảo về độ dài các vế nhưng lại thay đổi hoàn toàn từ nối mở đầu như vậy.

### 7. Bước 6 — Hệ thống Ví dụ Đối chiếu & Cặp Chỉnh sửa Tối thiểu
- **Ví dụ A (Dương tính rõ ràng — Trích xuất và phân tích từ ngữ liệu gốc của người dùng)**:
  > *(Câu 1)* **Trong bối cảnh cạnh tranh gay gắt hiện nay**, các ngân hàng thương mại đang đẩy mạnh quá trình số hóa dịch vụ, **qua đó nâng cao trải nghiệm cho khách hàng cá nhân.**
  > *(Câu 2)* **Trước những biến động khó lường của vĩ mô**, nhiều tổ chức tín dụng cũng chủ động thắt chặt khẩu vị rủi ro, **từ đó đảm bảo sự an toàn cho toàn bộ hệ thống.**
  > *(Câu 3)* **Thông qua việc ứng dụng trí tuệ nhân tạo**, quy trình thẩm định tín dụng đã được rút ngắn đáng kể, **góp phần tối ưu hóa chi phí vận hành của doanh nghiệp.**
  - *Phân tích cây cú pháp*: Cả 3 câu đều có cấu trúc: `[PP/AdvP (7–8 âm tiết)], [NP_subj + VP + NP_obj (12–14 âm tiết)], [Conj_result + VP_eval (8–10 âm tiết)]`.
- **Ví dụ B (Dương tính tinh vi — Đẳng cấu 2 nhịp không có trạng ngữ đầu câu)**:
  > *"Việc nâng lãi suất điều hành đã làm tăng chi phí huy động vốn, buộc các ngân hàng phải thu hẹp gói vay ưu đãi. Sự sụt giảm của thị trường trái phiếu cũng làm hạn chế kênh dẫn vốn trung hạn, khiến các doanh nghiệp bất động sản gặp khó khăn về dòng tiền. Quá trình siết chặt tiêu chuẩn tín dụng càng làm chậm tốc độ giải ngân, đẩy nhiều dự án vào tình trạng đình trệ."*
  - *Giải thích*: 3 câu liên tiếp đều theo khuôn: `[Danh ngữ Sự/Việc/Quá trình + V_gây_ra + O], [buộc/khiến/đẩy + O + vào trạng thái X]`.
- **Ví dụ C (Bề ngoài tương tự nhưng hợp lệ — Điệp cấu trúc tu từ có chủ đích)**:
  > *"Nếu chần chừ số hóa, ngân hàng sẽ mất khách hàng trẻ. Nếu buông lỏng thẩm định, ngân hàng sẽ gánh nợ xấu. Nhưng nếu siết tín dụng quá mức, ngân hàng lại tự cắt đi nguồn thu cốt lõi."*
  - *Giải thích*: Đây là phép điệp cấu trúc điều kiện (*"Nếu..., ngân hàng sẽ..."*) có chủ đích nghệ thuật để dồn nén một thế tiến thoái lưỡng nan (trilemma), các câu ngắn gọn (11–14 chữ) và xoay quanh cùng một chủ ngữ.
- **Ví dụ D / Cặp Trước – Sau khi Humanize (Phá vỡ đẳng cấu từ Ví dụ A)**:
  - **Sau khi Humanize**:
    > *"Cạnh tranh bán lẻ ngày càng khốc liệt buộc các ngân hàng thương mại phải tăng tốc số hóa. Nhờ đưa trí tuệ nhân tạo vào khâu thẩm định, thời gian duyệt hồ sơ đã rút ngắn đáng kể, vừa giữ chân được khách hàng cá nhân vừa cắt giảm chi phí vận hành. Tuy vậy, trước biến động vĩ mô khó lường, nhiều nhà băng vẫn chủ động siết lại khẩu vị rủi ro để giữ an toàn thanh khoản."*
  - *Giải thích vì sao bản sửa tốt hơn*:
    1. Câu 1 (16 chữ): Câu đơn trực diện, biến trạng ngữ *"Trong bối cảnh cạnh tranh..."* thành chủ ngữ tác động trực tiếp (*"Cạnh tranh bán lẻ... buộc..."*).
    2. Câu 2 (37 chữ): Gộp nội dung công nghệ AI (Câu 3 cũ) vào ngay sau ý số hóa (Câu 1 cũ) vì chúng có quan hệ nhân quả thực chất (AI chính là công cụ của số hóa!), đồng thời nối hai lợiích (*khách hàng cá nhân* và *chi phí vận hành*) bằng kết cấu *"vừa... vừa..."*.
    3. Câu 3 (24 chữ): Đưa ý thắt chặt khẩu vị rủi ro (Câu 2 cũ) xuống cuối làm đối trọng hợp lý. Toàn bộ 3 khuôn câu đẳng cấu đã bị triệt tiêu, mạch logic chặt hơn hẳn bản gốc.

### 8. Bước 7 & Bước 8 — Hệ quả, Quy tắc Humanize & Tiêu chí Kiểm thử
- **Hệ quả**: Gây hiệu ứng "thôi miên cơ học" (syntactic monotony), làm người đọc trượt qua văn bản mà không đọng lại trọng tâm; tách rời các câu có quan hệ nhân quả thực chất thành các mệnh đề song song giả tạo.
- **Quy tắc ra quyết định khi Humanize (Syntactic De-cloning Algorithm)**:
  1. **Phát hiện**: Gắn cờ khi có $\ge 2$ câu liên tiếp trùng chuỗi thẻ thành tố chính (`[AdvP/PP, Clause_Main, Clause_Result]`).
  2. **Kiểm tra quan hệ ngữ nghĩa thực giữa các câu**:
     - Nếu Câu $i$ và Câu $i+1$ thực chất là *Nguyên nhân – Cụ thể hóa* (như Số hóa $\rightarrow$ Ứng dụng AI thẩm định): **Gộp hoặc móc xích trực tiếp** thay vì để tách rời thành 2 câu song song.
     - Biến đổi vị trí thành phần câu: Câu 1 mở bằng Chủ ngữ/Đề ngữ trực diện $\rightarrow$ Câu 2 mở bằng المệnh đề phụ hoặc Động từ tỉnh lược chủ ngữ $\rightarrow$ Câu 3 dùng cấu trúc Đề–Thuyết hoặc câu ngắn chốt ý.
- **Tiêu chí kiểm thử**: Điểm tương đồng cây cú pháp (Tree Edit Distance / POS n-gram cosine similarity) giữa 3 câu liên tiếp bất kỳ phải $< 0.65$; không được có 2 câu liên tiếp cùng mở đầu bằng giới từ bối cảnh và cùng kết thúc bằng mệnh đề *"qua đó/từ đó/góp phần"*.

---

## HỒ SƠ 8: `SYN-02` — MỆNH ĐỀ PHỤ ĐÁNH GIÁ / HỆ QUẢ GIẢ TẠO CUỐI CÂU (`WP:SUPERFICIAL`)

### 1. Thông tin định danh
- **ID**: `SYN-02`
- **Tên dấu hiệu**: Mệnh đề phụ phân tích hời hợt / đánh giá hệ quả gắn đuôi câu (*Trailing Superficial Analysis / Participial Resultative Clause*).
- **Nguồn gốc trong danh sách gốc**: Khối II — `WP:SUPERFICIAL` (*Superficial analyses: highlighting, underscoring, ensuring, fostering, contributing to...*) & Khối I — Mục 2 (vế thứ 3 của khuôn câu AI tiếng Việt: *"..., qua đó nâng cao...", "..., từ đó đảm bảo...", "..., góp phần..."*).

### 2. Bước 1 — Định nghĩa vận hành, Phạm vi & Đơn vị quan sát
- **Cấp độ ngôn ngữ**: Cú pháp nội câu – Ngữ nghĩa mệnh đề phụ (Intra-sentential subordinate clause level).
- **Đơn vị quan sát**: Mệnh đề phụ đứng cuối câu (ngăn cách với mệnh đề chính bằng dấu phẩy).
- **Định nghĩa vận hành**: Hiện tượng gắn vào cuối một câu trần thuật dữ kiện một mệnh đề phụ mở đầu bằng từ nối hệ quả/đánh giá (tiếng Anh dùng phân từ hiện tại `-ing`: *highlighting, underscoring, fostering, ensuring, contributing to*; tiếng Việt dùng: **", qua đó..."**, **", từ đó..."**, **", góp phần..."**, **", điều này cho thấy / khẳng định / phản ánh..."**, **", mở ra..."**, **", tạo tiền đề cho..."**) nhằm đưa ra một nhận xét chung chung, hiển nhiên hoặc phóng đại về ý nghĩa/tác động của dữ kiện đứng trước mà không có bằng chứng nhân quả cụ thể.

### 3. Bước 2 — Phân tích các biểu hiện cụ thể
1. **`SYN-02a` — Đuôi hệ quả tất định giả tạo (*Pseudo-Causal Trailing Clause*)**:
   - *"..., qua đó đảm bảo sự phát triển bền vững"*, *"..., từ đó nâng cao toàn diện năng lực cạnh tranh"*, *"..., giúp tối ưu hóa hiệu quả hoạt động"*. (Thực tế hành động ở mệnh đề chính mới chỉ là bước thử nghiệm hoặc điều kiện cần, chưa hề dẫn đến kết quả vĩ mô ở đuôi câu).
2. **`SYN-02b` — Đuôi bình luận ý nghĩa/biểu trưng (*Evaluative/Symbolic Trailing Clause*)**:
   - *"..., điều này phản ánh xu hướng tất yếu của thời đại"*, *"..., khẳng định tầm nhìn chiến lược của tổ chức"*, *"..., làm nổi bật vai trò quan trọng của..."* (Dịch trực tiếp từ `..., reflecting the broader trend...`, `..., underscoring the strategic vision...`).

### 4. Bước 3 — Cơ chế hình thành & Bằng chứng khoa học
- **Cơ chế hình thành**:
  1. **Thói quen "Giải thích ý nghĩa" từ Instruction Tuning**: Khi người dùng hoặc tập huấn luyện RLHF yêu cầu mô hình "không chỉ liệt kê sự kiện mà phải phân tích ý nghĩa", mô hình hình thành thói quen gắn kèm một mệnh đề bình luận ngắn ngay ở cuối mỗi câu trần thuật để chứng tỏ câu văn "có phân tích" `[Cấp B]`.
  2. **Cấu trúc ngữ pháp tiếng Anh thuận lợi cho việc nối đuôi tự hồi quy**: Trong quá trình sinh token từ trái sang phải, sau khi đã hoàn thành mệnh đề chính `S + V + O`, việc thêm dấu phẩy `,` và một `V-ing` (*highlighting...*, *fostering...*) là cách dễ nhất về mặt cú pháp để kéo dài câu mà không phải mở câu mới `[Cấp B]`.
- **Bằng chứng ủng hộ**:
  - **Reinhart et al. (2024/2025, PNAS)** (*cite_note-Reinhart-16*): Chỉ ra định lượng rằng các mô hình LLM (đặc biệt là họ GPT-4 và GPT-4o) sử dụng mệnh đề phân từ hiện tại (`present participial clauses`) ở cuối câu với tần suất cao gấp nhiều lần văn viết của con người ở mọi thể loại khảo sát `[Cấp B]`.

### 5. Bước 4 — Phân tích đặc điểm chuyên sâu trong Tiếng Việt
- Tiếng Việt không có hình thái phân từ `-ing`. Khi chuyển dịch thói quen `Clause, V-ing...` của tiếng Anh sang tiếng Việt, các mô hình ngôn ngữ (và dữ liệu dịch thuật Anh–Việt) dùng 4 cấu trúc cố định để thay thế cho dấu phẩy + `V-ing`:
  1. **`, qua đó + [Động từ Hán-Việt]`** (*thereby V-ing / enhancing / ensuring*)
  2. **`, từ đó + [Động từ Hán-Việt]`** (*thus fostering / enabling*)
  3. **`, góp phần + [Động từ Hán-Việt]`** (*contributing to...*)
  4. **`, điều này nhấn mạnh / phản ánh / cho thấy + [Danh ngữ]`** (*highlighting / underscoring / reflecting...*)
- Trong tiếng Việt tự nhiên, nếu kết quả là mục đích hoặc hệ quả trực tiếp, người Việt nối thẳng bằng động từ chuỗi hoặc từ chỉ mục đích ngắn gọn (*"để..."*, *"giúp..."*, *"làm..."*); nếu kết quả là một luận điểm quan trọng cần chứng minh, người Việt sẽ tách thành câu riêng để phân tích cơ chế chứ không gắn một cái đuôi sáo rỗng 8 chữ vào cuối mọi câu.

### 6. Bước 5 — Mức độ đặc trưng và Khả năng chẩn đoán
- **Khả năng phân biệt**: Rất cao khi tần suất các đuôi câu `", qua đó..."`, `", từ đó..."`, `", góp phần..."`, `", điều này phản ánh..."` xuất hiện **$\ge 2$ lần trong một đoạn văn** hoặc lặp lại ở hầu hết các đoạn trong bài.

### 7. Bước 6 — Hệ thống Ví dụ Đối chiếu & Cặp Chỉnh sửa Tối thiểu
- **Ví dụ A (Dương tính rõ ràng)**:
  > *"Năm 2024, công ty đã ra mắt ứng dụng đặt hàng trên điện thoại, **qua đó khẳng định vị thế tiên phong trong kỷ nguyên số và góp phần định hình lại bức tranh toàn cảnh của ngành bán lẻ**."*
  - *Giải thích*: Mệnh đề chính là một dữ kiện rất bình thường (ra mắt app đặt hàng), nhưng đuôi câu `SYN-02` thổi phồng thành một kết luận vĩ mô không có căn cứ.
- **Ví dụ B (Dương tính tinh vi)**:
  > *"Ngân hàng đã điều chỉnh giảm 0,5% lãi suất cho vay mua nhà, **từ đó tạo điều kiện thuận lợi cho người dân tiếp cận nguồn vốn và thúc đẩy thị trường bất động sản phục hồi bền vững**."*
  - *Giải thích*: Việc giảm 0,5% lãi suất mới là động thái chính sách, chưa có dữ liệu chứng minh nó đã làm thị trường bất động sản "phục hồi bền vững".
- **Ví dụ C (Bề ngoài tương tự nhưng hợp lệ — Nhân quả định lượng thực chất)**:
  > *"Nhà máy đã thay thế hệ thống lò đốt than bằng lò điện cảm ứng vào quý II/2025, **qua đó cắt giảm được 14.200 tấn khí thải $\text{CO}_2$ trong 6 tháng cuối năm**."*
  - *Giải thích*: Ở đây *"qua đó cắt giảm được 14.200 tấn..."* là một **dữ kiện đo lường thực nghiệm cụ thể**, không phải nhận định đánh giá sáo rỗng.
- **Ví dụ D (Văn phong con người tự nhiên)**:
  > *"Tháng 6/2025, ngân hàng hạ 0,5% lãi suất vay mua nhà nhằm kích cầu tín dụng cá nhân, nhưng lượng hồ sơ giải ngân thực tế trong quý III vẫn tăng chậm do giá nhà neo cao."*
- **Ví dụ E (Trường hợp ngoại lệ cần giữ nguyên)**:
  > Khi đuôi câu dẫn tới một hệ quả kỹ thuật/pháp lý xác định là mắt xích bắt buộc cho câu tiếp theo (chain-linking).

### 8. Bước 7 & Bước 8 — Hệ quả, Quy tắc Humanize & Tiêu chí Kiểm thử
- **Hệ quả**: Tạo ra **lỗi tổng hợp vô căn cứ (`WP:SYNTH`)** và ngụy biện nhân quả (coi dự định/kỳ vọng như kết quả đã đạt được); làm câu văn dài dòng và rập khuôn.
- **Quy tắc ra quyết định khi Humanize (The Tail-Pruning Test)**:
  1. Khi gặp mệnh đề đuôi bắt đầu bằng `", qua đó..."`, `", từ đó..."`, `", góp phần..."`, `", điều này phản ánh/khẳng định..."`:
  2. **Kiểm tra dữ kiện (Information Test)**: Mệnh đề đuôi có chứa **con số mới, tên thực thể mới, hoặc cơ chế kỹ thuật mới** không?
     - `IF KHÔNG` (chỉ chứa từ vựng đánh giá như *nâng cao hiệu quả, phát triển bền vững, khẳng định vị thế, tối ưu hóa*): **Cắt bỏ hoàn toàn mệnh đề đuôi** (chấm câu ngay sau mệnh đề chính).
     - `IF CÓ` nhưng chỉ là *mục đích dự kiến* của chủ thể (chưa phải kết quả đã xảy ra): Đổi từ *"qua đó / từ đó [đạt được Y]"* (hệ quả thực tế) thành **"nhằm / để [hướng tới Y]"** (mục đích) để bảo toàn mức độ chắc chắn (epistemic accuracy).

---

## HỒ SƠ 9: `SYN-03` — CẤU TRÚC SÓNG ĐÔI PHỦ ĐỊNH (*NEGATIVE PARALLELISMS*) (`WP:AIPARALLEL`)

### 1. Thông tin định danh
- **ID**: `SYN-03`
- **Tên dấu hiệu**: Lạm dụng cấu trúc sóng đôi phủ định – khẳng định (*Overuse of Negative Parallelisms*).
- **Nguồn gốc trong danh sách gốc**: Khối II — `WP:AIPARALLEL` (*Not just X, but also Y*; *It's not X, it's Y*; *Y rather than X*) & Khối I — Bảng đối chiếu.

### 2. Bước 1 — Định nghĩa vận hành, Phạm vi & Đơn vị quan sát
- **Cấp độ ngôn ngữ**: Cú pháp – Tu từ mệnh đề (Syntactic-Rhetorical construction).
- **Đơn vị quan sát**: Câu đơn hoặc cặp câu liên tiếp sử dụng phép đối lập phủ định.
- **Định nghĩa vận hành**: Hiện tượng văn bản liên tục diễn đạt một nhận định thông qua việc **dựng lên một vế phủ định giả định $X$ rồi mới khẳng định $Y$** theo 3 mẫu hình cố định:
  1. *"Không chỉ [X], mà còn [Y]"* (`Not only/just X, but also Y`)
  2. *"Đó không phải là [X], mà là [Y]"* / *"Không có [X], không có [Y], chỉ có [Z]"* (`It's not X, it's Y`)
  3. *"[Y] thay vì [X]"* / *"Thay vì chỉ đơn thuần là [X], [S] đã..."* (`Y rather than X` / `Rather than simply X, S...`).
- **Phân biệt với hiện tượng gần nghĩa**: Một văn bản con người sử dụng cấu trúc *"Không phải X, mà là Y"* 1 lần ở câu luận điểm cốt lõi (như câu kết trong Bảng đối chiếu của người dùng: *"Bài toán lúc này không còn là mở rộng bằng mọi giá, mà là lọc lại chất lượng dịch vụ"*) là một thủ pháp tu từ sắc bén. Nó chỉ trở thành dấu hiệu `SYN-03` của AI khi: (a) xuất hiện dày đặc ($\ge 2-3$ lần trong một bài ngắn), hoặc (b) vế phủ định $X$ là một **bù nhìn rơm (strawman)** mà không ai thực sự nghĩ như vậy.

### 3. Bước 2 — Phân tích các biểu hiện cụ thể
1. **`SYN-03a` — Mẫu cộng gộp khuôn sáo: *"Không chỉ... mà còn..."* (`Not only... but also...`)**:
   - Dùng để nối hai thuộc tính hoàn toàn bình thường mà chỉ cần từ *"và"*: *"Giải pháp này không chỉ giúp tiết kiệm thời gian mà còn giảm chi phí"* (lặp lại ở mọi đoạn văn).
2. **`SYN-03b` — Mẫu bác bỏ kịch tính giả tạo: *"Đây không đơn thuần là X, mà là Y"* (`It's not just X — it's Y`)**:
   - Phong cách copywriting/diễn thuyết TED Talk của LLM: *"Chuyển đổi số không phải là câu chuyện của công nghệ, đó là cuộc cách mạng về tư duy."*
3. **`SYN-03c` — Mẫu đảo ngược thế hệ mới (2025–2026): *"[Y] thay vì [X]"* / *"Được xem như [Y] hơn là [X]"* (`Y rather than X`)**:
   - Cực kỳ phổ biến trong văn bản GPT-5/GPT-6, Claude 3.5/4 và Grok: *"Chiến lược này ưu tiên củng cố quyền lực thực nghiệm thay vì sự thuần khiết về ý thức hệ"* (`prioritizing empirical consolidation... rather than ideological purity`).

### 4. Bước 3 — Cơ chế hình thành & Bằng chứng khoa học
- **Cơ chế hình thành**:
  1. **Ảo giác về chiều sâu phản biện (Simulated Critical Nuance)**: Khi được huấn luyện bằng RLHF để viết "sâu sắc, có tư duy phân tích", LLM học được rằng cấu trúc phủ định một nhận thức bề mặt ($X$) để đưa ra nhận thức bản chất ($Y$) luôn được người gán nhãn chấm điểm cao hơn một câu khẳng định đơn thuần `[Cấp B]`.
  2. **Rào đón nhận thức luận (Epistemic Hedging via Contrast)**: Ở các mô hình 2025–2026 (`WP:AIDISCLAIMER`), cấu trúc *"nên được hiểu là Y thay vì X"* giúp mô hình tránh phải đưa ra khẳng định tuyệt đối `[Cấp B]`.
- **Bằng chứng ủng hộ**:
  - **Russell et al. (2025)**, **Kriss (2024/2025)**, **Merrill (2024)** và **The Economist Study (July 2026)** (*cite_note-economistJul2026-26*): Đều xác nhận các cấu trúc `not just X, it's Y`, `not only... but also...`, và `rather than` là một trong những dấu vân tay cú pháp đặc trưng nhất của LLM qua các thế hệ từ 2023 đến 2026 `[Cấp B]`.

### 5. Bước 4 — Phân tích đặc điểm chuyên sâu trong Tiếng Việt
- Trong văn AI tiếng Việt, `SYN-03` xuất hiện với tần suất dày đặc qua các khuôn câu dịch can:
  - *"Không chỉ dừng lại ở việc [X], [Chủ ngữ] còn [Y]..."*
  - *"Thay vì chỉ đơn thuần là [X], [Chủ ngữ] mang đến [Y]..."*
  - *"[X] không phải là đích đến cuối cùng, mà là bước khởi đầu cho [Y]."*
- Trong tiếng Việt tự nhiên, nếu hai vế cùng chiều, người bản ngữ ưu tiên các cặp phụ từ ngắn gọn nội câu như **"vừa... vừa..."**, **"cả... lẫn..."**, hoặc nối trực tiếp bằng dấu phẩy và từ **"đồng thời"**; còn cấu trúc *"không những / không chỉ... mà còn..."* chỉ dùng khi vế sau thực sự vượt lên một cấp độ bất ngờ so với vế trước (Diệp Quang Ban, 2005) `[Cấp C]`.

### 6. Bước 5 — Mức độ đặc trưng và Khả năng chẩn đoán
- **Khả năng phân biệt**: Cao khi tần suất $> 1$ lần trên 250–300 chữ, hoặc khi vế bị phủ định ($X$) là một giả định ngớ ngẩn/hiển nhiên (*"Thay vì chỉ đơn thuần là một tòa nhà bằng gạch đá, bảo tàng này còn là nơi lưu giữ ký ức..."* — không ai nghĩ bảo tàng chỉ là đống gạch đá!).

### 7. Bước 6 — Hệ thống Ví dụ Đối chiếu & Cặp Chỉnh sửa Tối thiểu
- **Ví dụ A (Dương tính rõ ràng — Phủ định bù nhìn rơm + Lặp khuôn)**:
  > *"Bộ phim Na Tra **không chỉ đơn thuần là** việc kể lại một truyền thuyết cổ điển, **mà còn** điều chỉnh câu chuyện theo bối cảnh đương đại. Sức hút của phim **không chỉ đến từ** kỹ xảo hình ảnh, **mà còn từ** khả năng chạm đến cảm xúc khán giả. Đây **không phải là** một tác phẩm giải trí thông thường, **mà là** một biểu tượng thần thoại hiện đại."* (3 câu liên tiếp dùng 3 biến thể `SYN-03`).
- **Ví dụ B (Dương tính tinh vi — Mẫu `Y thay vì X` năm 2026)**:
  > *"Chính sách mới tập trung vào việc kiểm soát rủi ro thanh khoản ngắn hạn **thay vì** theo đuổi mục tiêu tăng trưởng tín dụng thuần túy bằng mọi giá."*
- **Ví dụ C (Hợp lệ & Sắc bén — Dùng đúng 1 lần để chốt luận điểm thực chất)**:
  > *"Bài toán của ngành ngân hàng lúc này **không còn là** mở rộng quy mô bằng mọi giá, **mà là** lọc lại chất lượng từng khoản vay."* (Trích từ cột Văn phong Con người trong Bảng đối chiếu của người dùng — hợp lệ vì trước đó thực sự có giai đoạn ngân hàng chạy theo mở rộng quy mô, nên vế phủ định có cơ sở lịch sử thực tế).
- **Ví dụ D (Cặp Trước / Sau khi Humanize Ví dụ A)**:
  - **Sau khi Humanize**:
    > *"Bộ phim Na Tra làm mới truyền thuyết cổ điển bằng cách lồng ghép những trăn trở của xã hội Trung Quốc đương đại. Ngoài kỹ xảo hình ảnh bắt mắt, bộ phim thu hút khán giả nhờ xây dựng được một hình tượng thần thoại gần gũi với người xem hôm nay."*

### 8. Bước 7 & Bước 8 — Hệ quả, Quy tắc Humanize & Tiêu chí Kiểm thử
- **Hệ quả**: Lạm dụng `SYN-03` tạo ra giọng văn lên gân, thuyết giáo giả tạo (mock-profound tone) và làm người đọc bội thực vì cảm giác câu nào cũng đang cố "lật ngược vấn đề".
- **Quy tắc Humanize**:
  1. **Giới hạn tần suất (Quota Rule)**: Tối đa **01 cấu trúc đối lập phủ định (`Không phải X mà là Y`) trên mỗi 500 chữ**, và chỉ giữ lại ở câu luận điểm đắt giá nhất (nơi $X$ là một quan niệm sai lầm có thật trong thực tế).
  2. **Kiểm tra Strawman (Bù nhìn rơm)**: Với mọi câu *"Thay vì chỉ đơn thuần là X, S là Y"* hoặc *"Không chỉ X mà còn Y"*: Nếu $X$ là điều hiển nhiên hoặc không ai tranh cãi $\rightarrow$ **Chuyển thành câu khẳng định trực tiếp hoặc dùng kết cấu `"vừa X vừa Y"` / `"Bên cạnh X, S còn Y"`**.

---

## HỒ SƠ 10: `SYN-04` — QUY TẮC SỐ 3 CƠ HỌC (*MECHANICAL RULE OF THREE*) (`WP:RO3`)

### 1. Thông tin định danh
- **ID**: `SYN-04`
- **Tên dấu hiệu**: Lạm dụng quy tắc liệt kê bộ ba cơ học (*Overuse of the Rule of Three / Triadic Listing*).
- **Nguồn gốc trong danh sách gốc**: Khối II — `WP:RO3` (*Rule of three: `adj, adj, and adj` hoặc `phrase, phrase, and phrase`*).

### 2. Bước 1 — Định nghĩa vận hành, Phạm vi & Đơn vị quan sát
- **Cấp độ ngôn ngữ**: Cú pháp cụm từ đồng chức năng (Coordinate phrase level).
- **Đơn vị quan sát**: Các kết cấu đẳng lập liệt kê (`A, B và C`) trong câu.
- **Định nghĩa vận hành**: Hiện tượng văn bản liên tục đóng gói các tính từ, động từ hoặc cụm danh từ thành **bộ 3 phần tử (`A, B và C`)** ở hầu hết các câu trong đoạn, đặc biệt khi phần tử thứ 2 và thứ 3 gần như đồng nghĩa với phần tử thứ 1 (chỉ được thêm vào để lấp đầy nhịp 3) hoặc ghép đôi 2 bộ 3 trong cùng một câu (`...bảo tồn A, B và C trong khi định hình lại chúng qua X, Y và Z`).

### 3. Bước 2 — Phân tích các biểu hiện cụ thể
1. **`SYN-04a` — Bộ ba tính từ/động từ đồng nghĩa lấp chỗ trống (*Redundant Triadic Adjectives/Verbs*)**:
   - *"Giải pháp này mang tính **đồng bộ, toàn diện và hiệu quả**"*, *"Quá trình này đòi hỏi sự **kiên trì, bền bỉ và nỗ lực không ngừng**"*.
2. **`SYN-04b` — Bộ ba danh ngữ khái quát hóa giả tạo (*Pseudo-Comprehensive Noun Triads*)**:
   - Luôn liệt kê đúng 3 đối tượng để tạo cảm giác bao quát: *"tác động đến **cá nhân, doanh nghiệp và toàn xã hội**"*, *"kết hợp giữa **con người, quy trình và công nghệ**"*.
3. **`SYN-04c` — Bộ ba kép đối xứng trong một câu (*Double Triad in a Single Sentence*)**:
   - Ví dụ từ Wikipedia: *"Bộ phim bảo tồn các yếu tố cốt lõi như **[1] hình tượng thần thoại, [2] vũ khí phép thuật và [3] tinh thần phản kháng** trong khi tái định hình chúng thông qua **[1] các giá trị đương đại, [2] thẩm mỹ hiện đại và [3] công nghệ hoạt hình kỹ thuật số**."*

### 4. Bước 3 — Cơ chế hình thành & Bằng chứng khoa học
- **Cơ chế hình thành**: Quy tắc số 3 (*Tricolon / Rule of Three*) là một mẫu hình tu từ rất phổ biến trong văn viết tiếng Anh (bài luận mẫu, diễn văn, copywriting). Trong quá trình huấn luyện, LLM học được rằng một danh sách liệt kê nếu dừng ở 2 phần tử thì nghe "chưa trọn ý", còn kéo lên 4–5 phần tử thì "dài dòng", nên phân phối xác suất của dấu kết thúc danh sách (`", and [Item 3]."` / `"và [Phần tử 3]."`) đạt đỉnh cực đại ở phần tử thứ 3 `[Cấp B]` (Russell et al., 2025; Kriss, 2025; The Economist, 2026).

### 5. Bước 4 — Phân tích đặc điểm trong Tiếng Việt
- Tiếng Việt truyền thống vốn ưa **nhịp đôi / kết cấu tứ tự (4 âm tiết, 2 vế đối xứng)** hơn là nhịp 3 của phương Tây (ví dụ: *đồng bộ và hiệu quả*, *nhanh chóng và chính xác*, *vốn và thanh khoản*) `[Cấp C]`.
- Khi văn AI tiếng Việt liên tục nhồi nhịp 3 (*"minh bạch, công bằng và hiệu quả"*, *"nhanh chóng, chính xác và toàn diện"*, *"ngắn hạn, trung hạn và dài hạn"*), đặc biệt khi lặp lại nhiều bộ 3 trong cùng một đoạn, câu văn mang đậm mùi dịch thuật từ cấu trúc `A, B, and C` của tiếng Anh.

### 6. Bước 5 — Mức độ đặc trưng và Khả năng chẩn đoán
- **Khả năng phân biệt**: Trung bình nếu xuất hiện 1 lần; **Cao** nếu xuất hiện **$\ge 3$ bộ liệt kê 3 phần tử trong cùng một đoạn văn 150 chữ**, hoặc xuất hiện **bộ ba kép (`SYN-04c`)** trong một câu.

### 7. Bước 6 — Hệ thống Ví dụ Đối chiếu & Cặp Chỉnh sửa Tối thiểu
- **Ví dụ A (Dương tính rõ ràng — 3 bộ ba trong 2 câu)**:
  > *"Để nâng cao **hiệu suất, chất lượng và độ tin cậy**, ngân hàng đã đầu tư vào **hạ tầng dữ liệu, trí tuệ nhân tạo và điện toán đám mây**. Bước đi này mang lại lợi ích cho **khách hàng, cổ đông và đối tác chiến lược**."*
- **Ví dụ B (Dương tính tinh vi)**:
  > *"Chính sách mới giúp quy trình phê duyệt trở nên **rõ ràng, minh bạch và nhất quán hơn**."* (Rõ ràng và minh bạch trùng nghĩa).
- **Ví dụ C (Hợp lệ — Phân loại khoa học/nghiệp vụ thực sự có 3 nhóm)**:
  > *"Theo chuẩn mực Basel II, rủi ro trọng yếu trong trụ cột 1 bao gồm **rủi ro tín dụng, rủi ro thị trường và rủi ro hoạt động**."* (Đây là 3 cấu phần kỹ thuật bắt buộc của Hiệp ước Basel II, cấm cắt bớt!).
- **Ví dụ D (Cặp Trước / Sau khi Humanize Ví dụ A)**:
  - **Sau khi Humanize**:
    > *"Để tăng tốc độ xử lý và độ ổn định của hệ thống, ngân hàng đã nâng cấp hạ tầng đám mây kết hợp trí tuệ nhân tạo, giúp rút ngắn thời gian giao dịch cho khách hàng."*

### 8. Bước 7 & Bước 8 — Hệ quả, Quy tắc Humanize & Tiêu chí Kiểm thử
- **Hệ quả**: Tạo nhịp điệu đều đặn nhàm chán; pha loãng thông tin vì phần tử thứ 3 thường là từ độn (filler) đồng nghĩa.
- **Quy tắc Humanize**:
  1. Kiểm tra xem bộ 3 có phải là **phân loại cố định của chuyên ngành** (như 3 trụ cột Basel, 3 khu vực kinh tế) hay không. Nếu phải $\rightarrow$ **Giữ nguyên tuyệt đối**.
  2. Nếu là bộ 3 tính từ/danh từ chung chung: Kiểm tra độ trùng lắp ngữ nghĩa giữa 3 từ $\rightarrow$ **Gọt xuống 1 từ đắt nhất hoặc cặp 2 từ đối xứng (nhịp chẵn tiếng Việt)**.

---

## HỒ SƠ 11: `SYN-VN-01` — DƯ THỪA ĐẠI TỪ HỒI CHỈ / THIẾU TỈNH LƯỢC CHỦ NGỮ (ĐẶC THÙ TIẾNG VIỆT)

### 1. Thông tin định danh
- **ID**: `SYN-VN-01`
- **Tên dấu hiệu**: Dư thừa đại từ hồi chỉ và thiếu sự tỉnh lược chủ ngữ tự nhiên (*Over-explicit Pronominal Anaphora & Zero-Anaphora Deficit*).
- **Nguồn gốc trong danh sách gốc**: Khối I — Mục 6.1 (*Thiếu sự "Tỉnh lược chủ ngữ" [Zero-anaphora] tự nhiên*).

### 2. Bước 1 — Định nghĩa vận hành, Phạm vi & Đơn vị quan sát
- **Cấp độ ngôn ngữ**: Cú pháp – Liên kết tham chiếu diễn ngôn (Syntactic-Discourse Referential Cohesion).
- **Đơn vị quan sát**: Vị trí chủ ngữ của các mệnh đề phụ và các câu tiếp theo sau khi chủ đề/chủ thể đã được xác lập ở câu/mệnh đề trước.
- **Định nghĩa vận hành**: Hiện tượng câu văn tiếng Việt nhồi nhét một cách cơ học các đại từ nhân xưng ngôi thứ ba (**"nó"**, **"họ"**, **"chúng"**), tổ hợp chỉ định từ (**"điều này"**, **"việc này"**, **"sự kiện này"**, **"ngân hàng này"**) hoặc tính từ sở hữu (**"của mình"**, **"của nó"**, **"của họ"**) vào các vị trí chủ ngữ/định ngữ mà người bản ngữ tiếng Việt luôn **tỉnh lược (zero-anaphora / $\varnothing$)** vì đã hoàn toàn xác định từ ngữ cảnh đứng trước.

### 3. Bước 2 — Phân tích các biểu hiện cụ thể
1. **`SYN-VN-01a` — Lạm dụng đại từ vô tri `"nó / chúng"` làm chủ ngữ câu sau (*Inanimate Pronoun "Nó/Chúng" Overuse*)**:
   - *"Chính sách tiền tệ thắt chặt đã được ban hành. **Nó** giúp kiểm soát lạm phát nhưng **nó** cũng làm giảm tăng trưởng."* (Người Việt không bao giờ gọi chính sách tiền tệ là *"Nó"* ở đầu câu học thuật như dịch từ chữ *"It"*).
2. **`SYN-VN-01b` — Lạm dụng chỉ định từ tổng kết `"Điều này / Việc này"` ở đầu câu (*Sentence-Initial "Điều này/Việc này" Calque*)**:
   - Dịch trực tiếp từ *"This leads to..."*, *"This highlights..."*: Mọi câu thứ 2 trong đoạn đều bắt đầu bằng *"Điều này cho thấy..."*, *"Việc này đòi hỏi..."*, *"Điều đó dẫn đến..."*.
3. **`SYN-VN-01c` — Dư thừa định ngữ sở hữu `"của họ / của nó / của mình"` (*Possessive Determiner Calque*)**:
   - Dịch từ *their / its*: *"Các ngân hàng đang tái cơ cấu danh mục tín dụng **của họ** để bảo vệ biên lợi nhuận **của mình**"* (Trong tiếng Việt tự nhiên, danh mục tín dụng và biên lợi nhuận đương nhiên là của các ngân hàng đó, thêm *"của họ / của mình"* là thừa thãi).

### 4. Bước 3 — Cơ chế hình thành & Bằng chứng khoa học
- **Cơ chế hình thành**:
  1. **Sự khác biệt loại hình học ngôn ngữ (Typological Parameter Mismatch: Non-pro-drop vs. Radical pro-drop)**: Tiếng Anh là ngôn ngữ **không cho phép tỉnh lược chủ ngữ (non-pro-drop language)** và bắt buộc phải có từ hạn định sở hữu (*my, his, their, its*) trước danh từ đếm được. Ngược lại, tiếng Việt là ngôn ngữ **tỉnh lược đại từ triệt để dựa trên ngữ cảnh (radical pro-drop / discourse-oriented language)** `[Cấp C]` (Cao Xuân Hạo, 1991; Trần Ngọc Thêm, 1985; Neeleman & Szendrői, 2007).
  2. Khi LLM sinh tiếng Việt dưới ảnh hưởng của biểu diễn cú pháp tiếng Anh (hoặc dữ liệu huấn luyện dịch thuật Anh–Việt), mỗi khe chủ ngữ (`NP_subj`) và khe hạn định (`Det_poss`) trong cây cú pháp đều bị ép phải điền một token hiển ngôn (*Nó, Họ, Điều này, của họ*) thay vì token rỗng ($\varnothing$) `[Cấp C]`.

### 5. Bước 4 — Phân tích đặc điểm chuyên sâu trong Tiếng Việt
- Theo Trần Ngọc Thêm (1985, *Hệ thống liên kết văn bản tiếng Việt*), **phép tỉnh lược yếu tố cốt lõi** là phương thức liên kết có mật độ cao nhất và tự nhiên nhất trong văn bản tiếng Việt khi chủ thể không đổi.
- Đặc biệt, trong tiếng Việt, đại từ **"nó"** mang sắc thái khẩu ngữ, thân mật hoặc hạ thấp (thường dùng cho trẻ nhỏ, con vật, đồ vật nhỏ trong khẩu ngữ). Việc dùng **"nó"** để quy chiếu cho các khái niệm trừu tượng hoặc trang trọng (*chính sách vĩ mô, rủi ro thanh khoản, đạo luật, ngân hàng thương mại*) trong văn phong nghị luận/học thuật vừa phạm lỗi cú pháp dịch máy, vừa **phạm lỗi sắc thái phong cách (register clash)** nghiêm trọng `[Cấp C]`.

### 6. Bước 5 — Mức độ đặc trưng và Khả năng chẩn đoán
- **Khả năng phân biệt**: **Rất cao** đối với tính tự nhiên bản ngữ. Đây là dấu hiệu phân biệt rõ nhất giữa văn bản tiếng Việt có tư duy bản ngữ với văn bản sinh bởi LLM hoặc dịch máy.

### 7. Bước 6 — Hệ thống Ví dụ Đối chiếu & Cặp Chỉnh sửa Tối thiểu
- **Ví dụ A (Dương tính rõ ràng)**:
  > *"Rủi ro thanh khoản là một mối đe dọa lớn đối với các ngân hàng nhỏ. Khi **nó** xảy ra, **nó** có thể làm tê liệt hoạt động thanh toán **của họ**. **Điều này** buộc các nhà quản lý phải giám sát chặt chẽ các chỉ số dự trữ **của mình**."*
- **Ví dụ B (Dương tính tinh vi — Dư thừa sở hữu cách và lặp chủ ngữ phụ)**:
  > *"Khi khách hàng cá nhân gặp khó khăn về thu nhập, **họ** có xu hướng cắt giảm chi tiêu không thiết yếu **của mình** và ưu tiên trả các khoản nợ đến hạn **của họ**."*
- **Ví dụ C (Hợp lệ — Dùng đại từ để phân biệt khi có 2 chủ thể khác nhau cùng xuất hiện)**:
  > *"Ngân hàng mẹ đã bơm thêm 2.000 tỷ đồng cho công ty tài chính con, nhưng bản thân **công ty này** vẫn chưa thể tự cân đối dòng tiền."* (Nếu tỉnh lược hoàn toàn sau từ *"nhưng"*, người đọc sẽ nhầm chủ ngữ của *"vẫn chưa thể tự cân đối"* là *Ngân hàng mẹ*).
- **Ví dụ D (Cặp Trước / Sau khi Humanize Ví dụ A & B)**:
  - **Sửa Ví dụ A**: *"Rủi ro thanh khoản là mối đe dọa lớn đối với các ngân hàng nhỏ: một khi $\varnothing$ bùng phát, $\varnothing$ có thể làm tê liệt ngay hoạt động thanh toán, buộc cơ quan quản lý phải giám sát chặt tỷ lệ dự trữ."* (Xóa toàn bộ *nó, của họ, điều này, của mình*; nối câu bằng dấu hai chấm và phép tỉnh lược $\varnothing$).
  - **Sửa Ví dụ B**: *"Khi thu nhập sụt giảm, khách hàng cá nhân thường cắt bớt chi tiêu không thiết yếu để ưu tiên trả các khoản nợ đến hạn."* (Giảm từ 34 chữ xuống 23 chữ, giữ nguyên 100% nghĩa, câu văn thanh thoát hoàn toàn).

### 8. Bước 7 & Bước 8 — Hệ quả, Quy tắc Humanize & Tiêu chí Kiểm thử
- **Hệ quả**: Làm câu văn tiếng Việt nặng nề, ngô nghê như văn dịch từng chữ (word-for-word translation); phá hỏng sắc thái trang trọng khi dùng từ *"nó"*.
- **Quy tắc ra quyết định khi Humanize (Zero-Anaphora Restoration Rule)**:
  1. **Cấm tuyệt đối đại từ `"nó"`** khi quy chiếu tới khái niệm trừu tượng, tổ chức, chính sách, quy định trong văn bản trang trọng/học thuật.
  2. **Kiểm tra điều kiện đồng chủ ngữ (Co-reference Check)**: Nếu Mệnh đề 2 có cùng chủ ngữ với Mệnh đề 1 và ở giữa không có danh ngữ trung gian nào gây hiểu lầm $\rightarrow$ **Tỉnh lược chủ ngữ ở Mệnh đề 2 ($\varnothing$)**.
  3. **Quét cụm `"của họ / của nó / của mình / của chúng"`**: Nếu chủ sở hữu chính là chủ ngữ của câu đó và không có sự đối chiếu sở hữu với bên thứ hai $\rightarrow$ **Xóa bỏ cụm sở hữu cách**.

---

## HỒ SƠ 12: `SYN-VN-02` — ĐÁNH MẤT CẤU TRÚC ĐỀ – THUYẾT VÌ KHUNG CHỦ – VỊ DỊCH MÁY (ĐẶC THÙ TIẾNG VIỆT)

### 1. Thông tin định danh
- **ID**: `SYN-VN-02`
- **Tên dấu hiệu**: Đánh mất cấu trúc Đề – Thuyết (*Topic – Comment*) tự nhiên vì áp đặt cấu trúc Chủ – Vị (*Subject – Predicate*) kèm giới từ dịch máy.
- **Nguồn gốc trong danh sách gốc**: Khối I — Mục 6.2 (*Đánh mất cấu trúc Đề - Thuyết [Topic - Comment]*).

### 2. Bước 1 — Định nghĩa vận hành, Phạm vi & Đơn vị quan sát
- **Cấp độ ngôn ngữ**: Cú pháp chức năng & Cấu trúc thông tin của câu (Functional Syntax & Information Structure).
- **Đơn vị quan sát**: Cấu trúc mở đầu câu và mối quan hệ giữa khung đề (Topic/Frame) với phần thuyết (Comment).
- **Định nghĩa vận hành**: Hiện tượng câu văn tiếng Việt từ bỏ cách tổ chức câu theo cấu trúc **Đề – Thuyết** (đưa đối tượng/khung phạm vi cần bàn lên đầu câu một cách trực tiếp hoặc qua hư từ phân giới *thì, là, mà*), thay vào đó luôn bọc phần Đề trong các cụm giới từ cồng kềnh dịch từ tiếng Anh (**"Đối với vấn đề X,"**, **"Về mặt khía cạnh Y,"**, **"Xét trên phương diện Z,"**, **"Liên quan đến W,"**) rồi bắt phần sau phải có đầy đủ Chủ ngữ giả + Động từ bị động (**"...nó thường được xử lý bởi..."**).

### 3. Bước 2 — Phân tích các biểu hiện cụ thể
1. **`SYN-VN-02a` — Bọc phần Đề trong cụm giới từ dịch can rườm rà (*Prepositional Wrapper around Topic*)**:
   - Dịch từ *"Regarding the issue of X..."*, *"As for Y..."*, *"In terms of Z..."*:
   - Viết: *"Đối với vấn đề rủi ro thanh khoản, nó thường được các ngân hàng nhỏ xử lý..."* thay vì cấu trúc Đề–Thuyết tự nhiên: *"Rủi ro thanh khoản, các ngân hàng nhỏ thường xử lý bằng cách..."* hoặc *"Với rủi ro thanh khoản, ngân hàng nhỏ thường..."*.
2. **`SYN-VN-02b` — Thiếu vắng hư từ phân giới Đề – Thuyết bản ngữ (`thì`, `là`, `lại`, `vẫn`)**:
   - Trong tiếng Việt, hư từ **"thì"** (khi dùng đúng chỗ trong câu phức điều kiện hoặc câu đối chiếu Đề–Thuyết) và các phó từ **"lại"**, **"vẫn"**, **"mới"** là bản lề tự nhiên tạo nhịp uốn lượn cho câu. Văn AI gần như xóa sổ các bản lề này, thay bằng dấu phẩy cứng nhắc theo cú pháp tiếng Anh.

### 4. Bước 3 — Cơ chế hình thành & Bằng chứng khoa học
- **Cơ chế hình thành & Lý thuyết ngôn ngữ học nền tảng**:
  - Theo **Cao Xuân Hạo (1991/2004, *Tiếng Việt – Sơ thảo ngữ pháp chức năng*)** và phân loại loại hình học của **Charles N. Li & Sandra A. Thompson (1976, *Subject and Topic: A New Typology of Language*)**: Tiếng Anh là ngôn ngữ thiên Chủ ngữ (*Subject-prominent language*), trong đó quan hệ ngữ pháp cơ bản của câu là Chủ ngữ – Vị ngữ (Tác thể – Hành động). Ngược lại, tiếng Việt là ngôn ngữ thiên Chủ đề (*Topic-prominent language*), trong đó cấu trúc cơ bản của câu là **Đề (khung không gian, thời gian, hoặc đối tượng được đem ra bàn luận) – Thuyết (nhận định về phần Đề đó)** `[Cấp C]`.
  - Trong tiếng Anh, vì không thể đặt khơi khơi một danh ngữ không phải tác thể lên đầu câu (*"*Liquidity risk, small banks handle..."* là câu hơi gượng trong văn viết chuẩn tiếng Anh nếu không có giới từ), tiếng Anh bắt buộc phải dùng giới từ dẫn nhập (*"Regarding liquidity risk, it is handled by small banks..."*) hoặc chuyển thành câu bị động (*"Liquidity risk is handled by..."*). LLM áp đặt nguyên xi quy tắc cú pháp tiếng Anh này sang tiếng Việt `[Cấp C]`.

### 5. Bước 4 — Phân tích đặc điểm chuyên sâu trong Tiếng Việt
- Hãy so sánh 3 cách tổ chức cùng một thông tin trong tiếng Việt:
  1. **Cấu trúc dịch máy của AI (`SYN-VN-02` + `SYN-VN-01` + `SYN-VN-03`)**:
     *"Đối với vấn đề rủi ro thanh khoản, nó thường được các ngân hàng nhỏ xử lý thông qua việc vay mượn trên thị trường liên ngân hàng."* (26 chữ — vừa thừa giới từ *"Đối với vấn đề"*, vừa thừa đại từ *"nó"*, vừa bị động *"được... xử lý"*, vừa danh hóa *"thông qua việc"*).
  2. **Cấu trúc Chủ – Vị thuần túy**:
     *"Các ngân hàng nhỏ thường xử lý rủi ro thanh khoản bằng cách vay trên thị trường liên ngân hàng."* (19 chữ — đúng ngữ pháp, nhưng đặt *"Các ngân hàng nhỏ"* làm Đề, làm giảm sức nhấn vào *"Rủi ro thanh khoản"* nếu đoạn văn đang bàn về các loại rủi ro).
  3. **Cấu trúc Đề – Thuyết bản ngữ tiếng Việt (Bảo toàn trọng tâm thông tin + Tự nhiên tuyệt đối)**:
     *"Còn rủi ro thanh khoản, các ngân hàng nhỏ thường xoay xở bằng vốn vay liên ngân hàng."* (17 chữ — *"Rủi ro thanh khoản"* đứng đầu câu làm **Đề (Topic)** để nối mạch với câu trước, phần **Thuyết (Comment)** là một mệnh đề chủ động *"các ngân hàng nhỏ thường xoay xở..."* hoàn toàn không cần giới từ *"Đối với vấn đề"* hay đại từ *"nó"*!).

### 6. Bước 5 — Mức độ đặc trưng và Khả năng chẩn đoán
- **Khả năng phân biệt**: **Rất cao** ở cấp độ biên tập chuyên sâu. Khả năng sử dụng cấu trúc Đề – Thuyết linh hoạt (đặc biệt là câu có Đề ngữ là đối tượng受 tác nhưng phần Thuyết vẫn giữ dạng chủ động) là "dấu vân tay bản ngữ" mà hầu hết các LLM hiện nay chưa tự động tạo ra được nếu không có quy tắc hướng dẫn.

### 7. Bước 6 — Hệ thống Ví dụ Đối chiếu & Cặp Chỉnh sửa Tối thiểu
- **Ví dụ A (Dương tính rõ ràng)**:
  > *"Đối với phân khúc khách hàng doanh nghiệp vừa và nhỏ, họ thường gặp nhiều rào cản liên quan đến việc tiếp cận nguồn vốn tín dụng do sự thiếu hụt về tài sản thế chấp của họ."*
- **Ví dụ B (Dương tính tinh vi)**:
  > *"Xét trên khía cạnh chi phí vốn, mức lãi suất huy động đã được điều chỉnh giảm ở hầu hết các kỳ hạn dài."*
- **Ví dụ C (Hợp lệ — Văn bản quy phạm pháp luật phân tách đối tượng áp dụng)**:
  > *"Đối với tổ chức tín dụng được kiểm soát đặc biệt, Ngân hàng Nhà nước quy định tỷ lệ dự trữ bắt buộc riêng."* (Trong văn bản luật, *"Đối với [Nhóm đối tượng pháp lý]"* là cấu trúc chuẩn để khoanh vùng phạm vi điều chỉnh của điều khoản).
- **Ví dụ D (Cặp Trước / Sau khi Humanize Ví dụ A & B)**:
  - **Sửa Ví dụ A (Chuyển về Đề – Thuyết)**: *"Ở phân khúc doanh nghiệp vừa và nhỏ, rào cản lớn nhất khi tiếp cận vốn vay vẫn là thiếu tài sản thế chấp."* (Đặt *"Ở phân khúc DNNVV"* làm Khung Đề, *"rào cản lớn nhất..."* làm Đề phụ, *"vẫn là thiếu tài sản thế chấp"* làm Thuyết — giảm từ 35 chữ xuống 22 chữ).
  - **Sửa Ví dụ B**: *"Về chi phí vốn, lãi suất huy động ở hầu hết các kỳ hạn dài đều đã hạ nhiệt."*

### 8. Bước 7 & Bước 8 — Hệ quả, Quy tắc Humanize & Tiêu chí Kiểm thử
- **Hệ quả**: Làm câu văn tiếng Việt bị "Tây hóa" (Anglicized syntax), dài dòng, mất khả năng nhấn mạnh tiêu điểm thông tin ở đầu câu.
- **Quy tắc ra quyết định khi Humanize (Topic-Comment Transformation Rule)**:
  1. Khi gặp mở đầu câu dạng `"Đối với vấn đề [X], nó được [Y] thực hiện..."` hoặc `"Liên quan đến khía cạnh [X],..."`:
  2. **Bước 1**: Cắt bỏ vỏ bọc từ rỗng (*"vấn đề"*, *"khía cạnh"*, *"lĩnh vực"*, *"nó"*).
  3. **Bước 2**: Đưa trực tiếp `[X]` lên đầu câu làm **Đề (Topic)** (có thể dùng giới từ nhẹ *"Về [X],"* hoặc *"Với [X],"* hoặc đặt trực tiếp `"[X],"`), sau đó viết phần **Thuyết (Comment)** ở dạng chủ động `[Y] + [Động từ]`.

---

## HỒ SƠ 13: `SYN-VN-03` — `[BỔ SUNG]` LẠM DỤNG THỂ BỊ ĐỘNG DỊCH MÁY (`ĐƯỢC/BỊ`) & DANH HÓA ĐỘNG TỪ (`VIỆC/SỰ + V`)

### 1. Thông tin định danh
- **ID**: `SYN-VN-03`
- **Tên dấu hiệu**: Lạm dụng cấu trúc bị động dịch can (`được/bị ... bởi`) và danh hóa động từ bằng hư từ (`việc`, `sự`, `quá trình` + Động từ).
- **Nguồn gốc**: **Dấu hiệu bổ sung có căn cứ (`[NEW-VN-01]`)** do nhóm nghiên cứu tách ra từ các câu mẫu trong Mục 2 và Mục 6 của danh sách người dùng (*"Thông qua **việc** ứng dụng..., quy trình... đã **được** rút ngắn"*, *"việc đa dạng hóa..."*, *"thường **được** các ngân hàng nhỏ xử lý thông qua **việc**..."*).

### 2. Bước 1 — Định nghĩa vận hành, Phạm vi & Đơn vị quan sát
- **Cấp độ ngôn ngữ**: Cú pháp – Hình thái từ loại tiếng Việt (Morpho-syntactic voice & nominalization).
- **Đơn vị quan sát**: Cụm vị ngữ có trợ từ `được/bị` và cụm danh hóa mở đầu bằng `việc / sự / quá trình`.
- **Định nghĩa vận hành**: Hiện tượng câu văn tiếng Việt mắc đồng thời hoặc riêng lẻ hai lỗi dịch can từ tiếng Anh:
  1. **Bị động dịch máy (*Passive Voice Calquing*)**: Sử dụng từ `"được"` hoặc `"bị"` (thậm chí kèm giới từ `"bởi"` — dịch từ `by`) cho những câu trung tính về mặt lợi/hại hoặc những câu mà tiếng Việt tự nhiên chỉ cần đặt đối tượng lên làm Đề mà không cần từ `được/bị`.
  2. **Danh hóa động từ tràn lan (*Verbal Nominalization Overload*)**: Đóng gói các động từ hành động thành cụm danh từ bằng cách gắn thêm các danh từ chỉ loại trừu tượng `"việc"`, `"sự"`, `"quá trình"` ở phía trước (*"việc triển khai"*, *"sự gia tăng"*, *"thông qua việc sử dụng"*).

### 3. Bước 2 — Phân tích các biểu hiện cụ thể
1. **`SYN-VN-03a` — Cấu trúc `"được [V] bởi [Tác thể]"` (`is V-ed by Agent`)**:
   - *"Báo cáo này được viết bởi các chuyên gia phân tích"*, *"Quyết định tăng lãi suất được đưa ra bởi Cục Dự trữ Liên bang"*.
2. **`SYN-VN-03b` — Dùng `"được"` cho sự việc tiêu cực hoặc trung tính (Xung đột tình thái của từ `"được"`)**:
   - *"Nguyên nhân của vụ sập cầu được xác định là do..."*, *"Nhiều lỗ hổng bảo mật đã được phát hiện trong hệ thống"*.
3. **`SYN-VN-03c` — Đóng gói `"Thông qua việc [V] / Bằng việc [V] / Việc [V] đã..."`**:
   - Dịch từ `By V-ing / Through the use of / V-ing has...`: *"Thông qua việc cắt giảm chi phí..."*, *"Việc ngân hàng hạ lãi suất đã giúp..."*.

### 4. Bước 3 — Cơ chế hình thành & Bằng chứng khoa học
- **Cơ chế hình thành & Lý thuyết ngôn ngữ học tiếng Việt**:
  - Theo **Cao Xuân Hạo (1991)** và **Diệp Quang Ban (2005)**, tiếng Việt **không có phạm trù ngữ pháp Bị động (Passive Voice)** đối lập hình thái với Chủ động như tiếng Anh. Trong tiếng Việt, hai từ **`được`** (nhận lấy điều có lợi/đáng mừng) và **`bị`** (chịu đựng điều bất lợi/tai họa) bản chất là **hai vị từ tình thái đánh giá may/rủi (adversative/benefactive modal verbs)**, không phải trợ từ bị động thuần túy `[Cấp C]`.
  - Khi câu tiếng Việt muốn đưa đối tượng chịu tác động lên đầu câu mà không mang hàm ý khen/chê may/rủi, tiếng Việt dùng **cấu trúc Đề – Thuyết không có `được/bị`** (ví dụ: *"Cầu này xây từ năm 1990"*, *"Báo cáo này công bố hồi tháng 3"*, không nói *"Cầu này được xây dựng bởi..."*).
  - Tương tự, tiếng Anh bắt buộc phải danh hóa động từ (`Gerund V-ing` hoặc `the V-tion of`) khi động từ đứng sau giới từ (`through applying AI`) hoặc đứng làm chủ ngữ. Tiếng Việt cho phép động từ/mệnh đề đứng trực tiếp làm chủ ngữ hoặc đứng sau từ nối (*"Nhờ ứng dụng AI"*, không cần *"Thông qua việc ứng dụng AI"*) `[Cấp C]`.

### 5. Bước 4 & Bước 5 — Đặc điểm Tiếng Việt & Khả năng chẩn đoán
- **Khả năng phân biệt**: Rất cao. Mật độ từ `"việc"`, `"sự"` và cấu trúc `"được + V + bởi"` trong văn bản AI tiếng Việt cao gấp 3–5 lần văn viết của các cây bút tiếng Việt lão luyện `[Cấp D]`.

### 6. Bước 6 — Hệ thống Ví dụ Đối chiếu & Cặp Chỉnh sửa Tối thiểu
- **Ví dụ A (Dương tính rõ ràng)**:
  > *"**Việc** áp dụng chuẩn mực kế toán mới **được** kỳ vọng **bởi** các nhà đầu tư là sẽ mang lại **sự** cải thiện đối với **việc** minh bạch hóa báo cáo tài chính."* (3 từ *việc/sự*, 1 cấu trúc *được... bởi*).
- **Ví dụ B (Dương tính tinh vi)**:
  > *"Thông qua **việc** đẩy mạnh giải ngân đầu tư công, tăng trưởng GDP quý IV đã **được** hỗ trợ tích cực."*
- **Ví dụ C (Hợp lệ — Khi `được` thực sự mang nghĩa hưởng lợi tích cực hoặc `việc` dùng để danh hóa một mệnh đề làm tân ngữ phân biệt)**:
  > *"Doanh nghiệp công nghệ cao **được** miễn thuế thu nhập trong 4 năm đầu."* (Ở đây *"được miễn thuế"* mang nghĩa hưởng quyền lợi thực sự, hoàn toàn tự nhiên).
- **Ví dụ D (Cặp Trước / Sau khi Humanize Ví dụ A & B)**:
  - **Sửa Ví dụ A**: *"Giới đầu tư kỳ vọng chuẩn mực kế toán mới sẽ giúp báo cáo tài chính minh bạch hơn."* (Giảm từ 31 chữ xuống 18 chữ; xóa sạch 3 từ *việc/sự* và cấu trúc *được... bởi*).
  - **Sửa Ví dụ B**: *"Nhờ đẩy mạnh giải ngân đầu tư công, tăng trưởng GDP quý IV giữ được đà phục hồi."* (Thay *"Thông qua việc"* bằng *"Nhờ"*, chuyển bị động sang chủ động).

### 7. Bước 7 & Bước 8 — Hệ quả, Quy tắc Humanize & Tiêu chí Kiểm thử
- **Quy tắc ra quyết định khi Humanize**:
  1. **Quy tắc `[được/bị + V + bởi + Tác thể]`**: Bắt buộc đảo `Tác thể` lên làm chủ ngữ câu chủ động (`[Tác thể] + [V]`), xóa bỏ từ *"bởi"*.
  2. **Quy tắc `["Thông qua việc / Bằng việc" + V]`**: Đổi thành **"Nhờ [V]"**, **"Khi [V]"**, hoặc **"Bằng cách [V]"** (bỏ từ *"việc"*).
  3. **Quy tắc `["Việc / Sự" + V]` ở đầu câu**: Nếu có thể chuyển thành mệnh đề trạng ngữ mở đầu bằng *"Khi..."* hoặc để cụm động từ trực tiếp làm Đề ngữ $\rightarrow$ **Cắt bỏ từ `"việc / sự"`**.
