# BỘ TIÊU CHÍ ĐÁNH GIÁ, KIỂM THỬ CHẤT LƯỢNG VÀ DANH MỤC TÀI LIỆU THAM KHẢO ĐÃ XÁC MINH
**(Giai đoạn 6, Đầu ra F & Đầu ra H)**

---

## PHẦN I. ĐẦU RA F — BỘ TIÊU CHÍ ĐÁNH GIÁ VÀ KIỂM THỬ CHẤT LƯỢNG (EVALUATION & TESTING FRAMEWORK)

### 1.1. Phân định Nhận thức luận: "Đánh giá Chất lượng & Tính tự nhiên" vs. "Phát hiện Nguồn gốc AI"
Một sai lầm phương pháp luận phổ biến của các công cụ "AI Humanizer" trôi nổi trên thị trường là đồng nhất việc **cải thiện văn phong** với việc **đánh lừa các trình phát hiện AI (AI Detectors như GPTZero, Turnitin, Pangram)** bằng cách cố tình chèn lỗi chính tả, dùng từ lóng kỳ quặc hoặc bẻ gãy ngữ pháp. Hệ thống tri thức này bác bỏ cách tiếp cận đó và tách bạch hai bài toán:

| Tiêu chí đối chiếu | Bài toán 1: Dự đoán nguồn gốc AI (Forensic AI Detection) | Bài toán 2: Kiểm tra & Chuẩn hóa Văn phong Tự nhiên (Editorial Humanization) |
| :--- | :--- | :--- |
| **Câu hỏi cốt lõi** | *"Văn bản này do mô hình LLM nào sinh ra hay do con người viết?"* | *"Những đặc điểm diễn đạt nào đang làm giảm tính tự nhiên, độ chính xác lập luận và sự phù hợp thể loại của văn bản này?"* |
| **Giá trị của các dấu hiệu** | Phụ thuộc mạnh vào **Dấu vết Kỹ thuật (`FOR-01`)** và tổ hợp mật độ từ vựng thời kỳ (`LEX-01`). Tuy nhiên, đối với văn bản thuần phong cách, con người phân biệt chỉ ngang tung đồng xu (50–64%, Cheng et al., 2025; Fiedler et al., 2025) trừ nhóm chuyên gia sử dụng LLM cường độ cao (90%, Russell et al., 2025). | Không quan tâm tác giả ban đầu là AI hay người viết non tay/dịch máy. Nếu một câu mắc lỗi lặp đại từ *"Nó, Điều này"*, tắc nghẽn âm tiết Hán–Việt hoặc đóng hộp 4 bước sáo rỗng, nó **cần được biên tập lại** vì làm giảm chất lượng giao tiếp. |
| **Cách xử lý Ngoại lệ Thể loại** | Một văn bản hành chính của người Việt chứa nhiều từ *"đồng bộ, toàn diện"* có thể bị Detector báo nhầm là AI (False Positive). | Hệ thống kiểm tra ngữ cảnh thể loại: Nếu là văn bản hành chính nhà nước $\rightarrow$ giữ nguyên quy ước thể loại; nếu là bài phân tích kinh doanh/báo chí $\rightarrow$ đề xuất tinh chỉnh cho sắc bén. |

---

### 1.2. Hệ thống 6 Chỉ số Định lượng Kiểm thử Văn bản Tiếng Việt (Quantitative Diagnostic & Post-Edit Metrics)
Để AI Skill có thể tự chấm điểm (self-evaluate) văn bản trước và sau khi chỉnh sửa, hệ thống thiết lập 6 chỉ số toán học có thể tính toán tự động trên văn bản tiếng Việt:

#### (1) Chỉ số Biến thiên Nhịp câu ($CV_L$ & $\Delta L$) — Kiểm thử `RHY-01`
- **Công thức**:
  $$CV_L = \frac{\sigma_L}{\mu_L}, \quad \Delta L = \max_{1 \le i \le n}(l_i) - \min_{1 \le i \le n}(l_i)$$
  trong đó $l_i$ là số âm tiết (tách theo khoảng trắng) của câu thứ $i$ trong đoạn văn ($n \ge 4$).
- **Ngưỡng đạt chuẩn (Pass Criteria)**:
  - Văn bản phân tích / nghị luận / báo chí: **$0,28 \le CV_L \le 0,65$** và **$\Delta L \ge 16$ âm tiết**.
  - Bắt buộc có ít nhất 1 câu ngắn ($\le 15$ âm tiết) hoặc 1 câu phức đa tầng ($\ge 32$ âm tiết) trong mỗi cụm 5 câu.

#### (2) Chỉ số Đẳng cấu Cú pháp Liên câu ($ISI$ – Inter-sentential Syntactic Isomorphism) — Kiểm thử `SYN-01` & `SYN-02`
- **Cách đo**: Biểu diễn mỗi câu thành vector cấu trúc 3 thành phần $[I_{\text{AdvP\_init}}, I_{\text{Clause\_main}}, I_{\text{Tail\_eval}}]$ và tính tỷ lệ cặp câu liền kề $(S_i, S_{i+1})$ có cùng mẫu mở đầu + kết thúc.
- **Ngưỡng đạt chuẩn**:
  - Số chuỗi $\ge 3$ câu liên tiếp trùng khuôn cú pháp = **$0$**.
  - Mật độ mệnh đề đuôi `", qua đó / từ đó / góp phần / điều này khẳng định..."` (`SYN-02`) $\le 1$ lần trên 300 âm tiết.

#### (3) Chỉ số Tỉnh lược Bản ngữ & Kiểm soát Đại từ ($ZAR$ & $OPR$) — Kiểm thử `SYN-VN-01`
- **Công thức**:
  - **Mật độ đại từ/chỉ định từ dịch máy ($OPR$ – Over-explicit Pronoun Rate)**: Số lần xuất hiện của tập từ `{"nó", "chúng", "họ", "điều này", "việc này", "của họ", "của nó", "của mình"}` trên 100 âm tiết.
- **Ngưỡng đạt chuẩn**:
  - Tần suất từ `"nó"` quy chiếu tới khái niệm trừu tượng/tổ chức = **$0$ tuyệt đối**.
  - $OPR \le 0,8$ lần / 100 âm tiết (giảm tối thiểu 60–80% so với văn bản AI thô).

#### (4) Chỉ số Tắc nghẽn Hán–Việt & Danh hóa ($SVCI$ & $NMR$) — Kiểm thử `LEX-VN-01` & `SYN-VN-03`
- **Công thức**:
  - **$L_{\text{SV-max}}$**: Độ dài chuỗi âm tiết lớn nhất gồm toàn các từ ghép Hán–Việt và danh từ trừu tượng đứng liền nhau không có động từ thuần Việt hay hư từ ngắt nhịp.
  - **$NMR$ (Nominalization & Passive Calque Rate)**: Tổng số lần xuất hiện của `"việc + [Động từ]"`, `"sự + [Động từ]"`, `"thông qua việc"`, và `"được/bị + [Động từ] + bởi"` trên 100 âm tiết.
- **Ngưỡng đạt chuẩn**:
  - $L_{\text{SV-max}} \le 7$ âm tiết (không tính tên riêng cơ quan, văn bản luật).
  - Cấu trúc `"được/bị ... bởi"` = **$0$** (trừ khi nhấn mạnh tác thể bất ngờ trong văn dịch).
  - $NMR \le 1,0$ lần / 100 âm tiết.

#### (5) Chỉ số Đóng hộp Đoạn văn & Từ nối Đầu câu ($SICD$ & $BCR$) — Kiểm thử `DIS-01`, `DIS-02`, `DIS-03`
- **Công thức**:
  - **$SICD$ (Sentence-Initial Connective Density)**: Tỷ lệ số câu trong đoạn mở đầu bằng từ nối chuyển tiếp có dấu phẩy (`Cụ thể,`, `Tuy nhiên,`, `Do đó,`, `Hơn nữa,`, `Thêm vào đó,`, `Bên cạnh đó,`) trên tổng số câu.
  - **$BCR$ (Boxed Closure Rate)**: Tỷ lệ các đoạn văn thân bài kết thúc bằng câu tổng kết đóng hộp (`Như vậy,`, `Tóm lại,`, `Nhìn chung,`, `Chính vì vậy, cần... để phát triển bền vững`).
- **Ngưỡng đạt chuẩn**:
  - $SICD \le 0,25$ (tối đa 1 câu trên 4 câu mở đầu bằng từ nối đóng khung; ưu tiên dùng hư từ nội câu *cũng, còn, lại, vẫn, mới*).
  - $BCR = 0\%$ đối với các đoạn văn thân bài (chỉ đoạn kết cuối bài mới được phép tổng kết nếu cần).

#### (6) Chỉ số Bảo toàn Nội dung, Dữ kiện & Tình thái Nhận thức ($SEFS$ – Semantic & Epistemic Fidelity Score)
- **Định nghĩa**: Mọi bản chỉnh sửa Humanization **bị đánh trượt (Auto-Fail = 0 điểm)** nếu vi phạm bất kỳ điều kiện nào trong 5 ràng buộc bất biến sau:
  1. **Bảo toàn Dữ kiện & Số liệu (Fact Invariance)**: Giữ nguyên 100% con số, ngày tháng, tên riêng, tỷ lệ phần trăm, đơn vị đo. Không làm tròn số lẻ, không tự bịa thêm số liệu.
  2. **Bảo toàn Thuật ngữ Chuyên ngành (Terminology Lock)**: Giữ nguyên 100% thuật ngữ kỹ thuật, pháp lý, tài chính, y sinh của bản gốc (ví dụ: *biên lãi ròng [NIM], tỷ lệ dự trữ bắt buộc, trích lập dự phòng rủi ro*).
  3. **Bảo toàn Chiều hướng Nhân quả (Causal Polarity Preservation)**: Không làm đảo ngược quan hệ $A \rightarrow B$ thành $B \rightarrow A$, không biến nguyên nhân thành kết quả.
  4. **Bảo toàn Mức độ Chắc chắn (Epistemic Modality Invariance)**: Nếu bản gốc viết ở mức giả thuyết/khả năng (*"có thể dẫn đến"*, *"ước tính khoảng"*), bản sửa **cấm** biến thành khẳng định tuyệt đối (*"chắc chắn dẫn đến"*); ngược lại, nếu bản gốc là dữ kiện đã xảy ra, **cấm** gắn thêm rào đón mơ hồ (`LEX-05`).
  5. **Bảo toàn Nguồn trích dẫn (Citation Integrity)**: Giữ nguyên vị trí gắn thẻ trích dẫn `[1]`, `(Tác giả, Năm)` đúng với mệnh đề mà nguồn đó chứng minh.

---

### 1.3. Tiêu chí Đánh giá Độ chính xác Phát hiện & Độ nhất quán Chuyên gia (Detection & IAA Testing)
Khi kiểm thử bộ quy tắc nhận diện dấu hiệu trên tập ngữ liệu chuẩn (Benchmark Corpus):
1. **Precision & False Positive Rate (Tỷ lệ phát hiện nhầm)**:
   - Đánh giá riêng trên tập **Hard Negatives (Văn bản con người dễ bị nhầm là AI)**: Bao gồm (a) Nghị quyết, thông tư, báo cáo tổng kết của cơ quan nhà nước Việt Nam trước năm 2022; (b) Bài báo khoa học đăng trên các tạp chí chuyên ngành Việt Nam giai đoạn 2015–2021; (c) Bài dịch báo chí quốc tế của biên dịch viên con người.
   - Quy tắc phát hiện chỉ được chấp nhận đưa vào hệ thống tự động khi **False Positive Rate trên tập văn bản chuyên khảo của người viết giỏi $< 10\%$**.
2. **Độ nhất quán giữa những người đánh giá (Inter-Annotator Agreement – IAA)**:
   - Sử dụng hệ số **Krippendorff’s $\alpha$** (cho các nhãn mức độ nghiêm trọng từ 0–3) và **Cohen’s $\kappa$** (cho quyết định nhị phân: Cần sửa vs. Giữ nguyên).
   - Yêu cầu định nghĩa vận hành của từng dấu hiệu phải đạt **$\kappa \ge 0,75$** giữa hai biên tập viên tiếng Việt độc lập.

---

### 1.4. Ma trận Tương thích theo Thể loại Văn bản (Genre-Specific Calibration Matrix)
Một công cụ thông minh không áp dụng cùng một trọng số phạt cho mọi văn bản. Bảng dưới đây điều chỉnh độ nhạy của từng nhóm dấu hiệu theo 5 thể loại đích:

| Nhóm dấu hiệu | 1. Nghiên cứu Học thuật / Khoa học | 2. Phân tích Kinh doanh / Tài chính | 3. Báo chí Chính luận / Bình luận | 4. Văn bản Hành chính – Pháp quy VN | 5. Tài liệu Kỹ thuật / Hướng dẫn (Docs) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **`SYN-VN-01`, `02`, `03` (Tỉnh lược, Đề–Thuyết, Bị động/Danh hóa)** | **Sửa mạnh** (Ưu tiên câu chuẩn xác, rõ chủ thể) | **Sửa tối đa** (Cần nhịp văn sắc bén, tự nhiên) | **Sửa tối đa** (Đòi hỏi hơi thở bản ngữ cao nhất) | **Sửa nhẹ** (Chấp nhận danh hóa `việc/sự` theo mẫu hành chính) | **Sửa vừa** (Ưu tiên câu mệnh lệnh/hướng dẫn rõ ràng) |
| **`LEX-VN-01` (Tắc nghẽn Hán–Việt)** | **Sửa vừa** (Giữ thuật ngữ, giải nén động từ) | **Sửa mạnh** (Thay động từ rỗng bằng động từ chuyển động) | **Sửa tối đa** (Tăng từ thuần Việt giàu hình ảnh) | **Giữ nguyên / Sửa tối thiểu** (Đặc trưng phong cách công vụ) | **Sửa vừa** (Giữ thuật ngữ kỹ thuật, câu ngắn) |
| **`RHY-01` & `DIS-01` (Burstiness & Đoạn đóng hộp)** | **Sửa vừa** (Móc xích luận điểm liên đoạn) | **Sửa tối đa** (Cần câu chốt ngắn & câu phân tích sâu) | **Sửa tối đa** (Biến hóa nhịp điệu linh hoạt) | **Giữ nguyên** (Văn bản hành chính chia theo khoản/mục đều nhau) | **Giữ nguyên** (Ưu tiên cấu trúc module độc lập dễ tra cứu) |
| **`ARG-01` & `ARG-02` (Trọng số phẳng & Con lắc an toàn)** | **Sửa tối đa** (Cần phân tầng bằng chứng & điều kiện biên) | **Sửa tối đa** (Bắt buộc chỉ rõ nút thắt số 1 & trade-off) | **Sửa tối đa** (Cần lập trường sắc nét, tránh hòa cả làng) | **Giữ nguyên** (Báo cáo hành chính thường nêu cả ưu điểm & tồn tại) | **Không áp dụng** |
| **`FMT-01` (Danh sách in đậm, Bảng biểu)** | **Chuyển sang văn xuôi** (Hạn chế bullet vụn) | **Kết hợp** (Giữ bảng số liệu, viết xuôi phần phân tích) | **Chuyển sang văn xuôi 100%** | **Giữ định dạng Điều/Khoản/Điểm** | **Giữ nguyên 100%** (Danh sách & bảng là tối ưu cho Docs) |

---

## PHẦN II. ĐẦU RA H — DANH MỤC TÀI LIỆU THAM KHẢO ĐÃ XÁC MINH (VERIFIED BIBLIOGRAPHY & EVIDENCE AUDIT)

> **Tuyên bố minh bạch về phương pháp trích dẫn (Citation Integrity Statement)**:
> Tuân thủ tuyệt đối Mục 4.1 – 4.3 của Master Prompt:
> 1. Danh mục dưới đây **chỉ bao gồm các công trình khoa học, sách chuyên khảo và tài liệu kỹ thuật thực sự tồn tại**.
> 2. Phân biệt rõ hai nhóm nguồn:
>    - **Nhóm I**: Các công trình nghiên cứu gốc về NLP, Ngôn ngữ học tính toán và Ngôn ngữ học tiếng Việt mà thông tin thư mục, phương pháp và kết quả cốt lõi đã được xác minh trực tiếp.
>    - **Nhóm II**: Các nghiên cứu giai đoạn 2024–2026 được trích dẫn thông qua dữ liệu tổng hợp của *Wikipedia:Signs of AI writing* (đã cung cấp trong tài liệu đầu vào của người dùng); với các nguồn này, nhóm nghiên cứu ghi rõ phạm vi thông tin được trích xuất từ tài liệu đầu vào và **không tự suy diễn thêm chi tiết phương pháp nằm ngoài dữ liệu đã kiểm chứng**.

### 2.1. Nhóm I — Các công trình Thực nghiệm về Ngôn ngữ của LLM & Phát hiện Văn bản AI (Đã xác minh)

1. **Kobak, D., González-Márquez, R., Horvát, E.-Á., & Lause, J. (2024/2025).**
   - *Tên công trình*: "Delving into ChatGPT usage in academic writing through excess vocabulary."
   - *Nơi công bố / Định danh*: Preprint `arXiv:2406.07016` (2024) / Công bố trên *Science Advances* (2025), DOI: `10.1126/sciadv.adt3813` (và `10.48550/arXiv.2406.07016`).
   - *Phương pháp & Dữ liệu*: Phân tích định lượng tần suất từ vựng (excess word frequency analysis) trên hơn **14 triệu tóm tắt bài báo khoa học (PubMed abstracts)** công bố từ năm 2010 đến năm 2024 để đo lường sự dịch chuyển từ vựng bất thường sau khi ChatGPT ra mắt.
   - *Kết quả liên quan trực tiếp*: Xác định hàng trăm "từ vựng dư thừa" (excess words) tăng đột biến trong năm 2023–2024, đứng đầu là các động từ, tính từ và danh từ trừu tượng như *delves, showcasing, underscores, pivotal, intricate, realm, meticulous, fostering, garner, tapestry* (hỗ trợ trực tiếp hồ sơ `LEX-01` và `SYN-02`).
   - *Giới hạn sử dụng*: Nghiên cứu thực hiện trên văn bản tóm tắt y sinh học bằng **tiếng Anh** (`[Cấp B]`). Không kiểm chứng trực tiếp trên ngữ liệu tiếng Việt; từ vựng tương đương trong tiếng Việt là kết quả ánh xạ dịch thuật.

2. **Juzek, T. S., & Ward, Z. B. (2024/2025).**
   - *Tên công trình*: "Why Does ChatGPT 'Delve' So Much? Exploring the Sources of Lexical Overrepresentation in Large Language Models."
   - *Nơi công bố / Định danh*: *Proceedings of the 31st International Conference on Computational Linguistics (COLING 2025)* / Preprint `arXiv:2412.11385`, DOI: `10.48550/arXiv.2412.11385`.
   - *Phương pháp & Dữ liệu*: Phân tích ngữ liệu lịch sử kết hợp thực nghiệm so sánh giữa các mô hình nền (base models chỉ qua pre-training) và các mô hình đã qua tinh chỉnh hướng dẫn và phản hồi con người (SFT + RLHF) để tìm nguyên nhân gốc rễ của hiện tượng lạm dụng từ vựng như *delve, intricate, underscore, garner*.
   - *Kết quả liên quan trực tiếp*: Bác bỏ giả thuyết cho rằng dữ liệu tiền huấn luyện là nguyên nhân chính; chứng minh thực nghiệm rằng **quy trình RLHF (Reinforcement Learning from Human Feedback)** là tác nhân quyết định làm bùng nổ tần suất các từ vựng mang vẻ học thuật, trang trọng giả tạo (hỗ trợ trực tiếp Bước 3 của `LEX-01`, `ARG-02`, `ARG-03`).
   - *Giới hạn sử dụng*: Bằng chứng thực nghiệm trên tiếng Anh (`[Cấp B]`).

3. **Liang, W., Izzo, Z., Zhang, Y., Lepp, H., Wu, H., Zhao, X., Chen, L., ... & Zou, J. Y. (2024).**
   - *Tên công trình*: "Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews."
   - *Nơi công bố / Định danh*: *Proceedings of the 41st International Conference on Machine Learning (ICML 2024)*, PMLR 235 / Preprint `arXiv:2403.07183`, DOI: `10.48550/arXiv.2403.07183`.
   - *Phương pháp & Dữ liệu*: Ước lượng phân phối xác suất cấp độ quần thể (distributional quantification) trên tập dữ liệu lớn gồm các bản nhận xét bình duyệt (peer reviews) tại các hội nghị AI hàng đầu (ICLR, NeurIPS, CoRL, EMNLP) trước và sau khi có ChatGPT.
   - *Kết quả liên quan trực tiếp*: Phát hiện từ 6,5% đến 16,9% văn bản bình duyệt đã bị chỉnh sửa bởi LLM; chỉ ra sự gia tăng đột biến của các tính từ đánh giá tích cực/lịch sự chung chung (*commendable, meticulous, intricate, notable, versatile*) và cấu trúc nhận xét đóng khung (`LEX-01`, `ARG-02`).
   - *Giới hạn sử dụng*: Ngữ liệu bình duyệt khoa học tiếng Anh (`[Cấp B]`).

4. **Reinhart, A., Markey, B., Laudenbach, M., Pantusen, K., Yurko, R., Weinberg, G., & Brown, D. W. (2024/2025).**
   - *Tên công trình*: "Do LLMs write like humans? Variation in grammatical and rhetorical styles."
   - *Nơi công bố / Định danh*: *Proceedings of the National Academy of Sciences (PNAS)*, 2025 (Preprint `arXiv:2410.16107`, 2024), DOI: `10.1073/pnas.2422455122` (và `10.48550/arXiv.2410.16107`).
   - *Phương pháp & Dữ liệu*: Phân tích đa biến (multiberiate corpus analysis theo khung Biber's Multi-Dimensional Analysis) so sánh hàng trăm đặc trưng ngữ pháp, cú pháp và tu từ giữa văn bản con người (trên nhiều thể loại) và văn bản sinh bởi các LLM đương đại (bao gồm dòng GPT-4, GPT-4o, Claude, Llama).
   - *Kết quả liên quan trực tiếp*: Chứng minh LLM (đặc biệt là GPT-4o) có sự lệch chuẩn rõ rệt so với con người: **lạm dụng mệnh đề phân từ hiện tại (`present participial clauses`) để bình luận ở cuối câu (`SYN-02` / `WP:SUPERFICIAL`)**, mật độ danh hóa cao (`LEX-VN-01` / `SYN-VN-03`), thiếu các từ hạn định/tình thái tự nhiên của con người (*very, perhaps, tends to*), và độ biến thiên cấu trúc thấp hơn con người (`SYN-01`, `RHY-01`).
   - *Giới hạn sử dụng*: Phân tích trên ngữ liệu tiếng Anh (`[Cấp B]`).

5. **Geng, M., & Trotta, R. (2024/2025).**
   - *Tên công trình*: "Is ChatGPT Transforming Academics' Writing Style?" (và nghiên cứu tiếp nối về sự biến thiên tần suất từ trong bài báo khoa học).
   - *Nơi công bố / Định danh*: Preprint `arXiv:2404.08627` (2024), DOI: `10.48550/arXiv.2404.08627` (cùng các cập nhật năm 2025 được trích dẫn trong tài liệu Wikipedia tại `#cite_note-geng-22`, `#cite_note-geng2025-8`, `#cite_note-geng2-31`).
   - *Phương pháp & Dữ liệu*: Phân tích thống kê trên 1 triệu bài báo khoa học trên arXiv (giai đoạn 2018–2024) và thí nghiệm yêu cầu LLM viết lại 10.000 đoạn tóm tắt thực tế.
   - *Kết quả liên quan trực tiếp*: Chứng minh sự gia tăng mạnh của các từ nối và tính từ định hướng (*additionally, crucial, valuable, enhance*) (`LEX-01`, `DIS-03`) và đặc biệt phát hiện **sự sụt giảm hơn 10% tần suất sử dụng hệ từ cơ bản `"is"` và `"are"`** khi LLM viết mới hoặc biên tập lại văn bản của con người (`LEX-02` / `WP:AINOCOPULA`).
   - *Giới hạn sử dụng*: Ngữ liệu học thuật tiếng Anh (`[Cấp B]`).

6. **Meister, C., Pimentel, T., Wiher, G., & Cotterell, R. (2023).**
   - *Tên công trình*: "Locally Typical Sampling."
   - *Nơi công bố / Định danh*: *Transactions of the Association for Computational Linguistics (TACL)*, Vol. 11, pp. 102–121, DOI: `10.1162/tacl_a_00536` (Preprint `arXiv:2202.00666`).
   - *Phương pháp & Dữ liệu*: Lý thuyết thông tin (Information Theory) và thực nghiệm giải mã văn bản tự hồi quy trên các mô hình ngôn ngữ lớn, đối chiếu với giả thuyết *Uniform Information Density (UID)* (Levy & Jaeger, 2007).
   - *Kết quả liên quan trực tiếp*: Cung cấp cơ sở toán học giải thích tại sao quá trình sinh văn bản của LLM có xu hướng duy trì lượng thông tin (surprisal / entropy) phẳng và ổn định ở mọi bước sinh, dẫn đến **độ biến thiên chiều dài câu thấp (`RHY-01`)** và **mật độ thông tin đồng đều, phẳng hóa chi tiết (`ARG-01`)**.
   - *Giới hạn sử dụng*: Lý thuyết và thực nghiệm cơ chế giải mã tổng quát của LLM (`[Cấp B/C]`).

7. **Holtzman, A., Buys, J., Du, L., Forbes, M., & Choi, Y. (2020).**
   - *Tên công trình*: "The Curious Case of Neural Text Degeneration."
   - *Nơi công bố / Định danh*: *International Conference on Learning Representations (ICLR 2020)* / `arXiv:1904.09751`, DOI: `10.48550/arXiv.1904.09751`.
   - *Kết quả liên quan*: Giải thích sự khác biệt phân phối xác suất đuôi dài giữa văn bản con người (nhiều lựa chọn từ/cấu trúc bất ngờ nhưng hợp ngữ cảnh) và văn bản sinh từ cực đại hóa xác suất của mô hình thần kinh, cũng như vai trò của cơ chế phạt lặp từ dẫn đến `LEX-04` (`[Cấp B]`).

8. **Russell, J., Karpinska, M., & Iyyer, M. (2025).**
   - *Tên công trình*: "People who frequently use ChatGPT for writing tasks are accurate and robust detectors of AI-generated text."
   - *Nơi công bố / Định danh*: Preprint `arXiv:2501.15654` (2025), DOI: `10.48550/arXiv.2501.15654` (được trích dẫn trong tài liệu đầu vào tại `#cite_note-Russell-2`).
   - *Phương pháp & Kết quả liên quan*: Thực nghiệm mù đối chứng giữa nhóm người dùng ít sử dụng LLM (nhận diện chỉ nhỉnh hơn ngẫu nhiên) và nhóm chuyên gia sử dụng LLM thường xuyên (đạt độ chính xác 90%, tỷ lệ nhầm văn bản người là 3,3%). Các chuyên gia nhận diện không dựa vào "ngữ pháp hoàn hảo" mà dựa vào các dấu hiệu cấu trúc và từ vựng cụ thể: `LEX-01` (*delve, tapestry, testament, landscape, pivotal, foster*), `SYN-03` (*Negative parallelisms*), `SYN-04` (*Rule of three*), `ARG-04` (*Despite its X, faces challenges*), và `FMT-01` (*Title case headings*) (`[Cấp B]`).

9. **Yakura, H., Lopez-Lopez, E., Brinkmann, L., Serna, I., Gupta, P., & Rahwan, I. (2024).**
   - *Tên công trình*: "Empirical evidence of Large Language Model's influence on human spoken communication."
   - *Nơi công bố / Định danh*: Preprint `arXiv:2409.01754` (2024), DOI: `10.48550/arXiv.2409.01754` (trích dẫn tại `#cite_note-yakura2024-7`).
   - *Kết quả liên quan*: Phân tích hàng trăm nghìn giờ âm thanh podcast/video trước và sau 2022, chứng minh rằng con người đang bắt chước ngược lại các từ vựng đặc trưng của ChatGPT (*delve, intricate, underscore, realm*), làm giảm độ đặc hiệu của việc chỉ dùng danh sách từ đơn lẻ để kết luận văn bản do AI viết (`[Cấp B]`).

10. **Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., ... & Lowe, R. (2022).**
    - *Tên công trình*: "Training language models to follow instructions with human feedback."
    - *Nơi công bố / Định danh*: *Advances in Neural Information Processing Systems (NeurIPS 2022)*, 35, 27730–27744 / `arXiv:2203.02155`.
    - *Kết quả liên quan*: Tài liệu gốc giải thích quy trình SFT và RLHF tạo ra hành vi tuân thủ bố cục danh sách, giọng điệu lịch sự, rào đón an toàn và giải thích từng bước của các mô hình Instruct/Chat (`[Cấp B]`).

---

### 2.2. Nhóm II — Các công trình Lý thuyết Ngôn ngữ học Tiếng Việt & Ngữ pháp Chức năng (Đã xác minh)

11. **Cao Xuân Hạo (1991 / tái bản 2004).**
    - *Tên công trình*: *Tiếng Việt – Sơ thảo ngữ pháp chức năng (Quyển 1)*.
    - *Đơn vị xuất bản*: Nhà xuất bản Khoa học Xã hội (1991) / Nhà xuất bản Giáo dục (2004), Hà Nội.
    - *Nội dung & Giá trị đối với Knowledge Base*: Công trình nền tảng quan trọng nhất của Việt ngữ học hiện đại chứng minh tiếng Việt là ngôn ngữ thiên Chủ đề (**cấu trúc Đề – Thuyết / Topic – Comment**) chứ không phải cấu trúc Chủ – Vị (Subject – Predicate) của ngôn ngữ Ấn–Âu; đồng thời bác bỏ việc áp đặt phạm trù "câu bị động" (`được/bị`) của tiếng Anh/Pháp vào tiếng Việt. Đây là cơ sở lý thuyết trực tiếp (`[Cấp C]`) cho các hồ sơ `SYN-VN-01`, `SYN-VN-02`, và `SYN-VN-03`.

12. **Trần Ngọc Thêm (1985 / tái bản 1999).**
    - *Tên công trình*: *Hệ thống liên kết văn bản tiếng Việt*.
    - *Đơn vị xuất bản*: Nhà xuất bản Khoa học Xã hội (1985) / Nhà xuất bản Giáo dục (1999), Hà Nội.
    - *Nội dung & Giá trị đối với Knowledge Base*: Xây dựng hệ thống lý thuyết toàn diện về các phương thức liên kết câu và đoạn văn trong tiếng Việt (phép lặp, phép đối, phép thế, **phép tỉnh lược yếu tố cốt lõi**, phép nối bằng hư từ nội câu và liên kết móc xích liên đoạn). Cung cấp cơ sở khoa học (`[Cấp C]`) để xử lý lỗi thiếu tỉnh lược chủ ngữ (`SYN-VN-01`), lỗi lạm dụng từ nối đầu câu (`DIS-03`) và lỗi đoạn văn đóng hộp (`DIS-01`).

13. **Diệp Quang Ban (2005).**
    - *Tên công trình*: *Ngữ pháp tiếng Việt*.
    - *Đơn vị xuất bản*: Nhà xuất bản Giáo dục, Hà Nội.
    - *Nội dung & Giá trị đối với Knowledge Base*: Phân tích hệ thống từ loại, hư từ, quan hệ từ, cấu trúc câu đơn/câu ghép tiếng Việt và sự tương tác giữa cấu trúc cú pháp với cấu trúc nghĩa. Hỗ trợ trực tiếp quy tắc chuyển đổi từ nối đầu câu sang phụ từ nội câu (`cũng, còn, lại, vẫn, mới`) trong `DIS-03` và `SYN-VN-02` (`[Cấp C]`).

14. **Li, C. N., & Thompson, S. A. (1976).**
    - *Tên công trình*: "Subject and Topic: A New Typology of Language."
    - *Nơi công bố*: Trong C. N. Li (Ed.), *Subject and Topic* (pp. 457–489). New York: Academic Press.
    - *Nội dung & Giá trị*: Công trình kinh điển của ngôn ngữ học loại hình thế giới phân biệt 4 loại hình ngôn ngữ theo trục Subject-prominent (như tiếng Anh) và Topic-prominent (như tiếng Việt, tiếng Trung, tiếng Nhật), giải thích cơ chế tại sao việc dịch thẳng cấu trúc Chủ–Vị và đại từ nhân xưng từ tiếng Anh sang tiếng Việt tạo ra câu văn phi bản ngữ (`SYN-VN-01`, `SYN-VN-02`) (`[Cấp C]`).

15. **Levy, R., & Jaeger, T. F. (2007).**
    - *Tên công trình*: "Speakers optimize information density through syntactic reduction."
    - *Nơi công bố*: *Advances in Neural Information Processing Systems (NIPS)*, Vol. 19, pp. 849–856.
    - *Nội dung & Giá trị*: Đề xuất giả thuyết *Uniform Information Density (UID)* trong ngôn ngữ học tính toán (`ARG-01`) (`[Cấp C]`).

---

### 2.3. Nhóm III — Các nguồn tham chiếu thứ cấp được trích dẫn qua Tài liệu `Wikipedia:Signs of AI writing` (Công khai giới hạn truy cập)
Các nguồn dưới đây được trích xuất từ hệ thống chú thích của văn bản `Wikipedia:Signs of AI writing` do người dùng cung cấp. Nhóm nghiên cứu chỉ sử dụng đúng phạm vi kết luận được nêu trong văn bản nguồn và công khai giới hạn:
- **Cheng et al. (2025)** (`#cite_note-cheng2025-5`) & **Fiedler et al. (2025)** (`#cite_note-fiedler2025-6`): Các nghiên cứu thực nghiệm năm 2025 chứng minh người đọc thông thường (không chuyên) phân biệt văn bản AI và văn bản con người chỉ đạt mức tương đương ngẫu nhiên hoặc 57%–64% trên luận văn tiếng Đức. *(Giới hạn: Chỉ trích dẫn số liệu tổng quát theo bản tóm tắt của Wikipedia, không suy diễn chi tiết thiết kế mẫu).*
- **Huang et al. (2024/2025)** (`#cite_note-huang-23`): Nghiên cứu so sánh văn bản Wikipedia trước và sau năm 2023 với các bài viết bách khoa do GPT-4o-mini và Gemini-1.5-Flash sinh ra, ghi nhận hiện tượng né tránh hệ từ `is/are`, tăng đa dạng từ vựng do repetition penalty (`WP:AIELEVAR`), và lạm dụng từ nối `Additionally`.
- **Sun et al. (2024/2025)** (`#cite_note-sun-13`): Nghiên cứu so sánh sự khác biệt phong cách (idiolect) giữa các họ LLM, chỉ ra rằng ChatGPT và Grok có xu hướng nhấn mạnh bối cảnh rộng lớn hơn (`WP:AILEGACY`) và viết dài dòng hơn so với Gemini và Claude.
- **The Economist Study (July 2026)** (`#cite_note-economistJul2026-26`): Phân tích định lượng văn phong các mô hình đương đại giữa năm 2026, ghi nhận sự lạm dụng cụm *deep dive*, cấu trúc sóng đôi phủ định, quy tắc số 3, và phát hiện chỉ còn Claude dùng dấu gạch ngang dài (`—`) nhiều hơn nhà văn chuyên nghiệp trong khi ChatGPT đã giảm mạnh.
- **Anthropic (November 2024)**: *Claude 3.5 Sonnet System Prompt* (`#cite_note-sonnetprompt-34`) — Tài liệu gốc minh chứng việc định dạng Markdown, tiêu đề và danh sách được quy định trực tiếp trong system prompt của mô hình.
- **OpenAI (2023)**: *GPT-4 System Card* (`#cite_note-openaicdn-53`) — Tài liệu gốc minh chứng các mẫu câu rào đón giáo huấn (*"It is important to note..."*) trong các câu trả lời từ chối một phần (partial refusals).
