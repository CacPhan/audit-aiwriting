# HỒ SƠ NGHIÊN CỨU CHUYÊN SÂU — NHÓM 3: NHỊP ĐIỆU, ĐỘ BIẾN THIÊN, CẤU TRÚC ĐOẠN VĂN VÀ LIÊN KẾT DIỄN NGÔN (`RHY` & `DIS`)
**(Giai đoạn 3, Giai đoạn 4, Đầu ra B & C — Các hồ sơ `RHY-01` đến `DIS-04`)**

---

## HỒ SƠ 14: `RHY-01` — ĐỘ BIẾN THIÊN CHIỀU DÀI CÂU CỰC THẤP (*LOW BURSTINESS / METRONOMIC RHYTHM*)

### 1. Thông tin định danh
- **ID**: `RHY-01`
- **Tên dấu hiệu**: Độ biến thiên chiều dài câu và độ phức tạp cú pháp cực thấp (*Low Sentence-Length Burstiness / Metronomic Prose Rhythm*).
- **Nguồn gốc trong danh sách gốc**: Khối I — Mục 1 (*Độ biến thiên chiều dài câu cực thấp [Low Burstiness – Nhịp văn "máy đếm nhịp"]*) & Khối II — `WP:AIVOCAB` (ghi nhận xu hướng các mô hình giữa năm 2026 trở đi như GPT-6 nén câu quanh ngưỡng hẹp 8–20 từ và tăng mật độ dấu chấm/phẩy).

### 2. Bước 1 — Định nghĩa vận hành, Phạm vi & Đơn vị quan sát
- **Cấp độ ngôn ngữ**: Nhịp điệu thống kê liên câu & Tổ chức đoạn văn (Statistical Prosody & Sentence-Length Distribution).
- **Đơn vị quan sát**: Chuỗi chiều dài câu $L = (l_1, l_2, \dots, l_n)$ tính bằng **số âm tiết (chữ) tiếng Việt** trong một đoạn văn ($n \ge 4$ câu) hoặc trên toàn văn bản ($n \ge 10$ câu).
- **Định nghĩa vận hành**:
  Trong ngôn ngữ học định lượng, độ biến thiên chiều dài câu được đo bằng **Hệ số biến thiên (Coefficient of Variation – $CV$)** và **Độ lệch chuẩn hiệu chỉnh trung bình động (Local Rolling Standard Deviation)**:
  $$CV = \frac{\sigma_L}{\mu_L} = \frac{\sqrt{\frac{1}{n}\sum_{i=1}^{n}(l_i - \mu_L)^2}}{\mu_L}$$
  Một đoạn văn tiếng Việt bị xác định dương tính với `RHY-01` khi:
  1. $CV < 0,18$ (hoặc phương sai chiều dài giữa 4 câu liên tiếp $\sigma_L < 3,5$ chữ), **VÀ**
  2. Vắng bóng hoàn toàn sự luân phiên cực trị giữa **câu đơn ngắn tạo điểm nhấn ($l_i \le 12$ chữ)** và **câu phức phân tích đa tầng ($l_i \ge 35$ chữ)**; toàn bộ các câu đều tụ hội quanh một dải trung bình hẹp (18–28 chữ ở thế hệ mô hình 2023–2025, hoặc 12–20 chữ ở thế hệ mô hình cuối 2026).

### 3. Bước 2 — Phân tích các biểu hiện cụ thể (Sub-manifestations)
1. **`RHY-01a` — Nhịp trung bình an toàn (The 18–28 Word Plateau — Thế hệ GPT-4 / GPT-4o / Claude 3.5)**:
   - Mọi câu trong đoạn đều dài khoảng 22–26 chữ (như ví dụ trong Bảng đối chiếu của người dùng: `24 – 25 – 23 – 25 chữ`, $\mu_L = 24,25$, $\sigma_L = 0,83$, $CV = 0,034$).
2. **`RHY-01b` — Nhịp ngắn đều kiểu Staccato (The 12–20 Word Compressed Plateau — Thế hệ GPT-5.1 / GPT-6 giữa và cuối 2026)**:
   - Do bị huấn luyện hạn chế câu dài và cấm dùng dấu gạch ngang dài (`—`), mô hình cắt mọi câu về ngưỡng 12–18 chữ, tạo ra nhịp điệu đều đặn kiểu điện tín (staccato monotone), câu nào cũng 1 mệnh đề chính + 1 mệnh đề phụ ngắn.
3. **`RHY-01c` — Đồng nhất độ sâu cây cú pháp (*Uniform Parse-Tree Depth*)**:
   - Không chỉ bằng nhau về số lượng chữ, các câu còn có cùng số lượng dấu phẩy (thường đúng 1 hoặc 2 dấu phẩy mỗi câu) và cùng độ sâu phân nhánh cú pháp.

### 4. Bước 3 — Cơ chế hình thành & Bằng chứng khoa học
- **Cơ chế hình thành**:
  1. **Lấy mẫu điển hình cục bộ (*Locally Typical Sampling*) và tối ưu hóa xác suất tự hồi quy**: **Meister et al. (2023, *TACL*)** chứng minh rằng quá trình sinh văn bản của LLM (dưới top-$p$ / nucleus sampling và temperature $< 1$) tập trung xác suất vào vùng "điển hình cục bộ" (nơi entropy điều kiện của từng bước sinh xấp xỉ entropy kỳ vọng của mô hình). Trong một câu, xác suất xuất hiện token dấu chấm câu (`.`) tăng dần theo đường cong logistic mượt và đạt đỉnh quanh độ dài câu trung bình của tập huấn luyện (~20–25 token), khiến mô hình cực kỳ hiếm khi chấm câu sớm ở từ thứ 6 hoặc kéo dài câu lên từ thứ 45 `[Cấp B]`.
  2. **Thiếu vắng "Ý đồ nhịp điệu toàn cục" (Absence of Global Prosodic Planning)**: Con người khi viết có cảm thức về nhịp thở (nhịp nhanh khi khẳng định dứt khoát, nhịp chậm và nhiều tầng khi giải thích cơ chế phức tạp). LLM sinh từ trái sang phải từng token một mà không có bộ lập kế hoạch nhịp điệu cấp đoạn `[Cấp C]`.
- **Bằng chứng ủng hộ**:
  - **Gehrmann et al. (2019 - GLTR)**, **Mitchell et al. (2023 - DetectGPT)**, và các công cụ như GPTZero sử dụng *Burstiness* (phương sai của perplexity và độ dài câu giữa các câu liên tiếp) làm một trong hai đặc trưng thống kê cốt lõi để phân biệt văn bản máy và người `[Cấp B]`.
  - **Reinhart et al. (2025, PNAS)** và **The Economist Study (July 2026)** (*cite_note-economistJul2026-26*): Xác nhận sự co cụm chiều dài câu và sự sụt giảm độ đa dạng dấu câu ở các mô hình năm 2026 `[Cấp B]`.
- **Bằng chứng phản bác & Giới hạn**:
  - Như phần *Caveats* của Wikipedia đã chỉ ra (`WP:AIDETECTION` — Russell et al., 2025; Dik et al., 2025): Chỉ số *Burstiness* đơn lẻ có tỷ lệ dương tính giả (false positive) không nhỏ trên các văn bản có tính quy chuẩn cao như **tóm tắt bài báo khoa học (abstracts), tin vắn thông tấn xã, hoặc điều khoản pháp lý**, nơi người viết chuyên nghiệp cũng duy trì độ dài câu rất đều (20–25 chữ) `[Cấp B]`.

### 5. Bước 4 — Phân tích đặc điểm chuyên sâu trong Tiếng Việt
- Trong văn nghị luận và phân tích chuyên ngành tiếng Việt, nhịp điệu câu gắn liền với **luật phối thanh (bằng – trắc)** và **cấu trúc câu mở – câu đóng**:
  - Người viết tiếng Việt giỏi thường mở đầu đoạn hoặc chốt lại một phân tích dài bằng một **câu đơn ngắn từ 6 đến 12 âm tiết** (*"Thực tế lại hoàn toàn trái ngược."*, *"Nhưng dư địa không còn nhiều."*, *"Đó mới là phần nổi của tảng băng."*) để tạo độ lắng và định hướng sự chú ý.
  - Ngay sau hoặc trước câu ngắn đó là một **câu ghép nhiều tầng từ 35 đến 50 âm tiết** sử dụng dấu hai chấm (`:`), dấu chấm phẩy (`;`) hoặc cặp quan hệ từ tương phản (*trong khi... thì...*) để đặt hai mặt của vấn đề lên cùng một bàn cân.
- Văn AI tiếng Việt đánh mất hoàn toàn sự tương phản giữa "câu chốt ngắn" và "câu mổ xẻ dài", biến đoạn văn thành một dải băng chuyền đều tăm tắp.

### 6. Bước 5 — Mức độ đặc trưng và Khả năng chẩn đoán
- **Khả năng phân biệt**: Trung bình nếu đứng một mình; **Rất cao** khi kết hợp với `SYN-01` (Đẳng cấu cú pháp) và `DIS-01` (Đoạn văn đóng hộp).

### 7. Bước 6 — Hệ thống Ví dụ Đối chiếu & Cặp Chỉnh sửa Tối thiểu
- **Ví dụ A (Dương tính rõ ràng — Trích từ Bảng đối chiếu của người dùng: `24 – 25 – 23 – 25 chữ`, $CV = 0,034$)**:
  > *(Câu 1 - 24 chữ)* Trong bối cảnh biên lãi ròng thu hẹp, việc đa dạng hóa nguồn thu ngoài lãi đóng vai trò then chốt đối với các ngân hàng. *(Câu 2 - 25 chữ)* Cụ thể, các hoạt động dịch vụ thanh toán và kinh doanh ngoại hối đã mang lại nguồn thu ổn định, giúp giảm sự phụ thuộc vào tín dụng. *(Câu 3 - 23 chữ)* Tuy nhiên, mảng phân phối bảo hiểm qua ngân hàng lại đang đối mặt với nhiều thách thức lớn về niềm tin của khách hàng. *(Câu 4 - 25 chữ)* Do đó, các tổ chức tín dụng cần tái cấu trúc danh mục dịch vụ một cách toàn diện để đảm bảo sự phát triển bền vững.
- **Ví dụ B (Dương tính tinh vi — Kiểu câu ngắn đều năm 2026: `14 – 15 – 14 – 15 chữ`, $CV = 0,035$)**:
  > *(14 chữ)* Biên lãi ròng của các ngân hàng đang thu hẹp dần trong năm nay. *(15 chữ)* Do đó, nguồn thu ngoài lãi trở thành ưu tiên quan trọng của hệ thống. *(14 chữ)* Mảng dịch vụ thanh toán và ngoại hối vẫn duy trì mức tăng trưởng tốt. *(15 chữ)* Ngược lại, mảng phân phối bảo hiểm tiếp tục sụt giảm vì khủng hoảng niềm tin.
- **Ví dụ C (Bề ngoài tương tự nhưng hợp lệ — Tin vắn tài chính / Điểm tin số liệu)**:
  > *"Kết thúc phiên giao dịch ngày 06/11, VN-Index tăng 8,5 điểm lên mức 1.265 điểm. Thanh khoản toàn thị trường đạt 18.400 tỷ đồng trên cả ba sàn. Khối ngoại bán ròng nhẹ 120 tỷ đồng, tập trung ở nhóm cổ phiếu thép."* (Thể loại điểm tin nhanh có quy ước câu ngắn đều để đọc lướt số liệu).
- **Ví dụ D (Văn phong con người tự nhiên — Trích từ Bảng đối chiếu của người dùng: `11 – 38 – 16 chữ`, $CV = 0,54$)**:
  > *(Câu 1 - 11 chữ)* Khi NIM bị thu hẹp, các ngân hàng buộc phải tìm đường sống từ thu nhập ngoài lãi. *(Câu 2 - 38 chữ)* Nhưng bức tranh năm 2025–2026 không còn dễ dàng như giai đoạn trước: trong khi mảng thanh toán và kinh doanh ngoại hối giữ được nhịp tăng trưởng ổn định, thì "con gà đẻ trứng vàng" một thời là Bancassurance lại sụt giảm mạnh sau hàng loạt biến cố về niềm tin thị trường. *(Câu 3 - 16 chữ)* Bài toán lúc này không còn là mở rộng bằng mọi giá, mà là lọc lại chất lượng dịch vụ.

### 8. Bước 7 & Bước 8 — Hệ quả, Quy tắc Humanize & Tiêu chí Kiểm thử
- **Hệ quả**: Làm giảm khả năng duy trì sự chú ý của người đọc (attentional fatigue); làm mất khả năng dùng chiều dài câu để biểu đạt trọng số cảm xúc và sức nặng luận điểm.
- **Quy tắc ra quyết định khi Humanize (Prosodic Modulation Algorithm)**:
  1. Khi phát hiện đoạn văn $\ge 4$ câu có $CV < 0,18$:
  2. **Bước 1 (Tạo câu phức đối chiếu 35–45 chữ)**: Tìm 2 câu liền kề có quan hệ đối lập hoặc nhân quả (ví dụ Câu 2 nói mặt tích cực và Câu 3 nói mặt tiêu cực) $\rightarrow$ **Gộp lại thành 1 câu phức đa tầng** dùng dấu hai chấm (`:`) hoặc cặp liên từ *trong khi... thì...*.
  3. **Bước 2 (Tạo câu chốt ngắn 6–14 chữ)**: Rút gọn câu mở đoạn hoặc câu chuyển ý cuối đoạn thành một câu đơn sắc gọn ($\le 14$ chữ) bằng cách cắt bỏ các cụm trạng ngữ rườm rà.
- **Tiêu chí kiểm thử**: Hệ số biến thiên độ dài câu $CV$ của đoạn văn sau khi sửa đạt trong khoảng **$0,30 \le CV \le 0,65$**; chênh lệch giữa câu dài nhất và câu ngắn nhất trong đoạn $\ge 18$ chữ.

---

## HỒ SƠ 15: `DIS-01` — CẤU TRÚC "ĐOẠN VĂN ĐÓNG HỘP" 4 BƯỚC KHÉP KÍN (*BOXY, SELF-CONTAINED PARAGRAPHS*)

### 1. Thông tin định danh
- **ID**: `DIS-01`
- **Tên dấu hiệu**: Cấu trúc "Đoạn văn đóng hộp" 4 bước khép kín và sự đứt gãy mạch văn liên đoạn (*Boxy, Self-Contained Paragraphs & Inter-Paragraph Modularity*).
- **Nguồn gốc trong danh sách gốc**: Khối I — Mục 3 (*Cấu trúc "Đoạn văn đóng hộp" [Boxy, Self-Contained Paragraphs]*).

### 2. Bước 1 — Định nghĩa vận hành, Phạm vi & Đơn vị quan sát
- **Cấp độ ngôn ngữ**: Cấu trúc đoạn văn & Tổ chức diễn ngôn liên đoạn (Paragraph & Macro-discourse structure).
- **Đơn vị quan sát**: Từng đoạn văn (Paragraph) và ranh giới chuyển tiếp giữa Đoạn $k$ và Đoạn $k+1$.
- **Định nghĩa vận hành**: Hiện tượng văn bản được chia thành các đoạn văn có kích thước hình học gần như bằng nhau (thường 3–5 câu, dài 75–110 chữ mỗi đoạn), trong đó mỗi đoạn vận hành như một **"hộp kín tự cung tự cấp" (self-contained module)** tuân theo công thức 4 bước cố định:
  - **Bước 1 (Câu chủ đề)**: Nhận định khái quát.
  - **Bước 2 (Câu giải thích)**: Mở rộng câu 1 (*Cụ thể, Điều này có nghĩa là...*).
  - **Bước 3 (Câu chi tiết/phản biện nhẹ)**: Nêu biểu hiện chung chung hoặc mặt hạn chế (*Bên cạnh đó, Tuy nhiên...*).
  - **Bước 4 (Câu kết đoạn đóng nắp)**: Tự tóm tắt lại ý nghĩa hoặc đưa ra lời khuyên chung (*Như vậy, Do đó, Qua đó có thể thấy...*).
  - **Phép thử định danh cốt lõi (The Permutation Test)**: Có thể hoán đổi vị trí Đoạn $k$ và Đoạn $k+1$ (hoặc Đoạn 2 và Đoạn 4) mà không làm gãy bất kỳ liên kết ngữ pháp hay mạch dẫn dắt nào, vì câu cuối của đoạn trước không hề mở đường cho câu đầu của đoạn sau.

### 3. Bước 2 — Phân tích các biểu hiện cụ thể
1. **`DIS-01a` — Đồng dạng kích thước đoạn văn thị giác (*Visual Paragraph Uniformity*)**:
   - Toàn bộ bài viết gồm 5–7 đoạn văn có số dòng bằng hệt nhau (4–5 dòng/đoạn), không có đoạn ngắn 1–2 câu chuyển ý, cũng không có đoạn dài phân tích sâu.
2. **`DIS-01b` — Chu trình 4 bước khép kín nội đoạn (*Internal 4-Step Micro-Essay Cycle*)**:
   - Đoạn văn nào cũng tự mở bài ở câu 1 và tự kết bài ở câu 4 (`Topic -> Elaboration -> Caveat/Example -> Mini-Conclusion`).
3. **`DIS-01c` — Mất liên kết móc xích liên đoạn (*Absence of Inter-Paragraph Chaining / Bridge Sentences*)**:
   - Câu cuối của Đoạn $k$ đóng sập vấn đề lại bằng một khẩu hiệu (*"...để phát triển bền vững"*), buộc câu đầu của Đoạn $k+1$ phải khởi động lại từ con số 0 bằng một từ nối liệt kê (*"Bên cạnh đó, một yếu tố quan trọng khác là..."*).

### 4. Bước 3 — Cơ chế hình thành & Bằng chứng khoa học
- **Cơ chế hình thành**:
  1. **Khuôn mẫu "Đoạn văn chuẩn PEEL / TEEL" trong dữ liệu Instruction Tuning**: Trong giáo dục viết luận tiếng Anh đại chúng (IELTS, TOEFL, Five-Paragraph Essay), học sinh được dạy viết mỗi đoạn văn theo công thức **PEEL** (*Point – Explanation – Example – Link/Conclusion*). Khi các nhà phát triển AI thuê người gán nhãn (annotators) tạo dữ liệu SFT và chấm điểm RLHF, các đoạn văn tuân thủ khuôn PEEL có cấu trúc rõ ràng, dễ chấm điểm nhanh nên được thưởng điểm cao nhất `[Cấp C]`.
  2. **Sự suy giảm chú ý tầm xa đối với kế hoạch diễn ngôn (Discourse Planning Horizon)**: Khi sinh từng đoạn theo dàn ý ngầm, mô hình xử lý từng mục như một sub-task độc lập và có xu hướng "hoàn tất" (wrap up) mục đó trước khi chuyển sang mục tiếp theo `[Cấp C]`.

### 5. Bước 4 — Phân tích đặc điểm chuyên sâu trong Tiếng Việt
- Trong lý thuyết ngữ pháp văn bản tiếng Việt (Trần Ngọc Thêm, 1985/1999; Diệp Quang Ban, 2005), các đoạn văn trong văn bản nghị luận và khoa học chất lượng cao không chỉ liên kết theo kiểu **song hành (parallel structure)** mà chủ yếu kết hợp giữa **liên kết móc xích (chain linking)** và **câu chuyển đoạn bản lề (transitional pivot)**:
  - Câu cuối của đoạn trước thường **đặt ra một nghịch lý, một câu hỏi ngầm hoặc một giới hạn của luận điểm vừa bàn**, và câu đầu của đoạn sau bắt lấy chính từ khóa ở cuối đoạn trước làm phần **Đề (Topic)** để giải quyết tiếp `[Cấp C]`.
- Cấu trúc đóng hộp 4 bước của AI biến văn bản tiếng Việt thành một danh sách gạch đầu dòng trá hình dưới dạng đoạn văn xuôi.

### 6. Bước 5 — Mức độ đặc trưng và Khả năng chẩn đoán
- **Khả năng phân biệt**: **Rất cao** khi có $\ge 3$ đoạn văn liên tiếp trong bài cùng lặp lại công thức 4 bước và vượt qua "Phép thử hoán vị" (đổi chỗ các đoạn mà văn bản vẫn đọc như cũ). Lưu ý ngoại lệ: Bài thi viết luận ngoại ngữ (IELTS Writing Task 2) của học sinh con người luyện theo lò cũng có hiện tượng đóng hộp PEEL này `[Cấp C]`.

### 7. Bước 6 — Hệ thống Ví dụ Đối chiếu & Cặp Chỉnh sửa Tối thiểu
- **Ví dụ A (Dương tính rõ ràng — 2 đoạn văn đóng hộp liên tiếp có thể đảo vị trí tùy ý)**:
  > **[Đoạn 1]** *(1-Chủ đề)* Chuyển đổi số trong ngành ngân hàng đang mang lại nhiều lợi ích vượt trội cho hoạt động vận hành. *(2-Giải thích)* Cụ thể, việc tự động hóa các quy trình thủ công giúp giảm thiểu sai sót và rút ngắn thời gian giao dịch. *(3-Ví dụ)* Nhiều ngân hàng đã ứng dụng eKYC để khách hàng mở tài khoản chỉ trong vài phút. *(4-Kết hộp)* **Như vậy, đầu tư vào công nghệ số là chìa khóa tất yếu để nâng cao hiệu quả kinh doanh.**
  >
  > **[Đoạn 2]** *(1-Chủ đề)* Bên cạnh đó, vấn đề an ninh mạng đang trở thành một mối quan tâm hàng đầu của các tổ chức tài chính. *(2-Giải thích)* Thực tế cho thấy, các cuộc tấn công mạng ngày càng tinh vi và gây thiệt hại lớn về uy tín. *(3-Chi tiết)* Kẻ gian thường lợi dụng lỗ hổng bảo mật và sự mất cảnh giác của người dùng để chiếm đoạt tài sản. *(4-Kết hộp)* **Do đó, các ngân hàng cần tăng cường hệ thống phòng thủ để đảm bảo an toàn bền vững.**
- **Ví dụ D (Cặp Trước / Sau khi Humanize — Đập vỡ vỏ hộp và móc xích 2 đoạn thành dòng chảy liên tục)**:
  - **Sau khi Humanize**:
    > **[Đoạn 1 — Kết mở sang Đoạn 2]** Tự động hóa quy trình đang giúp các ngân hàng cắt giảm mạnh chi phí vận hành tại quầy. Nhờ định danh điện tử (eKYC), khách hàng hiện có thể mở tài khoản chỉ trong vài phút thay vì phải đến chi nhánh đối chiếu giấy tờ như trước. **Thế nhưng, chính tốc độ mở rộng quá nhanh của các kênh giao dịch trực tuyến này lại đang mở ra những kẽ hở mới về an ninh mạng.** *(Câu cuối Đoạn 1 không đóng hộp mà mở toang vấn đề sang Đoạn 2!)*
    >
    > **[Đoạn 2 — Bắt mạch trực tiếp từ cuối Đoạn 1]** Rủi ro lớn nhất hiện nay nằm ở chính khâu xác thực sinh trắc học và sự mất cảnh giác của người dùng cuối. Khi tội phạm công nghệ cao sử dụng deepfake để vượt qua lớp kiểm tra eKYC, thiệt hại không chỉ dừng ở số tiền bị chiếm đoạt mà còn đánh trực diện vào niềm tin đối với ngân hàng số.

### 8. Bước 7 & Bước 8 — Hệ quả, Quy tắc Humanize & Tiêu chí Kiểm thử
- **Hệ quả**: Triệt tiêu động lực đọc tiếp (narrative momentum) giữa các đoạn; tạo ra sự lặp lại cấu trúc gây buồn ngủ; làm văn bản thiếu chiều sâu phát triển ý.
- **Quy tắc ra quyết định khi Humanize (De-boxing & Chaining Protocol)**:
  1. **Bước 1 (Cắt đáy hộp)**: Xóa bỏ câu thứ 4 mang tính tổng kết sáo rỗng (*"Như vậy..., Do đó cần... để phát triển bền vững"*) ở cuối các đoạn văn thân bài (`DIS-02`).
  2. **Bước 2 (Tạo móc xích chuyển đoạn – Pivot Sentence)**: Biến câu cuối của Đoạn $k$ hoặc câu đầu của Đoạn $k+1$ thành một **câu bản lề** nối trực tiếp hệ quả/hạn chế của luận điểm $k$ với sự xuất hiện của luận điểm $k+1$.
  3. **Bước 3 (Phá vỡ kích thước đồng복)**: Cho phép các đoạn văn co giãn tự nhiên (có đoạn 2 câu ngắn làm bản lề chuyển mạch, có đoạn 5–6 câu phân tích sâu kèm số liệu).

---

## HỒ SƠ 16: `DIS-02` — CÂU KẾT ĐOẠN / KẾT MỤC TỔNG KẾT THỪA (`WP:CONCLUSION`)

### 1. Thông tin định danh
- **ID**: `DIS-02`
- **Tên dấu hiệu**: Câu kết đoạn hoặc mục kết luận tóm tắt lặp lại thừa thãi (*Redundant Paragraph/Section Summary & Formulaic Closure*).
- **Nguồn gốc trong danh sách gốc**: Khối II — `WP:CONCLUSION`, `WP:INCONCLUSION` (*In summary, In conclusion, Overall*) & Khối I — Mục 3 (Câu 4 kết đoạn: *"Như vậy,", "Nhìn chung,", "Qua đó có thể thấy...", "Chính vì vậy..."*).

### 2. Bước 1 — Định nghĩa vận hành, Phạm vi & Đơn vị quan sát
- **Cấp độ ngôn ngữ**: Liên kết diễn ngôn & Cấu trúc đóng đoạn/đóng mục (Discourse Closure level).
- **Đơn vị quan sát**: Câu cuối cùng của đoạn văn hoặc đoạn văn cuối cùng của một mục (section).
- **Định nghĩa vận hành**: Hiện tượng kết thúc một đoạn văn ngắn (100–150 chữ) hoặc một mục ngắn bằng một câu mở đầu bằng các cụm từ tổng kết (**"Tóm lại,"**, **"Nhìn chung,"**, **"Như vậy,"**, **"Tổng kết lại,"**, **"Qua đó có thể thấy rằng,"**) mà nội dung phía sau chỉ **lặp lại nguyên xi ý của câu chủ đề đầu đoạn bằng từ ngữ chung chung hơn** hoặc đưa ra một lời khuyên đạo lý hiển nhiên (*"cần có sự nỗ lực từ nhiều phía"*).

### 3. Bước 2 — Phân tích các biểu hiện cụ thể
1. **`DIS-02a` — Câu kết đoạn nhai lại câu chủ đề (*Echoic Mini-Conclusion*)**:
   - Câu 1 nói *"X rất quan trọng đối với Y"*, Câu 4 kết lại *"Tóm lại, không thể phủ nhận vai trò thiết yếu của X trong Y"*.
2. **`DIS-02b` — Câu kết đoạn kiểu lời khuyên hành chính sáo rỗng (*Bureaucratic Exhortation Closure*)**:
   - *"Chính vì vậy, các bên liên quan cần phối hợp chặt chẽ để phát huy tối đa tiềm năng và hướng tới tương lai bền vững."*
3. **`DIS-02c` — Mục "Kết luận" (`== Kết luận ==`) không cần thiết trong văn bản thông tin/bách khoa**:
   - Tự động chèn một mục *Kết luận / Tổng kết* ở cuối bài viết ngắn hoặc bài bách khoa thư (nơi quy ước thể loại kết thúc ngay sau mục thông tin cuối cùng) `[Cấp B]` (Ju et al., 2024).

### 4. Bước 3 — Cơ chế hình thành & Bằng chứng khoa học
- **Cơ chế hình thành**: Khi sinh văn bản trong môi trường hội thoại (chatbot), mỗi câu trả lời của AI được thiết kế như một thông điệp hoàn chỉnh có lời chào/mở đầu và lời kết gói gọn để người dùng cảm thấy câu trả lời đã trọn vẹn (conversational wrap-up bias). Khi áp dụng vào văn bản nhiều đoạn, cơ chế này tự động nhân bản lời kết vào cuối mỗi đoạn `[Cấp B]` (Ju et al., 2024).

### 5. Bước 4 & Bước 5 — Đặc điểm Tiếng Việt & Khả năng chẩn đoán
- Trong tiếng Việt, các cụm **"Qua đó có thể thấy rằng"**, **"Nhìn chung lại"**, **"Tóm lại một cách tổng thể"** ở cuối mỗi đoạn văn ngắn 4 câu là dấu hiệu cực mạnh của văn mẫu học đường hoặc văn AI. Người viết chuyên nghiệp chỉ dùng *"Tóm lại"* một lần duy nhất ở phần kết của một bài phân tích rất dài, hoặc không dùng từ báo hiệu mà kết bằng một nhận định sắc gọn.

### 6. Bước 6 — Hệ thống Ví dụ Đối chiếu & Cặp Chỉnh sửa Tối thiểu
- **Ví dụ A (Dương tính rõ ràng)**:
  > *"...Nhìn chung, qua những phân tích trên có thể thấy rằng chuyển đổi số vừa mang lại cơ hội lớn vừa đặt ra nhiều thách thức, đòi hỏi các doanh nghiệp phải chuẩn bị kỹ lưỡng để phát triển bền vững trong tương lai."* (Câu kết 39 chữ có độ rỗng thông tin = 100%).
- **Ví dụ B (Dương tính tinh vi)**:
  > *"...Như vậy, việc quản trị dòng tiền hiệu quả chính là yếu tố quyết định sự sống còn của doanh nghiệp trong giai đoạn suy thoái."* (Nằm ở cuối một đoạn văn mà câu đầu tiên đã nói *"Quản trị dòng tiền quyết định khả năng trụ vững của doanh nghiệp khi kinh tế suy thoái"*).
- **Ví dụ C (Hợp lệ — Kết luận tổng hợp định lượng sau chuỗi tính toán phức tạp)**:
  > *"...Như vậy, sau khi cộng gộp cả chi phí dự phòng rủi ro và chi phí vốn huy động mới, biên lợi nhuận thực tế của gói vay này chỉ còn 0,4%/năm — thấp hơn ngưỡng hòa vốn vận hành."* (Đưa ra con số tổng hợp mới sau phép tính, không phải lặp lại sáo rỗng).
- **Cặp Trước / Sau khi Humanize**:
  - Đối với Ví dụ A và Ví dụ B: **Xóa bỏ hoàn toàn câu kết đoạn** (100% deletion), để đoạn văn dừng lại ngay ở câu dữ kiện cụ thể đứng trước đó, hoặc thay bằng câu mở hướng sang đoạn tiếp theo.

### 7. Bước 7 & Bước 8 — Hệ quả, Quy tắc Humanize & Tiêu chí Kiểm thử
- **Quy tắc Humanize (Zero-Info Closure Deletion)**:
  - Thực hiện phép kiểm tra: *"Nếu xóa câu cuối đoạn bắt đầu bằng `Như vậy / Tóm lại / Nhìn chung / Do đó`, người đọc có mất đi bất kỳ dữ kiện, con số hay bước lập luận mới nào không?"*
  - `IF KHÔNG MẤT DỮ KIỆN MỚI` $\rightarrow$ **Xóa bỏ câu đó ngay lập tức**.

---

## HỒ SƠ 17: `DIS-03` — `[BỔ SUNG]` LẠM DỤNG TỪ NỐI KHUNG ĐẦU CÂU CƠ HỌC (*MECHANICAL SENTENCE-INITIAL CONNECTIVES*)

### 1. Thông tin định danh
- **ID**: `DIS-03`
- **Tên dấu hiệu**: Lạm dụng từ nối chuyển tiếp đóng khung ở đầu câu (*Overuse of Mechanical Sentence-Initial Discourse Markers*).
- **Nguồn gốc**: **Dấu hiệu bổ sung có căn cứ (`[NEW-VN-02]`)** từ Bảng đối chiếu trực quan của người dùng (*"Trong bối cảnh... $\rightarrow$ Cụ thể,... $\rightarrow$ Tuy nhiên,... $\rightarrow$ Do đó,..."*) và Khối II (`WP:AIVOCAB`: *Additionally* ở đầu câu).

### 2. Bước 1 — Định nghĩa vận hành, Phạm vi & Đơn vị quan sát
- **Cấp độ ngôn ngữ**: Liên kết hình thức giữa các câu (Formal Inter-sentential Cohesion).
- **Đơn vị quan sát**: Cụm từ đứng ở vị trí đầu câu, ngăn cách với mệnh đề chính bằng dấu phẩy (`[Connective], [Clause]`).
- **Định nghĩa vận hành**: Hiện tượng **$> 50\%$ số câu trong một đoạn văn** (hoặc $\ge 3$ câu liên tiếp) đều bắt đầu bằng một từ/cụm từ nối chuyển tiếp hiển ngôn có dấu phẩy đi kèm (như *"Cụ thể,"*, *"Hơn nữa,"*, *"Thêm vào đó,"*, *"Bên cạnh đó,"*, *"Ngoài ra,"*, *"Tuy nhiên,"*, *"Đáng chú ý là,"*, *"Do đó,"*, *"Kết quả là,"*), thay vì sử dụng liên kết ngữ nghĩa nội tại hoặc các phụ từ liên kết nằm bên trong vị ngữ của tiếng Việt.

### 3. Bước 2 — Phân tích các biểu hiện cụ thể
1. **`DIS-03a` — Chuỗi từ nối cộng thêm cơ học (*Additive Connective Stacking*)**:
   - Đoạn văn xếp chồng: Câu 2 *"Bên cạnh đó,"* $\rightarrow$ Câu 3 *"Hơn nữa,"* $\rightarrow$ Câu 4 *"Thêm vào đó,"* $\rightarrow$ Câu 5 *"Ngoài ra,"* (dịch trực tiếp từ *Furthermore, Moreover, Additionally, In addition*).
2. **`DIS-03b` — Chuỗi từ nối kịch bản 4 bước (*4-Step Scripted Connective Chain*)**:
   - Công thức cố định: *"Trong bối cảnh..."* $\rightarrow$ *"Cụ thể,"* $\rightarrow$ *"Tuy nhiên,"* $\rightarrow$ *"Do đó,"*.
3. **`DIS-03c` — Từ nối đánh giá đầu câu (*Evaluative Sentence Starters*)**:
   - *"Đáng chú ý là,"* (`Notably,`), *"Quan trọng hơn,"* (`More importantly,`), *"Thật vậy,"* (`Indeed,`), *"Không có gì ngạc nhiên khi"* (`Unsurprisingly,`).

### 4. Bước 3 — Cơ chế hình thành & Bằng chứng khoa học
- **Cơ chế hình thành & Bằng chứng**:
  - **Geng & Trotta (2024)** và **Huang et al. (2025)** chứng minh từ nối mở đầu câu *Additionally,* là một trong những từ có mức tăng trưởng đột biến cao nhất trong văn bản học thuật có sự can thiệp của LLM `[Cấp B]`.
  - Khi sinh văn bản theo từng câu, việc đặt một từ nối hiển ngôn ở vị trí token đầu tiên của câu mới (`Sentence_Start -> "Tuy nhiên," / "Hơn nữa,"`) giúp mô hình định hướng ngay phân phối xác suất của toàn bộ câu phía sau mà không cần xây dựng liên kết từ vựng tinh vi với câu trước `[Cấp C]`.

### 5. Bước 4 — Phân tích đặc điểm chuyên sâu trong Tiếng Việt
- **Sự khác biệt cốt lõi giữa Liên kết Đầu câu Tiếng Anh và Liên kết Nội câu Tiếng Việt**:
  - Tiếng Anh ưa dùng trạng từ liên kết đứng đầu câu kèm dấu phẩy (*"Additionally, S + V..."*, *"However, S + V..."*, *"Consequently, S + V..."*).
  - Ngược lại, tiếng Việt có một hệ thống **phó từ và hư từ liên kết đứng ngay trước vị ngữ (bên trong câu)** cực kỳ tinh tế (Diệp Quang Ban, 2005; Trần Ngọc Thêm, 1985) `[Cấp C]`:
    - Thay vì *"Thêm vào đó, ngân hàng đã mở rộng..."*, người Việt viết: *"Ngân hàng **cũng** mở rộng..."* hoặc *"Ngân hàng **còn** mở rộng..."* (phụ từ `cũng`, `còn` nằm sau chủ ngữ, nối mạch cực kỳ tự nhiên mà không cần cụm *"Thêm vào đó,"* ở đầu câu!).
    - Thay vì *"Tuy nhiên, mảng bảo hiểm đang sụt giảm..."*, người Việt viết: *"Mảng bảo hiểm **lại** sụt giảm..."* (phụ từ `lại` đặt trước vị ngữ tự thân đã mang nghĩa nghịch đối!).
    - Thay vì *"Do đó, các ngân hàng phải..."*, người Việt viết: *"Các ngân hàng **buộc phải / đành phải / mới phải**..."*.

### 6. Bước 5 — Mức độ đặc trưng và Khả năng chẩn đoán
- **Khả năng phân biệt**: Như phần *Ineffective indicators* của Wikipedia đã lưu ý, sự xuất hiện đơn lẻ của 1 từ nối không phải là bằng chứng AI. Nhưng khi **3–4 câu liên tiếp trong một đoạn đều mở đầu bằng `[Từ nối],`** và vắng bóng hoàn toàn các hư từ liên kết nội câu tiếng Việt (*cũng, còn, lại, vẫn, mới, đành*), giá trị chẩn đoán và nhu cầu biên tập là **Rất cao**.

### 7. Bước 6 — Hệ thống Ví dụ Đối chiếu & Cặp Chỉnh sửa Tối thiểu
- **Ví dụ A (Dương tính rõ ràng — 4 câu liên tiếp đóng đinh từ nối đầu câu)**:
  > *"Thị trường trái phiếu doanh nghiệp đã có dấu hiệu ấm lên. **Cụ thể,** giá trị phát hành riêng lẻ trong quý III tăng 25% so với quý trước. **Thêm vào đó,** nhóm ngành ngân hàng vẫn chiếm tỷ trọng phát hành lớn nhất. **Tuy nhiên,** áp lực đáo hạn vào cuối năm vẫn ở mức rất cao. **Do đó,** nhà đầu tư cá nhân cần hết sức thận trọng."*
- **Ví dụ D (Cặp Trước / Sau khi Humanize — Chuyển từ nối đầu câu vào hư từ nội câu & dấu câu)**:
  - **Sau khi Humanize**:
    > *"Thị trường trái phiếu doanh nghiệp đã bắt đầu ấm lên: giá trị phát hành riêng lẻ quý III tăng 25% so với quý trước, trong đó nhóm ngân hàng **vẫn** chiếm tỷ trọng áp đảo. Dù vậy, áp lực đáo hạn dồn vào cuối năm **còn** rất lớn, đòi hỏi nhà đầu tư cá nhân phải thẩm định kỹ dòng tiền của tổ chức phát hành."*
  - *Giải thích*: Thay *"Cụ thể,"* bằng dấu hai chấm (`:`); thay *"Thêm vào đó,"* bằng mệnh đề nối *", trong đó... vẫn..."*; thay *"Do đó,"* bằng mệnh đề tiếp nối *"...đòi hỏi..."*. Số từ nối đầu câu giảm từ 4 xuống 1, câu văn liền một mạch hơi thở.

### 8. Bước 7 & Bước 8 — Hệ quả, Quy tắc Humanize & Tiêu chí Kiểm thử
- **Quy tắc ra quyết định khi Humanize (Internalized Cohesion Rule)**:
  1. Trong một đoạn văn 4–5 câu, chỉ cho phép **tối đa 1 câu** mở đầu bằng từ nối có dấu phẩy (`[Từ nối],`).
  2. Chuyển hóa các từ nối đầu câu còn lại theo bảng ánh xạ bản ngữ tiếng Việt:
     - `"Cụ thể, [S + V]"` $\rightarrow$ Dùng dấu hai chấm `:` nối trực tiếp từ câu trước.
     - `"Thêm vào đó, / Hơn nữa, / Ngoài ra, [S + V]"` $\rightarrow$ Đổi thành `"[S] cũng / còn [V]"`.
     - `"Tuy nhiên, [S + V]"` $\rightarrow$ Đổi thành `"[S] lại / song [S] vẫn [V]"` hoặc `"Nhưng [S + V]"`.

---

## HỒ SƠ 18: `DIS-04` — MỞ ĐẦU ĐỊNH NGHĨA TIÊU ĐỀ NHƯ THỰC THỂ ĐỘC LẬP (*TITLE-AS-ENTITY LEAD*)

### 1. Thông tin định danh
- **ID**: `DIS-04`
- **Tên dấu hiệu**: Câu mở đầu định nghĩa tiêu đề danh sách hoặc chủ đề rộng như một danh từ riêng độc lập (*Leads Treating Broad Article Titles or Lists as Proper Nouns*).
- **Nguồn gốc trong danh sách gốc**: Khối II — *Leads treating Wikipedia lists or broad article titles as proper nouns*.

### 2. Bước 1 — Định nghĩa vận hành, Phạm vi & Đơn vị quan sát
- **Cấp độ ngôn ngữ**: Tổ chức câu mở đầu văn bản (Document-Initial Lead Sentence).
- **Đơn vị quan sát**: Câu đầu tiên của bài viết hoặc báo cáo.
- **Định nghĩa vận hành**: Khi tiêu đề văn bản là một cụm danh từ miêu tả phạm vi chủ đề hoặc danh sách (ví dụ: *"Danh sách các ngân hàng thương mại tại Việt Nam"*, *"Tác động của lạm phát đến tiêu dùng"*, *"Các kỳ đại hội thể thao EuroGames"*), văn bản lại bê nguyên xi cụm tiêu đề đó làm chủ ngữ của câu đầu tiên và định nghĩa nó như thể đó là một thực thể vật lý hoặc thuật ngữ chuyên ngành độc lập (*"**Danh sách các bài hát về Mexico** dùng để chỉ một tập hợp được tuyển chọn gồm các tác phẩm âm nhạc..."*, *"**Các kỳ đại hội EuroGames** là chuỗi sự kiện..."*).

### 3. Bước 2 – Bước 5 — Biểu hiện, Cơ chế & Đặc điểm trong Tiếng Việt
- **Cơ chế hình thành**: LLM được huấn luyện mạnh trên hàng triệu bài viết Wikipedia chuẩn (nơi bài viết về danh từ riêng *"Albert Einstein"* mở đầu bằng *"**Albert Einstein** là..."*). Khi gặp một tiêu đề dạng chủ đề tổng hợp hoặc danh sách, mô hình máy móc áp dụng công thức `"[Tiêu đề bài viết] là / đề cập đến / bao gồm..."` `[Cấp B]`.
- **Biểu hiện trong Tiếng Việt**:
  - Tiêu đề: *"Thực trạng nợ xấu của các ngân hàng thương mại Việt Nam năm 2026"*.
  - Câu mở đầu AI: *"**Thực trạng nợ xấu của các ngân hàng thương mại Việt Nam năm 2026** đề cập đến bức tranh tổng thể về các khoản vay quá hạn trong hệ thống tín dụng..."* (Ngô nghê và thừa thãi).
  - Câu mở đầu của con người tự nhiên: *"Bước sang năm 2026, tỷ lệ nợ xấu nội bảng của các ngân hàng thương mại Việt Nam bắt đầu phân hóa mạnh giữa nhóm quốc doanh và nhóm tư nhân..."*

### 4. Bước 6 – Bước 8 — Ví dụ Đối chiếu & Quy tắc Humanize
- **Ví dụ A (Dương tính rõ ràng)**:
  > *"**Các giải pháp phát triển tài chính xanh tại Việt Nam** là tập hợp những chính sách và công cụ tài chính nhằm hướng dòng vốn vào các dự án bảo vệ môi trường."*
- **Ví dụ D (Sau khi Humanize)**:
  > *"Để hướng dòng vốn vào các dự án bảo vệ môi trường, thị trường tài chính Việt Nam đang triển khai đồng thời nhiều công cụ tín dụng xanh và trái phiếu xanh."*
- **Quy tắc Humanize**: Nếu tiêu đề bài viết là một cụm danh từ phức mô tả chủ đề/danh sách (không phải tên riêng hay thuật ngữ cần định nghĩa), **cấm lặp lại nguyên cụm tiêu đề làm chủ ngữ đi kèm hệ từ `"là / đề cập đến"` ở câu đầu tiên**; hãy đi thẳng vào mệnh đề hành động hoặc dữ kiện trung tâm của chủ đề đó.
