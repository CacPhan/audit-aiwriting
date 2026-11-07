"""
Unified 8-Field Economics Lexicon (expanded with Econometrics, Quantitative Research & Legal terms),
Cleaned Sino-Vietnamese Abstract Syllable Inventory, Entity Synonym Cycle Groups,
26 AI Writing Style Rule Definitions, and Contextual Rewrite Suggestion Engine.
"""

import re
from typing import Any, Dict, List, Set, Tuple

# 1. UNIFIED 8-FIELD ECONOMICS, ECONOMETRICS & BUSINESS LEXICON
# Covers: Quản trị kinh doanh, Quản trị nhân sự, Logistics & Hậu cần, Marketing,
# Ngân hàng, Tài chính, Kế toán – Kiểm toán, Quản trị sản xuất & Vận hành,
# plus Kinh tế lượng (SPSS/AMOS/SmartPLS/Stata/EViews) & Pháp lý kinh tế.
UNIFIED_ECONOMICS_TERMS: List[str] = sorted(
    list(
        {
            # --- Tài chính – Ngân hàng ---
            "biên lãi ròng",
            "thu nhập lãi thuần",
            "tỷ lệ thu nhập lãi cận biên",
            "tỷ lệ nợ xấu",
            "nợ xấu nội bảng",
            "xử lý nợ xấu",
            "nợ có khả năng mất vốn",
            "nợ dưới tiêu chuẩn",
            "nợ cần chú ý",
            "nợ nghi ngờ",
            "nợ quá hạn",
            "tỷ lệ an toàn vốn tối thiểu",
            "tỷ lệ an toàn vốn",
            "hệ số an toàn vốn tối thiểu",
            "hệ số an toàn vốn",
            "dự phòng rủi ro tín dụng",
            "trích lập dự phòng rủi ro",
            "thanh khoản hệ thống",
            "rủi ro thanh khoản",
            "rủi ro tín dụng",
            "rủi ro lãi suất",
            "rủi ro tỷ giá",
            "rủi ro hoạt động",
            "rủi ro thị trường",
            "rủi ro đạo đức",
            "rủi ro hệ thống",
            "quản trị rủi ro tín dụng",
            "quản trị rủi ro thanh khoản",
            "quản trị rủi ro",
            "thị trường liên ngân hàng",
            "lãi suất điều hành",
            "chính sách tiền tệ quốc gia",
            "chính sách tiền tệ",
            "chính sách tài khóa",
            "chính sách tín dụng",
            "tỷ giá hối đoái",
            "cấu trúc vốn tối ưu",
            "cấu trúc vốn",
            "đòn bẩy tài chính",
            "đòn bẩy hoạt động",
            "dòng tiền chiết khấu",
            "giá trị hiện tại ròng",
            "tỷ suất sinh lời nội bộ",
            "tỷ suất hoàn vốn nội bộ",
            "tỷ suất sinh lời trên tổng tài sản",
            "tỷ suất sinh lời trên tài sản",
            "tỷ suất sinh lời trên vốn chủ sở hữu",
            "tỷ suất sinh lời trên doanh thu",
            "tỷ suất sinh lời",
            "khả năng sinh lời",
            "khả năng thanh toán ngắn hạn",
            "khả năng thanh toán nhanh",
            "khả năng thanh toán tức thời",
            "khả năng thanh toán",
            "tiền gửi không kỳ hạn",
            "tiền gửi thanh toán",
            "tiền gửi tiết kiệm",
            "tiền gửi có kỳ hạn",
            "phân phối bảo hiểm qua ngân hàng",
            "ngân hàng thương mại cổ phần",
            "ngân hàng thương mại nhà nước",
            "ngân hàng thương mại",
            "ngân hàng nông nghiệp và phát triển nông thôn",
            "ngân hàng chính sách xã hội",
            "ngân hàng trung ương",
            "ngân hàng nhà nước việt nam",
            "ngân hàng nhà nước",
            "ngân hàng số",
            "ngân hàng điện tử",
            "tổ chức tín dụng phi ngân hàng",
            "tổ chức tín dụng",
            "quỹ tín dụng nhân dân",
            "thẩm định tín dụng",
            "quy trình cấp tín dụng",
            "chất lượng tín dụng",
            "hiệu quả hoạt động tín dụng",
            "hạn mức tín dụng",
            "tăng trưởng tín dụng",
            "dư nợ tín dụng",
            "tín dụng bán lẻ",
            "tín dụng xanh",
            "tài chính xanh",
            "tài chính toàn diện",
            "khẩu vị rủi ro",
            "tài sản có rủi ro",
            "tài sản bảo đảm",
            "tài sản thế chấp",
            "bảo lãnh ngân hàng",
            "tín dụng chứng từ",
            "thanh toán quốc tế",
            "thanh toán không dùng tiền mặt",
            "định danh điện tử",
            "dự trữ bắt buộc",
            "nghiệp vụ thị trường mở",
            "tái cấp vốn",
            "tái chiết khấu",
            "thu nhập ngoài lãi",
            "vốn lưu động ròng",
            "quản trị vốn lưu động ròng",
            "quản trị vốn lưu động",
            "vốn chủ sở hữu",
            "vốn điều lệ",
            "vốn đầu tư trực tiếp nước ngoài",
            "chi phí sử dụng vốn bình quân gia quyền",
            "chi phí sử dụng vốn",
            "chi phí huy động vốn",
            "tình hình huy động vốn",
            "cơ cấu nguồn vốn huy động",
            "huy động vốn",
            "chi phí đại diện",
            "lý thuyết đại diện",
            "bất cân xứng thông tin",
            "thị trường chứng khoán",
            "thị trường vốn",
            "thị trường tiền tệ",
            "thị trường tài chính",
            "trái phiếu doanh nghiệp",
            "trái phiếu chính phủ",
            "cổ phiếu phổ thông",
            "danh mục đầu tư",
            "định giá tài sản vốn",
            "phái sinh tài chính",
            "chính sách cổ tức",
            "dòng tiền tự do",
            # --- Kế toán – Kiểm toán ---
            "báo cáo tài chính hợp nhất",
            "báo cáo tài chính",
            "bảng cân đối kế toán",
            "báo cáo kết quả hoạt động kinh doanh",
            "kết quả hoạt động sản xuất kinh doanh",
            "kết quả hoạt động kinh doanh",
            "báo cáo lưu chuyển tiền tệ",
            "thuyết minh báo cáo tài chính",
            "chuẩn mực kế toán việt nam",
            "chuẩn mực kế toán quốc tế",
            "chuẩn mực báo cáo tài chính quốc tế",
            "chuẩn mực kiểm toán việt nam",
            "hệ thống kiểm soát nội bộ",
            "kiểm soát nội bộ",
            "rủi ro có sai sót trọng yếu",
            "sai sót trọng yếu",
            "trọng yếu và rủi ro kiểm toán",
            "rủi ro kiểm toán",
            "rủi ro tiềm tàng",
            "rủi ro kiểm soát",
            "rủi ro phát hiện",
            "bằng chứng kiểm toán",
            "hồ sơ kiểm toán",
            "ý kiến kiểm toán chấp nhận toàn phần",
            "ý kiến kiểm toán ngoại trừ",
            "khấu hao tài sản cố định",
            "tài sản cố định hữu hình",
            "tài sản cố định vô hình",
            "tài sản cố định",
            "tài sản ngắn hạn",
            "tài sản dài hạn",
            "nợ phải trả",
            "khoản phải thu khách hàng",
            "dự phòng phải thu khó đòi",
            "khoản phải thu",
            "hàng tồn kho",
            "giá vốn hàng bán",
            "doanh thu thuần về bán hàng và cung cấp dịch vụ",
            "lợi nhuận sau thuế thu nhập doanh nghiệp",
            "lợi nhuận trước thuế",
            "lợi nhuận sau thuế",
            "lợi nhuận gộp",
            "chi phí trả trước",
            "kế toán quản trị",
            "kế toán tài chính",
            "tính giá thành sản phẩm",
            "kiểm toán độc lập",
            "kiểm toán nội bộ",
            "kiểm toán nhà nước",
            "ghi nhận doanh thu",
            "kỳ kế toán",
            "sổ cái",
            # --- Quản trị sản xuất & Vận hành ---
            "quản trị sản xuất tinh gọn",
            "sản xuất tinh gọn",
            "hoạch định nguồn lực doanh nghiệp",
            "hệ thống hoạch định nguồn lực doanh nghiệp",
            "quản lý chất lượng toàn diện",
            "quản trị chất lượng toàn diện",
            "hệ thống quản lý chất lượng",
            "bảo trì năng suất toàn diện",
            "cân bằng chuyền",
            "định mức nguyên vật liệu",
            "hoạch định nhu cầu nguyên vật liệu",
            "năng lực sản xuất",
            "công suất thiết kế",
            "điểm hòa vốn",
            "thời gian chu kỳ",
            "tỷ lệ phế phẩm",
            "kiểm soát chất lượng bằng thống kê",
            "sản xuất tức thời",
            "điều độ sản xuất",
            "bố trí mặt bằng sản xuất",
            "quản trị vận hành",
            "quản trị sản xuất và tác nghiệp",
            "hiệu suất thiết bị tổng thể",
            "tự động hóa quy trình",
            "năng suất nhân tố tổng hợp",
            # --- Logistics & Hậu cần ---
            "quản trị chuỗi cung ứng",
            "chuỗi cung ứng lạnh",
            "chuỗi cung ứng xanh",
            "chuỗi cung ứng",
            "tồn kho an toàn",
            "quản trị hàng tồn kho",
            "vòng quay hàng tồn kho",
            "thời gian chờ",
            "vận tải đa phương thức",
            "trung tâm phân phối",
            "kho ngoại quan",
            "dịch vụ logistics bên thứ ba",
            "dịch vụ logistics",
            "chi phí logistics",
            "truy xuất nguồn gốc",
            "chi phí lưu kho",
            "thông quan hàng hóa",
            "thủ tục hải quan điện tử",
            "luồng hàng hải",
            "vận đơn đường biển",
            "cảng cạn",
            "giao nhận hàng hóa quốc tế",
            "xuất nhập khẩu",
            "điều kiện thương mại quốc tế",
            "tối ưu hóa tuyến đường",
            "logistics ngược",
            # --- Quản trị kinh doanh, Nhân sự & Marketing ---
            "lợi thế cạnh tranh bền vững",
            "lợi thế cạnh tranh",
            "năng lực cạnh tranh cốt lõi",
            "năng lực cạnh tranh",
            "chuỗi giá trị toàn cầu",
            "chuỗi giá trị",
            "năng lực cốt lõi",
            "quản trị chiến lược",
            "quản trị doanh nghiệp",
            "cơ cấu tổ chức bộ máy quản lý",
            "cơ cấu tổ chức",
            "hội đồng quản trị",
            "ban kiểm soát",
            "ban giám đốc",
            "văn hóa doanh nghiệp",
            "đạo đức kinh doanh",
            "trách nhiệm xã hội của doanh nghiệp",
            "phát triển bền vững",
            "doanh nghiệp nhỏ và vừa",
            "doanh nghiệp vừa và nhỏ",
            "quản trị nguồn nhân lực",
            "phát triển nguồn nhân lực",
            "nguồn nhân lực chất lượng cao",
            "đánh giá thực hiện công việc",
            "thu hút và giữ chân nhân tài",
            "đãi ngộ toàn diện",
            "chế độ đãi ngộ",
            "tiền lương và phúc lợi",
            "thù lao lao động",
            "động lực làm việc của nhân viên",
            "động lực làm việc",
            "tạo động lực lao động",
            "sự gắn kết của nhân viên",
            "cam kết gắn bó với tổ chức",
            "gắn kết nhân viên",
            "sự hài lòng trong công việc",
            "đào tạo và phát triển nguồn nhân lực",
            "tuyển dụng và đào tạo",
            "hoạch định nguồn nhân lực",
            "khung năng lực",
            "định biên nhân sự",
            "bản mô tả công việc",
            "phân tích công việc",
            "thương hiệu nhà tuyển dụng",
            "quan hệ lao động",
            "năng suất lao động",
            "phân khúc thị trường",
            "thị trường mục tiêu",
            "định vị thương hiệu",
            "nhận diện thương hiệu",
            "nhận thức thương hiệu",
            "hình ảnh thương hiệu",
            "tài sản thương hiệu",
            "giá trị thương hiệu",
            "hành vi người tiêu dùng",
            "quyết định mua hàng",
            "ý định mua hàng",
            "truyền thông marketing tích hợp",
            "trải nghiệm khách hàng",
            "sự hài lòng của khách hàng",
            "chất lượng dịch vụ chăm sóc khách hàng",
            "chăm sóc khách hàng",
            "chất lượng dịch vụ",
            "giá trị cảm nhận của khách hàng",
            "giá trị vòng đời khách hàng",
            "lòng trung thành của khách hàng",
            "sự trung thành của khách hàng",
            "tiếp thị kỹ thuật số",
            "marketing kỹ thuật số",
            "hành trình khách hàng",
            "nghiên cứu thị trường",
            "kênh phân phối",
            "xúc tiến thương mại",
            "mua bán và sáp nhập",
            "quản trị quan hệ khách hàng",
            "khách hàng cá nhân",
            "khách hàng doanh nghiệp",
            "chuyển đổi số",
            # --- Kinh tế lượng, Thống kê & Phương pháp nghiên cứu ---
            "phân tích nhân tố khám phá",
            "phân tích nhân tố khẳng định",
            "mô hình cấu trúc tuyến tính",
            "mô hình phương trình cấu trúc",
            "phân tích hồi quy tuyến tính bội",
            "phân tích hồi quy đa biến",
            "hồi quy tuyến tính",
            "phương pháp bình phương nhỏ nhất",
            "mô hình tác động cố định",
            "mô hình tác động ngẫu nhiên",
            "phương pháp moment tổng quát",
            "kiểm định độ tin cậy thang đo",
            "hệ số tương quan biến tổng",
            "kiểm định giả thuyết nghiên cứu",
            "mức ý nghĩa thống kê",
            "ý nghĩa thống kê",
            "thống kê mô tả",
            "phân tích tương quan",
            "đa cộng tuyến",
            "phương sai sai số thay đổi",
            "tự tương quan",
            "phương sai trích",
            "hệ số tải nhân tố",
            "dữ liệu bảng",
            "mô hình thực nghiệm",
            "biến phụ thuộc",
            "biến độc lập",
            "biến kiểm soát",
            "biến trung gian",
            "biến điều tiết",
            "biến quan sát",
        }
    ),
    key=lambda s: len(s),
    reverse=True,
)


# 2. SINO-VIETNAMESE ABSTRACT SYLLABLES (Used for LEX-VN-01 Congestion Detection)
# Cleaned of pure Vietnamese / basic concrete words (ngân, hàng, rủi, ro, tiêu, dùng, số, lượng, chất, mức, độ, lợi, ích, nhân, lực)
# so that only genuine bureaucratic/abstract Sino-Vietnamese syllable chains are flagged.
SINO_VIETNAMESE_ABSTRACT_SYLLABLES: Set[str] = {
    "thực", "hiện", "quy", "trình", "chuyển", "đổi", "mô", "hình", "quản", "trị",
    "tập", "trung", "triển", "khai", "tối", "ưu", "hóa", "hiệu", "suất", "cấu",
    "trúc", "chiến", "lược", "hệ", "thống", "phương", "diện", "khía", "cạnh", "bối",
    "cảnh", "toàn", "diện", "đồng", "bộ", "phát", "triển", "bền", "vững", "tăng",
    "cường", "thúc", "đẩy", "nâng", "cao", "đảm", "bảo", "duy", "trì", "thiết",
    "lập", "định", "hướng", "vận", "hành", "tích", "hợp", "tương", "tác", "điều",
    "tiết", "kiểm", "soát", "phân", "bổ", "nguồn", "giải", "pháp", "cơ",
    "chế", "chính", "sách", "tác", "động", "biến", "vĩ",
    "tiềm", "năng", "thách", "thức", "triển", "vọng", "hiện", "đại",
    "tiêu", "chuẩn", "nguyên", "tắc", "mục", "nhiệm", "vụ", "chức",
    "vị", "thế", "thành", "tựu", "tiến", "giai", "đoạn", "xu", "hướng", "trạng", "thái",
    "phạm", "vi", "tổ", "chức", "hoàn", "thiện", "củng", "cố", "xác",
    "giám", "sát", "phối", "liên", "kết", "tổng", "thể", "khách", "quan", "chủ",
    "tất", "yếu", "đa", "chiều", "sâu", "sắc", "triệt", "để", "linh", "hoạt",
    "chuyên", "nghiệp", "minh", "bạch", "hài", "hòa", "xuyên", "suốt", "trọng", "tâm",
    "đột", "phá", "tiên", "phong", "cốt", "lõi", "nền", "tảng", "kiến", "tạo",
    "tiết", "giảm", "tái", "thích", "ứng",
}


# 3. AI INTENSIFIER VOCABULARY CLUSTER (For LEX-01b Density Counter)
AI_INTENSIFIER_VOCAB: Set[str] = {
    "then chốt",
    "cốt lõi",
    "toàn diện",
    "đồng bộ",
    "sâu sắc",
    "triệt để",
    "đột phá",
    "bền vững",
    "thiết yếu",
    "mạnh mẽ",
    "vượt bậc",
    "tối ưu",
    "sống còn",
    "cấp thiết",
    "khắt khe",
    "gắt gao",
    "bệ phóng",
    "kim chỉ nam",
    "nút thắt",
    "mắt xích",
    "trụ cột",
    "đòn bẩy",
    "khai phá",
    "kiến tạo",
    "tiền đề",
    "động lực",
    "hài hòa",
    "chuyên sâu",
}

# 4. VAGUE HEDGING QUALIFIER PATTERNS (For LEX-05 Stealth Academic AI Hedging Inflation)
VAGUE_HEDGING_PATTERNS: List[str] = [
    r"\btương\s+đối\s+(?:nhanh|chậm|cao|thấp|tốt|xấu|đầy\s+đủ|rõ\s+ràng|hợp\s+lý|tích\s+cực|tiêu\s+cực|đồng\s+đều|chặt\s+chẽ|hiệu\s+quả|ổn\s+định|lớn|nhỏ|phổ\s+biến|thuận\s+lợi|hoàn\s+thiện|cụ\s+thể|nhất\s+quán|phù\s+hợp)\b",
    r"\b(?:một\s+số|những)\s+[^,.!?]{2,35}?\s+nhất\s+định\b",
    r"\bở\s+mức\s+độ\s+nhất\s+định\b",
    r"\bphần\s+nào\s+(?:phản\s+ánh|thể\s+hiện|tác\s+động|ảnh\s+hưởng|cho\s+thấy|giúp|góp\s+phần|hạn\s+chế)\b",
]


# 5. ENTITY SYNONYM CYCLING GROUPS ACROSS 8 ECONOMICS FIELDS (12 Groups for LEX-04)
SYNONYM_CYCLE_GROUPS: List[List[str]] = [
    # 1. Ngân hàng / Tổ chức tín dụng
    [
        r"ngân\s+hàng(?:\s+này|\s+đó|\s+trên|\s+nói\s+trên|\s+vừa\s+nêu)?",
        r"tổ\s+chức\s+tín\s+dụng(?:\s+này|\s+đó|\s+trên|\s+nói\s+trên|\s+vừa\s+nêu)?",
        r"định\s+chế\s+tài\s+chính(?:\s+này|\s+đó|\s+trên|\s+nói\s+trên|\s+vừa\s+nêu)?",
        r"nhà\s+băng(?:\s+này|\s+đó|\s+trên|\s+nói\s+trên)?",
        r"đơn\s+vị\s+cấp\s+vốn(?:\s+này|\s+đó|\s+trên)?",
    ],
    # 2. Doanh nghiệp / Công ty / Tập đoàn
    [
        r"doanh\s+nghiệp(?:\s+này|\s+đó|\s+trên|\s+nói\s+trên|\s+vừa\s+nêu)",
        r"công\s+ty(?:\s+này|\s+đó|\s+trên|\s+nói\s+trên|\s+vừa\s+nêu)",
        r"tập\s+đoàn(?:\s+này|\s+đó|\s+trên|\s+nói\s+trên|\s+vừa\s+nêu)",
        r"đơn\s+vị\s+kinh\s+doanh(?:\s+này|\s+đó|\s+trên|\s+nói\s+trên)?",
        r"tổ\s+chức\s+kinh\s+tế(?:\s+này|\s+đó|\s+trên|\s+nói\s+trên)?",
        r"chủ\s+thể\s+kinh\s+doanh(?:\s+này|\s+đó|\s+trên)?",
        r"pháp\s+nhân\s+thương\s+mại(?:\s+này|\s+đó|\s+trên)?",
    ],
    # 3. Khách hàng / Người tiêu dùng
    [
        r"khách\s+hàng(?:\s+này|\s+đó|\s+trên)?",
        r"người\s+tiêu\s+dùng(?:\s+này|\s+đó|\s+trên)?",
        r"người\s+mua\s+hàng(?:\s+này|\s+đó)?",
        r"thượng\s+đế",
        r"đối\s+tượng\s+phục\s+vụ(?:\s+này|\s+đó)?",
        r"người\s+thụ\s+hưởng\s+dịch\s+vụ(?:\s+này|\s+đó)?",
    ],
    # 4. Nhân sự / Lao động
    [
        r"người\s+lao\s+động(?:\s+này|\s+đó|\s+trên)?",
        r"đội\s+ngũ\s+nhân\s+sự(?:\s+này|\s+đó|\s+trên)?",
        r"lực\s+lượng\s+nhân\s+viên(?:\s+này|\s+đó)?",
        r"cán\s+bộ\s+công\s+nhân\s+viên(?:\s+này|\s+đó)?",
        r"tài\s+sản\s+con\s+người",
        r"đội\s+ngũ\s+cán\s+bộ(?:\s+này|\s+đó|\s+trên)?",
    ],
    # 5. Nhà đầu tư / Cổ đông
    [
        r"nhà\s+đầu\s+tư(?:\s+này|\s+đó|\s+trên)?",
        r"cổ\s+đông(?:\s+này|\s+đó|\s+trên)?",
        r"chủ\s+sở\s+hữu\s+vốn(?:\s+này|\s+đó)?",
        r"nhà\s+rót\s+vốn(?:\s+này|\s+đó)?",
        r"các\s+bên\s+góp\s+vốn(?:\s+này|\s+đó|\s+trên)?",
    ],
    # 6. Thị trường / Thương trường
    [
        r"thị\s+trường(?:\s+này|\s+đó|\s+trên|\s+nói\s+trên)",
        r"sân\s+chơi\s+kinh\s+tế(?:\s+này|\s+đó)?",
        r"thương\s+trường(?:\s+này|\s+đó)?",
        r"môi\s+trường\s+cạnh\s+tranh(?:\s+này|\s+đó|\s+trên)?",
        r"không\s+gian\s+thương\s+mại(?:\s+này|\s+đó)?",
    ],
    # 7. Chuỗi cung ứng / Mạng lưới hậu cần
    [
        r"chuỗi\s+cung\s+ứng(?:\s+này|\s+đó|\s+trên)?",
        r"mạng\s+lưới\s+hậu\s+cần(?:\s+này|\s+đó|\s+trên)?",
        r"hệ\s+thống\s+phân\s+phối(?:\s+này|\s+đó|\s+trên)?",
        r"dòng\s+chảy\s+hàng\s+hóa(?:\s+này|\s+đó)?",
        r"mạch\s+máu\s+lưu\s+thông",
    ],
    # 8. Thương hiệu / Nhãn hàng / Nhà mốt
    [
        r"thương\s+hiệu(?:\s+này|\s+đó|\s+trên|\s+nói\s+trên|\s+vừa\s+nêu)",
        r"nhãn\s+hàng(?:\s+này|\s+đó|\s+trên|\s+nói\s+trên|\s+vừa\s+nêu)?",
        r"tên\s+tuổi(?:\s+này|\s+đó|\s+trên)?",
        r"nhà\s+mốt(?:\s+này|\s+đó|\s+trên)?",
    ],
    # 9. Dự án / Gói thầu / Thương vụ / Hợp đồng
    [
        r"dự\s+án(?:\s+này|\s+đó|\s+trên|\s+nói\s+trên|\s+vừa\s+nêu)",
        r"gói\s+thầu(?:\s+này|\s+đó|\s+trên|\s+nói\s+trên)?",
        r"thương\s+vụ(?:\s+này|\s+đó|\s+trên|\s+nói\s+trên)?",
        r"hợp\s+đồng(?:\s+này|\s+đó|\s+trên|\s+nói\s+trên)",
    ],
    # 10. Sản phẩm / Mặt hàng / Dòng sản phẩm / Giải pháp
    [
        r"sản\s+phẩm(?:\s+này|\s+đó|\s+trên|\s+nói\s+trên|\s+vừa\s+nêu)",
        r"mặt\s+hàng(?:\s+này|\s+đó|\s+trên|\s+nói\s+trên)?",
        r"dòng\s+sản\s+phẩm(?:\s+này|\s+đó|\s+trên|\s+nói\s+trên)?",
        r"giải\s+pháp(?:\s+này|\s+đó|\s+trên|\s+nói\s+trên)",
    ],
    # 11. Người quản lý / Nhà lãnh đạo / Cấp trên / Đội ngũ quản trị
    [
        r"người\s+quản\s+lý(?:\s+này|\s+đó|\s+trên)?",
        r"nhà\s+lãnh\s+đạo(?:\s+này|\s+đó|\s+trên)?",
        r"cấp\s+trên(?:\s+này|\s+đó|\s+trên)?",
        r"đội\s+ngũ\s+quản\s+trị(?:\s+này|\s+đó|\s+trên)?",
    ],
    # 12. Nền tảng / Sàn thương mại điện tử / Kênh trực tuyến / Hệ thống
    [
        r"nền\s+tảng(?:\s+này|\s+đó|\s+trên|\s+nói\s+trên)",
        r"sàn\s+thương\s+mại\s+điện\s+tử(?:\s+này|\s+đó|\s+trên)?",
        r"kênh\s+trực\s+tuyến(?:\s+này|\s+đó|\s+trên)?",
        r"hệ\s+thống(?:\s+này|\s+đó|\s+trên|\s+nói\s+trên)",
    ],
]


# 6. 26 STANDARDIZED AI WRITING STYLE RULES METADATA
RULE_METADATA: Dict[str, Dict[str, Any]] = {
    "LEX-01": {
        "id": "LEX-01",
        "name": "Mật độ cao 'Từ vựng định danh AI' & Sáo ngữ học thuật giả tạo",
        "category": "LEXICAL",
        "priority_stage": "P3",
        "severity": "warning",
        "severityLabel": "Nên sửa",
        "userTitle": "Từ vựng hoa mỹ hoặc mật độ từ khuếch đại cao",
        "userReason": "Các cụm từ như 'bức tranh toàn cảnh', 'kim chỉ nam xuyên suốt', 'nút thắt cổ chai', 'tảng băng chìm' hoặc mật độ từ khuếch đại dày đặc mang sắc thái chung chung, làm giảm độ sắc nét học thuật.",
        "userSuggestion": "Thay bằng động từ chuyên ngành hoặc chỉ số định lượng cụ thể phản ánh trực tiếp cơ chế kinh tế.",
    },
    "LEX-02": {
        "id": "LEX-02",
        "name": "Né tránh hệ từ cơ bản 'là/có' bằng động từ phô trương",
        "category": "LEXICAL",
        "priority_stage": "P3",
        "severity": "suggestion",
        "severityLabel": "Gợi ý",
        "userTitle": "Dùng động từ vòng vo thay cho hệ từ cơ bản 'là / có'",
        "userReason": "Các cụm 'đóng vai trò như là', 'được xem như là một', 'sở hữu', 'tự hào có', 'giữ vị thế là' khi mô tả khái niệm hoặc số liệu tạo cảm giác phô trương không cần thiết.",
        "userSuggestion": "Chuyển về hệ từ trực diện ('là', 'có', 'gồm', 'chiếm') để câu văn chuẩn mực và khách quan.",
    },
    "LEX-03": {
        "id": "LEX-03",
        "name": "Ngôn ngữ quảng cáo, tán dương sáo rỗng",
        "category": "LEXICAL",
        "priority_stage": "P3",
        "severity": "warning",
        "severityLabel": "Nên sửa",
        "userTitle": "Diễn đạt phóng đại thiếu thước đo cụ thể",
        "userReason": "Cụm từ mang sắc thái quảng cáo và tán dương ('bứt phá mạnh mẽ', 'nhảy vọt phi mã', 'vươn ra biển lớn', 'thành tựu rực rỡ') làm giảm tính khách quan của nghiên cứu.",
        "userSuggestion": "Lược bỏ các tính từ tán dương; chỉ giữ lại dữ kiện thực nghiệm, tỷ lệ phần trăm hoặc cơ chế tác động thực tế.",
    },
    "LEX-04": {
        "id": "LEX-04",
        "name": "Đa dạng từ vựng giả tạo / Né lặp từ cơ học",
        "category": "LEXICAL",
        "priority_stage": "P3",
        "severity": "suggestion",
        "severityLabel": "Gợi ý",
        "userTitle": "Xoay vòng từ đồng nghĩa gây nhiễu thuật ngữ",
        "userReason": "Việc thay thế liên tục một thuật ngữ chuẩn bằng nhiều cách gọi hoa mỹ ('ngân hàng này -> định chế tài chính trên -> nhà băng này') gây hiểu nhầm trong văn bản học thuật.",
        "userSuggestion": "Cố định 1 thuật ngữ chuẩn xuyên suốt hoặc tỉnh lược chủ ngữ khi hai mệnh đề cùng quy chiếu.",
    },
    "LEX-05": {
        "id": "LEX-05",
        "name": "Diễn đạt mơ hồ về mối liên hệ & Lạm dụng từ rào đón mức độ",
        "category": "LEXICAL",
        "priority_stage": "P3",
        "severity": "suggestion",
        "severityLabel": "Gợi ý",
        "userTitle": "Mô tả quan hệ nhân quả mơ hồ hoặc lạm dụng từ rào đón ('tương đối / nhất định')",
        "userReason": "Các cụm 'gắn liền với', 'có mối liên hệ mật thiết với' hoặc việc lặp lại dày đặc các từ rào đón 'tương đối...', 'một số... nhất định' không chỉ rõ mức độ tác động thực tế.",
        "userSuggestion": "Nêu trực tiếp động từ tác động và thay các từ rào đón mơ hồ ('tương đối', 'nhất định') bằng con số hoặc tỷ lệ phần trăm cụ thể.",
    },
    "LEX-VN-01": {
        "id": "LEX-VN-01",
        "name": "Tắc nghẽn âm tiết Hán – Việt & Danh hóa chuỗi",
        "category": "LEXICAL",
        "priority_stage": "P3",
        "severity": "warning",
        "severityLabel": "Nên sửa",
        "userTitle": "Chuỗi từ ghép Hán–Việt và danh hóa dày đặc",
        "userReason": "Nhiều từ ghép Hán–Việt trừu tượng nối tiếp nhau ('thực hiện quy trình chuyển đổi mô hình quản trị...') làm câu văn nặng nề, khó theo dõi.",
        "userSuggestion": "Giải nén danh từ trừu tượng thành động từ hành động cụ thể và giữ nguyên các thuật ngữ chuyên ngành cốt lõi.",
    },
    "SYN-01": {
        "id": "SYN-01",
        "name": "Đẳng cấu cú pháp liên câu (Syntactic Isomorphism)",
        "category": "SYNTACTIC",
        "priority_stage": "P2",
        "severity": "warning",
        "severityLabel": "Nên sửa",
        "userTitle": "Các câu liên tiếp lặp lại cùng một khuôn cú pháp",
        "userReason": "Nhiều câu liên tiếp đều mở đầu bằng cùng một khung trạng ngữ hoặc cùng một mẫu bình luận tiêu chí ('Tiêu chí X đạt Y điểm...'), tạo nhịp điệu đơn điệu.",
        "userSuggestion": "Gộp các câu có quan hệ nhân quả/so sánh trực tiếp và thay đổi cách mở câu (mở bằng chủ ngữ trực diện hoặc nhóm các tiêu chí có chung xu hướng).",
    },
    "SYN-02": {
        "id": "SYN-02",
        "name": "Mệnh đề phụ tổng kết/đánh giá giả tạo cuối câu",
        "category": "SYNTACTIC",
        "priority_stage": "P2",
        "severity": "warning",
        "severityLabel": "Nên sửa",
        "userTitle": "Mệnh đề đuôi 'qua đó / từ đó / góp phần' lặp lại cuối câu",
        "userReason": "Đuôi câu gắn thêm nhận định tổng kết chung chung ('qua đó nâng cao...', 'từ đó đảm bảo...', 'góp phần tối ưu hóa...') mà không bổ sung dữ kiện định lượng mới.",
        "userSuggestion": "Cắt bỏ mệnh đề đuôi nếu không chứa số liệu mới, hoặc thay bằng mục đích cụ thể ('nhằm giảm chi phí giao dịch').",
    },
    "SYN-03": {
        "id": "SYN-03",
        "name": "Cấu trúc sóng đôi phủ định (Negative Parallelisms)",
        "category": "SYNTACTIC",
        "priority_stage": "P3",
        "severity": "warning",
        "severityLabel": "Nên sửa",
        "userTitle": "Cấu trúc sóng đôi phủ định ('không chỉ... mà còn...', 'không phải X mà là Y', 'chứ không phải')",
        "userReason": "Cách đặt vấn đề theo khuôn mẫu phủ định vế đầu để tôn vế sau ('không phải là X mà là Y', 'X chứ không phải Y', 'không chỉ... mà còn...') lặp lại dày đặc mang dấu ấn diễn ngôn máy móc.",
        "userSuggestion": "Chuyển sang câu khẳng định trực diện nêu thẳng bản chất của đối tượng hoặc dùng cặp từ 'đồng thời', 'vừa... vừa...' gắn với chỉ tiêu cụ thể.",
    },
    "SYN-04": {
        "id": "SYN-04",
        "name": "Quy tắc số 3 cơ học (Mechanical Rule of Three)",
        "category": "SYNTACTIC",
        "priority_stage": "P3",
        "severity": "suggestion",
        "severityLabel": "Gợi ý",
        "userTitle": "Cấu trúc liệt kê ba vế tính từ/động từ lặp lại",
        "userReason": "Việc liệt kê liên tiếp các bộ ba từ gần nghĩa ('đồng bộ, toàn diện và hiệu quả' hoặc 'nâng cao..., tối ưu hóa... và thúc đẩy...') tạo cảm giác dàn trải.",
        "userSuggestion": "Rút gọn về 1–2 khái niệm chính xác nhất gắn với chỉ tiêu đo lường thực tế.",
    },
    "SYN-VN-01": {
        "id": "SYN-VN-01",
        "name": "Dư thừa đại từ chỉ định & Chèn 'vì vậy' giữa Chủ–Vị theo lối dịch máy",
        "category": "VIETNAMESE_SYNTAX",
        "priority_stage": "P2",
        "severity": "warning",
        "severityLabel": "Nên sửa",
        "userTitle": "Lạm dụng đại từ chỉ định hoặc chèn 'vì vậy' vào giữa Chủ ngữ và Vị ngữ",
        "userReason": "Câu văn lặp lại cơ học 'nó', 'điều này', 'của họ' hoặc chèn 'vì vậy' ngay giữa Chủ ngữ và Vị ngữ ('Doanh nghiệp vì vậy cần...') theo lối dịch từng từ từ tiếng Anh ('Subject therefore Verb').",
        "userSuggestion": "Chuyển liên từ 'Vì vậy,' lên đầu câu hoặc dùng 'nên / do đó' trước mệnh đề kết quả; lược bỏ các đại từ 'nó / của họ / của mình' dư thừa.",
    },
    "SYN-VN-02": {
        "id": "SYN-VN-02",
        "name": "Đánh mất cấu trúc Đề – Thuyết vì khung Chủ – Vị dịch máy",
        "category": "VIETNAMESE_SYNTAX",
        "priority_stage": "P2",
        "severity": "suggestion",
        "severityLabel": "Gợi ý",
        "userTitle": "Mở câu vòng vo bằng khung 'Đối với..., / Về mặt..., nó...'",
        "userReason": "Khuôn câu 'Đối với X, điều này / nó thường được...' tách rời chủ đề khỏi vị ngữ và chèn đại từ thừa.",
        "userSuggestion": "Đưa thẳng đối tượng X lên đầu câu làm Đề ngữ và chuyển vị ngữ sang dạng chủ động.",
    },
    "SYN-VN-03": {
        "id": "SYN-VN-03",
        "name": "Bị động dịch máy ('được/bị... bởi') & Danh hóa 'Việc + V' làm chủ ngữ",
        "category": "VIETNAMESE_SYNTAX",
        "priority_stage": "P2",
        "severity": "suggestion",
        "severityLabel": "Gợi ý",
        "userTitle": "Câu bị động ('được... bởi') và lạm dụng danh hóa ('Việc + động từ...') đầu câu",
        "userReason": "Lồng ghép nhiều cụm danh hóa mở đầu bằng 'Việc thực hiện / Việc triển khai...' hoặc thể bị động dịch máy khiến câu văn nặng nề.",
        "userSuggestion": "Đưa chủ thể hành động (doanh nghiệp, ngân hàng, bộ phận) lên làm chủ ngữ trực tiếp thay vì mở câu bằng 'Việc + động từ'.",
    },
    "RHY-01": {
        "id": "RHY-01",
        "name": "Độ biến thiên chiều dài câu cực thấp (Low Burstiness)",
        "category": "DISCOURSE",
        "priority_stage": "P3",
        "severity": "suggestion",
        "severityLabel": "Gợi ý",
        "userTitle": "Độ dài các câu trong đoạn quá đồng đều (nhịp văn đều đều)",
        "userReason": "Tất cả các câu trong đoạn đều có số lượng chữ xấp xỉ nhau, thiếu sự đan xen giữa câu ngắn nêu nhận định và câu phức phân tích sâu.",
        "userSuggestion": "Gộp 2 câu có quan hệ đối lập/nhân quả thành câu phức bằng dấu hai chấm (:) và rút gọn câu mở đoạn thành câu đơn ngắn gọn.",
    },
    "DIS-01": {
        "id": "DIS-01",
        "name": "Cấu trúc 'Đoạn văn đóng hộp' khép kín",
        "category": "DISCOURSE",
        "priority_stage": "P1",
        "severity": "warning",
        "severityLabel": "Nên sửa",
        "userTitle": "Đoạn văn đóng khung khép kín ('Nhận định -> Tuy nhiên/Cụ thể -> Do đó/Như vậy')",
        "userReason": "Đoạn văn vận hành theo khuôn mẫu cứng nhắc: Mở đoạn -> Giải thích/Phản biện -> Tự kết luận khép kín, làm đứt mạch liên kết tự nhiên sang đoạn tiếp theo.",
        "userSuggestion": "Lược bỏ câu tổng kết sáo rỗng cuối đoạn thân bài và chuyển ý trực tiếp sang vấn đề của đoạn kế tiếp.",
    },
    "DIS-02": {
        "id": "DIS-02",
        "name": "Câu kết đoạn / Đoạn kết tiểu mục tổng kết thừa (Echoic Closure)",
        "category": "DISCOURSE",
        "priority_stage": "P1",
        "severity": "warning",
        "severityLabel": "Nên sửa",
        "userTitle": "Câu hoặc đoạn kết tiểu mục tóm tắt lặp lại ý cũ ('Như vậy, / Nhìn chung, / Đây là cơ sở để...')",
        "userReason": "Câu hoặc đoạn ngắn cuối mục bắt đầu bằng 'Tóm lại,', 'Nhìn chung,', 'Như vậy,' hoặc kết bằng 'Đây là cơ sở để tiếp tục đề xuất giải pháp ở Chương 3' lặp lại ở cuối mọi tiểu mục gây dư thừa.",
        "userSuggestion": "Xóa đoạn/câu kết tiểu mục mang tính chuyển tiếp công thức, hoặc giữ lại tối đa 1 lần ở phần Kết luận cuối chương.",
    },
    "DIS-03": {
        "id": "DIS-03",
        "name": "Lạm dụng từ nối khung đầu câu cơ học",
        "category": "DISCOURSE",
        "priority_stage": "P2",
        "severity": "suggestion",
        "severityLabel": "Gợi ý",
        "userTitle": "Mật độ từ nối đóng khung đầu câu cao ('Cụ thể, / Tuy nhiên, / Do đó,')",
        "userReason": "Việc gắn từ nối kèm dấu phẩy ở đầu hầu hết các câu hoặc các đoạn liên tiếp làm mạch văn bị cắt khúc cơ học.",
        "userSuggestion": "Giữ tối đa 1 từ nối đầu câu trong đoạn; chuyển các liên kết còn lại vào phụ từ nội câu ('cũng', 'vẫn', 'lại', 'nhờ đó').",
    },
    "DIS-04": {
        "id": "DIS-04",
        "name": "Dẫn nhập siêu diễn ngôn & Định danh tiêu đề/bảng biểu rập khuôn",
        "category": "DISCOURSE",
        "priority_stage": "P3",
        "severity": "suggestion",
        "severityLabel": "Gợi ý",
        "userTitle": "Mở đầu bằng định nghĩa tiêu đề hoặc câu dẫn nhập bảng biểu rập khuôn",
        "userReason": "Các câu mở đầu dạng 'X được hiểu là...', 'Bảng trên cho thấy ba điểm...', 'X là hạng mục trọng tâm...' lặp lại cùng một công thức dẫn nhập.",
        "userSuggestion": "Đi thẳng vào số liệu nổi bật nhất trong bảng hoặc cơ chế nghiệp vụ thực tế thay vì câu dẫn nhập công thức.",
    },
    "ARG-01": {
        "id": "ARG-01",
        "name": "Trọng số luận điểm phẳng & Mật độ thông tin đồng đều",
        "category": "ARGUMENTATION",
        "priority_stage": "P1",
        "severity": "suggestion",
        "severityLabel": "Gợi ý",
        "userTitle": "Các luận điểm được chia dung lượng ngang nhau, thiếu trọng tâm và số liệu",
        "userReason": "Đoạn văn liệt kê các yếu tố ('Thứ nhất... Thứ hai... Thứ ba...' hoặc 'Trước hết... Bên cạnh đó... Ngoài ra...') với độ dài tương đương nhau và vắng bóng số liệu thực nghiệm.",
        "userSuggestion": "Phân bổ dung lượng sâu hơn cho nguyên nhân cốt lõi (kèm số liệu minh chứng) và gom các yếu tố phụ thành nhóm cộng hưởng.",
    },
    "ARG-02": {
        "id": "ARG-02",
        "name": "Đường cong lập luận kiểu 'Con lắc an toàn' 3 pha (Pendulum Hedging)",
        "category": "ARGUMENTATION",
        "priority_stage": "P1",
        "severity": "warning",
        "severityLabel": "Nên sửa",
        "userTitle": "Lập luận con lắc 3 pha ('Khen kết quả -> Tuy nhiên còn hạn chế -> Do đó cần hoàn thiện')",
        "userReason": "Khuôn lập luận 3 pha 'Nêu mặt tích cực -> Tuy nhiên còn hạn chế/chưa đồng đều -> Do đó cần tiếp tục hoàn thiện/rà soát' lặp lại tạo cảm giác trung dung, thiếu chiều sâu phân tích.",
        "userSuggestion": "Chỉ rõ nguyên nhân gốc rễ (về quy trình, ngân sách, nhân sự) hoặc bài toán đánh đổi (trade-off) thay cho lời khuyên tổng quát.",
    },
    "ARG-03": {
        "id": "ARG-03",
        "name": "Phóng đại tầm quan trọng, di sản và xu hướng vĩ mô",
        "category": "ARGUMENTATION",
        "priority_stage": "P1",
        "severity": "suggestion",
        "severityLabel": "Gợi ý",
        "userTitle": "Mở đầu hoặc nhận định bằng đại cảnh vĩ mô chung chung",
        "userReason": "Các cụm 'Trong bối cảnh toàn cầu hóa...', 'Trong kỷ nguyên kinh tế số...', 'khẳng định tầm vóc' xuất hiện lặp lại ở nhiều tài liệu.",
        "userSuggestion": "Đi thẳng vào vấn đề nghiệp vụ hoặc dữ liệu thực tế của ngành đang nghiên cứu.",
    },
    "ARG-04": {
        "id": "ARG-04",
        "name": "Kết luận đóng khung 'Thách thức & Triển vọng' và Khuyến nghị khẩu hiệu",
        "category": "ARGUMENTATION",
        "priority_stage": "P1",
        "severity": "suggestion",
        "severityLabel": "Gợi ý",
        "userTitle": "Đóng khung nhận định 'Mặc dù..., vẫn đối mặt...' hoặc khuyến nghị khẩu hiệu chung chung",
        "userReason": "Mẫu câu 'Mặc dù đạt được X, Y vẫn còn tồn tại...' hoặc 'Nếu được triển khai đồng bộ, các giải pháp sẽ góp phần nâng cao...' mang tính khẩu hiệu chung chung.",
        "userSuggestion": "Phân tích trực tiếp nút thắt nghiệp vụ hoặc nêu rõ lộ trình và chỉ tiêu KPI dự kiến đạt được.",
    },
    "PRG-01": {
        "id": "PRG-01",
        "name": "Quy chiếu nguồn mơ hồ & Nhấn mạnh rập khuôn độ phủ truyền thông",
        "category": "ARGUMENTATION",
        "priority_stage": "P4",
        "severity": "warning",
        "severityLabel": "Nên sửa",
        "userTitle": "Dẫn nguồn nhận định mơ hồ hoặc nhấn mạnh độ phủ truyền thông chung chung",
        "userReason": "Sử dụng cụm 'Các chuyên gia cho rằng', 'Nhiều nghiên cứu chỉ ra rằng', 'được đưa tin bởi các tạp chí' mà không nêu tên tác giả, năm công bố hay số liệu kiểm chứng.",
        "userSuggestion": "Bổ sung trích dẫn chuẩn học thuật (Tác giả, Năm) hoặc dẫn trực tiếp báo cáo thống kê của cơ quan chuyên ngành.",
    },
    "PRG-02": {
        "id": "PRG-02",
        "name": "Rào đón giáo huấn & Miễn trừ trách nhiệm dữ liệu/phương pháp luận",
        "category": "ARGUMENTATION",
        "priority_stage": "P4",
        "severity": "suggestion",
        "severityLabel": "Gợi ý",
        "userTitle": "Câu rào đón miễn trừ trách nhiệm về giới hạn dữ liệu hoặc cách hiểu chỉ số",
        "userReason": "Các câu tự thanh minh như 'Trong phạm vi dữ liệu nghiên cứu, chưa có tài liệu cho thấy...', 'Khóa luận chỉ sử dụng X như khung tham chiếu chứ không đồng nhất...' hoặc 'Điều quan trọng cần lưu ý là...' mang đậm dấu ấn rào đón của mô hình ngôn ngữ.",
        "userSuggestion": "Xóa câu rào đón tự thanh minh; trình bày thẳng kết quả phân tích từ dữ liệu hiện có (chuyển phần hạn chế dữ liệu về mục 'Hạn chế của đề tài' ở cuối khóa luận).",
    },
    "FMT-01": {
        "id": "FMT-01",
        "name": "Định dạng thị giác cơ học: Danh sách tiêu đề in đậm, Gạch ngang giải thích giữa câu",
        "category": "FORMATTING_FORENSIC",
        "priority_stage": "P0_P3",
        "severity": "suggestion",
        "severityLabel": "Gợi ý",
        "userTitle": "Lạm dụng dấu gạch ngang giải thích (— / -) giữa câu hoặc danh sách tiêu đề in đậm",
        "userReason": "Việc chèn mệnh đề giải thích bằng dấu gạch ngang dài (—) hoặc gạch nối (-) giữa câu theo lối tiếng Anh, hoặc liệt kê '- **Tiêu đề**:' lặp lại làm mất nhịp văn xuôi học thuật tiếng Việt.",
        "userSuggestion": "Thay dấu gạch ngang giải thích (— / -) bằng dấu phẩy (,), dấu ngoặc đơn () hoặc tách thành câu văn xuôi độc lập.",
    },
    "FOR-01": {
        "id": "FOR-01",
        "name": "Dấu vết kỹ thuật, Giao tiếp hội thoại thừa & Nguồn trích dẫn ảo giác",
        "category": "FORMATTING_FORENSIC",
        "priority_stage": "P0",
        "severity": "critical",
        "severityLabel": "Cần sửa ngay",
        "userTitle": "Trích dẫn chứa ký hiệu hệ thống hoặc mã nguồn cần xác minh ngay",
        "userReason": "Xuất hiện chuỗi ký hiệu hệ thống ('contentReference[oaicite]', 'turn0search', 'utm_source=chatgpt.com'), câu giao tiếp thừa hoặc mã DOI/placeholder chưa xác thực.",
        "userSuggestion": "Xóa hoàn toàn chuỗi ký hiệu hệ thống bị rò rỉ và đối chiếu lại thông tin bài báo gốc trước khi đưa vào danh mục tài liệu tham khảo.",
    },
}


def build_contextual_suggestion(rule_id: str, matched_text: str, sentence_text: str = "") -> str:
    """
    Contextual Rewrite Engine (Full 26/26 Rules Coverage):
    Generates a concrete, span-specific Vietnamese academic editorial rewrite
    containing «clean_match» and an academic model sentence/phrase.
    """
    base_suggestion = RULE_METADATA.get(rule_id, {}).get("userSuggestion", "")
    clean_match = matched_text.strip().strip('"')
    if not clean_match:
        return base_suggestion
    short_match = clean_match[:75] + ("..." if len(clean_match) > 75 else "")
    lower_m = clean_match.lower()

    # 1. LEX-01: AI Vocabulary & Intensifier Density
    if rule_id == "LEX-01":
        cliche_map = {
            "bức tranh toàn cảnh": "thống kê tổng hợp / thực trạng tổng thể",
            "tấm thảm đa sắc": "cơ cấu đa dạng",
            "sự giao thoa phức tạp": "mối tương quan / sự kết hợp",
            "bối cảnh không ngừng biến đổi": "giai đoạn biến động lãi suất / thị trường",
            "đóng vai trò": "quyết định trực tiếp đến / tác động đến",
            "khai phá tiềm năng": "khai thác hiệu quả nguồn lực",
            "kiến tạo hệ sinh thái": "xây dựng mạng lưới dịch vụ",
            "góc nhìn đa chiều": "phân tích đa biến / đánh giá từ nhiều khía cạnh",
            "kim chỉ nam": "nguyên tắc định hướng / tiêu chuẩn vận hành",
            "bệ phóng": "nền tảng hỗ trợ / điều kiện thuận lợi",
            "nút thắt cổ chai": "điểm nghẽn quy trình / hạn chế lớn nhất",
            "tảng băng chìm": "rủi ro tiềm ẩn chưa ghi nhận",
            "mắt xích": "khâu nghiệp vụ / bộ phận",
            "trụ cột chiến lược": "nhiệm vụ trọng tâm",
            "đòn bẩy chiến lược": "công cụ thúc đẩy",
            "cát cứ tri thức": "tình trạng phân mảnh thông tin giữa các bộ phận",
            "luồng sinh khí mới": "động lực cải tiến quy trình",
        }
        for k, v in cliche_map.items():
            if k in lower_m:
                return f"Thay cụm sáo ngữ «{short_match}» bằng thuật ngữ học thuật cụ thể: «{v}»."
        return (
            f"Giảm mật độ tính từ/danh từ khuếch đại tại «{short_match}»; "
            f"thay bằng chỉ tiêu đo lường cụ thể (ví dụ: «chiếm tỷ trọng lớn nhất», «tác động trực tiếp đến chi phí vận hành»)."
        )

    # 2. LEX-02: Copula Avoidance
    elif rule_id == "LEX-02":
        if any(w in lower_m for w in ["sở hữu", "tự hào có", "nổi bật với", "mang trong mình"]):
            return f"Thay cụm động từ phô trương «{short_match}» bằng hệ từ chỉ sở hữu khách quan: «có», «gồm» hoặc «đạt»."
        return f"Thay cụm động từ vòng vo «{short_match}» bằng hệ từ trực diện: «là», «chiếm» hoặc «thuộc nhóm»."

    # 3. LEX-03: Corporate & Academic Puffery
    elif rule_id == "LEX-03":
        return (
            f"Lược bỏ cụm từ tán dương phóng đại «{short_match}»; "
            f"thay bằng dữ kiện định lượng khách quan (ví dụ: «tăng trưởng 18,5%/năm», «đạt 4,2/5 điểm khảo sát»)."
        )

    # 4. LEX-04: Artificial Synonym Cycling
    elif rule_id == "LEX-04":
        return (
            f"Trong đoạn xuất hiện hiện tượng xoay vòng cách gọi «{short_match}»; "
            f"hãy thống nhất dùng 1 thuật ngữ định danh duy nhất (ví dụ: giữ nguyên «doanh nghiệp» hoặc tên viết tắt của đơn vị)."
        )

    # 5. LEX-05: Vague Association & Hedging Qualifier Inflation ("tương đối", "nhất định")
    elif rule_id == "LEX-05":
        if "tương đối" in lower_m or "nhất định" in lower_m or "phần nào" in lower_m:
            return (
                f"Thay cụm rào đón mức độ mơ hồ «{short_match}» bằng mức đánh giá định lượng cụ thể "
                f"(ví dụ: «đạt mức khá (3,85/5 điểm)», «chiếm 62,4% ý kiến đồng ý» hoặc xóa hẳn từ «tương đối / nhất định»)."
            )
        return (
            f"Thay cụm liên kết mơ hồ «{short_match}» bằng động từ chỉ rõ chiều hướng tác động "
            f"(ví dụ: «làm tăng chi phí...», «quyết định trực tiếp đến...», «tương quan thuận với...»)."
        )

    # 6. LEX-VN-01: Sino-Vietnamese Syllable Congestion & Nominalization Stacking
    elif rule_id == "LEX-VN-01":
        return (
            f"Giải nén chuỗi danh hóa / từ Hán–Việt dày đặc «{short_match}» bằng cách đưa chủ thể lên trước động từ "
            f"(ví dụ: «Doanh nghiệp chuẩn hóa quy trình đánh giá...» thay cho «Việc thực hiện quy trình hoàn thiện hoạt động...»)."
        )

    # 7. SYN-01: Syntactic Isomorphism
    elif rule_id == "SYN-01":
        return (
            f"Các câu trong đoạn «{short_match}» đang lặp lại cùng một khuôn mở đầu; "
            f"hãy gộp các tiêu chí có điểm số tương đồng vào chung 1 câu so sánh (ví dụ: «Hai tiêu chí X và Y cùng đạt mức cao trên 4,1 điểm, trong khi Z chỉ đạt 3,2 điểm»)."
        )

    # 8. SYN-02: Trailing Participial Summary Clause
    elif rule_id == "SYN-02":
        return (
            f"Cắt bỏ mệnh đề đuôi tổng kết chung chung «{short_match}» "
            f"hoặc tách thành câu độc lập nêu rõ kết quả định lượng thực tế."
        )

    # 9. SYN-03: Negative Parallelism (4 variants)
    elif rule_id == "SYN-03":
        if "không phải" in lower_m and "mà" in lower_m:
            return (
                f"Viết lại cấu trúc sóng đôi phủ định «{short_match}» thành câu khẳng định trực diện: "
                f"bỏ vế phủ định «không phải là...» và nêu thẳng bản chất của đối tượng ở vế sau."
            )
        if "chứ không" in lower_m:
            return (
                f"Rút gọn cụm đối lập «{short_match}» bằng cách khẳng định thẳng phân loại/bản chất nghiệp vụ "
                f"(hoặc dùng «thay vì» khi thực sự cần đối chiếu hai phương án)."
            )
        return (
            f"Chuyển cấu trúc sóng đôi «{short_match}» sang câu khẳng định trực diện dùng «đồng thời» hoặc «bên cạnh... còn...» gắn với số liệu cụ thể."
        )

    # 10. SYN-04: Mechanical Rule of Three
    elif rule_id == "SYN-04":
        return (
            f"Rút gọn cụm liệt kê ba vế «{short_match}»: chỉ giữ lại 1–2 khái niệm sát nhất với chỉ tiêu kinh tế đang phân tích."
        )

    # 11. SYN-VN-01: Redundant Pronouns & Mid-clause "vì vậy" Calque
    elif rule_id == "SYN-VN-01":
        if "vì vậy" in lower_m:
            return (
                f"Cụm «{short_match}» đang chèn «vì vậy» vào giữa Chủ ngữ và Vị ngữ theo lối dịch tiếng Anh (Subject therefore Verb); "
                f"hãy đưa «Vì vậy,» lên đầu câu hoặc đổi thành «Do đó, [Chủ ngữ] cần/phải...»."
            )
        if "của họ" in lower_m or "của mình" in lower_m or "của nó" in lower_m:
            return f"Xóa trực tiếp định ngữ sở hữu dịch máy «{short_match}» vì chủ thể đã xác định rõ trong câu."
        if "nó" in lower_m:
            return f"Lược bỏ đại từ «{short_match}» và nối trực tiếp vị ngữ vào danh từ chủ đề đứng trước."
        return (
            f"Thay đại từ chỉ định lặp lại «{short_match}» bằng danh ngữ cụ thể (ví dụ: «Mức chênh lệch này», «Cơ chế trên») hoặc nối thẳng vào câu trước."
        )

    # 12. SYN-VN-02: Topic-Comment Calque ("Đối với..., nó...")
    elif rule_id == "SYN-VN-02":
        m_top = re.match(
            r"^(?:Đối\s+với(?:\s+vấn\s+đề)?|Liên\s+quan\s+đến(?:\s+khía\s+cạnh)?|Xét\s+(?:về|trên)\s+(?:mặt|phương\s+diện|góc\s+độ|khía\s+cạnh)|Về\s+(?:mặt|phương\s+diện|phía|khía\s+cạnh)|Dưới\s+góc\s+(?:độ|nhìn)(?:\s+của)?)\s+([^,]+),\s*",
            clean_match,
            re.IGNORECASE,
        )
        if m_top:
            topic = m_top.group(1).strip()
            return f"Đưa thẳng chủ đề «{topic.capitalize()}» tại «{short_match}» lên đầu câu làm chủ ngữ trực tiếp và bỏ phần đệm mở đầu."
        return f"Rút gọn khung đề–thuyết dịch máy «{short_match}» bằng cách đưa danh từ trung tâm lên làm chủ ngữ chủ động."

    # 13. SYN-VN-03: Passive Calque & "Việc + V" Nominalization Subject
    elif rule_id == "SYN-VN-03":
        m_pas = re.search(
            r"\b(?:được|bị)\s+([a-zA-ZÀ-ỹ\s]{2,30}?)\s+bởi\s+([a-zA-ZÀ-ỹ\s]{2,40})",
            clean_match,
            re.IGNORECASE,
        )
        if m_pas:
            verb_part = m_pas.group(1).strip().lower()
            agent_part = m_pas.group(2).strip()
            return (
                f"Đổi trực tiếp cụm bị động dịch máy «{m_pas.group(0).strip()}» sang chủ động tiếng Việt: "
                f"«{agent_part} {verb_part}» hoặc «do {agent_part} {verb_part}»."
            )
        m_nom = re.search(
            r"thông\s+qua\s+việc\s+thực\s+hiện\s+(?:quy\s+trình\s+)?([a-zA-ZÀ-ỹ\s]{3,40})",
            clean_match,
            re.IGNORECASE,
        )
        if m_nom:
            action = m_nom.group(1).strip()
            return f"Rút gọn cụm danh hóa «{short_match}» thành: «nhờ {action}» hoặc «khi triển khai {action}»."
        return (
            f"Thay chủ ngữ danh hóa «{short_match}» bằng chủ thể thực hiện hành động "
            f"(ví dụ: «Khi doanh nghiệp...» hoặc «Bộ phận quản lý trực tiếp...»)."
        )

    # 14. RHY-01: Monotonous Sentence Rhythm
    elif rule_id == "RHY-01":
        return (
            f"Đoạn văn «{short_match}» có độ dài các câu quá đồng đều; "
            f"hãy rút gọn câu đầu thành câu nhận định ngắn dưới 15 từ và gộp hai câu giải thích kế tiếp bằng dấu hai chấm (:)."
        )

    # 15. DIS-01: Boxed 4-Step Paragraph
    elif rule_id == "DIS-01":
        return (
            f"Câu kết «{short_match}» đang đóng hộp khép kín đoạn văn; "
            f"hãy lược bỏ câu tổng kết cuối đoạn này để mạch phân tích nối tự nhiên sang đoạn tiếp theo."
        )

    # 16. DIS-02: Echoic Subsection / Paragraph Closure
    elif rule_id == "DIS-02":
        return (
            f"Xóa câu/đoạn kết tiểu mục mang tính tóm tắt công thức «{short_match}»; "
            f"chỉ giữ lại phần tổng hợp chung ở mục Tóm tắt cuối chương để tránh lặp lại giữa các tiểu mục."
        )

    # 17. DIS-03: Mechanical Connective Openers
    elif rule_id == "DIS-03":
        return f"Xóa từ nối đầu câu «{short_match}» hoặc chuyển thành phụ từ nội câu («cũng», «vẫn», «đồng thời») đặt sau chủ ngữ."

    # 18. DIS-04: Header-Echo Opener & Robotic Table Signposting
    elif rule_id == "DIS-04":
        if "bảng" in lower_m:
            return (
                f"Thay câu dẫn nhập bảng rập khuôn «{short_match}» bằng cách nêu thẳng xu hướng hoặc con số chênh lệch lớn nhất trong bảng "
                f"(ví dụ: «Số liệu tại Bảng cho thấy tỷ lệ hoàn thành KPI tăng từ 78% lên 86%...»)."
            )
        return (
            f"Bỏ lối mở đoạn định danh công thức «{short_match}»; "
            f"đi thẳng vào cách thức doanh nghiệp triển khai thực tế hoặc số liệu khảo sát."
        )

    # 19. ARG-01: Flat Epistemic Weight
    elif rule_id == "ARG-01":
        return (
            f"Các luận điểm trong «{short_match}» đang liệt kê dàn trải không kèm số liệu; "
            f"hãy bổ sung tỷ lệ %, số liệu bảng biểu cho nguyên nhân quan trọng nhất và gộp các ý phụ."
        )

    # 20. ARG-02: 3-Phase Pendulum Hedging
    elif rule_id == "ARG-02":
        return (
            f"Đoạn văn «{short_match}» đi theo quỹ đạo con lắc 3 pha (Khen -> Tuy nhiên hạn chế -> Do đó cần hoàn thiện); "
            f"hãy thay câu kết chung chung bằng nguyên nhân cụ thể gây ra hạn chế đó tại đơn vị."
        )

    # 21. ARG-03: Macro-Context Inflation
    elif rule_id == "ARG-03":
        return (
            f"Cắt bỏ phần mở màn đại cảnh vĩ mô «{short_match}» và mở đầu trực tiếp bằng bối cảnh nghiệp vụ tại đơn vị nghiên cứu."
        )

    # 22. ARG-04: Formulaic Challenges & Hollow Policy Slogans
    elif rule_id == "ARG-04":
        return (
            f"Thay câu nhận định/khuyến nghị khẩu hiệu «{short_match}» bằng mục tiêu định lượng cụ thể "
            f"(ví dụ: «Các giải pháp trên hướng tới mục tiêu giảm 15% tỷ lệ biến động nhân sự trong năm 2026»)."
        )

    # 23. PRG-01: Weasel Attribution & Media Coverage Clichés
    elif rule_id == "PRG-01":
        if any(w in lower_m for w in ["đưa tin", "tạp chí", "ấn phẩm", "truyền thông"]):
            return (
                f"Thay cụm nhấn mạnh truyền thông «{short_match}» bằng chỉ số nhận diện thương hiệu cụ thể (lượt tiếp cận, thị phần hoặc nguồn báo cáo khảo sát)."
            )
        return (
            f"Thay cụm quy chiếu mơ hồ «{short_match}» bằng trích dẫn học thuật cụ thể theo chuẩn (Tác giả, Năm) hoặc bỏ cụm dẫn nhập để nêu thẳng luận điểm."
        )

    # 24. PRG-02: Didactic Hedging & Methodological/Data Disclaimers (PRG-02a/b/c)
    elif rule_id == "PRG-02":
        if any(w in lower_m for w in ["phạm vi dữ liệu", "chưa có tài liệu", "dữ liệu hiện có", "không được công bố"]):
            return (
                f"Xóa câu tự thú nhận giới hạn dữ liệu «{short_match}» khỏi phần phân tích; "
                f"chỉ phân tích trên số liệu thực tế đang có và gom các giới hạn dữ liệu về mục «Hạn chế của đề tài» ở cuối khóa luận."
            )
        if any(w in lower_m for w in ["khung tham chiếu", "chỉ báo bổ sung", "không tính trực tiếp", "không dùng sự thay đổi"]):
            return (
                f"Lược bỏ câu rào đón miễn trừ phương pháp luận «{short_match}»; "
                f"chỉ cần giải thích quy ước đo lường 1 lần duy nhất tại phần Phương pháp nghiên cứu."
            )
        return f"Xóa cụm rào đón giáo huấn «{short_match}» và trình bày thẳng luận điểm chính của câu."

    # 25. FMT-01: Mechanical Formatting & Explanatory Dashes
    elif rule_id == "FMT-01":
        if "—" in clean_match or " - " in clean_match:
            return (
                f"Thay dấu gạch ngang chèn mệnh đề giải thích tại «{short_match}» bằng dấu phẩy (,), dấu ngoặc đơn () hoặc tách thành câu riêng."
            )
        return f"Chuyển cấu trúc định dạng liệt kê «{short_match}» thành câu văn xuôi học thuật hoàn chỉnh."

    # 26. FOR-01: Forensic Artifacts & Leaked Citations
    elif rule_id == "FOR-01":
        return f"Xóa ngay chuỗi ký hiệu rò rỉ / hội thoại AI «{short_match}» và kiểm tra lại tính xác thực của nguồn tài liệu tham khảo."

    return f"Biên tập lại cụm «{short_match}»: {base_suggestion}"

