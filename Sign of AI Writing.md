## **1\. Độ biến thiên chiều dài câu cực thấp (Low Burstiness – Nhịp văn "máy đếm nhịp")**

Trong ngôn ngữ học, **Burstiness** là chỉ số đo sự biến thiên về độ dài và độ phức tạp của các câu trong một văn bản.

* **Văn của con người (High Burstiness):** Nhịp điệu co giãn liên tục theo cảm xúc và sức nặng của ý tưởng. Người viết có thể viết một câu phức dài 45–50 chữ để giải thích một cơ chế tài chính phức tạp, rồi ngay lập tức chốt bằng một câu đơn ngắn 6 chữ (*"Thực tế lại hoàn toàn trái ngược."*), sau đó là một câu trung bình 20 chữ.  
* **Văn của AI (Low Burstiness):** Do sinh từ theo xác suất thống kê tối ưu, AI luôn duy trì độ dài câu ở mức trung bình an toàn — thường dao động trong khoảng **18 đến 28 chữ mỗi câu** (hoặc ở các mô hình cuối năm 2026 là **12 đến 20 chữ mỗi câu**). Phương sai độ dài câu gần như bằng không. Khi đọc lên, bạn sẽ thấy hơi thở của đoạn văn đều tăm tắp, không có câu nào quá ngắn để tạo điểm nhấn, cũng không có câu nào đủ dài để triển khai lập luận nhiều tầng.

## **2\. Hiện tượng "Đẳng cấu cú pháp" (Syntactic Isomorphism – Khác từ nhưng trùng khuôn câu)**

Đây là nguyên nhân trực tiếp tạo ra cảm giác "bình bình, đều đều" mà bạn nhắc tới. Dù AI đổi từ vựng liên tục để tránh lặp từ, **cây cú pháp (Parse Tree)** của các câu liên tiếp lại giống hệt nhau.

Khuôn câu ưa thích nhất của AI khi viết tiếng Việt là cấu trúc 3 nhịp:

**\[Trạng ngữ chỉ bối cảnh/thời gian\], \[Chủ ngữ \+ Động từ \+ Tân ngữ\], \[Mệnh đề phụ chỉ kết quả/ý nghĩa\].**

**Ví dụ điển hình trong văn AI tiếng Việt:**

*(Câu 1\)* **Trong bối cảnh cạnh tranh gay gắt hiện nay**, các ngân hàng thương mại đang đẩy mạnh quá trình số hóa dịch vụ, **qua đó nâng cao trải nghiệm cho khách hàng cá nhân.**

*(Câu 2\)* **Trước những biến động khó lường của vĩ mô**, nhiều tổ chức tín dụng cũng chủ động thắt chặt khẩu vị rủi ro, **từ đó đảm bảo sự an toàn cho toàn bộ hệ thống.**

*(Câu 3\)* **Thông qua việc ứng dụng trí tuệ nhân tạo**, quy trình thẩm định tín dụng đã được rút ngắn đáng kể, **góp phần tối ưu hóa chi phí vận hành của doanh nghiệp.**

Nếu bạn rút bỏ phần chữ và chỉ nhìn vào bộ khung ngữ pháp của 3 câu trên, chúng là **một câu duy nhất được nhân bản làm 3 lần**: \[Trạng ngữ 7-8 chữ\], \[Mệnh đề chính 12-14 chữ\], \[Mệnh đề phụ 8-10 chữ\]. Người thật không bao giờ viết 3 câu liên tiếp có cùng một cấu trúc ngữ pháp đối xứng cơ học như vậy.

## **3\. Cấu trúc "Đoạn văn đóng hộp" (Boxy, Self-Contained Paragraphs)**

Khi nhìn tổng thể một trang văn bản do AI viết từ xa (chưa cần đọc chữ), bạn sẽ thấy các đoạn văn có kích thước **đều nhau như những viên gạch được đúc từ một khuôn** (thường mỗi đoạn dài khoảng 4–5 dòng, tương đương 3–4 câu).

Nguy hiểm hơn, bên trong mỗi đoạn văn của AI luôn tuân theo một **công thức 4 bước khép kín** (giống như một bài văn thu nhỏ):

1. **Câu 1 (Câu chủ đề):** Nêu một nhận định khái quát.  
2. **Câu 2 (Giải thích):** Mở rộng câu 1 (thường bắt đầu bằng *"Cụ thể,"*, *"Điều này có nghĩa là..."*, *"Thật vậy,"*).  
3. **Câu 3 (Ví dụ/Chi tiết hóa):** Đưa ra một mặt biểu hiện chung chung.  
4. **Câu 4 (Câu kết đoạn \- Mini-conclusion):** Luôn tự tóm tắt lại ý nghĩa của đoạn đó (bắt đầu bằng *"Như vậy,"*, *"Nhìn chung,"*, *"Qua đó có thể thấy..."*, *"Chính vì vậy..."*).

**Hệ quả (Sự đứt gãy mạch văn liên đoạn):**

Vì đoạn nào AI cũng tự mở bài và tự kết bài ở câu thứ 4, các đoạn văn trở thành các **"hộp kín" độc lập**. Bạn có thể đảo vị trí Đoạn 2 xuống dưới Đoạn 4 mà văn bản không hề bị gãy mạch ngữ pháp. Ngược lại, trong văn viết của con người, câu cuối của đoạn trước thường mở ra một vấn đề bỏ lửng để đoạn sau giải quyết tiếp (các đoạn móc xích vào nhau chứ không đóng hộp).

## **4\. Trọng số luận điểm phẳng và Mật độ thông tin đồng đều (Uniform Information Density)**

Trong nghiên cứu học thuật hay phân tích kinh doanh của con người, các luận điểm **không bao giờ bình đẳng**:

* **Người viết thật:** Nếu có 4 nguyên nhân dẫn đến nợ xấu tăng, người viết sẽ dành **60% dung lượng** (3 đoạn văn dài, kèm bảng số liệu, trích dẫn thông tư cụ thể và phân tích sâu) cho nguyên nhân quan trọng nhất; 3 nguyên nhân phụ còn lại được gom chung vào 1 đoạn ngắn.  
* **AI viết:** Chia đều tài nguyên một cách máy móc. Nếu có 4 nguyên nhân, AI sẽ chia thành 4 mục hoặc 4 đoạn văn, **mỗi nguyên nhân được viết đúng 80 chữ**, mức độ đào sâu ngang nhau, giọng điệu nghiêm trọng ngang nhau.

Điều này tạo ra hiện tượng **"Phẳng hóa trọng số" (Flat Epistemic Weight)**: cái gì AI cũng khen là quan trọng, nhưng không có cái gì thực sự là trọng tâm. Toàn bộ bài viết lướt đi trên bề mặt ở cùng một độ cao (tầm nhìn vĩ mô chung chung) mà thiếu "độ nhám" của dữ kiện thực tế (con số lẻ, trường hợp ngoại lệ, sự kiện cụ thể theo thời gian).

## **5\. Đường cong lập luận kiểu "Con lắc an toàn" (Pendulum Hedging)**

Về mặt nhịp điệu tư duy, AI bị huấn luyện bởi RLHF để không làm mất lòng bất kỳ góc nhìn nào, dẫn đến cấu trúc lập luận luôn dao động như quả lắc đồng hồ:

**Khen (Khẳng định mặt tích cực) $\rightarrow$ Chê nhẹ (Chỉ ra rào cản/rủi ro) $\rightarrow$ Hòa cả làng (Kêu gọi sự kết hợp hài hòa / đồng bộ).**

Bất kể đoạn văn đang phân tích về chính sách tiền tệ, quản trị nhân sự hay chiến lược marketing, nhịp điệu tư duy đều đi theo vòng lặp: *"Mặt tích cực là A. Tuy nhiên, hạn chế là B. Do đó, cần có sự phối hợp đồng bộ giữa C và D để đạt hiệu quả tối ưu."* Khi cấu trúc tư duy này lặp lại ở mọi chương, mọi mục, người đọc sẽ rơi vào trạng thái mệt mỏi vì đoán trước được câu tiếp theo AI sẽ nói gì.

## **6\. Sự phá vỡ nhịp điệu bản ngữ Tiếng Việt (Cấu trúc Đề \- Thuyết, Tỉnh lược và Âm luật)**

Đây là dấu hiệu cấu trúc câu đặc thù khi đối chiếu giữa ngữ pháp tiếng Anh của AI và tiếng Việt tự nhiên:

* **Thiếu sự "Tỉnh lược chủ ngữ" (Zero-anaphora) tự nhiên:** Tiếng Việt là ngôn ngữ hướng ngữ cảnh. Khi chủ ngữ đã rõ ở câu trước, người Việt tự nhiên sẽ tỉnh lược chủ ngữ ở các mệnh đề sau để câu văn thanh thoát. AI (do tư duy theo cú pháp tiếng Anh bắt buộc mọi mệnh đề phải có Subject \+ Verb) luôn nhồi các đại từ nhân xưng hoặc danh từ chỉ định vào đầu mọi mệnh đề: *"Ngân hàng này...", "Họ...", "Nó...", "Điều này...", "Việc này..."*.  
* **Đánh mất cấu trúc Đề \- Thuyết (Topic \- Comment):** Người Việt rất chuộng cấu trúc đưa phần "Đề" (chủ đề cần bàn) lên đầu câu mà không cần giới từ rườm rà (Ví dụ: *"Rủi ro thanh khoản, các ngân hàng nhỏ thường xử lý bằng cách..."* hoặc *"Về phía khách hàng, lãi suất vẫn là yếu tố..."*). AI lại luôn viết theo cấu trúc Chủ \- Vị cứng nhắc kèm giới từ dịch từ tiếng Anh: *"Đối với vấn đề rủi ro thanh khoản, nó thường được các ngân hàng nhỏ xử lý thông qua việc..."*.  
* **Tắc nghẽn âm tiết Hán \- Việt (Syllabic Congestion):** Tiếng Việt có tính nhạc rất cao nhờ sự luân phiên giữa từ thuần Việt (mềm, cụ thể) và từ Hán \- Việt (trang trọng, khái quát), cùng nhịp chẵn (2-2, 4-4). Văn AI thường ghép nối liên tiếp 4–5 cụm danh từ Hán \- Việt trừu tượng không có động từ thuần Việt làm điểm tựa, khiến câu văn bị "đặc quánh" và mất nhịp thở.

## **Bảng đối chiếu trực quan: Nhịp điệu AI vs. Nhịp điệu Con người**

Hãy xem cùng một ý phân tích về **Thu nhập ngoài lãi của ngân hàng**, sự khác biệt về cấu trúc câu và đoạn diễn ra như thế nào:

| Tiêu chí cấu trúc | Văn bản mang cấu trúc & nhịp điệu AI | Văn bản mang cấu trúc & nhịp điệu Con người |
| :---- | :---- | :---- |
| **Đoạn văn mẫu** | *(Câu 1 \- 24 chữ)* Trong bối cảnh biên lãi ròng thu hẹp, việc đa dạng hóa nguồn thu ngoài lãi đóng vai trò then chốt đối với các ngân hàng. *(Câu 2 \- 25 chữ)* Cụ thể, các hoạt động dịch vụ thanh toán và kinh doanh ngoại hối đã mang lại nguồn thu ổn định, giúp giảm sự phụ thuộc vào tín dụng. *(Câu 3 \- 23 chữ)* Tuy nhiên, mảng phân phối bảo hiểm qua ngân hàng lại đang đối mặt với nhiều thách thức lớn về niềm tin của khách hàng. *(Câu 4 \- 25 chữ)* Do đó, các tổ chức tín dụng cần tái cấu trúc danh mục dịch vụ một cách toàn diện để đảm bảo sự phát triển bền vững. | *(Câu 1 \- 11 chữ)* Khi NIM bị thu hẹp, các ngân hàng buộc phải tìm đường sống từ thu nhập ngoài lãi. *(Câu 2 \- 38 chữ)* Nhưng bức tranh năm 2025–2026 không còn dễ dàng như giai đoạn trước: trong khi mảng thanh toán và kinh doanh ngoại hối giữ được nhịp tăng trưởng ổn định, thì "con gà đẻ trứng vàng" một thời là Bancassurance lại sụt giảm mạnh sau hàng loạt biến cố về niềm tin thị trường. *(Câu 3 \- 16 chữ)* Bài toán lúc này không còn là mở rộng bằng mọi giá, mà là lọc lại chất lượng dịch vụ. |
| **Độ dài các câu (Burstiness)** | **24 – 25 – 23 – 25 chữ.** (Đều tăm tắp như máy cắt, phương sai gần bằng 0). | **11 – 38 – 16 chữ.** (Ngắn mở đầu $\rightarrow$ Dài phân tích sâu có đối chiếu $\rightarrow$ Ngắn gọn sắc bén để chuyển ý). |
| **Liên kết giữa các câu** | Dùng từ nối đóng khung đầu câu: *Trong bối cảnh... $\rightarrow$ Cụ thể,... $\rightarrow$ Tuy nhiên,... $\rightarrow$ Do đó,...* | Liên kết bằng mạch ý và dấu hai chấm (:), không cần lạm dụng từ nối sáo rỗng ở mọi đầu câu. |
| **Cách kết đoạn** | Đóng hộp bằng lời khuyên chung chung (*"tái cấu trúc toàn diện để phát triển bền vững"*). | Mở ra định hướng cụ thể để đoạn tiếp theo đi thẳng vào phân tích số liệu chất lượng dịch vụ. |

This is a list of writing and formatting conventions typical of [AI chatbots](https://en.wikipedia.org/wiki/AI_chatbot) such as [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT), with real examples taken from Wikipedia articles, drafts, comments, and other content. It is a [field guide](https://en.wikipedia.org/wiki/Field_guide) to help detect [undisclosed AI-generated content](https://en.wikipedia.org/wiki/Wikipedia:LLMDISCLOSE) *on Wikipedia*: while some of the signs may be broadly applicable, some may not apply in a non-Wikipedia context.[\[a\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-1) Not all text featuring these indicators is AI-generated, as the [large language models](https://en.wikipedia.org/wiki/Large_language_model) that power AI chatbots are trained on human writing, including Wikipedia. Many elements of AI writing can be found in editorials, blogs, or fan fiction.

Moreover, this list is *descriptive*, not *prescriptive*; it consists of observations, not rules. Advice about formatting or language to avoid can be found in the [policies and guidelines](https://en.wikipedia.org/wiki/Wikipedia:PAG) and the [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:MOS), but does not belong on this page. The patterns listed here are also only potential *signs* of a problem, not *the problem itself*. While many of these issues are immediately obvious and easy to fix—e.g., excessive boldface, broken markup, citation style quirks—they can point to less outwardly visible problems that carry [much more serious policy risks](https://en.wikipedia.org/wiki/Wikipedia:AIFAIL). **Please do not merely treat these signs as the problems to be fixed; that could just make detection harder.** The actual problems are those deeper concerns, so make sure to address them, either yourself or by flagging them, per the [relevant guide](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup/Guide).

The [speedy deletion policy](https://en.wikipedia.org/wiki/Wikipedia:Speedy_deletion) criterion [G15](https://en.wikipedia.org/wiki/Wikipedia:G15) (Unambiguously LLM-generated pages) lists some signs of AI writing, but is limited to the most objective ones. The remaining signs covered here are not sufficient on their own for speedy deletion.

As of October 2026, the most common signs of newly AI-generated text on Wikipedia (besides the unambiguous indicators above) are [Markdown presence](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Use_of_Markdown), [AI edit summaries](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Edit_summaries), [hedging disclaimers about source availability and usage](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Hedging_disclaimers_about_source_availability_and_recommended_usage), [vague expression of connection or association](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Vague_expression_of_connection_or_association), and [canned emphasis on source attribution and media coverage](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Canned_emphasis_on_notability,_attribution,_and_media_coverage).

**Caveats**

**AI detection tools**

[Shortcuts](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AIDETECTION**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIDETECTION&redirect=no)  
* [**WP:AIDETECTOR**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIDETECTOR&redirect=no)

*See also: [Wikipedia:WikiProject AI Cleanup/Guide and resources § LLM detection software](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup/Guide_and_resources#LLM_detection_software)*

Do not solely rely on [artificial intelligence content detection](https://en.wikipedia.org/wiki/Artificial_intelligence_content_detection) tools (such as [GPTZero](https://en.wikipedia.org/wiki/GPTZero) and [Pangram](https://en.wikipedia.org/wiki/Pangram_\(AI_detector\))). While they perform better than random chance, these tools have non-trivial error rates.[\[1\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Russell-2)[\[2\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-dik2025-3) Detectors can be susceptible to factors such as text modifications (e.g. paraphrasing, markup, and spacing changes) and the use of models not seen during detector training.[\[3\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-4) A high percentage of detected AI writing from the results of a detection tool is **not** a valid criterion for speedy deletion under G15.

**Your detection ability**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AIDETECTIVE**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIDETECTIVE&redirect=no)

|  | Test your AI detection skills at [Wikipedia:AI or not quiz](https://en.wikipedia.org/wiki/Wikipedia:AI_or_not_quiz). |
| :---- | :---: |

Do not rely too much on your own judgment. Humans are notoriously bad at distinguishing human and LLM-generated text. While research on humans' abilities to detect AI-generated text is still limited, a 2025 study has shown that human ability to distinguish LLM text from human is no better than random chance.[\[4\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-cheng2025-5) Another 2025 study on German theses has shown that humans managed a "recognition rate of 57 % for AI texts and 64 % for human-generated texts".[\[5\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-fiedler2025-6)

In a 2025 preprint, a subset of 'expert' annotators correctly identified 90% of AI-generated text (and misidentified 3.3% of human-written text) as AI-generated. Study participants who didn't use LLMs much did only slightly better than random chance (in both directions).[\[1\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Russell-2)

Note, also, that human speech and writing is being influenced by LLMs, and thus they are becoming more similar. This was already evident in 2024, as shown by a study that detected a significant LLM influence in spoken content (e.g. conversational podcasts).[\[6\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-yakura2024-7) Further studies seem to confirm this influence on language,[\[7\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-geng2025-8) including semantics and word choices.[\[8\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-galpin2025-9) However, this is a lagging and patchwork process, and the reverse is not true: LLM output is not becoming more similar to that of human writing.[\[9\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-graphite-10)

**Content**

[Shortcuts](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AIWTW**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIWTW&redirect=no)  
* [**WP:AI-ISM**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AI-ISM&redirect=no)  
* [**WP:LLMISM**](https://en.wikipedia.org/w/index.php?title=Wikipedia:LLMISM&redirect=no)

LLMs (and [artificial neural networks](https://en.wikipedia.org/wiki/Artificial_neural_network) in general) use statistical algorithms to guess (infer) what should come next based on a large corpus of training material. It thus tends to [regress to the mean](https://en.wikipedia.org/wiki/Regression_to_the_mean); that is, the result tends toward the most statistically likely result that applies to the widest variety of cases. Most LLM-based tools then undergo another round of adjustment, called [reinforcement learning from human feedback](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback), to tailor its output toward the most broadly palatable prose. This can simultaneously be a strength and a "tell" for detecting AI-generated content.

For example, LLMs are usually trained on data from the internet in which famous people are generally described with positive, important-sounding language. Consequently, the LLM tends to omit specific, unusual, nuanced facts (which are statistically rare) and replace them with more generic, positive descriptions (which are statistically common). Thus the highly specific "inventor of the first train-coupling device" might become "a revolutionary titan of industry". It is like shouting louder and louder that a portrait shows a uniquely important person, while the portrait itself is fading from a sharp photograph into a blurry, generic sketch. The subject becomes simultaneously less specific and more exaggerated.[\[b\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-11)

This statistical regression to the mean, a smoothing over of specific facts into generic statements, that could equally apply to many topics, makes AI-generated content easier to detect.

**Undue emphasis on significance, legacy, and broader trends**

[Shortcuts](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AILEGACY**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AILEGACY&redirect=no)  
* [**WP:AITREND**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AITREND&redirect=no)

|  | Words to watch: *stands/serves as*, *is a testament/reminder*, *a crucial/pivotal/vital/significant/key role/moment*, *underscores/highlights its importance/significance*, *reflects broader*, *symbolizing its ongoing/enduring/lasting*, *contributing to the*, *setting the stage for*, *marking/shaping the*, *represents/marks a shift*, *key turning point*, *evolving landscape*, *focal point*, *indelible mark*, *deeply rooted*, *distinction \[matters/is important\] because*... ... |
| :---- | :---- |

LLM writing often [puffs up](https://en.wikipedia.org/wiki/Wikipedia:Puffery) the importance of the subject matter by adding statements about how arbitrary aspects of the topic represent or contribute to a broader topic.[\[10\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-chronicle-12)[\[11\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-sun-13) There is a distinct and easily identifiable repertoire of ways that it writes these statements.[\[12\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Juzek-14)

**Examples**

| From [this September 2024 revision](https://en.wikipedia.org/wiki/Special:Diff/1252053288) to [Statistical Institute of Catalonia](https://en.wikipedia.org/wiki/Statistical_Institute_of_Catalonia) |
| ----- |
|  |

| From [this October 2024 revision](https://en.wikipedia.org/wiki/Special:Diff/1248482444) to [Kumba, Cameroon](https://en.wikipedia.org/wiki/Kumba,_Cameroon) |
| ----- |
|  |

Another common manifestation of this sign is AI chatbots situating an article subject amid broader "debates," or noting that a subject has "participated in public discussions".

| From [this October 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1317624451) to [Deadbot](https://en.wikipedia.org/wiki/Deadbot) |
| ----- |
|  |

LLMs may even include these statements for even the most mundane of subjects like etymology or population data. Sometimes, they add hedging preambles acknowledging that the subject is of relatively low importance, before talking about its importance anyway.

| From [this December 2024 revision](https://en.wikipedia.org/wiki/Special:Diff/1265870147) to [Bacnotan](https://en.wikipedia.org/wiki/Bacnotan) |
| ----- |
|  |

| From [Draft:Goebel Goe II](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Goebel_Goe_II) (July 2025\) |
| ----- |
|  |

When talking about biology (e.g., when asked to discuss an animal or plant species), LLMs tend to over-emphasize connections to the broader ecosystem or environment, even when those connections are tenuous or generic. LLMs also tend to belabor the species' conservation status and research and preservation efforts, even if the status is unknown and no serious efforts exist.

| From [this July 2024 revision](https://en.wikipedia.org/wiki/Special:Diff/1235454313) to [Lethrinops lethrinus](https://en.wikipedia.org/wiki/Lethrinops_lethrinus) |
| ----- |
|  |

| From [this December 2024 revision](https://en.wikipedia.org/wiki/Special:Diff/1262033910) to [Nototrichium divaricatum](https://en.wikipedia.org/wiki/Nototrichium_divaricatum) |
| ----- |
|  |

As of mid-2026, LLMs frequently include these alongside [hedging disclaimers](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Hedging_disclaimers_about_source_availability_and_recommended_usage), editorializing about how a particular distinction or nuance is important.

**Canned emphasis on notability, attribution, and media coverage**

[Shortcuts](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:OVERATTRIBUTION**](https://en.wikipedia.org/w/index.php?title=Wikipedia:OVERATTRIBUTION&redirect=no)  
* [**WP:AIATTR**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIATTR&redirect=no)

*For non-AI-specific guidance about this, see [Wikipedia:Citing sources § In-text attribution](https://en.wikipedia.org/wiki/Wikipedia:Citing_sources#In-text_attribution).*

|  | Words to watch: *independent coverage*, *local/regional/national/\[country name\] media outlets*, *music/business/tech outlets*, *trade publications*, *cited/featured/profiled in*, *written by a leading expert*, *active social media presence*, *was identified by* |
| :---- | :---- |

Similarly, LLMs act as if the best way to prove that a subject is notable is to hit readers over the head with claims of notability, often by detailing sources that a subject has been covered in and specifying what kind of sources they are (e.g., trade publications, regional media, etc). They often inaccurately attribute their own [superficial analyses](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Superficial_analyses) to the source. This is more common in text from AI tools released in 2025 or later.

This sign is narrow and distinct from human-written press releases, which have of course also cited news clippings for decades. The distinctions are the idiosyncratic phrasing above and the fact that the focus is placed on characteristics of *the sources themselves*: their contents, their availability/unavailability in public searching, and their classification in relation to the media landscape and the article's subject. When LLMs are asked to write a Wikipedia article, the result often echoes the exact wording of [Wikipedia's guidelines](https://en.wikipedia.org/wiki/Wikipedia:N) like "independent coverage," as if the LLM has collapsed the context between the edit and its justification.[\[c\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-15)

In articles about people or entities that use social media, LLMs will often note that they "maintain an active social media presence" or something similar. This wording is particularly idiosyncratic to AI text and relatively uncommon on Wikipedia before \~2024.

**Examples**

| Early 2025 |
| ----- |
|  |

| August 2025 |
| ----- |
|  |

| November 2025 |
| ----- |
|  |

**Superficial analyses**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:SUPERFICIAL**](https://en.wikipedia.org/w/index.php?title=Wikipedia:SUPERFICIAL&redirect=no)

|  | Words to watch: *highlighting/underscoring/emphasizing ...*, *ensuring ...*, *reflecting/symbolizing ...*, *contributing to ...*, *cultivating/fostering ...*, *encompassing ...*, *enhancing ...*, *valuable insights*, *align/resonate with*, |
| :---- | :---- |

AI chatbots tend to insert superficial analysis of information, often in relation to its significance, recognition, or impact.[\[13\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Reinhart-16) This is often done by attaching a [present participle](https://en.wikipedia.org/wiki/Participle#Forms) ("-ing") phrase at the end of sentences, sometimes with [vague attributions](https://en.wikipedia.org/wiki/Wikipedia:AIWEASEL) to third parties (see below).[\[13\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Reinhart-16)[\[10\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-chronicle-12)

For the purpose of Wikipedia, such comments are usually [synthesis](https://en.wikipedia.org/wiki/Wikipedia:SYNTH) or unattributed opinions. Newer chatbots with [retrieval-augmented generation](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) (for example, an AI chatbot that can search the web) may attach these statements to [named sources](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Canned_emphasis_on_notability,_attribution,_and_media_coverage)—e.g., "Roger Ebert highlighted the lasting influence"—regardless of whether those sources say anything close.

**Examples**

| 2023–2025 |
| ----- |
|  |

| July 2026 |
| ----- |
|  |

**Promotional and advertisement-like language**

[Shortcuts](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AIPUFFERY**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIPUFFERY&redirect=no)  
* [**WP:AIPEACOCK**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIPEACOCK&redirect=no)

*For non-AI-specific guidance about this, see [Wikipedia:Manual of Style/Words to watch § Puffery](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Words_to_watch#Puffery).*

*See also: [Wikipedia:Marketing buzzspeak § Marketing buzzspeak and artificial intelligence](https://en.wikipedia.org/wiki/Wikipedia:Marketing_buzzspeak#Marketing_buzzspeak_and_artificial_intelligence)*

|  | Words to watch: *boasts a*, *vibrant*, *rich*, *profound*, *enhancing*, *showcasing*, *exemplifies*, *commitment to*, *natural beauty*, *nestled*, *in the heart of*, *groundbreaking*, *renowned*, *featuring*, *diverse array*,  ... |
| :---- | :---- |

LLMs have serious problems keeping a neutral tone. Even when prompted to use an encyclopedic style, their output will often tend toward advertisement-like writing, or like the prose of a travel guide. This may happen when generating new text or rewriting existing text: for instance, an edit summary claiming a rewrite "removed promotional tone" while actually introducing it. This may also happen when editors are not [deliberately trying to advertise](https://en.wikipedia.org/wiki/Wikipedia:COI) a subject.[\[14\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-rettberg-17)

Note: Not all promotional or spammy writing is AI-generated. LLMs tend to over-use the same set of promotional phrases no matter what the topic. Also, older LLMs (e.g., GPT-4) tend to output more blatantly positive text[\[15\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-sussman-18) than newer LLMs, which are more subtly positive and tend to avoid obviously superlative statements like "the best."

**Subtypes**

When writing about something that could be considered "cultural heritage," LLMs [constantly remind the reader of its importance](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Undue_emphasis_on_significance,_legacy,_and_broader_trends).

| From [this June 2023 revision](https://en.wikipedia.org/w/index.php?title=&diff=1162718043&oldid=) to [Alamata (woreda)](https://en.wikipedia.org/wiki/Alamata_\(woreda\)) |
| ----- |
|  |

| From [this July 2025 revision](https://en.wikipedia.org/w/index.php?title=&diff=1299567515&oldid=) to [Tamil Nadu Tourism Development Corporation](https://en.wikipedia.org/wiki/Tamil_Nadu_Tourism_Development_Corporation) |
| ----- |
|  |

When writing about people or companies, LLMs will often adopt a press-release or commercial-esque tone.

| From [this November 2024 revision](https://en.wikipedia.org/wiki/Special:Diff/1259548187) to [Kenya Airways](https://en.wikipedia.org/wiki/Kenya_Airways) |
| ----- |
|  |

| From [this April 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1285549984) to [Cadillac Sollei](https://en.wikipedia.org/wiki/Cadillac_Sollei) |
| ----- |
|  |

**Vague expression of connection or association**

[Shortcuts](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AICONNECT**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AICONNECT&redirect=no)  
* [**WP:AIASSOCIATION**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIASSOCIATION&redirect=no)

|  | Words to watch: *in connection with/to ...*, *connected with/to*, *in association with ...*, *associated with* |
| :---- | :---- |

Rather than directly stating a connection or relationship between two subjects (e.g., "In 2017, John Doe was the CEO of ExampleCorp", "Professor Jane Doe taught science at Example University"), LLMs will often allude vaguely to the two subjects being "connected to" or "associated with" each other (e.g., "In 2017, sources identified John Doe as being associated with leadership of ExampleCorp", "Professor Jane Doe was connected with science education at Example University"). This pattern is often combined with [promotional buzzspeak](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Promotional_and_advertisement-like_language) and [generic "AI vocabulary"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#High_density_of_%22AI_vocabulary%22_words), e.g. *particularly/widely associated*, sometimes even iteratively like in [this August 2026 revision](https://en.wikipedia.org/w/index.php?title=&diff=1369268966&oldid=) to [Draft:Amir Tajik](https://en.wikipedia.org/wiki/Draft:Amir_Tajik).

**Examples**

| From [this March 2025 revision](https://en.wikipedia.org/w/index.php?title=&diff=1279776010&oldid=) to [Draft:Jacques Blois](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Jacques_Blois_\(linguist\)) |
| ----- |
|  |

| From [this March 2026 revision](https://en.wikipedia.org/w/index.php?title=&diff=1346262620&oldid=) to [Draft:U.S. Patent 9,765,508 B2](https://en.wikipedia.org/wiki/Draft:U.S._Patent_9,765,508_B2) |
| ----- |
|   |

| From [this April 2026 revision](https://en.wikipedia.org/w/index.php?title=&diff=1349742168&oldid=) to [Draft:Karyn Strickler](https://en.wikipedia.org/wiki/Draft:Karyn_Strickler) |
| ----- |
|  |

| From [this June 2026 revision](https://en.wikipedia.org/w/index.php?title=&diff=1361005423&oldid=) to [Glenn R. Conrad](https://en.wikipedia.org/wiki/Glenn_R._Conrad) |
| ----- |
|  |

| From [this July 2026 revision](https://en.wikipedia.org/w/index.php?title=&diff=1365769694&oldid=) to [Draft:Hans Vermeersch](https://en.wikipedia.org/wiki/Draft:Hans_Vermeersch) |
| ----- |
|   |

**Vague attributions and overgeneralization of opinions**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AIWEASEL**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIWEASEL&redirect=no)

*For non-AI-specific guidance about this, see [Wikipedia:Manual of Style/Words to watch § Unsupported attributions](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Words_to_watch#Unsupported_attributions).*

|  | Words to watch: *Industry reports*, *Observers have cited*, *Experts argue*, *Some critics argue*, *several sources/publications* (when only few sources are cited), *such as* (before exhaustive word lists),  ... |
| :---- | :---- |

AI chatbots tend to attribute opinions or claims to some vague authority—a practice called [weasel wording](https://en.wikipedia.org/wiki/Weasel_wording). They also commonly exaggerate the quantity of sources that these opinions are attributed to. They may present views from one or two sources as widely held (often combined with the vague attributions above), mention the existence or opinion of multiple "reviewers" or "scholars" while only citing one person, or imply that lists of examples are non-exhaustive when the sources give no indication that other examples exist.

**Examples**

| From [this June 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1295362066) to [Haolai River](https://en.wikipedia.org/wiki/Haolai_River) |
| ----- |
|  |

| From [this July 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1299755238) to [BRICS](https://en.wikipedia.org/wiki/BRICS) |
| ----- |
|  |

| From [this November 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1323819205) to [Kwararafa Confederacy](https://en.wikipedia.org/wiki/Kwararafa_Confederacy) |
| ----- |
|  |

| From [this December 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1325377957) to [Rubik's WOWCube](https://en.wikipedia.org/wiki/Rubik's_WOWCube). |
| ----- |
|  |

**References**

1. ["BRICS leaders condemn April 22 Pahalgam attack: On terror, zero tolerance"](https://indianexpress.com/article/india/brics-leaders-condemn-jk-pahalgam-attack-on-terror-zero-tolerance-10110505/). *The Indian Express*. July 7, 2025\. Retrieved July 10, 2025\.  
2. ["Rubik's WOWCube"](https://thetoyinsider.com/products/rubiks-wow-cube/). *The Toy Insider*. October 31, 2025\. Retrieved December 2, 2025\.  
3. ["Cubios Inc teams with Spin Master for Rubik's WOWCube gaming platform"](https://www.mojo-nation.com/cubios-inc-teams-with-spin-master-for-rubiks-wowcube-gaming-platform/). *Mojo Nation*. July 26, 2025\. Retrieved December 2, 2025\.

**Outline-like conclusions about challenges and future prospects**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:FACESCHALLENGES**](https://en.wikipedia.org/w/index.php?title=Wikipedia:FACESCHALLENGES&redirect=no)

|  | Words to watch: *Despite its... faces several challenges...*, *Despite these challenges*, *Challenges and Legacy*, *Future Outlook* ... |
| :---- | :---- |

Many LLM-generated Wikipedia articles include a "Challenges" section, which typically begins with a sentence like "Despite its , faces challenges..." and ends with either a vaguely positive assessment of the article subject,[\[1\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Russell-2) or speculation about how ongoing or potential initiatives could benefit the subject. Such paragraphs usually appear at the end of articles with a rigid outline structure, which may also include a separate section for "Future Prospects."*\[positive/promotional words\]\[article subject\]*

Note: This sign is about the rigid formula, not simply the mention of challenges or challenging.

**Examples**

| 2023–2024 |
| ----- |
|  |

| 2025 |
| ----- |
|  |

| July 2026 |
| ----- |
|  |

**"Awards and recognition" section**

Section or subsection headers in the format of " and " are common in (but not exclusive to) AI generated articles. An "Awards and recognition" section is particularly common (indeed, also simply a "Recognition" section). This is a manifestation of AI-generated text's undue and particular focus on [legacy and trends](https://en.wikipedia.org/wiki/Wikipedia:AILEGACY) and its tendency to vaguely allude to ["coverage" or "recognition" of the subject](https://en.wikipedia.org/wiki/Wikipedia:AIATTR) by various outlets. *XY*

While human editors may also include sections about a subject's legacy or impact on the world or their industry, the specific wording of "Awards and recognition" is nearly ubiquitous in AI generated articles, and much more common than in human writing even when comparing against [articles tagged as containing promotional content](https://en.wikipedia.org/wiki/Category:Articles_with_a_promotional_tone).

**Language and grammar**

AI-generated text displays consistent patterns in syntax, word choice, and sentence construction that human writing does not display to nearly the same degree. Conversely, it often struggles to match some syntactic and linguistic patterns characteristic of human writing. Some LLMs deviate more from human writing than others; for example, GPT-4o, the language model used by ChatGPT from May 2024 to August 2025, produces output with more variation from human writing than other contemporaneous language models.[\[13\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Reinhart-16) Since these are linguistic patterns, they occur consistently regardless of the subject matter, which often gives AI-generated text an identifiable "voice".

**High density of "AI vocabulary" words**

[Shortcuts](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AIVOCAB**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIVOCAB&redirect=no)  
* [**WP:AIWORDS**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIWORDS&redirect=no)

|  | Words to watch: *Additionally* (especially beginning a sentence),[\[16\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-geng-22)[\[17\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-huang-23) *align with*,[\[12\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Juzek-14)[\[18\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kobak-24) *boasts* (meaning "has"),[\[19\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Juzek2-25) *bolstered*,[\[18\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kobak-24) *crucial*,[\[1\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Russell-2)[\[16\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-geng-22)[\[17\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-huang-23) *deep dive*,[\[20\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-economistJul2026-26) *delve*,[\[12\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Juzek-14)[\[18\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kobak-24)[\[1\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Russell-2)[\[21\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kriss-27) *emphasizing*,[\[12\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Juzek-14)[\[18\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kobak-24) *enduring*,[\[18\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kobak-24) *enhance*,[\[18\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kobak-24)[\[1\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Russell-2) *fostering*,[\[18\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kobak-24)[\[1\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Russell-2) *garner*,[\[12\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Juzek-14)[\[18\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kobak-24) *highlight* (as a verb),[\[1\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Russell-2)[\[21\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kriss-27) *interplay*,[\[18\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kobak-24) *intricate/intricacies*,[\[12\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Juzek-14)[\[18\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kobak-24)[\[13\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Reinhart-16)[\[21\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kriss-27) *key* (as an adjective),\[[*citation needed*](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)\] *landscape* (as an abstract noun),[\[1\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Russell-2) *meticulous/meticulously*,[\[19\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Juzek2-25)[\[18\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kobak-24) *pivotal*,[\[18\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kobak-24)[\[1\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Russell-2) *robust*, *showcase*,[\[12\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Juzek-14)[\[18\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kobak-24)[\[21\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kriss-27) *tapestry* (as an abstract noun),[\[1\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Russell-2)[\[13\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Reinhart-16)[\[21\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kriss-27) *testament*,[\[1\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Russell-2) *underscore* (as a verb),[\[12\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Juzek-14)[\[18\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kobak-24)[\[1\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Russell-2)[\[21\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kriss-27) *valuable*,[\[16\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-geng-22) *vibrant*[\[13\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Reinhart-16) |
| :---- | :---- |

Many studies have demonstrated that LLMs overuse specific words. These words started appearing far more frequently in text produced after 2022, when LLM chatbots became widely accessible.[\[12\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Juzek-14)[\[18\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kobak-24) They often co-occur in LLM output: where there is one, there are likely others.[\[22\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kousha-28) While most of these studies have analyzed scientific abstracts or fiction, "AI vocabulary" words are also ubiquitous in LLM-based encyclopedias, such as [Grokipedia](https://en.wikipedia.org/wiki/Grokipedia), and in AI-generated Wikipedia text. One or two of these words appearing in an edit may be coincidental, but an edit (post-2022) introducing lots of them, lots of times, is one of the strongest tells for AI use.

The words that LLMs overuse have changed over time. For instance, the word [*delve*](https://en.wiktionary.org/wiki/delve) was famously overused by ChatGPT in 2023 and early 2024, but became less frequent later in 2024, then dropped off sharply in 2025\.[\[23\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-merrill-29)[\[16\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-geng-22) Below is a breakdown of which words frequently recur together during which LLM "era". While these are not hard cutoffs, they should give you a rough idea of how "earlier" vs "later" LLM output reads.

* **2023 to mid-2024** (GPT-4): *Additionally*, *boasts*, *bolstered*, *crucial*, *delve*, *emphasizing*, *enduring*, *garner*, *intricate/intricacies*, *interplay*, *key*, *landscape*, *meticulously*, *pivotal*, *underscore*, *tapestry*, *testament*, *valuable*, *vibrant*  
* **Mid-2024 to mid-2025** (GPT-4o): *align with*, *bolstered*, *crucial*, *emphasizing*, *enhance*, *enduring*, *fostering*, *highlighting*, *pivotal*, *showcasing*, *underscore*, *vibrant*  
* **Mid-2025 to mid-2026** (GPT-5): *emphasizing*, *enhance*, *highlighting*, *showcasing* (plus words associated with ["Canned emphasis on notability, attribution, and media coverage"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Canned_emphasis_on_notability,_attribution,_and_media_coverage))  
* **Mid-2026 and on** (GPT-6): *challenge*, *clearer*, *dependable*, *echoed*, *foster*, *leverage*, *matters*, *multifaceted*, *practical*, *prioritize*, *quietly*, *steady*, *universally* (with much more [period and comma usage](https://en.wikipedia.org/wiki/Em-dash) and shorter sentences around a strict 8–20 word limit)[\[24\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-30)

The distribution of "AI vocabulary" is also somewhat different depending on the chatbot or LLM used.[\[13\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Reinhart-16) Grok output is particularly idiosyncratic: it overuses superficially "scientific" words like *causal*, *empirical*, *correlate*, and continues to overuse *underscore* as of 2026\.

This section is to be taken as literally as possible: a word being overused by AI does *not* imply that its synonyms are also overused. Also, keep context in mind. For example, while the figurative use of "underscore" is ubiquitous in earlier AI text, the word can also refer to a literal underline mark or to [incidental music](https://en.wikipedia.org/wiki/Incidental_music).

**Examples**

| From [this June 2024 revision](https://en.wikipedia.org/wiki/Special:Diff/956642606) to [Howdy Modi](https://en.wikipedia.org/wiki/Howdy_Modi) |
| ----- |
|  |

| From [this December 2024 revision](https://en.wikipedia.org/wiki/Special:Diff/1263234661) to [Jameh Mosque of Ashtarjan](https://en.wikipedia.org/wiki/Jameh_Mosque_of_Ashtarjan), which contains text pasted from [this revision](https://en.wikipedia.org/wiki/Special:Diff/1263233100) to [User:Hodaalamri/Jameh Mosque of Ashtarjan](https://en.wikipedia.org/wiki/User:Hodaalamri/Jameh_Mosque_of_Ashtarjan) |
| ----- |
|  |

| From [this May 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1292567688) to [Somali people](https://en.wikipedia.org/wiki/Somali_people) |
| ----- |
|  |

**Avoidance of basic copulatives ("is"/"are" phrases)**

[Shortcuts](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AINOCOPULA**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AINOCOPULA&redirect=no)  
* [**WP:AIREPRESENTS**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIREPRESENTS&redirect=no)

|  | Words to watch: *serves as/stands as/marks/functions as/operates as/represents \[a\]*, *boasts/features/maintains/offers \[a\]*, *refers to* |
| :---- | :---- |

LLM-generated text often replaces simple constructions that use [copulas](https://en.wikipedia.org/wiki/Copula_\(linguistics\)) such as *is* or *are* with constructions such as *serves as a* or *mark the*. This pattern has been observed in GPT and Gemini models.[\[17\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-huang-23) One study documented an over 10% decrease in the usage of the words *is* and *are* in academic writing in 2023, with no major changes in their frequency before that.[\[25\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-geng2-31) Similarly, LLMs prefer to use [marketing](https://en.wikipedia.org/wiki/Wikipedia:BUZZ)\-related verbs like *features*, *offers*, and the like to their neutral synonym *has*. (Note: Do not confuse this with *has* used in the [present perfect](https://en.wikipedia.org/wiki/Present_perfect) form, as in *has been featured*.) Sometimes--especially in more recent AI output--these constructions are more elaborate and link to [vague expressions of connection or association](https://en.wikipedia.org/wiki/Wikipedia:AICONNECT) between two topics, e.g., *ventured into politics as a candidate* versus *was a candidate*, or *began his career as* versus *was*.

A similar decline in "is"/"are" constructions has been observed on Wikipedia, especially when controlling for lead paragraphs (which usually follow a formulaic structure of "\[article subject\] is...\]" and thus skew the data).[\[17\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-huang-23) It is particularly visible in AI copyedits, which will often "improve" text in this way. The study above also demonstrated that when GPT-3.5 was prompted to "Revise the following sentence" in 10,000 abstracts, the words *is* and *are* appeared less often in the revised versions.[\[25\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-geng2-31)

In lead sentences, LLMs will sometimes avoid *is* by writing *refers to* [as though the article were about the word or term](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Leads_treating_Wikipedia_lists_or_broad_article_titles_as_proper_nouns) instead of the subject directly.

**Examples**

| − | Gallery 825 on \[\[La Cienega Boulevard\]\], which was purchased in 1958, is LAAA's exhibition arm for \[\[contemporary art\]\]. There are four individual gallery spaces\[...\] | \+ | Gallery 825 on \[\[La Cienega Boulevard\]\] serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces\[...\] |
| :---- | :---- | :---- | :---- |

—From [this August 2023 revision](https://en.wikipedia.org/wiki/Special:Diff/1168694674) to [Los Angeles Art Association](https://en.wikipedia.org/wiki/Los_Angeles_Art_Association)

| − | It is Malaysia's first \[\[Malay language\|Malay\]\] daily afternoon \[\[Tabloid (newspaper format)\|Tabloid\]\] \[...\] The ''Harian Metro'' was established in March 1991 and is the first and oldest Malay-language tabloid \[...\] | \+ | It was established in March 1991 as Malaysia's first Malay-language afternoon \[\[Tabloid journalism\|tabloid\]\] \[...\] Harian Metro holds the distinction of being the first and oldest Malay-language tabloid \[...\] |
| :---- | :---- | :---- | :---- |

—From [this November 2024 revision](https://en.wikipedia.org/wiki/Special:Diff/1259995938) to [Harian Metro](https://en.wikipedia.org/wiki/Harian_Metro)

**Negative parallelisms**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AIPARALLEL**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIPARALLEL&redirect=no)

*See also: [Negative parallelism](https://en.wikipedia.org/wiki/Negative_parallelism)*

When LLMs describe a subject, their output may seem as though it is clearing up a common misconception, or as though the audience may be reaching an incomplete or incorrect conclusion about that subject. This kind of contrast can come across as trying to retroactively challenge such thinking by pointing out another characteristic that the subject may possess alongside (or in the place of) one or more previously-mentioned characteristics. While it is common among human writers (especially in "common misconceptions" or "myths busted" [listicles](https://en.wikipedia.org/wiki/Listicle)), it is stereotypically an "AI sign."

**Not just , but also *XY***

It is common for LLMs to use parallel constructions involving "not", "but", or "however" such as "Not only ... but ..." or "It is not just ..., it's ...".[\[26\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-32)[\[1\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Russell-2)[\[23\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-merrill-29)[\[20\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-economistJul2026-26)

**Examples**

| 2024–2025 |
| ----- |
|  |

Yoo Sumin argues that Ne Zha should also be understood as a form of "modern mythology". Rather than simply retelling a classical legend, the film adapts the Nezha story to the emotional concerns and social context of contemporary China. According to Yoo, the film's popularity derives not only from its digital animation and visual spectacle, but also from its ability to make a traditional mythological figure meaningful to contemporary audiences.

— From [this June 2026 revisiion](https://en.wikipedia.org/wiki/Special:Diff/1359424195) to [Ne Zha (2019 film)](https://en.wikipedia.org/wiki/Ne_Zha_\(2019_film\))

Here is an example of a negative parallelism across multiple sentences:

He hailed from the esteemed Duse family, renowned for their theatrical legacy. Eugenio's life, however, took a path that intertwined both personal ambition and familial complexities.

— From [this April 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1284729136) to [Eugenio Duse](https://en.wikipedia.org/wiki/Eugenio_Duse)

**Not , but *XY***

Another common LLM pattern is parallelisms that explicitly state that a particular item doesn't possess the first characteristic at all. Such constructions are often expressed as "It's not ..., it's ..." or "no ..., no ..., just ...".[\[21\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kriss-27)[\[20\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-economistJul2026-26)

**Examples**

| From [this May 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1288356293) to [Self-portrait (Yayoi Kusama)](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Self-portrait_\(Yayoi_Kusama\)) |
| ----- |
|  |

| From [this June 2025 comment](https://en.wikipedia.org/wiki/Wikipedia:Articles_for_deletion/Lilly_Contino#c-Momentoftrue-20250617223200-Lilly_Contino) at [Wikipedia:Articles for deletion/Lilly Contino](https://en.wikipedia.org/wiki/Wikipedia:Articles_for_deletion/Lilly_Contino) |
| ----- |
|  |

***Y*** **rather than *X***

This pattern may also be reversed, a construction particularly common in recent LLM output.

**Examples**

Chiang's strategy emphasized military suppression of these holdouts to enforce subordination, prioritizing empirical consolidation of power amid fragmented loyalties rather than ideological purity.

— From [this April 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1349156160) to [First Battle of Guilin](https://en.wikipedia.org/wiki/First_Battle_of_Guilin), which explicitly states it is from Grokipedia

**Leads treating Wikipedia lists or broad article titles as proper nouns**

In AI-generated articles about topics with a title that is not a [proper name](https://en.wikipedia.org/wiki/Proper_name), such as a [list](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Lists), the first sentence of the lead may introduce or define the article's title as if it were a standalone real-world entity. While the [MOS](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Lead_section#Format_of_the_first_sentence) does allow such titles to be included at the beginning of the lead "in a natural way", these AI leads tend not to be so natural.

**Examples**

| From [this October 2024 revision](https://en.wikipedia.org/wiki/Special:Diff/1248996099) to [Catchment area (health)](https://en.wikipedia.org/wiki/Catchment_area_\(health\)) |
| ----- |
|  |

| From [this July 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1299100685) to [EuroGames editions](https://en.wikipedia.org/wiki/EuroGames_editions) |
| ----- |
|  |

| From [this July 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1300476090) to [List of songs about Mexico](https://en.wikipedia.org/wiki/List_of_songs_about_Mexico) |
| ----- |
|  |

**Rule of three**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:RO3**](https://en.wikipedia.org/w/index.php?title=Wikipedia:RO3&redirect=no)

LLMs overuse the [rule of three](https://en.wikipedia.org/wiki/Rule_of_three_\(writing\)). This can take different forms, from ", , " to ", , and ".[\[1\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Russell-2)[\[21\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kriss-27)[\[20\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-economistJul2026-26) LLMs often use this structure to make [superficial analyses](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Superficial_analyses) appear more comprehensive.*adjectiveadjectiveadjectiveshort phraseshort phraseshort phrase*

This sign is stronger when it appears in contexts where most people would not bother to include such stylistic flourishes, like [edit summaries](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Edit_summaries).

**Examples**

* \*\*Standard Rotary Saws\*\*: Typically used for drywall and light materials.  
* \*\*Heavy-Duty Rotary Saws\*\*: Designed for tougher materials such as tiles, metals, and plastics.  
* \*\*Corded and Cordless Versions\*\*: Corded rotary saws offer continuous power, while cordless versions provide portability and convenience

\[...\]

* \*\*Construction and Renovation\*\*: For cutting drywall, plywood, and other construction materials.  
* \*\*Electrical and Plumbing\*\*: To create openings for electrical outlets, switches, and plumbing fixtures.  
* \*\*Hobby and Craft\*\*: Used in model making, woodworking, and other craft projects.  
* \*\*Automotive\*\*: Employed in auto body repair and modification tasks.

— From [this July 2024 revision](https://en.wikipedia.org/wiki/Special:Diff/1237779206) to [Rotary saw](https://en.wikipedia.org/wiki/Rotary_saw) (note that these are [canned-format lists](https://en.wikipedia.org/wiki/Wikipedia:AILIST) that used [Markdown](https://en.wikipedia.org/wiki/Wikipedia:MARKDOWN))

The film preserves core elements such as Nezha's mythological image, magical weapons, and spirit of resistance while reshaping them through contemporary values, modern aesthetics, and digital animation technology.

— From [this June 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1359424195) to [Ne Zha (2019 film)](https://en.wikipedia.org/wiki/Ne_Zha_\(2019_film\))

**Style**

**Title case**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AITITLECASE**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AITITLECASE&redirect=no)

*For non–AI-specific guidance about this, see [Wikipedia:Manual of Style/Capital letters § Headings, headers, and captions](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Capital_letters#Headings,_headers,_and_captions).*

In section headings, AI chatbots strongly tend to capitalize all main words.[\[1\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Russell-2)

**Examples**

Impact of Technology and Digitalization

The advent of digital technology and the internet has revolutionized international economic law. \[...\]

Sustainable Development and Environmental Law

The integration of sustainable development goals into international economic law is increasingly important. \[...\]

Human Rights and Economic Law

The relationship between human rights and international economic law is a growing area of focus. \[...\]

— From [this December 2023 revision](https://en.wikipedia.org/wiki/Special:Diff/1189640895) to [International economic law](https://en.wikipedia.org/wiki/International_economic_law)

**Overuse of boldface**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AIBOLD**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIBOLD&redirect=no)

*For non-AI-specific guidance about this, see [Wikipedia:Manual of Style/Text formatting § Boldface](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Text_formatting#Boldface).*

AI chatbots may display various phrases in [boldface](https://en.wikipedia.org/wiki/Boldface) for emphasis in an excessive, mechanical manner. One of their tendencies, inherited from [readmes](https://en.wikipedia.org/wiki/Readme), fan wikis, how-tos, sales pitches, slide decks, listicles and other materials that heavily use boldface, is to emphasize every instance of a chosen word or phrase, often in a "key takeaways" fashion. Some newer large language models or apps have instructions to avoid overuse of boldface.

**Examples**

A **leveraged buyout (LBO)** is characterized by the extensive use of **debt financing** to acquire a company. This financing structure enables **private equity firms** and **financial sponsors** to control businesses while investing a relatively small portion of their own equity. The acquired company’s **assets and future cash flows** serve as collateral for the debt, making lenders more willing to provide financing.

— From [this February 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1274574473) to [Leveraged buyout](https://en.wikipedia.org/wiki/Leveraged_buyout)

**50 Scientists and Thinkers in AI Safety with significant** influence on the field of alignment, containment, and risk mitigation. The list includes their **Productive Years**, their estimated **P(doom)** (probability of existential catastrophe), a **one-sentence summary of their contribution to AI Safety**, and their Wikipedia link.

— From [this November 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1324781030) to [P(doom)](https://en.wikipedia.org/wiki/P\(doom\))

**Inline-header vertical lists**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AILIST**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AILIST&redirect=no)

*For non-AI-specific guidance about this, see [Wikipedia:Manual of Style/Lists § Use prose where understood easily](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Lists#Use_prose_where_understood_easily).*

AI chatbots output often includes vertical lists formatted in a specific way: an ordered or unordered list where the list marker (number, bullet, dash, etc.) is followed by an inline boldfaced header, separated with a colon from the remaining descriptive text.

Instead of [proper wikitext](https://en.wikipedia.org/wiki/H:LIST), a bullet point in an unordered list may appear as a bullet character (•), hyphen (-), en dash (–), [hash](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Use_of_Markdown) (\#), [emoji](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Emoji_as_formatting), or similar character. Ordered lists (i.e. numbered lists) may use explicit numbers (such as ) instead of standard wikitext. When [copied as bare text appearing on the screen](https://en.wikipedia.org/wiki/Wikipedia:SCOPY), some of the formatting information is lost, and line breaks may be lost as well.1\.

**Examples**

| From [this October 2024 comment](https://en.wikipedia.org/wiki/Wikipedia:Articles_for_deletion/Sarwan_Kumar_Bheel#c-IOmParkashSarwanBheel-20241014082300-Saqib-20241014080900) at [Wikipedia:Articles for deletion/Sarwan Kumar Bheel](https://en.wikipedia.org/wiki/Wikipedia:Articles_for_deletion/Sarwan_Kumar_Bheel) |
| ----- |
|  |

| From [this November 2024 revision](https://en.wikipedia.org/wiki/Special:PermanentLink/1255717748) to [Sundial (weapon)](https://en.wikipedia.org/wiki/Sundial_\(weapon\)) |
| ----- |
|  |

| From [this October 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1316572059) to [Draft:AI Visibility Optimization](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/AI_Visibility_Optimization_\(AVO\)) |
| ----- |
|   |

| From [this December 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1327088410) to [Navipet](https://en.wikipedia.org/wiki/Navipet) |
| ----- |
|   |

| From [this March 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1345180164) to [Wikipedia:Requests for page protection/Increase](https://en.wikipedia.org/wiki/Wikipedia:Requests_for_page_protection/Increase) |
| ----- |
|  |

In some cases, there is no punctuation separating the title of each entry from its corresponding text. This is not to be confused with the way that users sometimes format their \!votes in [XfD](https://en.wikipedia.org/wiki/Wikipedia:XFD) discussions, where words like Keep or Delete are typically written in boldface to set it apart from the arguments for the desired outcome.

| From [this December 2025 comment](https://en.wikipedia.org/wiki/Talk:Fish_and_chips/Archive_1#Expanding_the_%22Origins%22_section_to_acknowledge_Portuguese_culinary_technology) at [Talk:Fish and chips](https://en.wikipedia.org/wiki/Talk:Fish_and_chips) |
| ----- |
|  |

**Heading errors**

**Title heading**

AI chatbots tend to put a heading with the article name before all the content, since they don't usually imagine the title header when you make an article as being already there.

**Examples**

[**Pixaroo**](https://www.youtube.com/@Pixaroo-kid)

— From [this August 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1367361447) to [Draft:Pixaroo](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Pixaroo)

**Skipping heading levels**

AI chatbots tend to skip level 2 headings () and start sections from the third level (). [Because doing so is against Wikipedia's accessibility and style conventions](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Accessibility#Headings), it is very unlikely for a manually-formatted page to have this quirk.\=====

**Overuse of level 1 headings**

Level 1 headings are very rare and are typically not used. They are not even listed separately in [the headings section](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Accessibility#Headings), and it's typically only used by the MediaWiki system for the article lead.

This might be caused because of the AI translating [Markdown](https://en.wikipedia.org/wiki/Markdown) to wikitext.

**Examples**

**\= '''\[https\://www\.youtube.com/@Pixaroo-kid Pixaroo\]''' \=**  
\[...\]  
**\= History \=**  
\[...\]  
**\= Programming \=**  
\[...\]  
**\= Main Characters \=**  
\[...\]  
**\= Educational Goals \=**  
\[...\]  
**\= Style \=**  
\[...\]  
**\= Target Audience \=**  
\[...\]  
**\= External Links \=**  
\[...\]

— From [this August 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1367361447) to [Draft:Pixaroo](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Pixaroo)

**Headings only containing other headings**

AI chatbots may generate a heading that only stores other headings, without text of their own.

**Examples**

Programming

Pixy's Adventure Club

\[...\]

Main Characters

Pixy

\[...\]

— From [this August 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1367361447) to [Draft:Pixaroo](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Pixaroo)

**Emoji as formatting**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AIEMOJI**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIEMOJI&redirect=no)

AI chatbots have used [emoji](https://en.wikipedia.org/wiki/Emoji) in the past.[\[23\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-merrill-29)[\[16\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-geng-22) In particular, they sometimes decorated section headings or bullet points by placing emoji in front of them. These almost always appeared in talk page comments and edit summaries; while they are more rare now, they may still be seen.

**Examples**

| From [this April 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1285703047) to [User:Bhaskar sunsari](https://en.wikipedia.org/wiki/User:Bhaskar_sunsari) |
| ----- |
|   |

| From [this May 2025 comment](https://en.wikipedia.org/wiki/Wikipedia:Village_pump_\(policy\)/Archive_202#c-Diamondtier-20250525141800-Diamondtier-20250525141800) at [Wikipedia:Village pump (policy)](https://en.wikipedia.org/wiki/Wikipedia:Village_pump_\(policy\)) |
| ----- |
|  |

| From [this July 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1302443439/1303522049) to [History of trigonometry](https://en.wikipedia.org/wiki/History_of_trigonometry) |
| ----- |
|  |

**Unusual use of tables**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AITABLE**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AITABLE&redirect=no)

Some AIs create small, minimally formatted tables that could be better represented as prose or an [infobox](https://en.wikipedia.org/wiki/Wikipedia:INFOBOX).

**Examples**

| From [this November 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1323402246) to [Draft:Biobanks in India](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Biobanks_in_India) |
| ----- |
|   |

| From [this May 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1352783863) to [Draft:Pacific Mall](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Pacific_Mall,_Tagore_Garden) |
| ----- |
|   |

| From [these](https://en.wikipedia.org/wiki/Special:PermanentLink/1365728625#Shared_Artifact_Types_in_Shan_Culture) [sections](https://en.wikipedia.org/wiki/Special:PermanentLink/1365728625#5.3_Comparison_of_Traditions) of a July 2026 revision to [Xorai](https://en.wikipedia.org/wiki/Xorai) |
| ----- |
|   |

Sometimes, AIs will attempt to insert [markdown table formatting](https://en.wikipedia.org/wiki/Wikipedia:AIMARKDOWN) inside wikitables, which renders as an obvious garbled mess.

**Curly quotation marks and apostrophes**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AICURLY**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AICURLY&redirect=no)

*For non-AI-specific guidance about this, see [Wikipedia:Manual of Style § Quotation characters](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style#Quotation_characters), and [Wikipedia:Manual of Style § Apostrophes](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style#Apostrophes).*

ChatGPT and [DeepSeek](https://en.wikipedia.org/wiki/DeepSeek) typically use curly quotation marks (“...” or ‘...’) instead of straight quotation marks ("..." or '...'). In some cases, AI chatbots inconsistently use pairs of curly and straight quotation marks in the same response. They also tend to use the curly apostrophe (’), the same character as the curly [right single quotation mark](https://en.wikipedia.org/wiki/Right_single_quotation_mark), instead of the straight apostrophe ('), such as in [contractions](https://en.wikipedia.org/wiki/Contraction_\(grammar\)) and [possessive forms](https://en.wikipedia.org/wiki/English_possessive). They may also do this inconsistently.

Curly quotes alone do not prove LLM use. Directional quotation marks (curly or typographer) are often used in published works written and edited using the [Chicago Manual of Style](https://en.wikipedia.org/wiki/Chicago_Manual_of_Style).[\[27\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-33) [Microsoft Word](https://en.wikipedia.org/wiki/Microsoft_Word) has a "[smart quotes](https://en.wikipedia.org/wiki/Smart_quotes)" feature that converts straight quotes to curly quotes. So does the default system-wide configuration on [macOS](https://en.wikipedia.org/wiki/MacOS) and [iOS](https://en.wikipedia.org/wiki/IOS) devices, except on some applications (or if turned off, as may be necessary for [programming](https://en.wikipedia.org/wiki/Computer_programming)). Grammar correcting tools such as [LanguageTool](https://en.wikipedia.org/wiki/LanguageTool) may also have such a feature. Curly quotation marks and apostrophes are common in professionally typeset works such as major newspapers. Citation tools like [Citer](https://citer.toolforge.org/) may repeat those that appear in the title of a web page: for example,

McClelland, Mac (2017-09-27). ["When ‘Not Guilty’ Is a Life Sentence"](https://www.nytimes.com/2017/09/27/magazine/when-not-guilty-is-a-life-sentence.html). *The New York Times*. Retrieved 2025-08-03.

Note that Wikipedia allows users to [customize](https://en.wikipedia.org/wiki/Wikipedia:CUSTOM) the fonts used to display text. Some fonts display matched curly apostrophes as straight, in which case the distinction is invisible to the user. Additionally, [Gemini](https://en.wikipedia.org/wiki/Gemini_\(language_model\)) and [Claude](https://en.wikipedia.org/wiki/Claude_\(language_model\)) models typically do not use curly quotes.

**Communication intended for the user**

**Collaborative communication**

[Shortcuts](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:CERTAINLY**](https://en.wikipedia.org/w/index.php?title=Wikipedia:CERTAINLY&redirect=no)  
* [**WP:COLLABCOMM**](https://en.wikipedia.org/w/index.php?title=Wikipedia:COLLABCOMM&redirect=no)

|  | Words to watch: *a Wikipedia-style article*, *I hope this helps*, *Of course\!*, *Certainly\!*, *You're absolutely right\!*, *Would you like...*, *is there anything else*, *let me know*, *more detailed breakdown*, *here is a* ... |
| :---- | :---- |

Editors sometimes paste text from an AI chatbot that was meant as correspondence, prewriting or advice, rather than article content. This may appear in article text or within comments ().\<\!-- \--\>

**Examples**

| 2023–2025 |
| ----- |
|  |

Delete this section before submission. After pasting the article, convert as many items as possible in the citation list into inline references attached to the exact sentences they support. If a reviewer questions print-era sources, explain that the article relies on identifiable published books, journals and newspapers from the pre-internet period, several of which survive only as scans from original printed copies.

— From [this April 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1348412352) to [Draft:Gurmukh Singh Jeet](https://en.wikipedia.org/wiki/Draft:Gurmukh_Singh_Jeet)  
*\<\!-- WIKIPEDIA DRAFT — Triple Entry Accounting, version 2 \--\>*  
*\<\!-- Written to Wikipedia Manual of Style. Neutral tone, sourced throughout. \--\>*  
*\<\!-- Author has declared a conflict of interest. Submit via WP:AFC. \--\>*  
*\<\!-- Disclose COI on Talk page and in edit summary before saving. \--\>*

*\<\!-- SUBMISSION NOTES \--\>*  
*\<\!-- 1\. This article should be created at "Triple Entry Accounting" (not "Triple-entry accounting" — follow Grigg's own capitalisation in the JRFM title). \--\>*  
*\<\!-- 2\. The existing article [\[\[Momentum accounting and triple-entry bookkeeping\]\]](https://en.wikipedia.org/wiki/Momentum_accounting_and_triple-entry_bookkeeping) needs a hatnote added pointing here. \--\>*  
*\<\!-- 3\. Submit via WP:AFC (Articles for Creation), not directly to mainspace. \--\>*  
*\<\!-- 4\. Declare COI explicitly: in the AFC submission notes, on the article Talk page, and in the edit summary. \--\>*  
*\<\!-- 5\. Post to WP:COIN (Conflict of Interest Noticeboard) after submission. \--\>*  
*\<\!-- 6\. The Finanstilsynet citation currently relies on Sunde's paper as intermediary. If a direct sandbox report URL exists on finanstilsynet.no, substitute it. \--\>*  
*\<\!-- 7\. The diagram uploaded by the user (showing REA/TEA/Blockchain streams) would be excellent as a figure, but requires CC-BY-SA release by its creator before it can be uploaded to Wikimedia Commons. \--\>*

— From [Draft:Triple Entry Accounting](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Triple_Entry_Accounting) in May 2026, incorrectly advising a user with a COI to self-report to COI/N "after submission"  
**\== Before creating a real Wikipedia page \==**  
To have a good chance of acceptance, your channel should ideally have:  
**\*** Over **'''100,000 subscribers'''** (not required, but often helps)  
**\*** Coverage in **'''reliable independent news sources'''**  
**\*** Awards or industry recognition  
**\*** Significant cultural or educational impact  
**\*** Independent references that verify the information

— From [Draft:Pixaroo](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Pixaroo) in August 2026, telling the user what to have before creating a Wikipedia page

**Hedging disclaimers about source availability and recommended usage**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AIDISCLAIMER**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIDISCLAIMER&redirect=no)

|  | Words to watch: *While specific details are limited/scarce...*, *not widely available/documented/disclosed*, *...in the provided/available sources / search results...*, *\[claim\] should be \[treated/presented\] as... rather than...*, *based on available information*, *...does not by itself establish...* ... |
| :---- | :---- |

Chatbots with [retrieval-augmented generation](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) (e.g., the ability to search the web) often fail to find sources on a given topic, or to find information within the sources a user provides. When this happens, they often output a statement claiming that the information is not publicly available. They may also pair it with text about what that information "likely" may be and why it is significant. This information is entirely [speculative](https://en.wikipedia.org/wiki/Wikipedia:OR) (including the very claim that it's "not documented") and may be based on loosely related topics or completely fabricated. When that unknown information is about an individual's personal life, this disclaimer often states that the person "maintains a low profile", "keeps personal details private", etc. This is also speculative.

As of mid-2026, chatbots frequently include disclaimers about how sources should be used, similarly to the ["didactic disclaimers"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Didactic_disclaimers_\(November_2022%E2%80%932024\)) common in GPT-4 output. Generally, these take the form of [negative parallelism](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Y_rather_than_X) constructions warning that a source or claim should be treated as \[something speculative/subjective/symbolic\] rather than \[something definitive/verified\], or cautioning that the available information does not support \[some firm conclusion\].[\[9\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-graphite-10)

**Examples**

| 2023–2025 |
| ----- |
|  |

As an underground release, detailed lyrics are not widely transcribed on major sites like Genius or AZLyrics, likely due to the artist's limited mainstream exposure. My analysis is based on available track titles, featured artists, public song snippets from streaming platforms (e.g., Spotify, Apple Music, Deezer), and Honcho's overall discography themes. Where lyrics aren't fully accessible, I've inferred common motifs from similar trap tracks and Honcho's style. ...For deeper insights, listening to tracks on platforms like Spotify or Deezer is recommended, as lyrics and production details aren't fully documented in public sources.

— From [Draft:Haiti Honcho](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Haiti_Honcho) (2026)

\[...\] claims concerning its miraculous suspension should be treated as religious tradition rather than as an archaeological explanation.

— From [this August 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1370834520) to [Nemgiri](https://en.wikipedia.org/wiki/Nemgiri), disclosed as either ChatGPT or Claude

\[...\] The guidance explains why subsurface conditions require separate attention from visible planting. It does not establish that Benjakitti has a particular contamination problem or groundwater configuration.

— From [this October 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1378535842) to [Benjakitti Park](https://en.wikipedia.org/wiki/Benjakitti_Park)

**Phrasal templates and placeholder text**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AIPLACEHOLDER**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIPLACEHOLDER&redirect=no)

AI chatbots may generate responses with fill-in-the-blank [phrasal templates](https://en.wikipedia.org/wiki/Phrasal_template) (as seen in the game [*Mad Libs*](https://en.wikipedia.org/wiki/Mad_Libs)) for the LLM user to replace with words and phrases pertaining to their use case. However, some LLM users forget to fill in those blanks. Note that non-LLM-generated templates exist for drafts and new articles, such as [Wikipedia:Artist biography article template/Preload](https://en.wikipedia.org/wiki/Wikipedia:Artist_biography_article_template/Preload) and pages in [Category:Article creation templates](https://en.wikipedia.org/wiki/Category:Article_creation_templates).

**Examples**

| 2024 |
| ----- |
|  |

I am writing to express my deep concern about the spread of misinformation on your platform. Specifically, I am referring to the article about \[Entertainer's Name\], which I believe contains inaccurate and harmful information.

— From [this March 2025 comment](https://en.wikipedia.org/wiki/Talk:Kjersti_Flaa#Inaccurate_Information) at [Talk:Kjersti Flaa](https://en.wikipedia.org/wiki/Talk:Kjersti_Flaa)

* Official YouTube Channel: *(Add your channel URL here)*  
* Official Website: *(If available)*

— From [this August 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1367361447) to [Draft:Pixaroo](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Pixaroo)

Large language models may also insert placeholder dates like "2025-xx-xx" into citation fields, particularly the access-date parameter and [rarely the date parameter as well](https://en.wikipedia.org/wiki/Special:PermanentLink/1295449767#References), producing errors.

| From [this November 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1324292862) to [Michelle Osis](https://en.wikipedia.org/wiki/Michelle_Osis) |
| ----- |
|  |

**Links to searches**

* [insource:/20\[0-9\]\[0-9\]-(XX\|xx)-(XX\|xx)/](https://en.wikipedia.org/w/index.php?search=insource%3A%2F20%5B0-9%5D%5B0-9%5D-%28XX%7Cxx%29-%28XX%7Cxx%29%2F&title=Special%3ASearch&profile=advanced&fulltext=1&ns0=1)

In some cases, LLM-generated citations may also contain placeholders in other fields.

**Examples**

| From [this December 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1330090335) to [Dmitry Kuznetsov (politician)](https://en.wikipedia.org/wiki/Dmitry_Kuznetsov_\(politician\)) |
| ----- |
|  |

| From [this February 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1337437306) to [Nelly Joy](https://en.wikipedia.org/wiki/Nelly_Joy) |
| ----- |
|  |

LLM-generated infobox edits may contain comments stating that text or images should be added if/when sources are available, and sometimes contain instructions to upload images to Wikimedia Commons. These are not the same as the predefined boilerplate comments included in many templates, such as [Infobox company](https://en.wikipedia.org/wiki/Template:Infobox_company), despite occasional resemblances \-- for example, articles with [Infobox military person](https://en.wikipedia.org/wiki/Template:Infobox_military_person) often contain the boilerplate "Add spouse if reliably sourced." Before citing this sign, check whether the comment in question is part of the infobox template.

**Examples**

\| leader\_name \= \<\!-- Add if available with citation \--\>

— From [this July 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1301011748) to [Pindi Saidpur](https://en.wikipedia.org/wiki/Pindi_Saidpur)

**Markup**

**Use of Markdown**

[Shortcuts](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:MARKDOWN**](https://en.wikipedia.org/w/index.php?title=Wikipedia:MARKDOWN&redirect=no)  
* [**WP:AIMARKDOWN**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIMARKDOWN&redirect=no)

*Further information: [Wikitext wrapped in Markdown code blocks from chatbots](https://en.wikipedia.org/wiki/Wikipedia:AISIGNS/Wikitext_wrapped_in_Markdown_code_blocks_from_chatbots)*

Wikipedia's prose is formatted in [wikitext](https://en.wikipedia.org/wiki/H:WT), a [markup language](https://en.wikipedia.org/wiki/Markup_language) used to tell Wikipedia's [MediaWiki](https://en.wikipedia.org/wiki/MediaWiki) software how to format an article. This is a niche markup language, found mostly on Wikipedia, other Wikimedia wikis, and other MediaWiki-based platforms like [Miraheze](https://en.wikipedia.org/wiki/Miraheze). While LLM-based chatbots do have the ability to produce wikitext, it is neither the most common markup language in their datasets nor the most salient one to their userbase – the overwhelming majority of whom are not Wikipedia editors.

Instead, the default formatting style of most chatbots is Markdown, a markup language conceptually similar to wikitext but more commonly used, especially for technology applications. Their system-level instructions often direct them to format article components like lists and headings with Markdown syntax, and the chatbot apps then render that syntax as formatted text on a user's screen. For example, the system prompt for Claude Sonnet 3.5 (November 2024\) includes:[\[28\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-sonnetprompt-34)

Claude uses Markdown formatting. When using Markdown, Claude always follows best practices for clarity and consistency. It always uses a single space after hash symbols for headers (e.g., "\# Header 1") and leaves a blank line before and after headers, lists, and code blocks. For emphasis, Claude uses asterisks or underscores consistently (e.g., italic or bold). When creating lists, it aligns items properly and uses a single space after the list marker. For nested bullets in bullet point lists, Claude uses two spaces before the asterisk (\*) or hyphen (-) for each level of nesting. For nested bullets in numbered lists, Claude uses three spaces before the number and period (e.g., "1.") for each level of nesting.

As the above indicates, Markdown syntax is completely different from wikitext. Markdown uses asterisks (\*) or underscores (\_) instead of single-quotes (') for bold and italic formatting, hash symbols (\#) instead of equals signs (=) for section headings, parentheses (()) instead of square brackets (\[\]) around URLs, and three symbols (---, \*\*\*, or \_\_\_) instead of four hyphens (----) for thematic breaks.

When told to "generate an article", chatbots often default to using Markdown for the generated output. This formatting is preserved in clipboard text by the copy functions on some chatbot platforms. If instructed to generate content for Wikipedia, the chatbot might "realize" the need to generate Wikipedia-compatible code, and might include a message like *Would you like me to ... turn this into actual Wikipedia markup format (\`wikitext\`)?*[\[d\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-35) in its output. If the chatbot is told to proceed, the resulting syntax is often rudimentary, syntactically incorrect, or both. The chatbot might put its attempted wikitext content in a Markdown-style [fenced code block](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Wikitext_wrapped_in_Markdown_code_blocks_from_chatbots) (its syntax for [preformatted plain text](https://en.wikipedia.org/wiki/Wikipedia:PRE)) surrounded by Markdown-based syntax and content, which may also be preserved by platform-specific copy-to-clipboard functions, leading to a telling footprint of both markup languages' syntax. This might include the appearance of three backticks in the text, such as: .[\[e\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-36)[\[f\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-37)\`\`\`wikitext

The presence of faulty wikitext syntax mixed with Markdown syntax is a strong indicator that content is LLM-generated, especially if in the form of a fenced Markdown code block. However, Markdown *alone* is not such a strong indicator. Software developers, researchers, technical writers, and experienced internet users frequently use Markdown in tools like [Obsidian](https://en.wikipedia.org/wiki/Obsidian_\(software\)) and [GitHub](https://en.wikipedia.org/wiki/GitHub_Flavored_Markdown), and on platforms like [Reddit](https://support.reddithelp.com/hc/en-us/articles/360043033952-Formatting-Guide), [Discord](https://support.discord.com/hc/en-us/articles/210298617-Markdown-Text-101-Chat-Formatting-Bold-Italic-Underline), and [Slack](https://slack.com/help/articles/202288908-Format-your-messages). Some writing tools and apps, such as [iOS Notes](https://en.wikipedia.org/wiki/IOS_Notes), [Google Docs](https://en.wikipedia.org/wiki/Google_Docs), and [Windows Notepad](https://en.wikipedia.org/wiki/Windows_Notepad), support Markdown editing or exporting. The increasing ubiquity of Markdown may also lead new editors to expect or assume Wikipedia to support Markdown by default.

*See also: [Markdown § Examples](https://en.wikipedia.org/wiki/Markdown#Examples)*

**Misuse of asterisks**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AIASTERISK**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIASTERISK&redirect=no)

LLMs incorrectly use asterisks to wrap text that [it intends to be written in boldface](https://en.wikipedia.org/wiki/Wikipedia:AIBOLD).

**Examples**

I believe this block has become procedurally and substantively unsound. Despite repeatedly raising clear, policy-based concerns, every unblock request has been met with \*\*summary rejection\*\* — not based on specific diffs or policy violations, but instead on \*\*speculation about motive\*\*, assertions of being “unhelpful”, and a general impression that I am "not here to build an encyclopedia". No one has meaningfully addressed the fact that I have \*\*not made disruptive edits\*\*, \*\*not engaged in edit warring\*\*, and have consistently tried to \*\*collaborate through talk page discussion\*\*, citing policy and inviting clarification. Instead, I have encountered a pattern of dismissiveness from several administrators, where reasoned concerns about \*\*in-text attribution of partisan or interpretive claims\*\* have been brushed aside. Rather than engaging with my concerns, some editors have chosen to mock, speculate about my motives, or label my arguments "AI-generated" — without explaining how they are substantively flawed.

— From [this April 2025 unblock request](https://en.wikipedia.org/wiki/User_talk:Fileas_Fogg#c-Fileas_Fogg-20250410203700-I_ask_that_this_be_considered_seriously_and_in_good_faith.) at [User talk:Fileas Fogg](https://en.wikipedia.org/wiki/User_talk:Fileas_Fogg)

**Misuse of number signs**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AIHASHTAG**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIHASHTAG&redirect=no)

LLMs incorrectly use to denote section headings, which MediaWiki interprets as a numbered list. \#\#

**Examples**

1. Geography

Villers-Chief is situated in the [Jura Mountains](https://en.wikipedia.org/wiki/Jura_Mountains), in the eastern part of the Doubs department. \[...\]

1. History

Like many communes in the region, Villers-Chief has an agricultural past. \[...\]

1. Administration

Villers-Chief is part of the [Canton of Valdahon](https://en.wikipedia.org/wiki/Canton_of_Valdahon) and the [Arrondissement of Pontarlier](https://en.wikipedia.org/wiki/Arrondissement_of_Pontarlier). \[...\]

1. Population

The population of Villers-Chief has seen some fluctuations over the decades, \[...\]

— From [this June 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1294887075) to [Villers-Chief](https://en.wikipedia.org/wiki/Villers-Chief)

**Unusual link formatting**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AILINK**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AILINK&redirect=no)

Instead of , an LLM might incorrectly format external links in a manner similar to Gemini's [WP:STARTSPAN](https://en.wikipedia.org/wiki/Wikipedia:STARTSPAN) citation formatting, like this: \[Example\](example.com)\[example.com this\]

**Examples**

\- \*\*Recent Changes\*\*: You can track my latest edits \[here\]([https\://en.wikipedia.org/wiki/Special:Contributions/DoubleCrogs](https://en.wikipedia.org/wiki/Special:Contributions/DoubleCrogs)).

\[...\]

**Contact Me**

\- \*\*Talk Page\*\*: If you want to discuss anything related to Wikipedia or need assistance, you can reach out to me on my \[talk page\]([https\://en.wikipedia.org/wiki/User\_talk:DoubleCrogs](https://en.wikipedia.org/wiki/User_talk:DoubleCrogs)).

— From [this August 2024 revision](https://en.wikipedia.org/wiki/Special:Diff/1240254631) to [User:Doublecrogs](https://en.wikipedia.org/wiki/User:Doublecrogs)

\- The Wikipedia entry does not explicitly mention the "Cyberhero League" being recognized as a winner of the World Future Society's BetaLaunch Technology competition, as detailed in the interview with THE FUTURIST (\[https\://consciouscreativity.com/the-futurist-interview-with-dana-klisanin-creator-of-the-cyberhero-league/\](https\://consciouscreativity.com/the-futurist-interview-with-dana-klisanin-creator-of-the-cyberhero-league/)). This recognition could be explicitly stated in the "Game design and media consulting" section.

— From [this May 2025 revision](https://en.wikipedia.org/w/index.php?title=&diff=1290202502&oldid=) to [Talk:Dana Klisanin](https://en.wikipedia.org/wiki/Talk:Dana_Klisanin)

**Thematic breaks between sections**

AI chatbots sometimes include a thematic break () or () between each section in its output.\-------

**Examples**

| From [this March 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1344638960) to [Draft:Ichafu](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Ichafu) |
| ----- |
|  |

| From [this August 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1367361447) to [Draft:Pixaroo](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Pixaroo) |
| ----- |
|  |

**Broken wikitext**

Since AI chatbots are typically not proficient in wikitext and templates, they often produce faulty syntax. A noteworthy instance is garbled code related to [Template:AfC submission](https://en.wikipedia.org/wiki/Template:AfC_submission), as new editors might ask a chatbot how to submit their [Articles for Creation](https://en.wikipedia.org/wiki/Wikipedia:Articles_for_Creation) draft; see [this discussion among AfC reviewers](https://en.wikipedia.org/wiki/Special:PermanentLink/1299830745#Messed_up_templates).

**Examples**

\[\[Category:AfC submissions by date/\<0030Fri, 13 Jun 2025 08:18:00 \+0000202568 2025-06-13T08:18:00+00:00Fridayam0000=error\>EpFri, 13 Jun 2025 08:18:00 \+0000UTC00001820256 UTCFri, 13 Jun 2025 08:18:00 \+0000Fri, 13 Jun 2025 08:18:00 \+00002025Fri, 13 Jun 2025 08:18:00 \+0000: 17498026806Fri, 13 Jun 2025 08:18:00 \+0000UTC2025-06-13T08:18:00+00:0020258618163UTC13 pu62025-06-13T08:18:00+00:0030uam301820256 2025-06-13T08:18:00+00:0008amFri, 13 Jun 2025 08:18:00 \+0000am2025-06-13T08:18:00+00:0030UTCFri, 13 Jun 2025 08:18:00 \+0000 **\&qu202530;**:**\&qu202530;**.\</0030Fri, 13 Jun 2025 08:18:00 \+0000202568\>June 2025\|sandbox\]\]

— From [this revision](https://en.wikipedia.org/wiki/Special:PermanentLink/1295363321) to [User:Dr. Omokhudu Idogho/sandbox](https://en.wikipedia.org/wiki/User:Dr._Omokhudu_Idogho/sandbox)

**Internal formatting and reference markup bugs**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:OAICITE**](https://en.wikipedia.org/w/index.php?title=Wikipedia:OAICITE&redirect=no)

LLM output sometimes exposes its internal formatting metadata, which is an unambiguous indicator that the text originated with AI. The specific bugs vary by chatbot or tool.

**ChatGPT: contentReference, oaicite/oai\_citation, \+1, turn0search0, attributableIndex**

ChatGPT sometimes adds code in the form of , , or in place of links to references in output text.:contentReference\[oaicite:0\]{index=0}Example+1oai\_citation

**Examples**

| From [this June 2025 revision](https://en.wikipedia.org/w/index.php?title=&diff=1294765751&oldid=) to [Talk:Sial (tribe)](https://en.wikipedia.org/wiki/Talk:Sial_\(tribe\)). |
| ----- |
|  |

| From [this June 2025 revision](https://en.wikipedia.org/w/index.php?title=&diff=1296028135&oldid=) to [Talk:Independent Together](https://en.wikipedia.org/wiki/Talk:Independent_Together) |
| ----- |
|  |

| From [this November 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1325099471) to [ISO/IEC 27017](https://en.wikipedia.org/wiki/ISO/IEC_27017) |
| ----- |
|  |

ChatGPT may include (surrounded by Unicode points in the [Private Use Area](https://en.wikipedia.org/wiki/Private_Use_Area)) at the ends of sentences, with the number after "search" increasing as the text progresses. There also exists an alternate shorter form with only the increasing number surrounded by PUA Unicode like . These are places where the chatbot links to an external site, but a human pasting the conversation into Wikipedia has that link converted into placeholder code. This was first observed in February 2025\. Less often, the pattern may appear as a ref name, e.g., \<ref name="0search12"\>.citeturn0search00

A set of images in a response may also render as . Rarely, other markup of a similar style, such as ([example](https://en.wikipedia.org/wiki/Special:PermanentLink/1276934509)), ([example](https://en.wikipedia.org/wiki/Special:PermanentLink/1286349902)), or ([example](https://en.wikipedia.org/wiki/Special:PermanentLink/1276907078)), may appear.iturn0image0turn0image1turn0image4turn0image5citeturn0news0citeturn1file0cite*generated-reference-identifier*

| From [this February 2025 revision](https://en.wikipedia.org/w/index.php?title=&diff=1274664396&oldid=) to [List of English-medium schools in Bangladesh](https://en.wikipedia.org/wiki/List_of_English-medium_schools_in_Bangladesh) |
| ----- |
|  |

| From [Draft:Reze (Chainsaw Man)](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Reze_\(Chainsaw_Man\)) (2025) |
| ----- |
|   |

ChatGPT may add [JSON](https://en.wikipedia.org/wiki/JSON)\-formatted code at the end of sentences in the form of , with and being increasing numeric indices.({"attribution":{"attributableIndex":"*X*\-*Y*"}})*XY*

| From [Draft:Aleftina Evdokimova](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Aleftina_Evdokimova) (2025) |
| ----- |
|  |

| From [this April 2025 revision](https://fr.wikipedia.org/wiki/Special:Diff/225259294) to [fr:Syndicalisme aux États-Unis](https://fr.wikipedia.org/wiki/Syndicalisme%20aux%20%C3%89tats-Unis) |
| ----- |
|  |

**Links to searches**

* ["contentReference" OR "oaicite" OR "oai\_citation"](https://en.wikipedia.org/w/index.php?search=%22contentReference%22+OR+%22oaicite%22+OR+%22oai_citation%22&title=Special%3ASearch)  
* [turn0search0 OR turn0search1 OR turn0search2 OR turn0search3 OR turn0search4 OR turn0search5 OR turn0search6 OR turn0search7](https://en.wikipedia.org/w/index.php?title=Special:Search&search=turn0search0+OR+turn0search1+OR+turn0search2+OR+turn0search3+OR+turn0search4+OR+turn0search5+OR+turn0search6+OR+turn0search7&ns0=1&fulltext=Search)  
* [turn0image0 OR turn0image1 OR turn0image2 OR turn0image3 OR turn0image4 OR turn0image5 OR turn0image6 OR turn0image7](https://en.wikipedia.org/w/index.php?title=Special:Search&search=turn0image0+OR+turn0image1+OR+turn0image2+OR+turn0image3+OR+turn0image4+OR+turn0image5+OR+turn0image6+OR+turn0image7&ns0=1&fulltext=Search)  
* [insource:/turn0(search\|image\|news\|file)\[0-9\]+/](https://en.wikipedia.org/w/index.php?title=Special:Search&search=insource%3A%2Fturn0%28search%7Cimage%7Cnews%7Cfile%29%5B0-9%5D%2B%2F&ns0=1&fulltext=Search)

**Gemini: \[cite: 1\], \[span\_1\](start\_span)**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:STARTSPAN**](https://en.wikipedia.org/w/index.php?title=Wikipedia:STARTSPAN&redirect=no)

Text copied from [Google Gemini](https://en.wikipedia.org/wiki/Google_Gemini) may contain or style markers.\[cite: 1\]\[cite: 3, 12, 13\]

**Examples**

| From [Parmod Maloo](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Parmod_Maloo) in February 2026 |
| ----- |
|  |

Gemini text may also contain formatting bugs in the form of and .\[span\_1\](start\_span)\[span\_1\](end\_span)

| From [this July 2026 revision](https://en.wikipedia.org/w/index.php?title=&diff=1363979466&oldid=) to [Huey Lewis and the News](https://en.wikipedia.org/wiki/Huey_Lewis_and_the_News) |
| ----- |
|  |

**Links to searches**

* ["span 0 start span" OR "span 0 end span" OR "start span span 0" OR "span 1 start span" OR "span 1 end span" OR "start span span 1" OR "span 2 start span" OR "span 2 end span" OR "start span span 2"](https://en.wikipedia.org/w/index.php?search=%22span+0+start+span%22+OR+%22span+0+end+span%22+OR+%22start+span+span+0%22+OR+%22span+1+start+span%22+OR+%22span+1+end+span%22+OR+%22start+span+span+1%22+OR+%22span+2+start+span%22+OR+%22span+2+end+span%22+OR+%22start+span+span+2%22&title=Special%3ASearch&profile=advanced&fulltext=1&ns0=1&ns1=1&ns2=1&ns3=1&ns4=1&ns5=1&ns6=1&ns7=1&ns8=1&ns9=1&ns10=1&ns11=1&ns12=1&ns13=1&ns14=1&ns15=1&ns100=1&ns101=1&ns118=1&ns119=1&ns126=1&ns127=1&ns710=1&ns711=1&ns828=1&ns829=1&ns1728=1&ns1729=1)  
* [insource:"start span" insource:/$star{t}_{s}pan$/](https://en.wikipedia.org/w/index.php?search=insource%3A%22start+span%22+insource%3A%2F%5C%28start_span%5C%29%2F&title=Special%3ASearch&profile=advanced&fulltext=1&ns0=1&ns1=1&ns2=1&ns3=1&ns4=1&ns5=1&ns6=1&ns7=1&ns8=1&ns9=1&ns10=1&ns11=1&ns12=1&ns13=1&ns14=1&ns15=1&ns100=1&ns101=1&ns118=1&ns119=1&ns126=1&ns127=1&ns710=1&ns711=1&ns828=1&ns829=1&ns1728=1&ns1729=1)

**Grok: grok\_card, grok\_render\_citation\_card\_json**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:GROKCARD**](https://en.wikipedia.org/w/index.php?title=Wikipedia:GROKCARD&redirect=no)

Text generated by Grok may occasionally include [XML](https://en.wikipedia.org/wiki/XML)\-styled tags after citations.grok\_card

**Examples**

| From [this November 2025 revision](https://en.wikipedia.org/wiki/Special:PermanentLink/1323207968) to [Draft:Mehak Malik](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Mehak_Malik) |
| ----- |
|  |

Grok may also include in place of links to reference in the output text.grok\_render\_citation\_card\_json

| From [this May 2026 revision](https://en.wikipedia.org/wiki/Special:PermanentLink/1352634865) to [Draft:TUSAŞ Gölge tactical UAV](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/TUSA%C5%9E_G%C3%B6lge_tactical_UAV) |
| ----- |
|  |

**Links to searches**

* [grok-card data-id](https://en.wikipedia.org/w/index.php?search=%22grok-card+data-id%22&title=Special%3ASearch&profile=advanced&fulltext=1&ns0=1&ns1=1&ns2=1&ns3=1&ns4=1&ns5=1&ns6=1&ns7=1&ns8=1&ns9=1&ns10=1&ns11=1&ns12=1&ns13=1&ns14=1&ns15=1&ns100=1&ns101=1&ns118=1&ns119=1&ns126=1&ns127=1&ns710=1&ns711=1&ns828=1&ns829=1&ns1728=1&ns1729=1)

**DeepSeek: lenticular brackets, dagger symbols**

As of June 2025, markup with [lenticular brackets](https://en.wikipedia.org/wiki/Lenticular_brackets) and [dagger symbols](https://en.wikipedia.org/wiki/Dagger_symbol), like , has also been seen. This format appears to be specific to [DeepSeek](https://en.wikipedia.org/wiki/DeepSeek) and its derivatives.[\[29\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-38)【85†L261-269】

| From [this June 2025 revision](https://en.wikipedia.org/wiki/Special:PermanentLink/1295285879) to [Draft:Gillingham High Street](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Gillingham_High_Street) |
| ----- |
|  |

| From [this August 2025 revision](https://en.wikipedia.org/wiki/Special:PermanentLink/1304282215) to [Draft:Paytra](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Paytra) |
| ----- |
|  |

| From [Draft:JAF-GT300](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/JAF-GT300) in March 2026 |
| ----- |
|  |

**Links to searches**

* [insource:/【\[0-9\]+†/](https://en.wikipedia.org/w/index.php?search=insource%3A%2F%E3%80%90%5B0-9%5D%2B%E2%80%A0%2F&title=Special%3ASearch&profile=advanced&fulltext=1&ns118=1) (in drafts only)

**Perplexity: attached\_file, ppl-ai-file-upload**

As of fall 2025, tags like and have been seen at the end of sentences. This may be [Perplexity](https://en.wikipedia.org/wiki/Perplexity_AI)\-specific.[\[30\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-wildperplexityappeared-39)\[attached\_file:1\]\[web:1\]

During his time as CEO, Philip Morris’s reputation management and media relations brought together business and news interests in ways that later became controversial, with effects still debated in contemporary regulatory and legal discussions.\[attached\_file:1\]

— From [this October 2025 revision](https://en.wikipedia.org/w/index.php?title=&diff=1316436509&oldid=) to [Hamish Maxwell](https://en.wikipedia.org/wiki/Hamish_Maxwell)

Perplexity may also cite text to an [Amazon S3](https://en.wikipedia.org/wiki/Amazon_S3) bucket, with in the URL.ppl-ai-file-upload

**Links to searches**

* ["ppl-ai-file-upload"](https://en.wikipedia.org/w/index.php?search=%22ppl-ai-file-upload%22&title=Special%3ASearch&profile=advanced&fulltext=1&ns0=1&ns2=1&ns118=1)

**Unclassified: :::writing**

As of June 1, 2026, markup in the format , where \[NUMBER\] is a random 5-digit number, has been spotted; the triple colons at the beginning may or may not be interpreted as an indent. Triple colons at the end of the "document" are often paired with this. The markup may or may not be in other languages.:::writing{variant="document" id="\[NUMBER\]"}

**Examples**

| From [this June 2026 revision](https://en.wikipedia.org/wiki/Special:PermanentLink/1358854076) to [User:Drrbharanidharan](https://en.wikipedia.org/wiki/User:Drrbharanidharan) |
| ----- |
|  |

| From [this June 2026 revision](https://en.wikipedia.org/wiki/Special:PermanentLink/1357217465) to [Draft:Ak7](https://en.wikipedia.org/wiki/Draft:Ak7) |
| ----- |
|  |

**Non-existent or out-of-place categories**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AIREDCAT**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIREDCAT&redirect=no)

LLMs may hallucinate non-existent categories, sometimes for generic concepts that *seem like* plausible category titles (or [SEO](https://en.wikipedia.org/wiki/Search_engine_optimization) keywords), and sometimes because their training set includes obsolete and renamed categories. These will appear as [red links](https://en.wikipedia.org/wiki/Wikipedia:REDNOT). You may also find category redirects, such as the longtime spammer favorite [Category:Entrepreneurs](https://en.wikipedia.org/wiki/Category:Entrepreneurs). More recent LLMs will occasionally omit punctuation and words in category markup (e.g. [Category people](https://en.wikipedia.org/wiki/Category_people?action=edit&redlink=1) instead of [Category:Living people](https://en.wikipedia.org/wiki/Category:Living_people)), visibly breaking them.

Note that the presence of bad or nonexistent categories does not necessarily prove the use of AI by itself, as human editors regularly make similar mistakes. New users are unlikely to be familiar with Wikipedia's categorization system, and older users may be used to now-deprecated categories. Broken categories are, however, valid corroborating evidence if a page also shows other signs of AI editing, and given that it relies on the removal of actual words from a category name rather than just a coding error alone, the "Category people" form of category breakage is a strong AI tell as this is not an error typically made by human editors.

**Examples**

\[\[**Category**:**American hip hop musicians**\]\]

— From [this August 2025 revision](https://en.wikipedia.org/wiki/Special:PermanentLink/1304282215) to [Draft:Paytra](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Paytra)

rather than

\[\[**Category**:**American hip-hop musicians**\]\]

**Non-existent templates**

LLMs often hallucinate non-existent templates (especially plausible-sounding types of [infoboxes](https://en.wikipedia.org/wiki/Wikipedia:Infoboxes)) and template parameters. These will also appear as red links, and non-existent template parameters in existing templates have no effect. LLMs may also use templates that were deleted after their knowledge cutoff date (such as the [lang-*??* series](https://en.wikipedia.org/wiki/Wikipedia:Templates_for_discussion/Log/2024_September_27/lang-%3F%3F_templates)).

**Examples**

{{**Infobox ancient population**  
\| name \= Gangetic Hunter-Gatherer (GHG)  
\| image \= \[\[**File**:**GHG\_reconstruction.png**\|250px\]\]  
\| caption \= Artistic reconstruction of a Gangetic Hunter-Gatherer male, based on Mesolithic skeletal data from the Ganga Valley  
\| regions \= Ganga Valley (from Haryana to Bengal, between the Vindhyas and Himalayas)  
\| period \= Mesolithic–Early Neolithic (10,000–5,000 BCE)  
\| descendants \= Gangetic peoples, Indus Valley Civilisation, South Indian populations  
\| archaeological\_sites \= Bhimbetka, Sarai Nahar Rai, Mahadaha, Jhusi, Chirand  
}}

— From [this revision](https://en.wikipedia.org/wiki/Special:PermanentLink/1326132735) to [Draft:Gangetic hunter-gatherers](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Gangetic_hunter-gatherers)

rather than

{{**Infobox archaeological culture**  
\| name \= Gangetic Hunter-Gatherer (GHG)  
\| map \= \[\[**File**:**GHG\_reconstruction.png**\|250px\]\]  
\| mapcaption \= Artistic reconstruction of a Gangetic Hunter-Gatherer male, based on Mesolithic skeletal data from the Ganga Valley  
\| region \= Ganga Valley (from Haryana to Bengal, between the Vindhyas and Himalayas)  
\| period \= Mesolithic–Early Neolithic (10,000–5,000 BCE)  
\| followedby \= Gangetic peoples, Indus Valley Civilisation, South Indian populations  
\| majorsites \= Bhimbetka, Sarai Nahar Rai, Mahadaha, Jhusi, Chirand  
}}

**Non-infobox examples**

\== *\<\!-- EDIT BELOW THIS LINE \--\>* \== markup  
{{**Update submission** \|reasons\=Complete biographical rewrite executed to strip out promotional prose. Incorporated independent third-party literary journal analysis from Ashvamegh Journal to satisfy WP:NBIOGRAPHY. \|ts\=2026-06-08T12:19:00Z}}

— From [this revision](https://en.wikipedia.org/wiki/Special:PermanentLink/1358339625) to [User:Blueskyreader/sandbox](https://en.wikipedia.org/wiki/User:Blueskyreader/sandbox)

**Links to searches**

* [Wikipedia:Database reports/Transclusions of non-existent templates](https://en.wikipedia.org/wiki/Wikipedia:Database_reports/Transclusions_of_non-existent_templates) – many of these broken templates are legitimate mistakes, but the "infobox" and "lang" sections are likely to contain LLM hallucinations

**Citations**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AIFICTREF**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIFICTREF&redirect=no)

*For non-AI-specific guidance about this, see [Wikipedia:Fictitious references](https://en.wikipedia.org/wiki/Wikipedia:Fictitious_references).*

*See also: [Template:Failed verification](https://en.wikipedia.org/wiki/Template:Failed_verification)*

**Broken external links**

If a new article or draft has multiple citations with external links, and **several** of them are broken (e.g., non-existent websites or [404 errors](https://en.wikipedia.org/wiki/404_error)), this is a strong sign of an AI-generated page, particularly if the dead links are not found in website archiving sites like the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive). Most links [become broken over time](https://en.wikipedia.org/wiki/Link_rot), but these factors make it unlikely that the link was ever real.

Watch out for: Links that don't work for you, but do work for other people (e.g., journal articles accessed through a university library); links that were mangled by bots and scripts (e.g., to add incorrect identifiers or to remove seemingly unnecessary parts of the URL); links that are missing the start or end (a sign of a human copy/pasting the URL).

**Invalid DOI and ISBNs**

*For non-AI-specific guidance about DOI and ISBNs, see [Wikipedia:DOI](https://en.wikipedia.org/wiki/Wikipedia:DOI) and [Wikipedia:ISBN](https://en.wikipedia.org/wiki/Wikipedia:ISBN).*

A [checksum](https://en.wikipedia.org/wiki/Checksum) can be used to verify [ISBNs](https://en.wikipedia.org/wiki/ISBN). An invalid checksum is a very likely sign that an ISBN is incorrect, and citation templates display [a warning](https://en.wikipedia.org/wiki/Help:CS1_errors#bad_isbn) if so. Similarly, [DOIs](https://en.wikipedia.org/wiki/Digital_object_identifier) are more resistant to link rot than regular hyperlinks. Unresolvable DOIs and invalid ISBNs can be indicators of [hallucinated](https://en.wikipedia.org/wiki/Hallucination_\(AI\)) references.

**DOIs that lead to unrelated articles**

An LLM may generate references to non-existent scholarly articles with DOIs that appear valid but are, in reality, assigned to unrelated articles. Example passage generated by ChatGPT:

Ohm’s Law applies to many materials and components that are "ohmic," meaning their resistance remains constant regardless of the applied voltage or current. However, it does not hold for non-linear devices like diodes or transistors \[1\]\[2\].

1\. M. E. Van Valkenburg, “The validity and limitations of Ohm’s law in non-linear circuits,” Proceedings of the IEEE, vol. 62, no. 6, pp. 769–770, Jun. 1974\. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\)):[10.1109/PROC.1974.9547](https://doi.org/10.1109%2FPROC.1974.9547)

2\. C. L. Fortescue, “Ohm’s Law in alternating current circuits,” Proceedings of the IEEE, vol. 55, no. 11, pp. 1934–1936, Nov. 1967\. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\)):[10.1109/PROC.1967.6033](https://doi.org/10.1109%2FPROC.1967.6033)

Both *Proceedings of the IEEE* citations are completely made up. The DOIs lead to different citations and have other problems as well. For instance, [C. L. Fortescue](https://en.wikipedia.org/wiki/Charles_LeGeyt_Fortescue) was dead for 30+ years at the purported time of writing, and [Vol 55, Issue 11](https://ieeexplore.ieee.org/xpl/tocresult.jsp?isnumber=31102&punumber=5) does not list any articles that match anything remotely close to the information given in reference 2\.

Note: From 2018 to 2023, [a UX issue in VisualEditor](https://phabricator.wikimedia.org/T198456) led many editors to accidentally insert references to [PubMed](https://en.wikipedia.org/wiki/PubMed) articles with low ID numbers (PMIDs), resulting in obviously irrelevant citations like an article about rat livers (PMID 9\) being cited in [List of Disney television films](https://en.wikipedia.org/wiki/Special:Diff/972043377) in 2020\. These may resemble AI hallucinations (and should be fixed regardless), but they generally are not.

**Book citations without page numbers or URLs**

LLMs often generate book citations that do not include page numbers. This passage, for example, was generated by ChatGPT:

Ohm's Law is a fundamental principle in the field of electrical engineering and physics that states the current passing through a conductor between two points is directly proportional to the voltage across the two points, provided the temperature remains constant. Mathematically, it is expressed as V=R, where V is the voltage, I is the current, and R is the resistance. The law was formulated by German physicist Georg Simon Ohm in 1827, and it serves as a cornerstone in the analysis and design of electrical circuits \[1\].

1\. Dorf, R. C., & Svoboda, J. A. (2010). Introduction to Electric Circuits (8th ed.). Hoboken, NJ: John Wiley & Sons. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\)) [9780470521571](https://en.wikipedia.org/wiki/Special:BookSources/9780470521571).

The book reference appears valid – a book on electric circuits would likely have information about Ohm's law – but without the page number, that citation is not useful for verifying the claims in the prose.

Some LLM-generated book citations include page numbers, and the book exists, but the cited pages do not verify the text. Signs to look out for: the book is on a somewhat general topic or frequently referenced in its field, and the citation does not include a URL (not mandatory for book citations, but editors creating legitimate book citations often include a link to [an online version of the text](https://en.wikipedia.org/wiki/Wikipedia:Book_sources#Online_text)). Example:

Analysts note that traditionalists often appeal to prudence, stability, and Edmund Burke’s notion of “prescription,” while reactionaries invoke moral urgency and cultural emergency, framing the present as a deviation from an idealized past. \[1\]

1\. Goldwater, Barry (1960). The Conscience of a Conservative. Victor Publishing. p. 12\.

This may look like a reasonable citation, but searching an [online version of the book for "Burke" produces no results](https://www.google.com/books/edition/The_Conscience_of_a_Conservative/PKd_EQAAQBAJ?hl=en&gbpv=1&bsq=burke).

**Incorrect or unconventional use of references**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AICITESTYLE**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AICITESTYLE&redirect=no)

AI tools may have been prompted to include references, and make an attempt to do so as Wikipedia expects, but fail with some key implementation details or stand out when compared with conventions.

**Examples**

In the first example, note the incorrect attempt at re-using references. The tool used there was not capable of searching for non-confabulated sources (as it was done the day before [Bing](https://en.wikipedia.org/wiki/Microsoft_Bing) Deep Search launched) but nonetheless found one real reference. The syntax for re-using the references was incorrect.

In that case, the *Smith, R. J.* source – being the "third source" the tool presumably generated the link '[https\://pubmed.ncbi.nlm.nih.gov/3'](https://pubmed.ncbi.nlm.nih.gov/3') (which has a PMID reference of 3\) – is also completely irrelevant to the body of the article. The user did not check the reference before they converted it to a {{[cite journal](https://en.wikipedia.org/wiki/Template:Cite_journal)}} reference, even though the links resolve.

The LLM in that case has diligently included the incorrect re-use syntax after every single full stop.

| From [this December 2023 revision](https://en.wikipedia.org/wiki/Special:PermanentLink/1188218670) to [Cognitive orthotics](https://en.wikipedia.org/wiki/Cognitive_orthotics) |
| ----- |
|  |

Some LLMs or chatbot interfaces use the character around footnotes. The character is often used on other websites to provide a link for the user to jump back to the article after reading the footnote.↩

| From [this August 2025 revision](https://en.wikipedia.org/wiki/Special:PermanentLink/1304723248) to [Draft:CureMD](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/CureMD) |
| ----- |
|   |

**utm\_source=**

ChatGPT may add the [UTM parameters](https://en.wikipedia.org/wiki/UTM_parameter) or to URLs that it is using as sources. Microsoft Copilot may add to URLs. Grok uses . Other LLMs, such as Gemini or Claude, use UTM parameters less often.[\[g\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-40)utm\_source=openaiutm\_source=chatgpt.comutm\_source=copilot.comreferrer=grok.com

Note: While this near-definitively proves ChatGPT's involvement,[\[h\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-41) it doesn't prove, on its own, that ChatGPT also generated the writing. Some editors use AI tools to find citations for existing text; this will be apparent in the edit history.

**Examples**

Following their marriage, Burgess and Graham settled in Cheshire, England, where Burgess serves as the head coach for the Warrington Wolves rugby league team. \[https\://www\.theguardian.com/sport/2025/feb/11/sam-burgess-interview-warrington-rugby-league-luke-littler?utm\_source=chatgpt.com\]

— From [this revision](https://en.wikipedia.org/w/index.php?title=&diff=1277944793&oldid=) to [Sam Burgess](https://en.wikipedia.org/wiki/Sam_Burgess)

**Links to searches**

* [utm\_source=chatgpt.com](https://en.wikipedia.org/w/index.php?search=%utm_source=chatgpt.com%22&title=Special:Search&profile=advanced&fulltext=1&ns0=1)  
* [insource:"utm\_source=chatgpt.com"](https://en.wikipedia.org/w/index.php?search=insource%3A%22utm_source%3Dchatgpt.com%22&title=Special%3ASearch&profile=advanced&fulltext=1&ns0=1)  
* [insource:"utm\_source=openai"](https://en.wikipedia.org/w/index.php?search=insource%3A%22utm_source%3Dopenai%22&title=Special%3ASearch&profile=advanced&fulltext=1&ns0=1)  
* [insource:"utm\_source=copilot.com"](https://en.wikipedia.org/w/index.php?search=insource%3A%22utm_source%3Dcopilot.com%22&title=Special%3ASearch&profile=advanced&fulltext=1&ns0=1)  
* [insource:"referrer=grok.com"](https://en.wikipedia.org/w/index.php?search=insource%3A%22referrer%3Dgrok.com%22&title=Special%3ASearch&profile=advanced&fulltext=1&ns0=1)

**Named references declared in references section but unused in article body**

A common referencing error produced by LLMs involves sources in a tag which are not used inline. LLMs can also produce [named references](https://en.wikipedia.org/wiki/Wikipedia:NAMEDREF) which are not defined, although this can also be the result of a copy-paste from a different article. **Examples**\<**references**\>

| From [this May 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1291491974#References) to [Draft:Josef von Rickenbach](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Josef_von_Rickenbach) |
| ----- |
|  |

| From [this May 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1291558682#References) to [Draft:Caligomos Art](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Caligomos_Art) |
| ----- |
|  |

**Links to searches**

* [Category:Pages with incorrect ref formatting](https://en.wikipedia.org/wiki/Category:Pages_with_incorrect_ref_formatting)  
* [Pages without inline citations](https://en.wikipedia.org/w/index.php?title=Special:WhatLinksHere/Template:No_footnotes&hidelinks=1&hidetrans=1)  
* ["Cite error: A list-defined reference named" \+ "is not used in the content (see the help page)."](https://en.wikipedia.org/w/index.php?search=%22Cite+error%3A+A+list-defined+reference+named%22+%22is+not+used+in+the+content+%28see+the+help+page%29.%22&title=Special%3ASearch&profile=advanced&fulltext=1&ns0=1&ns2=1&ns118=1)

**Comment-specific indicators**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AICOMMENT**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AICOMMENT&redirect=no)

*Further information: [Wikipedia:Signs of AI use in comments](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_use_in_comments)*

*See also: [Wikipedia:Identifying LLM unblock requests](https://en.wikipedia.org/wiki/Wikipedia:Identifying_LLM_unblock_requests) and [Wikipedia:The LLM-written ANI report](https://en.wikipedia.org/wiki/Wikipedia:The_LLM-written_ANI_report)*

In many cases, some users have copy-pasted text from AI chatbots into their comments. Comments and nominations suspected of having been pasted from an LLM may be collapsed via {{[collapse AI](https://en.wikipedia.org/wiki/Template:Collapse_AI)}} or closed entirely in accordance with [Wikipedia:Talk page guidelines § LLM-generated](https://en.wikipedia.org/wiki/Wikipedia:Talk_page_guidelines#LLM-generated). Asides from making any of the mistakes listed on this page, editors who use large language models or similar technology to write their comments are also likely to:

* [Misquote policies and guidelines](https://en.wikipedia.org/wiki/Wikipedia:AIFICTPOLICY) and [cite made-up shortcuts](https://en.wikipedia.org/wiki/Wikipedia:AISHORTCUT) that don't lead to any existing project page.  
* [Transclude maintenance banners](https://en.wikipedia.org/wiki/Wikipedia:AITRANSCLUSION) whenever they mention them.  
* Post lengthy comments [divided into sections with titles](https://en.wikipedia.org/wiki/Wikipedia:AISECTION), either written in [Markdown](https://en.wikipedia.org/wiki/Wikipedia:MARKDOWN), plain text, or as [level-2 or level-3 subheadings](https://en.wikipedia.org/wiki/Wikipedia:AISUBHEADING).  
* Downplay their LLM use by [claiming to have put some human effort into their work](https://en.wikipedia.org/wiki/Wikipedia:AIMADEBUTSTILLOK) or that [their comments reflect their thoughts](https://en.wikipedia.org/wiki/Wikipedia:AICOMMENTSAREMINE).  
* [Request input from their critics](https://en.wikipedia.org/wiki/Wikipedia:AIWANTFEEDBACK) or [other editors](https://en.wikipedia.org/wiki/Wikipedia:AIREVIEW) to help them determine [exactly what needs to be improved](https://en.wikipedia.org/wiki/Wikipedia:WHERESTHEAI).  
* Dismiss concerns about the origin of their content as being based on [unsubstantiated speculation](https://en.wikipedia.org/wiki/Wikipedia:AIUNPROVEN) rather than "[concrete](https://en.wikipedia.org/wiki/Wikipedia:CONCRETE)" facts or evidence.  
* Urge critics to [redirect their concerns towards improving content](https://en.wikipedia.org/wiki/Wikipedia:LETSFOCUSON) instead of worrying about whether it was produced by or modified via a large language model.

Many LLM-generated comments tend to sound like they're coming from a [clerk](https://en.wikipedia.org/wiki/Clerk) or [customer service](https://en.wikipedia.org/wiki/Customer_service) representative, with users claiming to have "carefully reviewed" things, [apologizing for any inconvenience they "may have" caused](https://en.wikipedia.org/wiki/Wikipedia:AIUR), and saying things along the lines of "If there are specific issues that need to be resolved, please point them out to me, and I will try to resolve them." Given that AI-powered writing assistance tools are often marketed for use at work, this may not be surprising.

**Links to searches**

* [I understand \[the/your\] concern(s) \[about/regarding\] AI-generated...](https://en.wikipedia.org/w/index.php?search=%22I+understand+concern+AI-generated%22%7E2+OR+%22I+understand+concerns+AI-generated%22%7E2&title=Special%3ASearch&profile=advanced&fulltext=1&ns1=1&ns3=1&ns4=1&ns5=1&ns119=1)  
* Dear Wikipedia Editorial Team:  
  * [I am writing to ...](https://en.wikipedia.org/w/index.php?search=%22Dear+Wikipedia+Editorial+Team%22+%22I+am+writing+to%22&title=Special%3ASearch&profile=advanced&fulltext=1&ns1=1&ns3=1&ns4=1&ns5=1&ns118=1)  
  * [I hope/trust this message finds you well.](https://en.wikipedia.org/w/index.php?search=%22Dear+Wikipedia+Editorial+Team%22+%22this+message+finds+you+well%22&title=Special%3ASearch&profile=advanced&fulltext=1&ns1=1&ns3=1&ns4=1&ns5=1&ns118=1)

**Edit summaries**

[Shortcuts](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AISUMMARY**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AISUMMARY&redirect=no)  
* [**WP:AISUMM**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AISUMM&redirect=no)

AI [edit summaries](https://en.wikipedia.org/wiki/Help:Edit_summary) tend to follow "templates" with distinct idiosyncracies that are uncommon to nonexistent in edit summaries prior to 2023\. The presence of such summaries strongly suggests that the edits themselves are also AI-generated, as it is unlikely someone would use AI for a simple summary but not the much more time-consuming task of writing.

Note that these are *rigid formulae*. The more a summary deviates from the pattern, the less likely it is to be AI-generated. Edit summaries with [common abbreviations](https://en.wikipedia.org/wiki/Wikipedia:Edit_summary_legend), such as "ce" for "copy edit," are also unlikely to be wholly AI-generated.

As with all LLM-generated text, typical AI edit summaries have changed over time. Older AI edit summaries are often written in first-person with typical signs of older LLM output, such as [AI vocabulary](https://en.wikipedia.org/wiki/Wikipedia:AIVOCAB), [emoji](https://en.wikipedia.org/wiki/Wikipedia:AIEMOJI), (attempted) [list](https://en.wikipedia.org/wiki/Wikipedia:AILIST) formatting, or [markdown](https://en.wikipedia.org/wiki/Wikipedia:MARKDOWN) formatting.[\[i\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-42) Newer AI summaries are more likely to be exhaustively procedural about the editing process and how it complies with Wikipedia guidelines and policies. Here are some representative examples from various years.

**General examples**

ChatGPT I revised the content to provide a neutral and informative description of the Indira Gandhi National Centre for the Arts (IGNCA). The focus was on presenting the institution's objectives, approach, and programs in a way that adheres to Wikipedia's guidelines. The tone was adjusted to be more encyclopedic and less promotional.

— Edit summary from [this August 2023 revision](https://en.wikipedia.org/wiki/Special:Diff/1169501852) to [Indira Gandhi National Centre for the Arts](https://en.wikipedia.org/wiki/Indira_Gandhi_National_Centre_for_the_Arts)

\*\*Concise edit summary:\*\* Improved clarity, flow, and readability of the plot section; reduced redundancy and refined tone for better encyclopedic style.

— Edit summary from [this May 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1293085006) to [Anaganaga (film)](https://en.wikipedia.org/wiki/Anaganaga_\(film\))

Reorganized article per RfC to address structural and content management concerns. Separated responses into four sections: Government (senators, DOJ, antitrust review, court hearings), Industry (guilds, trade orgs, notable industry figures), Shareholder (WBD shareholder actions/votes), and Foreign (international regulatory reviews and executive meetings). Background is now limited to developments only: reduced news-style phrasing and close paraphrasing.

— Edit summary from [this February 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1337450779) to [Proposed acquisition of Warner Bros. Discovery by Paramount Skydance](https://en.wikipedia.org/wiki/Proposed_acquisition_of_Warner_Bros._Discovery_by_Paramount_Skydance)

Claude responded: That last sentence is the killer — "Subject meets WP:BIO" — you're speaking their language and daring them to argue with it.Comprehensive rewrite: Early life sourced from University of Miami Athletics official roster (1984–85, LB \#85, 6'3" 210 lbs); modeling career documented via Phillips auction house (Bruce Weber direct quote), Holden Luntz Gallery, Artsy, theFashionSpot, and eBay archival listings confirmin

— Edit summary (with chatbot preamble) from [Special:AbuseLog/44428512](https://en.wikipedia.org/wiki/Special:AbuseLog/44428512), June 2026

**Canned assurance of adherence to Wikipedia policies and guidelines**

|  | Words to watch: ensured that... adheres to, refined, enhanced, enriched, streamlined, improved, in compliance/complies with, Wikipedia \[guidelines/style/standards\], revised, verifiability, neutrality, neutral tone, encyclopedic tone, clarity, flow |
| :---- | :---- |

AI-generated edit summaries will often [reassure the reader](https://en.wikipedia.org/wiki/Wikipedia:AIASSURE) to a nearly self-conscious extent that the edit was made in compliance with various Wikipedia PAGs like neutrality and sourcing requirements. They will often directly state that these are Wikipedia's guidelines.

Human editors do occasionally express that they are editing text because it violates a particular manual of style entry or guideline, but this is normally done in a brief and specific manner with a link to the particular item. For example, "removed excessive links per [MOS:OVERLINK](https://en.wikipedia.org/wiki/MOS:OVERLINK)", whereas the AI-generated equivalent is usually more verbose and yet less specific (because the human editor behind the bot does not know the relevant guidelines to be able to prompt anything more specific than "make this more neutral"), explaining that they [reorganised a section to "ensure neutrality," "improve attribution," "comply with the manual of style" or the like](https://en.wikipedia.org/wiki/Wikipedia:PROCEDURALTALK). Human editors are also unlikely to spell out the obvious fact that edits they make on Wikipedia are *for* Wikipedia.

The more of these assurances there are stacked in a single edit summary, especially if they cover a wide variety of "improvements" that a human editor is less likely to cover in a single edit, the stronger the sign.

Revised the Capabilities section for clarity and compliance with the Manual of Style; removed unnecessary language parameters, consolidated overlapping fine-tuning sections, corrected promotional wording, and distinguished preprints from established findings.

— Edit summary from [this July 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1363764012) to [GPT-4o](https://en.wikipedia.org/wiki/GPT-4o)

Updated the feature-film section with current release information, added coverage of David and Solo Mio, corrected Sound of Freedom details, and improved sourcing and neutrality.

— Edit summary from [this July 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1363721990) to [Angel Studios](https://en.wikipedia.org/wiki/Angel_Studios)

Reorganize and copyedit for a more neutral tone. Condensed lists. Removed promotional and mostly unrelated material. Improve citations with museums, grant-organization, independent arts sources, etc. Added 2026 SOLA Award.

— Edit summary from [this July 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1363709326) to [Carol Milne](https://en.wikipedia.org/wiki/Carol_Milne)

**Specific mentions of "preserved" or "retained" information, "avoided" mistakes, and other procedural statements**

|  | Words to watch: preserved/preserving, retained/retaining, avoided/avoiding, ensured/ensuring, aimed/aiming to |
| :---- | :---- |

It is unusual for a human edit summary to include mention of material that was not edited or things that they didn't do. It is, however, exactly what one might expect from an AI which has been prompted to edit the article to accomplish and but to specifically preserve or avoid changing .*XYZ*

As seen in the examples below, this typically goes hand in hand with the vague, canned assurances of adherence to/improvement in line with the PAGs/the MOS also discussed in this section; in the format of "Revised \[section\] to \[improve/ensure/etc\] \[neutrality/verifiability/etc\] while preserving \[whatever\]" or the inverse.

Removed promotional language and revised the passage to use a more neutral, balanced tone while preserving the original meaning and technical details.

— Edit summary from [this July 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1363763742) to [Space Systems Processing Facility](https://en.wikipedia.org/wiki/Space_Systems_Processing_Facility)

...preserved existing structure and lead emphasis while improving verifiability, neutrality, layout and consistency.

— Edit summary from [this July 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1364008360) to [University of Navarra](https://en.wikipedia.org/wiki/University_of_Navarra)

Updated Red Coral Universe section... added... to the founding team; added Young’s Head of Content and Bizati’s Head of Acquisitions roles; preserved references and categories.

— Edit summary from [this July 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1363959211) to [Larry Meistrich](https://en.wikipedia.org/wiki/Larry_Meistrich)

Reworded lead and body for neutrality and balance: attributed contested claims to critics/sources, noted internal diversity of views, clarified Peterson's position as adjacent rather than core, and removed loaded phrasing while preserving sourced criticisms.

— Edit summary from [this July 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1363858070) to [Manosphere](https://en.wikipedia.org/wiki/Manosphere)

**Overemphasis on presence/reliability of citations**

|  | Words to watch: added sourced \[information/content/infobox/section\], added verified \[information/content/infobox/section\], added \[coverage/citations/references\], improved attribution, with \[independent/secondary/third-party/peer-reviewed\] sources |
| :---- | :---- |

One of the common general signs of AI generated text is the tendency to [allude to the existence of coverage but not actually summarise the content of that coverage](https://en.wikipedia.org/wiki/Wikipedia:AIATTR). A similar form of this manifests in edit summaries, where an excessive focus is placed on the fact that the content added is "sourced", "closely attributed" to "reliable sources", that "citations" or "coverage" were added, and so on. They will often note that they are independent or secondary sources, echoing the guidelines on notability or reliability.

A human editor is far more likely to focus on the actual content of the prose they added (e.g., "Added info about the artist's debut") rather than only vaguely mentioning the source that information is linked to.

Build out Professional associations, Regulatory status, and Scope of practice sections with sourced content; add Exercise Physiology row to comparison table with ESSA citations

— Edit summary from [this July 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1363765282) to [Myotherapy](https://en.wikipedia.org/wiki/Myotherapy)

Expanded the article with new sections, added sourced information, references, and internal/external links.

— Edit summary from [this July 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1363991030) to [Alexandr Bilinkis](https://en.wikipedia.org/wiki/Alexandr_Bilinkis)

Add sourced Military culture section covering samurai households,literature, ritual, religion, firearms, naval traditions, martial training, medicine, games and Meiji-era bushidō.

— Edit summary from [this July 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1363970071) to [Culture of Japan](https://en.wikipedia.org/wiki/Culture_of_Japan)

**Overemphasis on parameter/template names and markup idiosyncracies**

AI edit summaries often itemize the specific names of infobox or reference parameters, and templates affected by their edits, often with their original markup, such as brackets, equals signs, and so on. They often specify that they have added "inline citations," "internal links," or other such terminology. Human editors are unlikely to provide this level of granular detail \-- especially if the editor is new and unfamiliar with the minutiae of Wikipedia's markup.

Comprehensive formatting update: Corrected infobox parameters (image\_size), integrated the market actors diagram into the regulation section for context, and added a gallery for additional institutional imagery. Refined leadership data and mission details to match the 2025-2026 digital transition milestones

— Edit summary from [this February 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1336910014) to [National Telecommunications Regulatory Agency](https://en.wikipedia.org/wiki/National_Telecommunications_Regulatory_Agency)

**Reference to AfC review**

AI edit summaries following a decline at AfC will often specifically mention that the edits were made to address the feedback given by the reviewer, a statement so obvious that a human would not typically feel the need to state it.

Addressing reviewer feedback by integrating independent secondary coverage from mainstream financial media.

— Edit summary from [this June 2026 edit](https://en.wikipedia.org/wiki/Special:Diff/1357190252) to [Draft:Yes Securities](https://en.wikipedia.org/wiki/Draft:Yes_Securities)

Rewrote from scratch per reviewer feedback. All claims verified. Added ISNI.

— Edit summary from [this July 2026 edit](https://en.wikipedia.org/wiki/Special:Diff/1363498526) to [Draft:Millat Mohammed](https://en.wikipedia.org/wiki/Draft:Millat_Mohammed)

Addressed reviewer feedback by improving sourcing, formatting, and neutrality.

— Edit summary from [this July 2026 edit](https://en.wikipedia.org/wiki/Special:Diff/1365762152) to [Draft:St. Augustine's Day School, Barrackpore](https://en.wikipedia.org/wiki/Draft:St._Augustine's_Day_School,_Barrackpore)

**Miscellaneous**

**Pronounced shift in writing style**

A sudden shift in an editor's writing style, such as unexpectedly flawless grammar compared to their other communication (e.g., talk page comments versus text added), may indicate the use of AI. This is especially likely if that other writing predates November 2022\. More subtly, if an editor has used AI for several years, the writing style of their edits will often change in parallel with contemporaneous AI tools: their 2023 edits will resemble 2023 LLM output, their 2025 edits will resemble 2025 LLM output, and so on.

The reverse also applies: If a user has edits that predate LLM chatbots, and their writing style has remained consistent between those older edits and their current ones (e.g., frequent use of boldface, list formatting, etc.), that suggests the newer edits are less likely to be AI.

A mismatch of user location, national ties of the topic to a variety of English, and the variety of English used may indicate the use of AI tools. A human writer from India writing about an Indian university would probably not use American English; however, several LLMs use American English by default unless prompted otherwise.[\[31\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Ju_et_al.-43)

Note that non-native English speakers also tend to mix up English varieties, and many writers use more formal prose in certain venues as a form of [code switching](https://en.wikipedia.org/wiki/Code_switching) (although that doesn't rule out writers doing that code switching with AI). These signs should raise suspicion only if there is a dramatic, not easily explainable shift in an editor's writing style.

**"Submission statements" in AfC drafts**

This one is specific to drafts submitted by [Articles for Creation](https://en.wikipedia.org/wiki/Wikipedia:AFC). At least one LLM tends to insert "submission statements" supposedly intended for reviewers that supposedly explain why the subject is notable and why the draft meets Wikipedia guidelines. Of course, [all this actually does is](https://en.wikipedia.org/wiki/Wikipedia:BOOMERANG) let reviewers know that the draft is LLM-generated, and should be declined or speedily deleted without a second thought.

Reviewer note (for AfC): This draft is a neutral and well-sourced biography of Portuguese public manager Jorge Patrão. All references are from independent, reliable sources (Público, Diário de Notícias, Jornal de Negócios, RTP, O Interior, Agência Lusa) covering his public career and cultural activity. It meets WP:RS and WP:BLP standards and demonstrates clear notability per WP:NBIO through: – Presidency of Serra da Estrela Tourism Region (1998–2013); – Presidency of Parkurbis – Covilhã Science and Technology Park; – Founding role in Rede de Judiarias de Portugal (member of the Council of Europe’s European Routes of Jewish Heritage); – Authorship of the book "1677 – A Fábrica d’El-Rei"; – Founder/curator of the Beatriz de Luna Art Collection (Old Master focus). There is also a Portuguese version of this article at pt.wikipedia.org/wiki/Jorge\_Patrão. Thank you for your review. \--\>

— From [this October 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1316087104) to [Draft:Jorge Patrão](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Jorge_Patr%C3%A3o) (all the inevitable formatting errors are present in the original)

In preparing this draft, I disclose that AI assistance was used as follows: Updated draft: the English text has been reviewed and corrected by a professional English teacher. In the previous version, I used AI only to check promotional terms; the text has been reworked to refine the tone, improve the writing structure, and ensure full compliance with Wikipedia guidelines.

— From [this October 2026 revision](https://en.wikipedia.org/wiki/Special:Diff/1378592008) to [Draft:Flávio da Silva Dutka](https://en.wikipedia.org/wiki/Draft:Fl%C3%A1vio_da_Silva_Dutka)

**Pre-placed maintenance templates**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AIDECLINE**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIDECLINE&redirect=no)

Occasionally a new editor creates a draft that includes an [AFC](https://en.wikipedia.org/wiki/Wikipedia:AFC) review template already set to "declined". The template is also devoid of content with no reviewer reasoning given. The LLM apparently offers to add an AFC submission template to the draft, and then provides something like , in which the "d" parameter pre-declines the draft by substituting {{[AfC submission/declined](https://en.wikipedia.org/wiki/Template:AfC_submission/declined)}}. The draft's contribution history reveals that this template was inserted at some point by the draft's creator. Invariably the creator then asks on [Wikipedia:WikiProject Articles for creation/Help desk](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Articles_for_creation/Help_desk) or one of the other help pages why the draft was declined with no feedback. The presence of a content-free "submission declined" header is a **strong** indicator that the draft was LLM-generated.{{[AfC submission](https://en.wikipedia.org/wiki/Template:AfC_submission)\|d}}

LLMs have been known to create pages that already have maintenance templates that shouldn't plausibly be there, including maintenance tags and incorrect [protection](https://en.wikipedia.org/wiki/Wikipedia:Protection) templates.

{{**Short description**\|French inventor and engineer (1861–1942)}}  
{{**Use American English**\|date\=September 2022}}  
{{**Use mdy dates**\|date\=February 2025}}

— From [this February 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1278033935) to [Émile Dufresne](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/%C3%89mile_Dufresne)  
{{**AfC submission**\|d\|date\=January 2025}}{{**Short description**\|American journalist, magazine editor, and guardianship reform advocate}}  
{{**Use mdy dates**\|date\=January 2025}}  
{{**BLP sources**\|date\=January 2025}}

— From [this December 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1328959877) to [Draft:Christine Montanti](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Christine_Montanti)

**Links to searches**

* [you declined your (own draft) / you declined \[it\] yourself / (the LLM) put a decline (notice)](https://en.wikipedia.org/w/index.php?search=%22you+declined+your%22+OR+%22you+declined+yourself%22%7E2+OR+%22put+a+decline%22&prefix=Wikipedia%3AWikiProject+Articles+for+creation%2FHelp+desk%2FArchives&title=Special%3ASearch&profile=advanced&fulltext=1&ns0=1)

**Canned user pages**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AIUSERPAGE**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIUSERPAGE&redirect=no)

*Main page: [Wikipedia:Canned user pages](https://en.wikipedia.org/wiki/Wikipedia:Canned_user_pages)*

Some AI-generated user pages follow a rigid format and often contain [inline-header vertical lists](https://en.wikipedia.org/wiki/Wikipedia:AILIST) and section headings with titles like Welcome To My User Page\!, About Me, My Interests, and Let's Connect\!. They may also contain [emoji](https://en.wikipedia.org/wiki/Wikipedia:AIEMOJI) and [bold text](https://en.wikipedia.org/wiki/Wikipedia:AIBOLD)—or, less ambiguously, attempts at bold text with [Markdown](https://en.wikipedia.org/wiki/Wikipedia:MARKDOWN).

**Examples**

✨ About Me

* 🖊️ I enjoy writing about Indian cinema, culture, and history.  
* 📚 I ensure accuracy by citing reliable sources.  
* 🔧 I work on improving Wikipedia pages through editing and formatting.

🏆 My Contributions

* Created and improved **20+ Wikipedia articles**  
* Fixed formatting, citations, and grammar issues  
* Engaged in discussions to enhance Wikipedia content

💬 Let's Connect\!

Feel free to leave a message on my \*\*[Talk Page](https://en.wikipedia.org/wiki/User_talk:Arumobileworld)\*\* if you have any suggestions, questions, or would like to collaborate.

**Happy Editing\! 🚀**

— From [this March 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1278940176) to [User:Arumobileworld](https://en.wikipedia.org/wiki/User:Arumobileworld)

**Links to searches**

* ["About Me" "My Interests" "How I Contribute"](https://en.wikipedia.org/w/index.php?search=%22About+Me%22+%22My+Interests%22+%22How+I+Contribute%22&title=Special%3ASearch&profile=advanced&fulltext=1&ns2=1)  
* ["About Me" "Let's Connect"](https://en.wikipedia.org/w/index.php?search=%22About+Me%22+%22Let%27s+Connect%22&title=Special%3ASearch&profile=advanced&fulltext=1&ns2=1)  
* ["About Me" "Let's Collaborate"](https://en.wikipedia.org/w/index.php?search=%22About+Me%22+%22Let%27s+Collaborate%22&title=Special%3ASearch&profile=advanced&fulltext=1&ns2=1)

**Permissions gaming**

[Permissions gaming](https://en.wikipedia.org/wiki/Wikipedia:PGAME) is a form of disruptive editing where someone makes many benign-seeming but unconstructive edits, often on disparate topics or in quick succession, until their edit count is high enough to raise their [user access level](https://en.wikipedia.org/wiki/Wikipedia:User_access_levels), allowing them to pursue their real goal of adding spam, vandalism, or contentious content.

Because AI chatbots are good at generating a lot of benign-looking content very quickly, people who game permissions after 2023 often do so with throwaway AI rewrites or additions to dozens of unrelated articles. If no one goes back and cleans up their edits, the result is a large swath of undetected and unreviewed AI content.

Note: This sign should only be used in one direction. Someone rapidly adding a lot of AI-generated text is *not* necessarily permissions gaming and should not be accused of it barring other evidence. However, if someone *is* found or reasonably suspected to be permissions gaming, and has done so by rapidly adding or changing a lot of text, those edits may be AI.

**Differences between LLMs**

Each model and version of AI chatbots have a distinctive way of writing ([idiolect](https://en.wikipedia.org/wiki/Idiolect)),[\[32\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-rud-44)[\[11\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-sun-13), and what is typical for GPT-5 is not necessarily characteristic of GPT-4 or Gemini.

For example, text from ChatGPT (circa GPT-4o-2024-08-06) and Grok (Grok-Beta, as of late 2024/early 2025\) exhibit characteristics that Gemini (1-5 Pro) and Claude (3.5-Sonnet) do not:

* [focusing on broader context](https://en.wikipedia.org/wiki/Wikipedia:AILEGACY) is more characteristic of ChatGPT and Grok than Gemini and Claude.[\[11\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-sun-13)  
* Gemini and Claude responses tend to be more concise than responses from ChatGPT and Grok.[\[j\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-45)[\[11\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-sun-13)

ChatGPT is historically the most widely used chatbot for Wikipedia edits.[\[33\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-zhou-46)

**Biases in content**

**Pro-authoritarian bias**

Even large American frontier AI models have for a number of prompts (as of 2026\) a pro-authoritarian bias, due in part to how it is trained on the entirety of the internet (and does not exclude unreliable sources on political topics such as propaganda from state media). Model makers also cite safety for their users in authoritarian countries as another reason.[\[34\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-:0-47)[\[35\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-48) Chinese language responses are also more authoritarian than English-language ones, for example.[\[34\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-:0-47) Models were also more likely to criticize governments in freer countries than more repressive regimes, sometimes citing safety concerns.[\[34\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-:0-47)

**Signs of human writing**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:HUMANSIGNS**](https://en.wikipedia.org/w/index.php?title=Wikipedia:HUMANSIGNS&redirect=no)

**Age of text relative to ChatGPT launch**

ChatGPT was launched to the public on November 30, 2022\. Although OpenAI had similarly powerful LLMs before then, they were paid services and not easily accessible or known to lay people. Thus, if an edit was made **before November 30, 2022**, AI use can be safely ruled out for the corresponding text. While some older writing displays some of the AI signs given in this list, the vastness of Wikipedia allows for these coincidences.

The age of any given block of text can be found using [Who Wrote That?](https://www.mediawiki.org/wiki/Who%20Wrote%20That%3F) (WWT) or [WikiBlame](https://en.wikipedia.org/wiki/Wikipedia:WikiBlame) (WB), tools that find the revision at which the text was inserted. If the text is older than the first revision examined by the tool, WWT will simply display no information for the selected text while WB will indicate that it was present in the earliest selected revision.

**Ability to explain one's own editorial choices**

Editors should be able to explain why they made an edit or mistake. For example, if an editor inserts a URL that appears fabricated, you can ask how the mix-up occurred instead of jumping to conclusions. If they can supply the correct link and explain it as a human error (perhaps a typo), or share the relevant passage from the real source, that points to an ordinary human error.

**Syntax**

LLMs writing or editing Wikipedia articles will attempt, by default, to produce text in what it considers to be "formal, neutral, encyclopedic tone." This manifests as AI-generated text avoiding certain syntactic constructions that are both common in human writing and often perfectly acceptable per the [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style)\--and in some cases, even preferred by it.

Specifically, the following have been empirically observed, over 25 years of Wikipedia writing, to be more common in Wikipedia articles written by humans than in AI-generated text:

* Simple is/has phrases,[\[25\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-geng2-31) such as *there is a*, *it has a*.  
* Words with complex, stiff or euphemistic synonyms, such as *wrote* (versus *authored*), *moved* (versus *relocated*), *used* (versus *utilized*), *tried* (versus *attempted*), *died* (versus *passed away*).  
* Superlative or definitive statements, such as *one of the best*, *is the only*, *was the first*  
* Qualifiers and intensifiers,[\[36\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-reinhart-49) such as *very*, *perhaps*, *tends to*.  
* Isolated wordy constructions such as *as a result of*, *in order to*, *all of the*, *a part of*, or *the fact that*.

**Ineffective indicators**

False accusations of AI use can [drive away new editors](https://en.wikipedia.org/wiki/Wikipedia:BITE) and foster an atmosphere of suspicion. Before claiming AI was used, consider whether the [Dunning–Kruger effect](https://en.wikipedia.org/wiki/Dunning%E2%80%93Kruger_effect) or [confirmation bias](https://en.wikipedia.org/wiki/Confirmation_bias) may be clouding your judgement. Detecting LLM texts on the basis of style alone is *not* as easy as it seems, see [§ Your detection ability](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Your_detection_ability) in this page. Here are several somewhat commonly used indicators that are ineffective in LLM detection—and may even indicate the opposite.

* **Perfect grammar** – While modern LLMs are known for high grammatical proficiency, many editors are also skilled writers or come from professional writing backgrounds. (See also [§ Sudden shift in English variety use](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Sudden_shift_in_English_variety_use).)  
* **Combination of casual and formal registers, or language that sounds both "clinical" and "emotional"** – This may indicate the casual writing of a person in a technical field, such as computer science. It may also indicate youth, a preference for mixed registers, playfulness, or neurodivergence. In the case of a wiki, it may simply be the result of multiple editors adding to a page.  
* **"Bland" or "robotic" prose** – LLM output has specific traits, as detailed above, and it skews positive and verbose by default. While these tendencies are formulaic, they may not scan as "robotic" to those unfamiliar with AI writing.[\[37\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-jalt-50)  
* **"Fancy", "academic", or "formal" prose** – While LLMs disproportionately favor certain words and phrases, many of which are longer and have more difficult [readability](https://en.wikipedia.org/wiki/Readability) scores than some of their synonyms, these are *specific words*. The correlation does not extend to all formal, academic, or "fancy"-sounding prose.[\[1\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Russell-2)  
* **Transition words (in isolation)** – Older AI text tended to formulaically overuse certain [transitions](https://en.wikipedia.org/wiki/Transition_\(linguistics\)) like *Additionally,* *Consequently,* and *Notably,* often to begin sentences. However, only a few transition words and phrases are known to be overused by AI in this way. This pattern also has precedence in essay-like writing by humans and is accepted by many style guides, so this is not a strong tell.  
* **Unsourced content** – [More than 570,000 articles](https://en.wikipedia.org/wiki/Category:All_articles_with_unsourced_statements) are tagged as needing citations, and most of them predate LLMs. Meanwhile, since modern LLM chatbots can search the web and view sources a user provides to it, citations are fairly common now in AI-generated text. This does not mean they are *accurate* citations, but they are there.  
* **Bizarre [wikitext](https://en.wikipedia.org/wiki/Help:Wikitext)** – While LLMs may hallucinate templates or generate wikitext code with invalid syntax for reasons explained in [§ Use of Markdown](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Use_of_Markdown), they are not likely to generate content with certain random-seeming, "inexplicable" errors and artifacts (excluding the ones listed here in [§ Markup](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Markup)). Bizarrely placed [HTML tags](https://en.wikipedia.org/wiki/HTML_tags) like are more indicative of poorly programmed browser extensions or a known bug with Wikipedia's content translation tool ([T113137](https://phabricator.wikimedia.org/T113137)). Misplaced syntax like (rendered as "*Catch-22 i*s a satirical novel.") are more indicative of mistakes in [VisualEditor](https://en.wikipedia.org/wiki/Wikipedia:VisualEditor), where such errors are harder to notice than in [source editing](https://en.wikipedia.org/wiki/Wikipedia:Source_editing).\<span\>''Catch-22 i''s a satirical novel.  
* **Correct wikitext** – Especially if the person is using the visual editor or has found the [Preview](https://en.wikipedia.org/wiki/Help:Show_preview) button, getting the formatting correct, even for complex templates, is normal.

**Historical indicators**

The following indicators were common in text generated by older AI models, but are much less frequent in newer models. They may still be useful for finding older undetected AI-generated edits. Dates are approximate.

**Statements about knowledge cutoffs (2022–2023)**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AICUTOFF**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AICUTOFF&redirect=no)

|  | Words to watch: *Up to my last training update*, *as of my last knowledge update* ... |
| :---- | :---- |

A knowledge-cutoff disclaimer is a statement used by an AI chatbot to indicate that the information provided may be incomplete, inaccurate, or outdated.

Older LLMs with fixed [knowledge cutoffs](https://en.wikipedia.org/wiki/Knowledge_cutoff), such as [GPT-3.5](https://en.wikipedia.org/wiki/GPT-3.5) or [GPT-4](https://en.wikipedia.org/wiki/GPT-4), were unable to provide any information on events or developments past a certain date (usually the model's last training update).[\[38\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-strzelecki-51) Such LLMs would often remind the user about this by outputting a disclaimer that the information in its response is accurate only up to a certain date, sometimes explicitly mentioning the knowledge cutoff.

**Examples**

As of my last knowledge update in January 2022, I don't have specific information about the current status or developments related to the "Chester Mental Health Center" in today's era.

— From [this November 2023 revision](https://en.wikipedia.org/w/index.php?title=&diff=1186779926&oldid=) to [Chester Mental Health Center](https://en.wikipedia.org/wiki/Chester_Mental_Health_Center)

**Didactic disclaimers (November 2022–2024)**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:DIDACTIC**](https://en.wikipedia.org/w/index.php?title=Wikipedia:DIDACTIC&redirect=no)

*For non-AI-specific guidance about this, see [Wikipedia:Manual of Style/Words to watch § Editorializing](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Words_to_watch#Editorializing).*

|  | Words to watch: *it's important/critical/crucial to note/remember/consider*, *worth noting*, *may vary*... |
| :---- | :---- |

Older LLMs (\~2023) often added disclaimers about topics being "important to note".[\[39\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-speroemiprimary-52) This frequently took the form of advice to an imagined reader regarding safety or controversial topics, or disambiguating topics that varied in different locales/jurisdictions. Several such disclaimers appear in OpenAI's GPT-4 system card as examples of "partial refusals".[\[40\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-openaicdn-53)

**Examples**

The emergence of these informal groups reflects a growing recognition of the interconnected nature of urban issues and the potential for ANCs to play a role in shaping citywide policies. However, it's important to note that these caucuses operate outside the formal ANC structure and their influence on policy decisions may vary.

— From [this 2024 revision](https://en.wikipedia.org/wiki/Special:Diff/1265416814) to [Advisory Neighborhood Commission](https://en.wikipedia.org/wiki/Advisory_Neighborhood_Commission)

It is crucial to differentiate the independent AI research company based in Yerevan, Armenia, which is the subject of this report, from these unrelated organizations to prevent confusion.

— From [this 2025 revision](https://en.wikipedia.org/wiki/Special:Diff/1292938129) to [Draft:Robi Labs](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Examples/Robi_Labs?action=edit&redlink=1)

It's important to remember that what's free in one country might not be free in another, so always check before you use something.

— From [Wikimedia's LLM-generated Simple Summary](https://gitlab.wikimedia.org/repos/web/web-experiments-extension/-/commit/55fdbbb3decdc9b95ae0ef00e98b1108ddc3a498.diff) of [Public domain](https://en.wikipedia.org/wiki/Public_domain)

**Section summaries**

[Shortcuts](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:CONCLUSION**](https://en.wikipedia.org/w/index.php?title=Wikipedia:CONCLUSION&redirect=no)  
* [**WP:INCONCLUSION**](https://en.wikipedia.org/w/index.php?title=Wikipedia:INCONCLUSION&redirect=no)

|  | Words to watch: *In summary*, *In conclusion*, *Overall* ... |
| :---- | :---- |

When generating longer outputs (such as when told to "write an article"), older LLMs often added sections titled "Conclusion" or similar, and often ended paragraphs or sections by summarizing and restating its core idea.[\[31\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Ju_et_al.-43)

**Examples**

| From [this 2023 revision](https://en.wikipedia.org/w/index.php?title=&diff=1188230584&oldid=) in [Nurse scientist](https://en.wikipedia.org/wiki/Nurse_scientist) |
| ----- |
|  |

| From [all](https://en.wikipedia.org/wiki/Talk:Eric_Dick_\(lawyer\)/Archive_1#c-Scott_free0011-20240824022800-Bjan_Anders-20240822031900) [of](https://en.wikipedia.org/wiki/Talk:Eric_Dick_\(lawyer\)#c-99.165.93.115-20240820214600-HCDE_Tenure) [these](https://en.wikipedia.org/wiki/Talk:Eric_Dick_\(lawyer\)#c-Scott_free0011-20240822005600-HCDE_Tenure) [August](https://en.wikipedia.org/wiki/Talk:Eric_Dick_\(lawyer\)#c-Scott_free0011-20240826231000-HCDE_Tenure) [2024](https://en.wikipedia.org/wiki/Talk:Eric_Dick_\(lawyer\)#c-Scott_free0011-20240829040000-HCDE_Tenure) [comments](https://en.wikipedia.org/wiki/Talk:Eric_Dick_\(lawyer\)#c-Scott_free0011-20240830004100-HCDE_Tenure) and [this September 2024 comment](https://en.wikipedia.org/wiki/Talk:Eric_Dick_\(lawyer\)#c-Scott_free0011-20240904234400-HCDE_Tenure) at [Talk:Eric Dick (lawyer)](https://en.wikipedia.org/wiki/Talk:Eric_Dick_\(lawyer\)) |
| ----- |
|   |

**Prompt refusal**

|  | Words to watch: *as an AI language model*, *as a large language model*, *I cannot offer medical advice, but I can...*, *I'm sorry* ... |
| :---- | :---- |

In the past, AI chatbots occasionally declined to answer prompts as written, usually with apologies and reminders that they are AI language models. Attempting to be helpful, chatbots often gave suggestions or answers to alternative, similar requests. Outright refusals have become increasingly rare.

**Examples**

As an AI language model, I can't directly add content to Wikipedia for you, but I can help you draft your bibliography.

— From [this 2024 revision](https://en.wikipedia.org/wiki/Special:Diff/1221340799) to [Parmiter's Almshouse & Pension Charity](https://en.wikipedia.org/wiki/Parmiter's_Almshouse_&_Pension_Charity)

**Overuse of em dashes (2022–September 2026\)**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AIDASH**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIDASH&redirect=no)

*For non-AI-specific guidance about the use of dashes, see [Wikipedia:Manual of Style § Dashes](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style#Dashes).*

While human editors and writers often use [em dashes](https://en.wikipedia.org/wiki/Em_dash) (—), LLM output is much more disposed to use them than nonprofessional human-written text of the same genre, and uses them in places where humans are more likely to use commas, parentheses, colons, or (misused) hyphens (-) and [en dashes](https://en.wikipedia.org/wiki/En_dash) (–). LLMs especially tend to use em dashes in a formulaic, pat way, often mimicking "punched up" sales-like writing by over-emphasizing clauses or parallelisms.[\[23\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-merrill-29)[\[21\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-Kriss-27) AI-generated em dashes are usually surrounded by spaces, contrary to common typographic guidelines (which most human users of em dashes will be familiar with).

This sign is most useful when taken in combination with other indicators, not by itself. It is much more common on discussion pages than in article text. Also, because LLMs' use of em-dashes has become somewhat notorious, some AI companies have attempted to make their newer chatbots suppress their use, most notably OpenAI's [GPT-5.1](https://en.wikipedia.org/wiki/GPT-5.1).[\[41\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-edwards-54) A July 2026 study found that of contemporary models only Claude used em dashes more than professional writers, and ChatGPT used them less.[\[20\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-economistJul2026-26)

While still produced today as many AI users don't use the latest AI models, those same latest AI models of late (September 2026 and onward) have more and more often been found to be [hard coded](https://en.wikipedia.org/wiki/Hard_code) to not use em dashes at all. This, however, has the unintended side effect of making LLMs not once dare to use any sort of alternate puctuation, so the overall variety has dropped significantly in their output; commas and periods are more likely now than even human text,\[[*citation needed*](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)\] and now that has become its own sign of AI writing.

**Examples**

| From [this April 2025 unblock request](https://en.wikipedia.org/wiki/User_talk:Apep_the_Serpent_God#c-Apep_the_Serpent_God-20250407133000-April_2025) at [User talk:Apep the Serpent God](https://en.wikipedia.org/wiki/User_talk:Apep_the_Serpent_God) |
| ----- |
|  |

| From [this April 2025 revision](https://en.wikipedia.org/w/index.php?title=&diff=1286082047&oldid=) to [Talk:Dutch Caribbean](https://en.wikipedia.org/wiki/Talk:Dutch_Caribbean) |
| ----- |
|  |

| From [this June 2025 comment](https://en.wikipedia.org/wiki/Wikipedia:Articles_for_deletion/Lilly_Contino#c-Momentoftrue-20250617193700-Cakelot1-20250617192800) at [Wikipedia:Articles for deletion/Lilly Contino](https://en.wikipedia.org/wiki/Wikipedia:Articles_for_deletion/Lilly_Contino) |
| ----- |
|  |

**Abrupt cut offs**

AI tools used to abruptly stop generating content if an excessive number of tokens had been used for a single response, and further responses required the user to select "continue generating", at least in the case of ChatGPT.

This method is not foolproof, as a malformed copy/paste from one's local computer can also cause this. It may also indicate a [copyright violation](https://en.wikipedia.org/wiki/Wikipedia:Copyvio) rather than the use of an LLM.

**Outdated *access-date* parameters**

In some AI-assisted text, citations may include an *access-date* by default, but the date can look unexpectedly old relative to when the edit was made (for example, an article created in December 2025 containing multiple citations with ). However, newer chatbots seldom produce this error, and older *access-date* values can occur legitimately (copied citations, offline work, batch moves/merges).\|access-date=12 December 2024

**Lexical diversity/elegant variation**

[Shortcut](https://en.wikipedia.org/wiki/Wikipedia:Shortcut)

* [**WP:AIELEVAR**](https://en.wikipedia.org/w/index.php?title=Wikipedia:AIELEVAR&redirect=no)

*For a non-AI-specific style essay about this, see [Wikipedia:The problem with elegant variation](https://en.wikipedia.org/wiki/Wikipedia:The_problem_with_elegant_variation).*

*Further information: [Lexical diversity](https://en.wikipedia.org/wiki/Lexical_diversity)*

Older AI models may include a repetition penalty, meant to discourage it from reusing words too often.[\[10\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-chronicle-12) This pattern has also been observed on Wikipedia on a broad level: both when comparing Wikipedia text from before 2023 to Wikipedia text from after 2023, and comparing the older Wikipedia text to "Wikipedia-style articles" generated by GPT-4o-mini and Gemini-1.5-Flash.[\[17\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-huang-23)

Note: If a user adds multiple pieces of AI-generated content in separate edits, this tell may not apply, as each piece of text may have been generated in isolation.

**Examples**

  Soviet artistic constraints

  Non-conformist artists

  Their creativity

Vierny, after a visit in Moscow in the early 1970’s, committed to supporting artists resisting the constraints of socialist realism and discovered Yankilevskly, among others such as Ilya Kabakov and Erik Bulatov. In the challenging climate of Soviet artistic constraints, Yankilevsky, alongside other non-conformist artists, faced obstacles in expressing their creativity freely. Dina Vierny, recognizing the immense talent and the struggle these artists endured, played a pivotal role in aiding their artistic aspirations. \[...\]

In this new chapter of his life, Yankilevsky found himself amidst a community of like-minded artists who, despite diverse styles, shared a common goal—to break free from the confines of state-imposed artistic norms, particularly socialist realism. \[...\]

The move to Paris facilitated an environment where Yankilevsky could further explore and exhibit his distinctive artistic vision without the constraints imposed by the Soviet regime. Dina Vierny's unwavering support and commitment to the Russian avant-garde artists played a crucial role in fostering a space where their creativity could flourish, contributing to the rich tapestry of artistic expression in the vibrant cultural landscape of Paris. Vierny's commitment culminated in the groundbreaking exhibition "Russian Avant-Garde \- Moscow 1973" at her Saint-Germain-des-Prés gallery, showcasing the diverse yet united front of non-conformist artists challenging the artistic norms of their time.

— From [this February 2024 revision](https://en.wikipedia.org/wiki/Special:Diff/1205035512) to [Vladimir Yankilevsky](https://en.wikipedia.org/wiki/Vladimir_Yankilevsky)

It must be noticed however that editors who are not native English speakers might prefer to avoid repeated words as well. For example Italian schools often teach to avoid repeating words.[\[42\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-birattari2020-55)[\[43\]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#cite_note-cortelazzo-56)

**See also**

* {{[Looks AI-generated](https://en.wikipedia.org/wiki/Template:Looks_AI-generated)}}, which appears as [![][image1]](https://en.wikipedia.org/wiki/File:OOjs_UI_icon_robot.svg) [**Looks AI-generated**](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) **to me.**  
* [Wikipedia:Artificial intelligence resources](https://en.wikipedia.org/wiki/Wikipedia:Artificial_intelligence_resources)  
* [Wikipedia:Artificial intelligence](https://en.wikipedia.org/wiki/Wikipedia:Artificial_intelligence)  
* [User:Guy Macon/AI Slop Detection](https://en.wikipedia.org/wiki/User:Guy_Macon/AI_Slop_Detection)

**Notes**

1. Specifically, this guide is less useful for texts which are not informational writing. For example, the many tells specific to fiction (whispering woods, [Elara Voss](https://maxread.substack.com/p/who-is-elara-voss), etc.) are less relevant in Wikipedia and are not listed here.  
2. This can be directly observed by examining images generated by [text-to-image models](https://en.wikipedia.org/wiki/Text-to-image_model); they look acceptable at first glance, but specific details tend to be blurry and malformed. This is especially true for background objects and text.  
3. This effect is similar to how Claude's reasoning [can seem to leak into its conversational output](https://slhck.info/software/2026/06/22/claudish.html).  
4. [Example](https://en.wikipedia.org/wiki/Special:PermanentLink/1300700102) (deleted, administrators only)  
5. [Example](https://en.wikipedia.org/wiki/Special:PermanentLink/1297827841) of \`\`\`wikitext on a draft.  
6. See [WP:AISIGNS/Wikitext wrapped in Markdown code blocks from chatbots](https://en.wikipedia.org/wiki/Wikipedia:AISIGNS/Wikitext_wrapped_in_Markdown_code_blocks_from_chatbots)  
7. See [T387903](https://phabricator.wikimedia.org/T387903).  
8. There are extremely rare exceptions: for instance, Google has occasionally indexed URLs containing this parameter, which will remain if you click those results.  
9. Even older examples may be found [in this dataset](https://huggingface.co/datasets/msakota/edisum_dataset) of edit summaries generated with GPT 3.5-turbo.  
10. This can be seen in articles on Grokipedia, which are extremely long.

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAkUlEQVR4Xr2TSw6CQBAFew+eQi+DHEc24IaLulC8h3QnTUveAunnhEpqMzW/TDIiv7moD/cMjaJTP+4NGoXd8KU+pdANjdEtxujuplXf8n2rrJPayIp/Nlu0dw4wsgYYerVSh2QLMNQ+fkq2AIOdbgvvyRZgYA0wsAYYWHdBLdqC2rDE17vKChvASVmP/XqsMgOSuOiPx8OXWgAAAABJRU5ErkJggg==>