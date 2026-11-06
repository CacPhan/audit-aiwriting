# HỒ SƠ NGHIÊN CỨU CHUYÊN SÂU — NHÓM 4: LẬP LUẬN, MẬT ĐỘ THÔNG TIN, QUY CHIẾU VÀ NGỮ DỤNG HỌC (`ARG` & `PRG`)
**(Giai đoạn 3, Giai đoạn 4, Đầu ra B & C — Các hồ sơ `ARG-01` đến `PRG-02`)**

---

## HỒ SƠ 19: `ARG-01` — TRỌNG SỐ LUẬN ĐIỂM PHẲNG & MẬT ĐỘ THÔNG TIN ĐỒNG ĐỀU (*UNIFORM INFORMATION DENSITY & FLAT EPISTEMIC WEIGHT*)

### 1. Thông tin định danh
- **ID**: `ARG-01`
- **Tên dấu hiệu**: Trọng số luận điểm phẳng, phân bổ dung lượng chia đều cơ học và bào mòn chi tiết đặc thù (*Flat Epistemic Weight, Uniform Resource Allocation & Regression to the Mean*).
- **Nguồn gốc trong danh sách gốc**: Khối I — Mục 4 (*Trọng số luận điểm phẳng và Mật độ thông tin đồng đều [Uniform Information Density]*) & Khối II — Phần mở đầu *Content* (`WP:AI-ISM`, `WP:LLMISM`: *Statistical regression to the mean / smoothing over of specific facts into generic statements*).

### 2. Bước 1 — Định nghĩa vận hành, Phạm vi & Đơn vị quan sát
- **Cấp độ ngôn ngữ**: Cấu trúc lập luận toàn văn bản & Lý thuyết thông tin diễn ngôn (Macro-Argumentation & Information-Theoretic Discourse level).
- **Đơn vị quan sát**: Tỷ lệ phân bổ dung lượng (số chữ/số đoạn) giữa các luận điểm $P_1, P_2, \dots, P_k$ trong cùng một mục và mật độ thực thể cụ thể (Named Entities, số liệu lẻ, mốc thời gian, ngoại lệ) trên mỗi 100 chữ.
- **Định nghĩa vận hành**: Hiện tượng một văn bản phân tích nhiều nguyên nhân, giải pháp hoặc khía cạnh của một vấn đề nhưng:
  1. **Chia đều dung lượng cơ học (*Equal Budget Partitioning*)**: Mỗi luận điểm $P_i$ được cấp phát một lượng chữ gần như bằng nhau (ví dụ: 4 nguyên nhân $\rightarrow$ 4 đoạn văn, mỗi đoạn 80–90 chữ; độ lệch chuẩn dung lượng giữa các luận điểm $< 15\%$), bất chấp trong thực tế có một nguyên nhân cốt lõi chiếm 60–70% tác động.
  2. **Làm phẳng độ nhám dữ kiện (*Granularity Smoothing / Regression to the Mean*)**: Thay thế các chi tiết đặc thù, góc cạnh, có xác suất xuất hiện thấp (như *"người phát minh ra thiết bị nối toa tàu đầu tiên"*, *"nợ xấu nhóm 5 tăng vọt ở phân khúc bất động sản nghỉ dưỡng tại Bình Thuận quý III/2025"*) bằng các nhận định khái quát hóa mức trung bình có xác suất cao (*"một người tiên phong cách mạng trong ngành công nghiệp"*, *"nợ xấu gia tăng ở một số phân khúc tiềm ẩn rủi ro cao"*).

### 3. Bước 2 — Phân tích các biểu hiện cụ thể (Sub-manifestations)
1. **`ARG-01a` — Bình quân chủ nghĩa về dung lượng luận điểm (*Egalitarian Point Allocation*)**:
   - Liệt kê 4–5 luận điểm, mỗi luận điểm 1 đoạn văn dài bằng nhau, không có luận điểm chính (primary driver) và luận điểm phụ (secondary factor).
2. **`ARG-01b` — Phẳng hóa từ vựng đánh giá tầm quan trọng (*Flat Importance Modality*)**:
   - Luận điểm 1 được gọi là *"đóng vai trò then chốt"*, luận điểm 2 là *"yếu tố cốt lõi"*, luận điểm 3 là *"vô cùng quan trọng"*, luận điểm 4 là *"không thể thiếu"* $\rightarrow$ Khi mọi thứ đều là "trọng tâm", không còn gì là trọng tâm.
3. **`ARG-01c` — Bay ở cùng một độ cao trừu tượng (*Constant High-Altitude Abstraction*)**:
   - Văn bản duy trì mức độ khái quát vĩ mô từ đầu đến cuối, thiếu sự chuyển dịch độ phóng đại (zoom-in / zoom-out) từ nhận định tổng quát xuống một trường hợp điển hình (case study), một con số lẻ (ví dụ `14,7%` thay vì *"đáng kể"*), hoặc một điều khoản văn bản pháp lý cụ thể.

### 4. Bước 3 — Cơ chế hình thành & Bằng chứng khoa học
- **Cơ chế hình thành**:
  1. **Giả thuyết Mật độ Thông tin Đồng đều (*Uniform Information Density – UID*) trong mô hình sinh ngôn ngữ**: Khởi nguồn từ nghiên cứu của **Levy & Jaeger (2007, *NIPS*)** về giao tiếp con người và được **Meister et al. (2023, *TACL*, *"Locally Typical Sampling"*)** chứng minh trong bối cảnh LLM: Các thuật toán giải mã hiện đại tối ưu hóa sao cho lượng thông tin (surprisal / negative log-probability $-\log P(w_t | w_{<t})$) ở mỗi bước sinh luôn bám sát mức entropy kỳ vọng trung bình của mô hình. Những dữ kiện quá cụ thể, hiếm gặp có surprisal rất cao (xác suất thấp) nên bị loại bỏ (smoothed out) trong quá trình lấy mẫu, nhường chỗ cho các mệnh đề khái quát có xác suất trung bình cao `[Cấp B]`.
  2. **Thiếu mô hình nhân quả miền chuyên sâu (Lack of Domain Causal Weighting)**: Khi không được cung cấp dữ liệu trọng số thực nghiệm trong prompt, LLM coi các mục trong một danh sách kiến thức có trọng số ngang nhau để đảm bảo "tính toàn diện bề mặt" (surface comprehensiveness) `[Cấp C]`.

### 5. Bước 4 — Phân tích đặc điểm chuyên sâu trong Tiếng Việt
- Trong văn nghị luận và báo cáo phân tích chuyên sâu tiếng Việt, "độ nhám" (texture) của văn bản được tạo ra từ:
  - **Sự phân tầng chính – phụ rõ rệt**: Người viết dùng các cụm phân cấp trọng số rất dứt khoát (*"Nguyên nhân gốc rễ nằm ở..."*, *"Nút thắt lớn nhất là..."*, *"Còn các yếu tố như X, Y thực chất chỉ là hệ quả phái sinh..."*).
  - **Sự đan cài giữa khái quát và chi tiết đời thực**: Đang bàn về vĩ mô liền hạ xuống một ví dụ sát sườn (*"Chẳng hạn, ngay sau khi Thông tư 02 hết hiệu lực..."*).
- Văn AI tiếng Việt trải đều một lớp sương mù từ vựng Hán–Việt ở mọi đoạn (*các tổ chức, các bên liên quan, nhiều thách thức, một số hạn chế*), khiến người đọc đọc xong 1.000 chữ vẫn không nắm được đâu là nút thắt số 1.

### 6. Bước 5 — Mức độ đặc trưng và Khả năng chẩn đoán
- **Khả năng phân biệt**: **Rất cao** khi đánh giá toàn văn bản ($\ge 400$ chữ). Một bài viết chia 4–5 mục có số chữ chênh nhau không quá 10 chữ và hoàn toàn không có phân cấp luận điểm chính/phụ gần như chắc chắn là đầu ra thô của LLM hoặc đề cương tóm tắt sơ sài.

### 7. Bước 6 — Hệ thống Ví dụ Đối chiếu & Cặp Chỉnh sửa Tối thiểu
- **Ví dụ A (Dương tính rõ ràng — Chia đều 3 nguyên nhân phẳng lặng)**:
  > *"Nợ xấu ngân hàng tăng do ba nguyên nhân chính. Thứ nhất, sự suy giảm của nền kinh tế vĩ mô khiến thu nhập của người vay sụt giảm, làm ảnh hưởng đến khả năng trả nợ đúng hạn (34 chữ). Thứ hai, thị trường bất động sản trầm lắng khiến việc xử lý tài sản đảm bảo gặp nhiều khó khăn và kéo dài thời gian thu hồi vốn (33 chữ). Thứ ba, công tác thẩm định tín dụng tại một số đơn vị còn chưa chặt chẽ, dẫn đến việc cấp vốn cho các khách hàng tiềm ẩn rủi ro (34 chữ)."*
- **Ví dụ D (Cặp Trước / Sau khi Humanize — Tạo phân cấp trọng số 65% – 35% và tăng độ nhám dữ kiện)**:
  - **Sau khi Humanize**:
    > *"Đợt tăng nợ xấu lần này chủ yếu bắt nguồn từ sự đóng băng của thị trường bất động sản và sự cố trái phiếu doanh nghiệp giai đoạn 2022–2024: khi hơn 70% tài sản thế chấp tại các ngân hàng là bất động sản nhưng thanh khoản thị trường tắc nghẽn và vướng mắc pháp lý chưa tháo gỡ xong, ngân hàng dù có thu giữ tài sản cũng không thể phát mãi để thu hồi nợ. Hai yếu tố còn lại — gồm sức cầu tiêu dùng suy yếu làm giảm thu nhập người vay cá nhân và việc nới lỏng tiêu chuẩn thẩm định ở giai đoạn tiền rẻ trước đó — đóng vai trò cộng hưởng, đẩy nợ nhóm 3 và nhóm 4 chuyển nhanh sang nợ có khả năng mất vốn."*
  - *Giải thích*: Xác lập rõ nguyên nhân số 1 (bất động sản & tài sản thế chấp chiếm 65% dung lượng câu chữ và có cơ chế nghiệp vụ cụ thể), còn hai nguyên nhân phụ được gom gọn vào câu thứ hai như "yếu tố cộng hưởng".

### 8. Bước 7 & Bước 8 — Hệ quả, Quy tắc Humanize & Tiêu chí Kiểm thử
- **Hệ quả**: Làm bài viết nông cạn, thiếu sức thuyết phục với người đọc có chuyên môn; đánh đồng nguyên nhân cốt lõi với triệu chứng phụ.
- **Quy tắc ra quyết định khi Humanize (Hierarchy & Granularity Rule)**:
  1. **Quy tắc Phân bổ Trọng số 60/40 (Pareto Allocation)**: Khi có $\ge 3$ luận điểm, bắt buộc xác định 1–2 luận điểm cốt lõi để dành 60–70% dung lượng phân tích sâu cơ chế; các luận điểm phụ còn lại gom chung vào 1 đoạn ngắn (30–40% dung lượng).
  2. **Quy tắc Bảo toàn Độ nhám (Anti-Smoothing Safeguard)**: Khi biên tập lại văn bản của người dùng, **cấm tuyệt đối** việc tóm tắt các con số lẻ, tên riêng, mã thông tư/nghị định hoặc chi tiết kỹ thuật thành các cụm từ chung chung (*"nhiều quy định"*, *"một số khu vực"*).

---

## HỒ SƠ 20: `ARG-02` — ĐƯỜNG CONG LẬP LUẬN KIỂU "CON LẮC AN TOÀN" (*PENDULUM HEDGING*)

### 1. Thông tin định danh
- **ID**: `ARG-02`
- **Tên dấu hiệu**: Đường cong lập luận kiểu "Con lắc an toàn" (*Pendulum Hedging: Khen $\rightarrow$ Chê nhẹ $\rightarrow$ Hòa cả làng*).
- **Nguồn gốc trong danh sách gốc**: Khối I — Mục 5 (*Đường cong lập luận kiểu "Con lắc an toàn" [Pendulum Hedging]*).

### 2. Bước 1 — Định nghĩa vận hành, Phạm vi & Đơn vị quan sát
- **Cấp độ ngôn ngữ**: Cấu trúc lập luận & Lập trường nhận thức luận (Argumentative Trajectory & Epistemic Stance).
- **Đơn vị quan sát**: Đoạn văn nghị luận hoặc mục phân tích chính sách/chiến lược.
- **Định nghĩa vận hành**: Hiện tượng mọi đoạn văn hoặc mọi mục phân tích trong bài đều lặp lại cùng một quỹ đạo tư duy 3 pha cố định:
  - **Pha 1 (Khẳng định mặt tích cực – Thesis)**: *"Một mặt / Không thể phủ nhận rằng [X] mang lại nhiều lợi ích to lớn như A, B..."*
  - **Pha 2 (Chỉ ra rào cản/rủi ro một cách trung tính – Antithesis)**: *"Tuy nhiên / Bên cạnh đó, [X] cũng đối mặt với không ít thách thức và hạn chế như C, D..."*
  - **Pha 3 (Hòa cả làng / Kêu gọi kết hợp đồng bộ – Hollow Synthesis)**: *"Do đó, để phát huy tối đa hiệu quả, cần có sự phối hợp đồng bộ và hài hòa giữa [Yếu tố 1] và [Yếu tố 2]."*

### 3. Bước 2 — Phân tích các biểu hiện cụ thể
1. **`ARG-02a` — Con lắc nội đoạn (*Intra-paragraph Pendulum*)**:
   - Trong 4 câu của một đoạn văn đóng hộp (`DIS-01`), câu 1–2 khen, câu 3 chê nhẹ (`Tuy nhiên...`), câu 4 hòa giải (`Do đó cần kết hợp hài hòa...`).
2. **`ARG-02b` — Con lắc cấp mục (*Section-level Pros-and-Cons Symmetry*)**:
   - Bất kỳ chủ đề nào cũng bị chia thành *"Lợi ích / Cơ hội"* và *"Thách thức / Rủi ro"* cân xứng 50–50, rồi kết thúc bằng lời khuyên *"cần cân bằng giữa lợi ích và rủi ro"*.
3. **`ARG-02c` — Giải pháp "Đồng bộ – Toàn diện – Hài hòa" (*The Hollow Synthesis Cliché*)**:
   - Thay vì chỉ ra đánh đổi thực tế (trade-off: muốn được A thì phải chấp nhận hy sinh B), AI luôn kết luận bằng một giải pháp không tưởng là *"vừa đảm bảo A tối đa, vừa giữ vững B toàn diện thông qua sự phối hợp đồng bộ"*.

### 4. Bước 3 — Cơ chế hình thành & Bằng chứng khoa học
- **Cơ chế hình thành**:
  1. **Huấn luyện RLHF tránh gây tranh cãi (Neutrality & Sycophancy Alignment)**: **Ouyang et al. (2022)** và **Perez et al. (2023)** chỉ ra rằng quy trình RLHF phạt nặng các câu trả lời có vẻ thiên lệch một chiều trên các vấn đề mở. Để tối đa hóa điểm thưởng (reward model score) từ những người đánh giá có quan điểm khác nhau, chính sách tối ưu (optimal policy) của LLM là luôn trình bày cả hai mặt rồi kết thúc bằng một câu dung hòa không ai bắt bẻ được `[Cấp B]`.
  2. **Sự vắng mặt của Lý thuyết Đánh đổi (Absence of Economic/Practical Trade-off Commitment)**: Mô hình ngôn ngữ không phải chịu trách nhiệm thực thi quyết định, nên nó luôn chọn giải pháp ngôn từ "cả hai cùng thắng" (*kết hợp hài hòa, phối hợp đồng bộ*) thay vì nêu rõ chi phí cơ hội `[Cấp C]`.

### 5. Bước 4 — Phân tích đặc điểm chuyên sâu trong Tiếng Việt
- Trong tiếng Việt, "con lắc an toàn" cộng hưởng mạnh với thói quen viết văn mẫu nghị luận phổ thông (*"Một mặt... Mặt khác... Tóm lại chúng ta cần kết hợp hài hòa..."*) và văn phong báo cáo tổng kết hành chính (*"Bên cạnh những kết quả đạt được, vẫn còn một số tồn tại hạn chế... Do đó trong thời gian tới cần triển khai đồng bộ các giải pháp..."*).
- Tuy nhiên, trong văn bản phân tích học thuật, tài chính, kỹ thuật hoặc quản trị chuyên sâu, việc lặp lại điệp khúc *"cần có sự phối hợp đồng bộ giữa các bên liên quan để đạt hiệu quả tối ưu"* ở cuối mọi đoạn làm triệt tiêu hoàn toàn giá trị tư vấn của văn bản.

### 6. Bước 5 — Mức độ đặc trưng và Khả năng chẩn đoán
- **Khả năng phân biệt**: **Rất cao** khi quỹ đạo `Khen -> Tuy nhiên (Chê) -> Do đó cần phối hợp đồng bộ` lặp lại ở **$\ge 2$ đoạn/mục liên tiếp**.

### 7. Bước 6 — Hệ thống Ví dụ Đối chiếu & Cặp Chỉnh sửa Tối thiểu
- **Ví dụ A (Dương tính rõ ràng)**:
  > *"Chính sách nới lỏng tín dụng mang lại động lực quan trọng giúp doanh nghiệp phục hồi sản xuất và thúc đẩy tăng trưởng kinh tế. **Tuy nhiên**, việc bơm vốn quá nhanh cũng tiềm ẩn nguy cơ gia tăng lạm phát và phát sinh nợ xấu trong tương lai. **Do đó**, Ngân hàng Nhà nước cần có sự điều hành linh hoạt, phối hợp đồng bộ và hài hòa giữa mục tiêu tăng trưởng và kiểm soát rủi ro để đảm bảo sự phát triển bền vững."*
- **Ví dụ C (Hợp lệ — Khi nêu rõ cơ chế điều kiện biên cụ thể chứ không "hòa cả làng")**:
  > *"Nới lỏng tín dụng giúp giải tỏa cơn khát vốn ngắn hạn cho doanh nghiệp sản xuất, nhưng nếu tốc độ tăng trưởng cung tiền M2 vượt ngưỡng 14%/năm trong khi đầu tư công giải ngân chậm, dòng tiền rẻ sẽ chảy sang đầu cơ tài sản thay vì vào khu vực sản xuất."*
- **Ví dụ D (Cặp Trước / Sau khi Humanize Ví dụ A — Thay thế lời khuyên "hòa cả làng" bằng điều kiện đánh đổi thực chất)**:
  - **Sau khi Humanize**:
    > *"Nới lỏng tín dụng giúp doanh nghiệp sớm có vốn quay vòng sản xuất, nhưng cái giá phải trả là áp lực lạm phát và rủi ro nợ xấu sẽ trễ pha khoảng 12–18 tháng. Vì không thể vừa bơm tiền mạnh vừa giữ lạm phát thấp cùng lúc, bài toán điều hành hiện nay buộc phải chấp nhận ưu tiên phân bổ hạn mức tín dụng cho nhóm sản xuất – xuất khẩu và tiếp tục kiểm soát chặt dòng vốn vào bất động sản thứ cấp."*

### 8. Bước 7 & Bước 8 — Hệ quả, Quy tắc Humanize & Tiêu chí Kiểm thử
- **Hệ quả**: Làm người đọc đoán trước được mọi câu tiếp theo (predictability fatigue); biến phân tích chuyên môn thành lời khuyên sáo rỗng vô thưởng vô phạt.
- **Quy tắc ra quyết định khi Humanize (Anti-Pendulum & Trade-off Rule)**:
  1. **Xóa câu kết "Hòa cả làng"**: Cắt bỏ các mệnh đề kết kiểu *"cần phối hợp đồng bộ, hài hòa giữa A và B để phát triển bền vững"*.
  2. **Biến đối lập chung chung thành Điều kiện biên (Boundary Condition)**: Thay vì viết *"A tốt. Tuy nhiên A có rủi ro B. Do đó cần hài hòa"*, hãy cấu trúc lại thành: **"A phát huy tác dụng khi [Điều kiện X], nhưng sẽ dẫn đến rủi ro B nếu vượt quá [Ngưỡng Y]"** (nếu dữ kiện có sẵn trong văn bản), hoặc kết thúc đoạn ngay tại việc chỉ ra bài toán đánh đổi (trade-off) thực tế.

---

## HỒ SƠ 21: `ARG-03` — PHÓNG ĐẠI TẦM QUAN TRỌNG, DI SẢN VÀ XU HƯỚNG VĨ MÔ (`WP:AILEGACY` / `WP:AITREND`)

### 1. Thông tin định danh
- **ID**: `ARG-03`
- **Tên dấu hiệu**: Nhấn mạnh quá mức tầm quan trọng, di sản lâu dài và sự phản ánh "xu hướng rộng lớn hơn" (*Undue Emphasis on Significance, Legacy, and Broader Trends*).
- **Nguồn gốc trong danh sách gốc**: Khối II — `WP:AILEGACY`, `WP:AITREND`.

### 2. Bước 1 — Định nghĩa vận hành, Phạm vi & Đơn vị quan sát
- **Cấp độ ngôn ngữ**: Lập luận – Đánh giá ngữ dụng (Rhetorical Evaluation & Framing).
- **Đơn vị quan sát**: Câu hoặc đoạn văn bình luận về tầm vóc/ý nghĩa của chủ thể.
- **Định nghĩa vận hành**: Hiện tượng văn bản tự động thổi phồng tầm quan trọng của những sự việc, dữ kiện hoặc chủ thể rất bình thường (thậm chí là số liệu dân số, tên gọi địa phương, một loài cá nhỏ, hoặc một quyết định hành chính thường nhật) bằng cách gắn chúng vào các đại tự sự như *"đánh dấu một bước ngoặt lịch sử"*, *"là minh chứng sống động cho sức sống bền bỉ"*, *"phản ánh xu hướng rộng lớn hơn của khu vực"*, *"để lại dấu ấn không thể phai mờ"*, *"đặt nền móng cho..."*, hoặc tự bình luận rằng *"sự phân biệt này rất quan trọng vì..."* (`distinction matters because...`).

### 3. Bước 2 — Phân tích các biểu hiện cụ thể
1. **`ARG-03a` — Gắn kết cưỡng ép với "Xu hướng rộng lớn hơn" (`reflects broader trends`)**:
   - Một cửa hàng mở thêm chi nhánh cũng được bình luận là *"phản ánh xu hướng chuyển dịch vĩ mô của nền kinh tế bán lẻ khu vực"*.
2. **`ARG-03b` — Phóng đại di sản và bước ngoặt (`indelible mark`, `key turning point`, `testament to`)**:
   - *"Sự kiện này đã để lại dấu ấn không thể phai mờ"*, *"đứng như một minh chứng cho tinh thần bất khuất"*.
3. **`ARG-03c` — Rào đón tầm quan trọng ngược (*Reverse-Hedging Importance*)**:
   - Thừa nhận đối tượng nhỏ bé rồi vẫn cố tình ca ngợi tầm vóc: *"Mặc dù chỉ là một con tem hành chính nhỏ (hoặc dữ liệu dân số khiêm tốn), nó vẫn đóng vai trò thiết yếu trong việc phản ánh..."*.
4. **`ARG-03d` — Hội chứng "Bảo tồn sinh thái" trong chủ đề sinh học/môi trường**:
   - Khi viết về bất kỳ loài động/thực vật nào (dù chưa có dữ liệu bảo tồn), AI luôn tự thêm đoạn nhấn mạnh *"vai trò quan trọng trong việc duy trì cân bằng hệ sinh thái địa phương và sự cần thiết của các nỗ lực nghiên cứu, bảo tồn"*.

### 4. Bước 3 — Cơ chế hình thành & Bằng chứng khoa học
- **Cơ chế hình thành & Bằng chứng**:
  - **Juzek & Ward (2024/2025)**, **Sun et al. (2024/2025)** (*cite_note-sun-13*), và **The Chronicle of Higher Education (2024)**: Chỉ ra rằng các mô hình (đặc biệt là ChatGPT và Grok) được tinh chỉnh để trả lời câu hỏi theo hướng "giúp người đọc hiểu tại sao chủ đề này đáng quan tâm" (*Why it matters* framing). Khi áp dụng vào mọi chủ đề bất kể lớn nhỏ, cơ chế này tạo ra sự lạm phát ý nghĩa (significance inflation) `[Cấp B]`.

### 5. Bước 4 – Bước 8 — Đặc điểm Tiếng Việt, Ví dụ & Quy tắc Humanize
- **Biểu hiện trong Tiếng Việt**: Lạm dụng các cụm *"là minh chứng rõ nét cho..."*, *"đánh dấu một cột mốc quan trọng trong hành trình..."*, *"phản ánh bức tranh rộng lớn hơn về..."*, *"góp phần định hình tương lai của..."*.
- **Ví dụ A (Dương tính rõ ràng)**:
  > *"Mặc dù số liệu thống kê dân số của thị trấn năm 2020 khá khiêm tốn, những con số này **đóng vai trò là minh chứng quan trọng phản ánh xu hướng chuyển dịch nhân khẩu học rộng lớn hơn của toàn vùng, đặt nền móng cho việc hoạch định chính sách phát triển bền vững trong tương lai**."*
- **Ví dụ C (Hợp lệ)**:
  > Sự kiện lịch sử thực sự là bước ngoặt có dẫn chứng học thuật: *"Sự sụp đổ của Lehman Brothers ngày 15/9/2008 đã châm ngòi cho cuộc khủng hoảng tài chính toàn cầu 2008–2009."*
- **Cặp Trước / Sau khi Humanize Ví dụ A**:
  - **Sau khi Humanize**: *"Theo thống kê năm 2020, dân số của thị trấn đạt 14.200 người, giảm 3% so với năm 2010 do lao động trẻ di cư về các khu công nghiệp lân cận."* (Chỉ giữ dữ kiện nhân khẩu học thực tế, cắt bỏ toàn bộ phần thổi phồng ý nghĩa vĩ mô).
- **Quy tắc Humanize**: Xóa bỏ mọi mệnh đề bình luận kiểu *"phản ánh xu hướng rộng lớn hơn"*, *"là minh chứng cho"*, *"để lại dấu ấn không phai mờ"* trừ khi bản thân câu đó đi kèm số liệu so sánh vĩ mô hoặc trích dẫn trực tiếp từ một công trình nghiên cứu đánh giá tầm ảnh hưởng đó.

---

## HỒ SƠ 22: `ARG-04` — KẾT LUẬN ĐÓNG KHUNG "THÁCH THỨC & TRIỂN VỌNG" VÀ ĐỀ MỤC ĐỐI XỨNG (`WP:FACESCHALLENGES`)

### 1. Thông tin định danh
- **ID**: `ARG-04`
- **Tên dấu hiệu**: Kết luận đóng khung kiểu đề cương về "Thách thức và Triển vọng tương lai" & Tiêu đề mục dạng `"X và Y"` (*Outline-Like Conclusions on Challenges/Future Prospects & Canned Section Headers*).
- **Nguồn gốc trong danh sách gốc**: Khối II — `WP:FACESCHALLENGES` (*Outline-like conclusions about challenges and future prospects*) & *"Awards and recognition" section*.

### 2. Bước 1 – Bước 5 — Định nghĩa, Cơ chế & Đặc điểm trong Tiếng Việt
- **Định nghĩa vận hành**:
  1. Ở phần cuối bài viết, văn bản tự động sinh ra một mục hoặc đoạn kết theo đúng khuôn mẫu: **"Mặc dù đạt được những [thành tựu/lợi thế tích cực], [Chủ thể] vẫn phải đối mặt với không ít thách thức như [A, B, C]... Tuy nhiên, với [các sáng kiến hiện tại / tiềm năng sẵn có], triển vọng tương lai của [Chủ thể] vẫn rất hứa hẹn."**
  2. Hệ thống tiêu đề mục (headings) bị chia theo khuôn kép đối xứng `"X và Y"`, đặc biệt là các tiêu đề rập khuôn: *"Thách thức và Cơ hội"*, *"Thách thức và Triển vọng tương lai"*, *"Giải thưởng và Sự ghi nhận"* (*Awards and recognition*), *"Tác động và Di sản"* (*Impact and legacy*).
- **Bằng chứng ủng hộ**: **Russell et al. (2025)** (*cite_note-Russell-2*) xác định cấu trúc kết bài *"Despite its [positive words], [subject] faces several challenges..."* là một trong những chỉ báo cấu trúc đáng tin cậy nhất được các chuyên gia nhận diện văn bản AI sử dụng `[Cấp B]`.

### 3. Bước 6 – Bước 8 — Ví dụ Đối chiếu & Quy tắc Humanize
- **Ví dụ A (Dương tính rõ ràng)**:
  > **== Thách thức và Triển vọng tương lai ==**
  > *"Mặc dù đạt được tốc độ tăng trưởng ấn tượng, ngành logistics Việt Nam vẫn đối mặt với nhiều thách thức như chi phí vận tải cao, hạ tầng chưa đồng bộ và thiếu hụt nhân lực chất lượng cao. Tuy nhiên, với sự đầu tư mạnh mẽ vào các dự án cao tốc và chuyển đổi số, triển vọng tương lai của ngành được đánh giá là vô cùng tươi sáng."*
- **Ví dụ D (Sau khi Humanize)**:
  > **== Nút thắt chi phí và lộ trình hạ tầng giai đoạn 2026–2030 ==**
  > *"Chi phí logistics tại Việt Nam hiện vẫn chiếm khoảng 16,5% GDP — cao hơn mức trung bình 11% của thế giới — chủ yếu do tình trạng vận tải đường bộ gánh tới 75% sản lượng hàng hóa nhưng thiếu kết nối đường sắt với cảng biển. Điểm nghẽn này chỉ có thể hạ nhiệt từ sau năm 2027 khi các tuyến cao tốc trục dọc và luồng hàng hải Cái Mép – Thị Vải hoàn tất nâng cấp."*
- **Quy tắc Humanize**:
  1. Đổi các tiêu đề mục sáo rỗng (*"Thách thức và Triển vọng"*, *"Tác động và Di sản"*) thành **tiêu đề nêu thẳng vấn đề trọng tâm hoặc con số/giai đoạn cụ thể**.
  2. Phá bỏ mẫu câu mở mục *"Mặc dù đạt được X, Y vẫn đối mặt với nhiều thách thức..."*; đi thẳng vào phân tích điểm nghẽn cụ thể và lộ trình thực tế.

---

## HỒ SƠ 23: `PRG-01` — QUY CHIẾU NGUỒN MƠ HỒ & NHẤN MẠNH RẬP KHUÔN ĐỘ PHỦ TRUYỀN THÔNG (`WP:AIWEASEL` / `WP:OVERATTRIBUTION`)

### 1. Thông tin định danh
- **ID**: `PRG-01`
- **Tên dấu hiệu**: Quy chiếu nguồn mơ hồ (*Weasel Wording*), khái quát hóa quá mức ý kiến và nhấn mạnh rập khuôn về loại hình nguồn/độ phủ truyền thông (*Canned Emphasis on Notability, Attribution & Media Coverage*).
- **Nguồn gốc trong danh sách gốc**: Khối II — `WP:AIWEASEL` (*Vague attributions and overgeneralization of opinions*) & `WP:OVERATTRIBUTION` / `WP:AIATTR` (*Canned emphasis on notability, attribution, and media coverage*).

### 2. Bước 1 — Định nghĩa vận hành, Phạm vi & Đơn vị quan sát
- **Cấp độ ngôn ngữ**: Ngữ dụng học trích dẫn & Minh chứng học thuật (Pragmatic Attribution & Evidentiality).
- **Đơn vị quan sát**: Cụm từ dẫn nguồn trong câu (*in-text attribution*).
- **Định nghĩa vận hành**: Bao gồm 2 biểu hiện có cùng bản chất là **dùng vỏ bọc nguồn tin để hợp thức hóa nhận định chung chung**:
  1. **`PRG-01a` — Quy chiếu nặc danh đám đông (`WP:AIWEASEL`)**: Quy gán các nhận định cho những chủ thể mơ hồ không thể kiểm chứng như *"Các chuyên gia cho rằng..."*, *"Nhiều nhà quan sát nhận định..."*, *"Các báo cáo ngành chỉ ra rằng..."*, *"Một số nhà phê bình lập luận..."*, hoặc phóng đại 1 nguồn duy nhất thành số nhiều (*"nhiều học giả..."* nhưng chỉ trích dẫn 1 bài).
  2. **`PRG-01b` — Nhấn mạnh rập khuôn về phân loại nguồn tin & truyền thông (`WP:OVERATTRIBUTION` — Đặc trưng mạnh của LLM 2025–2026)**: Thay vì tóm tắt nội dung thực chất mà nguồn tin viết, văn bản lại mô tả **đặc tính thể loại của chính nguồn tin đó** bằng các cụm từ rập khuôn: *"đã nhận được sự đưa tin độc lập từ các cơ quan truyền thông địa phương, khu vực và quốc gia"* (`independent coverage from local, regional, and national media outlets`), *"được giới thiệu trên các ấn phẩm chuyên ngành công nghệ và kinh doanh"* (`featured in trade publications and business outlets`), *"duy trì sự hiện diện tích cực trên mạng xã hội"* (`maintains an active social media presence`).

### 3. Bước 2 – Bước 5 — Cơ chế hình thành & Đặc điểm trong Tiếng Việt
- **Cơ chế hình thành**:
  - Đối với `PRG-01a`: Khi không có nguồn cụ thể trong ngữ cảnh, LLM sinh các cụm *"Theo các chuyên gia..."* để tạo vẻ khách quan bề mặt `[Cấp B]`.
  - Đối với `PRG-01b`: Khi các mô hình thế hệ 2025–2026 (có tích hợp RAG / Web Search) được yêu cầu viết bài chứng minh độ nổi bật hoặc tổng hợp hồ sơ, mô hình **đánh sập ranh giới (context collapse)** giữa *tiêu chí đánh giá nguồn* (ví dụ quy định của Wikipedia yêu cầu "nguồn độc lập, báo chí chuyên ngành") và *nội dung bài viết*, nên bê nguyên các thuật ngữ phân loại nguồn (*"các ấn phẩm thương mại chuyên ngành"*, *"báo chí độc lập"*) vào trong câu văn xuôi `[Cấp B]`.
- **Biểu hiện trong Tiếng Việt**:
  - *"Theo nhiều chuyên gia kinh tế..."*, *"Giới quan sát thị trường đánh giá..."*, *"Các báo cáo phân tích trong ngành chỉ ra rằng..."*.
  - *"Dự án đã thu hút sự chú ý rộng rãi từ các cơ quan truyền thông chính thống và các ấn phẩm chuyên ngành tài chính"*, *"Ông cũng duy trì sự hiện diện tích cực trên các nền tảng mạng xã hội"*.

### 4. Bước 6 – Bước 8 — Ví dụ Đối chiếu & Quy tắc Humanize
- **Ví dụ A (Dương tính rõ ràng)**:
  > *"Hoạt động của công ty đã được ghi nhận thông qua các bài viết độc lập trên các ấn phẩm thương mại chuyên ngành và các cơ quan truyền thông quốc gia. Các nhà phân tích trong ngành thường trích dẫn mô hình của công ty như một ví dụ điển hình về đổi mới sáng tạo."*
- **Ví dụ C (Hợp lệ)**:
  > *"Theo Báo cáo Ổn định Tài chính tháng 10/2026 của Quỹ Tiền tệ Quốc tế (IMF), tỷ lệ đòn bẩy của khu vực phi ngân hàng đã tăng thêm 4,2 điểm phần trăm."* (Nêu đích danh tổ chức, tên báo cáo, thời điểm và con số cụ thể).
- **Quy tắc ra quyết định khi Humanize**:
  1. **Nếu có nguồn cụ thể trong văn bản/dữ liệu đầu vào**: Thay thế ngay *"Các chuyên gia / Các ấn phẩm chuyên ngành"* bằng **tên riêng của tác giả, tổ chức phát hành hoặc tờ báo** và đi thẳng vào dữ kiện mà nguồn đó nêu.
  2. **Nếu KHÔNG có nguồn cụ thể**:
     - Xóa bỏ vỏ bọc *"Các chuyên gia cho rằng / Giới quan sát nhận định rằng"* và trình bày mệnh đề đó như một phân tích logic trực tiếp (nếu mệnh đề tự đứng vững về mặt lập luận), **HOẶC** gắn nhãn cảnh báo `[CẦN BỔ SUNG NGUỒN CỤ THỂ]` cho tác giả.
     - Xóa bỏ các câu khoe độ phủ truyền thông rỗng (*"được đưa tin trên các báo địa phương và quốc gia"*, *"duy trì sự hiện diện tích cực trên mạng xã hội"*).

---

## HỒ SƠ 24: `PRG-02` — RÀO ĐÓN GIÁO HUẤN & MIỄN TRỪ TRÁCH NHIỆM NGUỒN TIN (`WP:DIDACTIC` / `WP:AIDISCLAIMER`)

### 1. Thông tin định danh
- **ID**: `PRG-02`
- **Tên dấu hiệu**: Rào đón giáo huấn người đọc (*Didactic Disclaimers*) và rào đón siêu ngôn ngữ về sự khan hiếm nguồn tin / cách sử dụng thông tin (*Hedging Disclaimers about Source Availability & Recommended Usage*).
- **Nguồn gốc trong danh sách gốc**: Khối II — `WP:DIDACTIC` (2022–2024: *It's important/crucial to note/remember...*) & `WP:AIDISCLAIMER` (2025–2026: *While specific details are limited in available sources...*, *should be treated as X rather than Y*, *does not by itself establish...*).

### 2. Bước 1 – Bước 5 — Định nghĩa, Biểu hiện & Cơ chế hình thành
- **Định nghĩa vận hành**: Hiện tượng văn bản chèn các câu nhắc nhở mang tính sư phạm/giáo huấn người đọc hoặc tự thú nhận quá trình tìm kiếm thông tin của chính AI:
  1. **`PRG-02a` — Rào đón giáo huấn (`WP:DIDACTIC`)**: *"Điều quan trọng cần lưu ý là..."*, *"Cần phải nhớ rằng..."*, *"Đáng lưu tâm là kết quả có thể khác nhau tùy thuộc vào..."* (`It is important to note that... may vary`).
  2. **`PRG-02b` — Tự thuật về sự thiếu hụt nguồn tìm kiếm (`WP:AIDISCLAIMER` – RAG Era 2025–2026)**: Khi công cụ tìm kiếm (RAG) không tìm thấy dữ liệu chi tiết (ví dụ lời bài hát, doanh thu chi tiết, đời tư cá nhân), AI viết thẳng vào bài: *"Mặc dù các chi tiết cụ thể không được công bố rộng rãi trong các nguồn hiện có, nhưng có khả năng..."*, *"Ông duy trì lối sống kín tiếng và giữ kín thông tin cá nhân"*, *"Dựa trên các kết quả tìm kiếm / tài liệu được cung cấp..."*.
  3. **`PRG-02c` — Rào đón hướng dẫn cách hiểu nguồn (`WP:AIDISCLAIMER` – Giữa và cuối 2026)**: *"Tuyên bố này nên được xem như là [truyền thống/biểu tượng] thay vì [bằng chứng xác thực]"*, *"Hướng dẫn này giải thích tại sao cần chú ý đến X. Nó không tự thân chứng minh rằng Y có vấn đề..."* (`It does not by itself establish that...`).
- **Cơ chế hình thành & Bằng chứng**:
  - `PRG-02a` xuất phát từ các mẫu "partial refusals" và safety disclaimers trong GPT-4 System Card (OpenAI, 2023) `[Cấp B]`.
  - `PRG-02b` và `PRG-02c` xuất phát từ system prompt của các hệ thống RAG thế hệ 2025–2026 (như ChatGPT Search, Perplexity, Claude) yêu cầu mô hình *"không được suy diễn vượt quá nguồn cung cấp (do not extrapolate beyond provided sources) và phải nêu rõ khi thông tin bị giới hạn"* — mô hình tuân thủ cực đoan bằng cách in luôn câu quy tắc đó ra văn bản đầu ra `[Cấp B]` (Graphite Study, 2026; Wikipedia AI Cleanup, Oct 2026).

### 3. Bước 6 – Bước 8 — Ví dụ Đối chiếu & Quy tắc Humanize
- **Ví dụ A (Dương tính rõ ràng — `PRG-02a` + `PRG-02b`)**:
  > *"Dựa trên các thông tin công khai hiện có, chi tiết cụ thể về cấu trúc cổ đông của công ty không được công bố rộng rãi, có thể do công ty duy trì chính sách bảo mật thông tin. Tuy nhiên, điều quan trọng cần lưu ý là quy định công bố thông tin có thể khác nhau tùy theo từng khu vực pháp lý."*
- **Ví dụ B (Dương tính tinh vi — `PRG-02c` năm 2026)**:
  > *"Số liệu này phản ánh quy mô đăng ký vốn trên giấy phép kinh doanh. Tự thân nó không chứng minh rằng doanh nghiệp đã thực góp đủ số vốn trên vào tài khoản phong tỏa."*
- **Ví dụ C (Hợp lệ — Phần Phương pháp luận / Giới hạn nghiên cứu trong bài báo khoa học)**:
  > Trong mục *Limitations of the Study* của một bài báo khoa học: *"Nghiên cứu này chỉ tiếp cận được dữ liệu báo cáo tài chính đã kiểm toán của 27 ngân hàng niêm yết; số liệu của các ngân hàng chưa niêm yết không được công bố đầy đủ trong giai đoạn khảo sát."*
- **Quy tắc ra quyết định khi Humanize**:
  1. **Xóa bỏ 100%** các cụm dẫn nhập dư thừa *"Điều quan trọng cần lưu ý là"*, *"Cần phải nhớ rằng"*, *"Đáng chú ý là"* — nếu mệnh đề phía sau thực sự quan trọng, hãy viết thẳng mệnh đề đó.
  2. **Xóa bỏ 100%** các câu suy diễn từ việc không tìm thấy nguồn (*"Vì thông tin không có trên mạng nên có lẽ ông ấy sống kín tiếng"*, *"Trong các nguồn được cung cấp..."*) vì đây là lỗi suy diễn từ sự thiếu vắng bằng chứng (*argument from ignorance / OR*).
