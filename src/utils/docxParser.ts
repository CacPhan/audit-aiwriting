import mammoth from 'mammoth';
import { DocumentAuditResult, ParsedThesisSection } from '../types/auditor';

const EXCLUDED_HEADING_REGEX =
  /^(?:TRANG\s+BÌA|BÌA\s+LUẬN\s+VĂN|MỤC\s+LỤC|DANH\s+MỤC\s+(?:CÁC\s+)?(?:TÀI\s+LIỆU\s+THAM\s+KHẢO|BẢNG(?:\s+BIỂU|\s+SỐ\s+LIỆU)?|HÌNH(?:\s+VẼ|\s+ẢNH)?|BIỂU\s+ĐỒ|SƠ\s+ĐỒ|TỪ\s+VIẾT\s+TẮT|CHỮ\s+VIẾT\s+TẮT|KÝ\s+HIỆU)|TÀI\s+LIỆU\s+THAM\s+KHẢO|PHỤ\s+LỤC(?:\s*\d+|\b)|LỜI\s+CAM\s+ĐOAN|LỜI\s+CẢM\s+ƠN|LỜI\s+CÁM\s+ƠN)/i;

const COVER_PREAMBLE_REGEX =
  /^(?:BỘ\s+GIÁO\s+DỤC\s+VÀ\s+ĐÀO\s+TẠO|ĐẠI\s+HỌC\s+KINH\s+TẾ|TRƯỜNG\s+ĐẠI\s+HỌC|HỌC\s+VIỆN\s+|KHÓA\s+LUẬN\s+TỐT\s+NGHIỆP|KHOÁ\s+LUẬN\s+TỐT\s+NGHIỆP|LUẬN\s+VĂN\s+THẠC\s+SĨ|CHUYÊN\s+ĐỀ\s+THỰC\s+TẬP|BÁO\s+CÁO\s+TỔNG\s+HỢP)/i;

const CHAPTER_OR_SECTION_HEADING_REGEX =
  /^(?:CHƯƠNG\s*(?:\d+|[IVXLC]+)(?:\b|(?=[A-ZÀ-ỸĐ:]))|PHẦN\s+(?:MỞ\s+ĐẦU|KẾT\s+LUẬN|\d+|[IVXLC]+)|MỞ\s+ĐẦU\b|LỜI\s+MỞ\s+ĐẦU\b|KẾT\s+LUẬN(?:\s+VÀ\s+KHUYẾN\s+NGHỊ|\s+CHUNG)?\b|\d+\.\d+\.?(?!\d)\s+\S+|[1-9]\.\s+[A-ZÀ-ỸĐ]{2,}(?:\s+[A-ZÀ-ỸĐ0-9,–\-()]+)+$)/i;

const TOP_LEVEL_UPPER_HEADING_REGEX =
  /^[1-9]\.\s+[A-ZÀ-ỸĐ]{2,}(?:\s+[A-ZÀ-ỸĐ0-9,–\-()]+)+$/;

const DEEP_SUBHEADING_LINE_REGEX =
  /^\d+\.\d+\.\d+(?:\.\d+)*\.?\s+[^\n]{2,130}$/;

const TABLE_OR_FIGURE_METADATA_REGEX =
  /^(?:(?:Bảng|Hình|Biểu\s+đồ|Sơ\s+đồ|Hộp)\s+\d+(?:[.,]\d+)*\s*[:.\-–]?|(?:Nguồn|Trích\s+nguồn|Đơn\s+vị(?:\s+tính)?|Ghi\s+chú)\s*[:])/i;

const TOC_DOT_LEADER_REGEX = /(?:\.{3,}|…+)\s*(?:\d+|[ivxlcdm]+)?\s*$/i;
const TOC_TAB_PAGE_REGEX = /\t+\s*(?:\d+|[ivxlcdm]+)\s*$/i;
const TOC_TRAILING_PAGE_IN_INDEX_REGEX =
  /^(?:CHƯƠNG\s*\d+|PHẦN\s+|MỞ\s+ĐẦU|LỜI\s+|KẾT\s+LUẬN|TÀI\s+LIỆU\s+THAM\s+KHẢO|PHỤ\s+LỤC|DANH\s+MỤC|\d+(?:\.\d+)+\.?|Bảng\s+\d+|Hình\s+\d+|Biểu\s+đồ\s+\d+|Sơ\s+đồ\s+\d+).*?\s+(?:\d{1,3}|[ivxlcdm]{1,6})$/i;

function normalizeText(input: string): string {
  return (input || '').normalize('NFC');
}

function isExcludedHeading(line: string): boolean {
  const cleaned = normalizeText(line)
    .trim()
    .replace(/^[*#\-\s]+|[*#\s]+$/g, '');
  return EXCLUDED_HEADING_REGEX.test(cleaned);
}

function isTocEntryLine(line: string, insideIndexSection = false): boolean {
  const normalized = normalizeText(line).trim();
  if (TOC_DOT_LEADER_REGEX.test(normalized)) return true;
  if (TOC_TAB_PAGE_REGEX.test(normalized)) return true;
  if (
    insideIndexSection &&
    TOC_TRAILING_PAGE_IN_INDEX_REGEX.test(normalized)
  ) {
    return true;
  }
  if (
    insideIndexSection &&
    /^(?:Bảng|Hình|Biểu\s+đồ|Sơ\s+đồ)\s+\d+/i.test(normalized)
  ) {
    return true;
  }
  return false;
}

function isNonProseMetadataOrSubheading(line: string): boolean {
  const cleaned = normalizeText(line).trim();
  if (!cleaned) return true;
  if (cleaned.length <= 160 && TABLE_OR_FIGURE_METADATA_REGEX.test(cleaned)) {
    return true;
  }
  if (
    cleaned.length <= 130 &&
    DEEP_SUBHEADING_LINE_REGEX.test(cleaned) &&
    !/[.!?]$/.test(cleaned)
  ) {
    return true;
  }
  return false;
}

function isChapterOrSubHeading(
  line: string,
  isExplicitHeadingTag = false,
  insideIndexSection = false,
  insideBibliographyOrAppendix = false
): boolean {
  const cleaned = normalizeText(line).trim();
  if (!cleaned || cleaned.length > 180) return false;
  if (isTocEntryLine(cleaned, insideIndexSection)) return false;
  if (isExcludedHeading(cleaned)) return true;

  // Inside Bibliography or Appendix, do not split on numbered references like "1. Nguyễn Văn A..."
  if (insideBibliographyOrAppendix) {
    if (
      /^(?:CHƯƠNG\s*(?:\d+|[IVXLC]+)|PHẦN\s+(?:MỞ\s+ĐẦU|KẾT\s+LUẬN)|MỞ\s+ĐẦU\b|LỜI\s+MỞ\s+ĐẦU\b|KẾT\s+LUẬN\b)/i.test(
        cleaned
      )
    ) {
      return true;
    }
    return false;
  }

  // Deep subheadings (1.1.1, 2.1.2.1) stay inside their parent 1.1 / 2.1 section
  if (DEEP_SUBHEADING_LINE_REGEX.test(cleaned)) {
    return false;
  }

  // Check if it is a top-level uppercase numbered chapter (e.g., "1. LỊCH SỬ HÌNH THÀNH...")
  if (/^[1-9]\.\s+/.test(cleaned) && !/^\d+\.\d+/.test(cleaned)) {
    return TOP_LEVEL_UPPER_HEADING_REGEX.test(cleaned);
  }

  if (CHAPTER_OR_SECTION_HEADING_REGEX.test(cleaned)) return true;
  if (
    isExplicitHeadingTag &&
    cleaned.length <= 140 &&
    !TABLE_OR_FIGURE_METADATA_REGEX.test(cleaned)
  ) {
    return true;
  }
  return false;
}

function buildShortTitle(fullTitle: string, idx: number): string {
  const trimmed = normalizeText(fullTitle)
    .replace(/^(CHƯƠNG\s*\d+)(?=[A-ZÀ-ỸĐ])/i, '$1: ')
    .replace(/^(PHỤ\s+LỤC\s*\d+)(?=[A-ZÀ-ỸĐ])/i, '$1: ')
    .trim();
  if (trimmed.length <= 36) return trimmed;
  const colonParts = trimmed.split(':');
  if (colonParts.length > 1 && colonParts[0].length <= 28) {
    const rhsWords = colonParts[1].trim().split(/\s+/).slice(0, 4).join(' ');
    return `${colonParts[0].trim()}: ${rhsWords}`;
  }
  return trimmed.slice(0, 34).trim() + '…';
}

export function splitRawTextOrHtmlIntoSections(
  content: string,
  isHtml = false
): ParsedThesisSection[] {
  const normalizedContent = normalizeText(content);
  if (!normalizedContent || !normalizedContent.trim()) {
    return [];
  }

  interface RawBlock {
    text: string;
    isHeadingTag: boolean;
  }

  const blocks: RawBlock[] = [];

  if (isHtml && typeof DOMParser !== 'undefined') {
    const parser = new DOMParser();
    const doc = parser.parseFromString(normalizedContent, 'text/html');
    const elements = doc.body.querySelectorAll('h1, h2, h3, h4, p, li');
    elements.forEach((el) => {
      // 1. Eliminate table cell leakage: never extract <p> or <li> inside <table>
      if (el.closest('table')) return;
      const tag = el.tagName.toLowerCase();
      // 2. Eliminate <li> + nested <p> double extraction
      if (tag === 'p' && el.closest('li')) return;

      const rawTxt = normalizeText(el.textContent || '');
      const hasTabPage = TOC_TAB_PAGE_REGEX.test(rawTxt);
      const txt = rawTxt.replace(/[ \f\v]+/g, ' ').trim();
      if (!txt) return;
      const isHeading =
        (tag === 'h1' || tag === 'h2') &&
        !hasTabPage &&
        !DEEP_SUBHEADING_LINE_REGEX.test(txt);
      blocks.push({ text: txt, isHeadingTag: isHeading });
    });
  } else {
    const rawChunks = normalizedContent
      .split(/\r?\n\s*\r?\n|\r?\n/)
      .map((line) => line.trim())
      .filter(Boolean);
    rawChunks.forEach((txt) => {
      blocks.push({ text: txt, isHeadingTag: false });
    });
  }

  const rawSections: ParsedThesisSection[] = [];
  let currentSection: ParsedThesisSection | null = null;
  let insideIndexSection = false;
  let insideBibOrAppendix = false;

  blocks.forEach((block) => {
    const { text, isHeadingTag } = block;

    if (
      isChapterOrSubHeading(
        text,
        isHeadingTag,
        insideIndexSection,
        insideBibOrAppendix
      )
    ) {
      const excluded = isExcludedHeading(text);
      const normalizedHeading = normalizeText(text)
        .replace(/^(CHƯƠNG\s*\d+)(?=[A-ZÀ-ỸĐ])/i, '$1: ')
        .replace(/^(PHỤ\s+LỤC\s*\d+)(?=[A-ZÀ-ỸĐ])/i, '$1: ')
        .replace(/\t+/g, ' ')
        .trim();

      insideIndexSection =
        /^(?:MỤC\s+LỤC|DANH\s+MỤC\s+)/i.test(normalizedHeading);
      insideBibOrAppendix =
        /^(?:DANH\s+MỤC\s+TÀI\s+LIỆU\s+THAM\s+KHẢO|TÀI\s+LIỆU\s+THAM\s+KHẢO|PHỤ\s+LỤC)/i.test(
          normalizedHeading
        );

      const secIndex = rawSections.length + 1;
      currentSection = {
        id: `sec-${secIndex}`,
        title: normalizedHeading,
        shortTitle: buildShortTitle(normalizedHeading, secIndex),
        sectionLabel: excluded
          ? `Mục loại trừ · Phần ${secIndex}`
          : `Phần ${secIndex} · Bản thảo`,
        paragraphs: [],
        isExcluded: excluded,
      };
      rawSections.push(currentSection);
    } else {
      if (!currentSection) {
        const isCoverPreamble = COVER_PREAMBLE_REGEX.test(text);
        currentSection = {
          id: 'sec-1',
          title: isCoverPreamble
            ? 'Trang bìa & Thông tin chung'
            : 'Chương 1: Nội dung bản thảo',
          shortTitle: isCoverPreamble ? 'Trang bìa' : 'Chương 1: Bản thảo',
          sectionLabel: isCoverPreamble
            ? 'Mục loại trừ · Trang bìa'
            : 'Chương 1 · Bản thảo',
          paragraphs: [],
          isExcluded: isCoverPreamble,
        };
        rawSections.push(currentSection);
      }

      const cleanedLine = text.replace(/\t+/g, ' ').trim();
      // Filter out Table/Figure captions, Source attributions, and deep subheadings (1.1.1) from audited prose
      if (currentSection.isExcluded || !isNonProseMetadataOrSubheading(cleanedLine)) {
        currentSection.paragraphs.push(cleanedLine);
      }
    }
  });

  if (
    rawSections.length > 1 &&
    rawSections[0].title === 'Chương 1: Nội dung bản thảo'
  ) {
    rawSections[0].title = 'Trang bìa & Thông tin chung';
    rawSections[0].shortTitle = 'Trang bìa';
    rawSections[0].sectionLabel = 'Mục loại trừ · Trang bìa';
    rawSections[0].isExcluded = true;
  }

  // Post-processing:
  // 1. Fold 0-paragraph chapter outline bullets (e.g., "Chương 1: ...", "Chương 2: ...") back into MỞ ĐẦU
  // 2. Consolidate 0-paragraph parent headings (e.g., "1. LỊCH SỬ..." immediately followed by "1.1...")
  const consolidated: ParsedThesisSection[] = [];
  for (let i = 0; i < rawSections.length; i++) {
    const sec = rawSections[i];
    if (sec.isExcluded) {
      consolidated.push(sec);
      continue;
    }

    if (sec.paragraphs.length === 0) {
      const prev = consolidated[consolidated.length - 1];
      const next = rawSections[i + 1];
      // If inside/right after MỞ ĐẦU and this is an empty "Chương X: ..." outline bullet
      if (
        prev &&
        !prev.isExcluded &&
        /^Chương\s+\d+\s*:/i.test(sec.title) &&
        (!next || /^Chương\s+\d+/i.test(next.title))
      ) {
        prev.paragraphs.push(sec.title);
        continue;
      }
      // If followed by a non-excluded child section, attach parent title context to child's sectionLabel
      if (next && !next.isExcluded) {
        next.sectionLabel = `${buildShortTitle(sec.title, i + 1)} · ${next.shortTitle}`;
        continue;
      }
    }

    consolidated.push(sec);
  }

  // Re-index section IDs sequentially
  return consolidated.map((sec, idx) => ({
    ...sec,
    id: `sec-${idx + 1}`,
  }));
}

export async function extractSectionsFromDocx(
  file: File
): Promise<ParsedThesisSection[]> {
  let arrayBuffer: ArrayBuffer;
  if (typeof file.arrayBuffer === 'function') {
    arrayBuffer = await file.arrayBuffer();
  } else {
    arrayBuffer = await new Response(file).arrayBuffer();
  }

  const mammothInput: { arrayBuffer: ArrayBuffer; buffer?: Buffer } = {
    arrayBuffer,
  };
  if (typeof Buffer !== 'undefined') {
    mammothInput.buffer = Buffer.from(arrayBuffer);
  }

  const result = await mammoth.convertToHtml(mammothInput as any);
  const sections = splitRawTextOrHtmlIntoSections(result.value, true);
  if (sections.length > 0) {
    return sections;
  }
  const rawTextResult = await mammoth.extractRawText(mammothInput as any);
  return splitRawTextOrHtmlIntoSections(rawTextResult.value, false);
}

/**
 * Built-in initial sample audit matching ai-writing-style-auditor-ui.html
 * so the 3-screen SaaS interface renders immediately on load and in tests.
 */
export const INITIAL_SAMPLE_AUDIT: DocumentAuditResult = {
  title: 'Ban_thao_nghien_cuu_hoc_thuat.docx',
  isDemo: true,
  sections: [
    {
      id: 'sec-1',
      chapterNumber: 1,
      title: 'Chương 1: Cơ sở lý luận và Tổng quan nghiên cứu',
      shortTitle: 'Chương 1: Cơ sở lý luận',
      sectionLabel: 'Chương 1 · Mục 1.1 – 1.3',
      isExcluded: false,
      wordCount: 82,
      flagCount: 3,
      aiStyleScore: 48,
      paragraphs: [
        {
          index: 0,
          prefix: '1.1. Bối cảnh và tính cấp thiết của đề tài',
          text: 'Trong bối cảnh toàn cầu hóa và cuộc cách mạng công nghiệp diễn ra mạnh mẽ hiện nay, hoạt động tối ưu hóa chuỗi cung ứng lạnh (cold chain) kết hợp với quản trị vốn lưu động ròng (Net Working Capital) đóng vai trò như một chất xúc tác then chốt và mang tính bước ngoặt lịch sử đối với năng lực cạnh tranh của các doanh nghiệp sản xuất và phân phối.',
          wordCount: 52,
          sentenceCount: 1,
          metrics: { cvLength: 0.35, deltaLength: 0, isi: 0, opr: 0, svci: 3, sicd: 0, bcr: 0 },
          protectedTerms: ['chuỗi cung ứng lạnh', 'quản trị vốn lưu động ròng', 'năng lực cạnh tranh'],
          aiStyleScore: 30,
          flags: [
            {
              id: 'f1',
              ruleId: 'ARG-03',
              severity: 'suggestion',
              severityLabel: 'Gợi ý',
              title: 'Mở đầu đoạn bằng nhận định vĩ mô chung chung',
              excerpt: '"Trong bối cảnh toàn cầu hóa và cuộc cách mạng công nghiệp diễn ra mạnh mẽ hiện nay,"',
              matchedText: 'Trong bối cảnh toàn cầu hóa và cuộc cách mạng công nghiệp diễn ra mạnh mẽ hiện nay,',
              reason: 'Cách mở đầu bằng đại cảnh toàn cầu hóa xuất hiện lặp lại ở nhiều tài liệu khiến đoạn văn chậm đi vào trọng tâm nghiên cứu cụ thể.',
              suggestion: 'Đi thẳng vào bối cảnh ngành: "Đối với các doanh nghiệp chế biến và xuất khẩu thực phẩm, việc đồng bộ chuỗi cung ứng lạnh với quản trị vốn lưu động ròng..."',
              start: 0,
              end: 83,
              sectionId: 'sec-1',
              chapterNumber: 1,
              chapterTitle: 'Chương 1: Cơ sở lý luận và Tổng quan nghiên cứu',
              paragraphIndex: 0,
              status: 'pending',
            },
            {
              id: 'f2',
              ruleId: 'LEX-03',
              severity: 'warning',
              severityLabel: 'Nên sửa',
              title: 'Diễn đạt phóng đại thiếu thước đo cụ thể',
              excerpt: '"đóng vai trò như một chất xúc tác then chốt và mang tính bước ngoặt lịch sử"',
              matchedText: 'đóng vai trò như một chất xúc tác then chốt và mang tính bước ngoặt lịch sử',
              reason: 'Cụm từ mang sắc thái quảng cáo và phóng đại tầm vóc nhưng không chỉ rõ cơ chế tác động thực tế, làm giảm tính khách quan của văn phong học thuật.',
              suggestion: '"tác động trực tiếp đến chu kỳ luân chuyển tiền mặt và khả năng kiểm soát chi phí vận hành của doanh nghiệp."',
              start: 199,
              end: 274,
              sectionId: 'sec-1',
              chapterNumber: 1,
              chapterTitle: 'Chương 1: Cơ sở lý luận và Tổng quan nghiên cứu',
              paragraphIndex: 0,
              status: 'pending',
            },
          ],
        },
        {
          index: 1,
          prefix: '1.2. Khung phân tích mối quan hệ giữa vận hành và hiệu quả tài chính',
          text: 'Việc đồng bộ dữ liệu tồn kho theo thời gian thực giúp doanh nghiệp chủ động điều phối nguồn lực, qua đó góp phần nâng cao hiệu suất sử dụng tài sản, tối ưu hóa chi phí giao dịch và thúc đẩy giá trị bền vững cho cổ đông.',
          wordCount: 38,
          sentenceCount: 1,
          metrics: { cvLength: 0.35, deltaLength: 0, isi: 0, opr: 0, svci: 4, sicd: 0, bcr: 0 },
          protectedTerms: [],
          aiStyleScore: 18,
          flags: [
            {
              id: 'f3',
              ruleId: 'SYN-04',
              severity: 'warning',
              severityLabel: 'Nên sửa',
              title: 'Cấu trúc liệt kê ba động từ tổng kết lặp lại',
              excerpt: '"qua đó góp phần nâng cao hiệu suất sử dụng tài sản, tối ưu hóa chi phí giao dịch và thúc đẩy giá trị bền vững cho cổ đông."',
              matchedText: 'qua đó góp phần nâng cao hiệu suất sử dụng tài sản, tối ưu hóa chi phí giao dịch và thúc đẩy giá trị bền vững cho cổ đông.',
              reason: 'Đuôi câu nối tiếp bằng ba cụm động từ khái quát ("nâng cao..., tối ưu hóa..., thúc đẩy...") tạo cảm giác công thức và dàn trải.',
              suggestion: '"nhờ đó giảm chi phí giao dịch và cải thiện trực tiếp tỷ suất sinh lời trên tổng tài sản (ROA) của doanh nghiệp."',
              start: 97,
              end: 220,
              sectionId: 'sec-1',
              chapterNumber: 1,
              chapterTitle: 'Chương 1: Cơ sở lý luận và Tổng quan nghiên cứu',
              paragraphIndex: 1,
              status: 'pending',
            },
          ],
        },
      ],
    },
    {
      id: 'sec-2',
      chapterNumber: 2,
      title: 'Chương 2: Phương pháp nghiên cứu và Dữ liệu',
      shortTitle: 'Chương 2: Phương pháp nghiên cứu',
      sectionLabel: 'Chương 2 · Mục 2.1 – 2.2',
      isExcluded: false,
      wordCount: 54,
      flagCount: 1,
      aiStyleScore: 12,
      paragraphs: [
        {
          index: 0,
          prefix: '2.1. Thiết kế nghiên cứu và quy trình thu thập dữ liệu',
          text: 'Khi đánh giá tác động của đòn bẩy tài chính (financial leverage) và tỷ lệ an toàn vốn tối thiểu (Basel III CAR) lên tỷ suất sinh lời ROA và ROE, việc các quyết định phân bổ ngân sách được thực hiện bởi bộ phận kế toán quản trị đã được chứng minh là có sự ảnh hưởng đáng kể tới khả năng kiểm soát chi phí đại diện (agency cost) trong doanh nghiệp.',
          wordCount: 54,
          sentenceCount: 1,
          metrics: { cvLength: 0.35, deltaLength: 0, isi: 0, opr: 0, svci: 3, sicd: 0, bcr: 0 },
          protectedTerms: ['đòn bẩy tài chính', 'tỷ lệ an toàn vốn tối thiểu', 'kế toán quản trị', 'chi phí đại diện'],
          aiStyleScore: 12,
          flags: [
            {
              id: 'f4',
              ruleId: 'SYN-VN-03',
              severity: 'suggestion',
              severityLabel: 'Gợi ý',
              title: 'Câu bị động và danh hóa kéo dài',
              excerpt: '"việc các quyết định phân bổ ngân sách được thực hiện bởi bộ phận kế toán quản trị đã được chứng minh là có sự ảnh hưởng đáng kể"',
              matchedText: 'việc các quyết định phân bổ ngân sách được thực hiện bởi bộ phận kế toán quản trị đã được chứng minh là có sự ảnh hưởng đáng kể',
              reason: 'Việc lồng ghép nhiều cụm danh hóa ("việc...", "sự ảnh hưởng") và thể bị động ("được thực hiện bởi", "đã được chứng minh") làm câu văn nặng nề.',
              suggestion: '"kế toán quản trị trực tiếp kiểm soát phân bổ ngân sách sẽ giúp doanh nghiệp giảm đáng kể chi phí đại diện (agency cost)."',
              start: 146,
              end: 273,
              sectionId: 'sec-2',
              chapterNumber: 2,
              chapterTitle: 'Chương 2: Phương pháp nghiên cứu và Dữ liệu',
              paragraphIndex: 0,
              status: 'pending',
            },
          ],
        },
      ],
    },
    {
      id: 'sec-3',
      chapterNumber: 3,
      title: 'Chương 3: Kết quả phân tích và Thảo luận',
      shortTitle: 'Chương 3: Kết quả và Thảo luận',
      sectionLabel: 'Chương 3 · Mục 3.1 – 3.3',
      isExcluded: false,
      wordCount: 72,
      flagCount: 2,
      aiStyleScore: 53,
      paragraphs: [
        {
          index: 0,
          prefix: '3.1. Kết quả kiểm định mô hình thực nghiệm',
          text: 'Kết quả ước lượng trên dữ liệu bảng cho thấy thời gian lưu kho trung bình giảm có ý nghĩa thống kê ở mức 1%. Theo tổng hợp mới nhất (Nguyen & Tran, 2024, doi:10.1016/j.jcorpfin.2024.999999 — contentReference[oaicite:0]{index=0}), việc tích hợp hệ thống dự báo nhu cầu giúp giảm 18,4% lượng hàng tồn kho chậm luân chuyển.',
          wordCount: 44,
          sentenceCount: 2,
          metrics: { cvLength: 0.35, deltaLength: 4, isi: 0, opr: 0, svci: 2, sicd: 0, bcr: 0 },
          protectedTerms: ['dữ liệu bảng', 'ý nghĩa thống kê', 'hàng tồn kho'],
          aiStyleScore: 35,
          flags: [
            {
              id: 'f5',
              ruleId: 'FOR-01',
              severity: 'critical',
              severityLabel: 'Cần sửa ngay',
              title: 'Trích dẫn chứa ký hiệu hệ thống và mã nguồn cần xác minh',
              excerpt: '"(Nguyen & Tran, 2024, doi:10.1016/j.jcorpfin.2024.999999 — contentReference[oaicite:0]{index=0})"',
              matchedText: '(Nguyen & Tran, 2024, doi:10.1016/j.jcorpfin.2024.999999 — contentReference[oaicite:0]{index=0})',
              reason: 'Xuất hiện chuỗi ký hiệu hệ thống ("contentReference[oaicite:0]") phát sinh khi sao chép văn bản và mã DOI có dấu hiệu không khớp danh mục xuất bản thực tế.',
              suggestion: 'Xóa hoàn toàn chuỗi "contentReference[oaicite:0]{index=0}" và đối chiếu lại thông tin bài báo gốc trước khi đưa vào danh mục trích dẫn.',
              start: 132,
              end: 228,
              sectionId: 'sec-3',
              chapterNumber: 3,
              chapterTitle: 'Chương 3: Kết quả phân tích và Thảo luận',
              paragraphIndex: 0,
              status: 'pending',
            },
          ],
        },
        {
          index: 1,
          prefix: '3.2. Thảo luận kết quả',
          text: 'Đây không chỉ là một giải pháp vận hành đơn thuần mà còn là một tuyên ngôn chiến lược toàn diện giúp doanh nghiệp duy trì thanh khoản ổn định trong giai đoạn biến động lãi suất.',
          wordCount: 33,
          sentenceCount: 1,
          metrics: { cvLength: 0.35, deltaLength: 0, isi: 0, opr: 0, svci: 3, sicd: 0, bcr: 0 },
          protectedTerms: [],
          aiStyleScore: 18,
          flags: [
            {
              id: 'f6',
              ruleId: 'SYN-03',
              severity: 'warning',
              severityLabel: 'Nên sửa',
              title: 'Cấu trúc đối lập khuếch đại ý nghĩa',
              excerpt: '"Đây không chỉ là một giải pháp vận hành đơn thuần mà còn là một tuyên ngôn chiến lược toàn diện"',
              matchedText: 'Đây không chỉ là một giải pháp vận hành đơn thuần mà còn là một tuyên ngôn chiến lược toàn diện',
              reason: 'Cách đặt vấn đề theo khuôn mẫu "không chỉ là X đơn thuần mà còn là tuyên ngôn Y" mang tính hùng biện hơn là phân tích dữ liệu thực nghiệm.',
              suggestion: '"Giải pháp này đồng thời hỗ trợ điều tiết tồn kho ngắn hạn và ổn định cấu trúc thanh khoản dài hạn của doanh nghiệp."',
              start: 0,
              end: 95,
              sectionId: 'sec-3',
              chapterNumber: 3,
              chapterTitle: 'Chương 3: Kết quả phân tích và Thảo luận',
              paragraphIndex: 1,
              status: 'pending',
            },
          ],
        },
      ],
    },
    {
      id: 'sec-4',
      chapterNumber: 4,
      title: 'Chương 4: Kết luận và Khuyến nghị quản trị',
      shortTitle: 'Chương 4: Kết luận và Khuyến nghị',
      sectionLabel: 'Chương 4 · Mục 4.1 – 4.2',
      isExcluded: false,
      wordCount: 42,
      flagCount: 1,
      aiStyleScore: 18,
      paragraphs: [
        {
          index: 0,
          prefix: '4.1. Kết luận chung',
          text: 'Tóm lại, có thể khẳng định chắc chắn rằng sự kết hợp hài hòa giữa chiến lược nhân sự, marketing số và quản trị sản xuất chính là chìa khóa vàng mở ra cánh cửa thành công rực rỡ cho mọi doanh nghiệp trong kỷ nguyên mới.',
          wordCount: 42,
          sentenceCount: 1,
          metrics: { cvLength: 0.35, deltaLength: 0, isi: 0, opr: 0, svci: 3, sicd: 0, bcr: 1 },
          protectedTerms: [],
          aiStyleScore: 18,
          flags: [
            {
              id: 'f7',
              ruleId: 'DIS-02',
              severity: 'warning',
              severityLabel: 'Nên sửa',
              title: 'Câu kết đoạn mang tính khẩu hiệu chung',
              excerpt: '"Tóm lại, có thể khẳng định chắc chắn rằng sự kết hợp hài hòa... chính là chìa khóa vàng mở ra cánh cửa thành công rực rỡ cho mọi doanh nghiệp trong kỷ nguyên mới."',
              matchedText: 'Tóm lại, có thể khẳng định chắc chắn rằng sự kết hợp hài hòa giữa chiến lược nhân sự, marketing số và quản trị sản xuất chính là chìa khóa vàng mở ra cánh cửa thành công rực rỡ cho mọi doanh nghiệp trong kỷ nguyên mới.',
              reason: 'Các hình ảnh ẩn dụ như "chìa khóa vàng", "thành công rực rỡ", "trong kỷ nguyên mới" không phù hợp với phần kết luận của nghiên cứu khoa học.',
              suggestion: '"Kết quả nghiên cứu cho thấy doanh nghiệp cần phối hợp đồng bộ giữa kế hoạch nhân sự, tiếp thị và điều độ sản xuất để duy trì biên lợi nhuận mục tiêu."',
              start: 0,
              end: 217,
              sectionId: 'sec-4',
              chapterNumber: 4,
              chapterTitle: 'Chương 4: Kết luận và Khuyến nghị quản trị',
              paragraphIndex: 0,
              status: 'pending',
            },
          ],
        },
      ],
    },
  ],
  findings: [
    {
      id: 'f1',
      ruleId: 'ARG-03',
      severity: 'suggestion',
      severityLabel: 'Gợi ý',
      title: 'Mở đầu đoạn bằng nhận định vĩ mô chung chung',
      excerpt: '"Trong bối cảnh toàn cầu hóa và cuộc cách mạng công nghiệp diễn ra mạnh mẽ hiện nay,"',
      matchedText: 'Trong bối cảnh toàn cầu hóa và cuộc cách mạng công nghiệp diễn ra mạnh mẽ hiện nay,',
      reason: 'Cách mở đầu bằng đại cảnh toàn cầu hóa xuất hiện lặp lại ở nhiều tài liệu khiến đoạn văn chậm đi vào trọng tâm nghiên cứu cụ thể.',
      suggestion: 'Đi thẳng vào bối cảnh ngành: "Đối với các doanh nghiệp chế biến và xuất khẩu thực phẩm, việc đồng bộ chuỗi cung ứng lạnh với quản trị vốn lưu động ròng..."',
      start: 0,
      end: 83,
      sectionId: 'sec-1',
      chapterNumber: 1,
      chapterTitle: 'Chương 1: Cơ sở lý luận và Tổng quan nghiên cứu',
      paragraphIndex: 0,
      status: 'pending',
    },
    {
      id: 'f2',
      ruleId: 'LEX-03',
      severity: 'warning',
      severityLabel: 'Nên sửa',
      title: 'Diễn đạt phóng đại thiếu thước đo cụ thể',
      excerpt: '"đóng vai trò như một chất xúc tác then chốt và mang tính bước ngoặt lịch sử"',
      matchedText: 'đóng vai trò như một chất xúc tác then chốt và mang tính bước ngoặt lịch sử',
      reason: 'Cụm từ mang sắc thái quảng cáo và phóng đại tầm vóc nhưng không chỉ rõ cơ chế tác động thực tế, làm giảm tính khách quan của văn phong học thuật.',
      suggestion: '"tác động trực tiếp đến chu kỳ luân chuyển tiền mặt và khả năng kiểm soát chi phí vận hành của doanh nghiệp."',
      start: 199,
      end: 274,
      sectionId: 'sec-1',
      chapterNumber: 1,
      chapterTitle: 'Chương 1: Cơ sở lý luận và Tổng quan nghiên cứu',
      paragraphIndex: 0,
      status: 'pending',
    },
    {
      id: 'f3',
      ruleId: 'SYN-04',
      severity: 'warning',
      severityLabel: 'Nên sửa',
      title: 'Cấu trúc liệt kê ba động từ tổng kết lặp lại',
      excerpt: '"qua đó góp phần nâng cao hiệu suất sử dụng tài sản, tối ưu hóa chi phí giao dịch và thúc đẩy giá trị bền vững cho cổ đông."',
      matchedText: 'qua đó góp phần nâng cao hiệu suất sử dụng tài sản, tối ưu hóa chi phí giao dịch và thúc đẩy giá trị bền vững cho cổ đông.',
      reason: 'Đuôi câu nối tiếp bằng ba cụm động từ khái quát ("nâng cao..., tối ưu hóa..., thúc đẩy...") tạo cảm giác công thức và dàn trải.',
      suggestion: '"nhờ đó giảm chi phí giao dịch và cải thiện trực tiếp tỷ suất sinh lời trên tổng tài sản (ROA) của doanh nghiệp."',
      start: 97,
      end: 220,
      sectionId: 'sec-1',
      chapterNumber: 1,
      chapterTitle: 'Chương 1: Cơ sở lý luận và Tổng quan nghiên cứu',
      paragraphIndex: 1,
      status: 'pending',
    },
    {
      id: 'f4',
      ruleId: 'SYN-VN-03',
      severity: 'suggestion',
      severityLabel: 'Gợi ý',
      title: 'Câu bị động và danh hóa kéo dài',
      excerpt: '"việc các quyết định phân bổ ngân sách được thực hiện bởi bộ phận kế toán quản trị đã được chứng minh là có sự ảnh hưởng đáng kể"',
      matchedText: 'việc các quyết định phân bổ ngân sách được thực hiện bởi bộ phận kế toán quản trị đã được chứng minh là có sự ảnh hưởng đáng kể',
      reason: 'Việc lồng ghép nhiều cụm danh hóa ("việc...", "sự ảnh hưởng") và thể bị động ("được thực hiện bởi", "đã được chứng minh") làm câu văn nặng nề.',
      suggestion: '"kế toán quản trị trực tiếp kiểm soát phân bổ ngân sách sẽ giúp doanh nghiệp giảm đáng kể chi phí đại diện (agency cost)."',
      start: 146,
      end: 273,
      sectionId: 'sec-2',
      chapterNumber: 2,
      chapterTitle: 'Chương 2: Phương pháp nghiên cứu và Dữ liệu',
      paragraphIndex: 0,
      status: 'pending',
    },
    {
      id: 'f5',
      ruleId: 'FOR-01',
      severity: 'critical',
      severityLabel: 'Cần sửa ngay',
      title: 'Trích dẫn chứa ký hiệu hệ thống và mã nguồn cần xác minh',
      excerpt: '"(Nguyen & Tran, 2024, doi:10.1016/j.jcorpfin.2024.999999 — contentReference[oaicite:0]{index=0})"',
      matchedText: '(Nguyen & Tran, 2024, doi:10.1016/j.jcorpfin.2024.999999 — contentReference[oaicite:0]{index=0})',
      reason: 'Xuất hiện chuỗi ký hiệu hệ thống ("contentReference[oaicite:0]") phát sinh khi sao chép văn bản và mã DOI có dấu hiệu không khớp danh mục xuất bản thực tế.',
      suggestion: 'Xóa hoàn toàn chuỗi "contentReference[oaicite:0]{index=0}" và đối chiếu lại thông tin bài báo gốc trước khi đưa vào danh mục trích dẫn.',
      start: 132,
      end: 228,
      sectionId: 'sec-3',
      chapterNumber: 3,
      chapterTitle: 'Chương 3: Kết quả phân tích và Thảo luận',
      paragraphIndex: 0,
      status: 'pending',
    },
    {
      id: 'f6',
      ruleId: 'SYN-03',
      severity: 'warning',
      severityLabel: 'Nên sửa',
      title: 'Cấu trúc đối lập khuếch đại ý nghĩa',
      excerpt: '"Đây không chỉ là một giải pháp vận hành đơn thuần mà còn là một tuyên ngôn chiến lược toàn diện"',
      matchedText: 'Đây không chỉ là một giải pháp vận hành đơn thuần mà còn là một tuyên ngôn chiến lược toàn diện',
      reason: 'Cách đặt vấn đề theo khuôn mẫu "không chỉ là X đơn thuần mà còn là tuyên ngôn Y" mang tính hùng biện hơn là phân tích dữ liệu thực nghiệm.',
      suggestion: '"Giải pháp này đồng thời hỗ trợ điều tiết tồn kho ngắn hạn và ổn định cấu trúc thanh khoản dài hạn của doanh nghiệp."',
      start: 0,
      end: 95,
      sectionId: 'sec-3',
      chapterNumber: 3,
      chapterTitle: 'Chương 3: Kết quả phân tích và Thảo luận',
      paragraphIndex: 1,
      status: 'pending',
    },
    {
      id: 'f7',
      ruleId: 'DIS-02',
      severity: 'warning',
      severityLabel: 'Nên sửa',
      title: 'Câu kết đoạn mang tính khẩu hiệu chung',
      excerpt: '"Tóm lại, có thể khẳng định chắc chắn rằng sự kết hợp hài hòa... chính là chìa khóa vàng mở ra cánh cửa thành công rực rỡ cho mọi doanh nghiệp trong kỷ nguyên mới."',
      matchedText: 'Tóm lại, có thể khẳng định chắc chắn rằng sự kết hợp hài hòa giữa chiến lược nhân sự, marketing số và quản trị sản xuất chính là chìa khóa vàng mở ra cánh cửa thành công rực rỡ cho mọi doanh nghiệp trong kỷ nguyên mới.',
      reason: 'Các hình ảnh ẩn dụ như "chìa khóa vàng", "thành công rực rỡ", "trong kỷ nguyên mới" không phù hợp với phần kết luận của nghiên cứu khoa học.',
      suggestion: '"Kết quả nghiên cứu cho thấy doanh nghiệp cần phối hợp đồng bộ giữa kế hoạch nhân sự, tiếp thị và điều độ sản xuất để duy trì biên lợi nhuận mục tiêu."',
      start: 0,
      end: 217,
      sectionId: 'sec-4',
      chapterNumber: 4,
      chapterTitle: 'Chương 4: Kết luận và Khuyến nghị quản trị',
      paragraphIndex: 0,
      status: 'pending',
    },
  ],
  summary: {
    totalWords: 250,
    totalSentences: 6,
    totalSections: 4,
    auditedSections: 4,
    totalFlags: 7,
    criticalCount: 1,
    warningCount: 4,
    suggestionCount: 2,
    overallAiStyleScore: 33,
    protectedTermsMatched: [
      'chuỗi cung ứng lạnh',
      'quản trị vốn lưu động ròng',
      'đòn bẩy tài chính',
      'tỷ lệ an toàn vốn tối thiểu',
      'kế toán quản trị',
      'chi phí đại diện',
      'dữ liệu bảng',
      'ý nghĩa thống kê',
      'hàng tồn kho',
    ],
  },
};
