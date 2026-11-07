import fs from 'node:fs';
import path from 'node:path';
import { describe, it, expect } from 'vitest';
import {
  extractSectionsFromDocx,
  splitRawTextOrHtmlIntoSections,
} from '../docxParser';
import { generateStandaloneHtmlReport } from '../reportExporter';

function loadDocxFixtureAsFile(filename: string): File {
  const filePath = path.resolve(process.cwd(), 'tests', 'fixtures', filename);
  const buffer = fs.readFileSync(filePath);
  const uint8 = new Uint8Array(buffer);
  const file = new File([uint8], filename, {
    type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
  });
  Object.defineProperty(file, 'arrayBuffer', {
    value: async () =>
      buffer.buffer.slice(
        buffer.byteOffset,
        buffer.byteOffset + buffer.byteLength
      ),
  });
  return file;
}

describe('Thesis .docx Section Splitter & Audit Report Exporter', () => {
  it('splits plain or bold chapter headings (CHƯƠNG 1, 1.1) and auto-excludes MỤC LỤC and TÀI LIỆU THAM KHẢO', () => {
    const rawThesis = [
      'MỤC LỤC',
      'Chương 1: Cơ sở lý luận ........................ 1',
      'CHƯƠNG 1: CƠ SỞ LÝ LUẬN VỀ QUẢN TRỊ CHUỖI CUNG ỨNG',
      'Đoạn văn phân tích cơ sở lý luận về tồn kho an toàn và vận tải đa phương thức.',
      '1.1. Khái niệm quản trị sản xuất tinh gọn',
      'Đoạn văn phân tích hoạch định nguồn lực doanh nghiệp.',
      'DANH MỤC TÀI LIỆU THAM KHẢO',
      '1. Nguyễn Văn A (2024), Quản trị học, NXB Kinh tế Quốc dân.',
    ].join('\n\n');

    const sections = splitRawTextOrHtmlIntoSections(rawThesis, false);
    expect(sections.length).toBe(4);
    expect(sections[0].isExcluded).toBe(true);
    expect(sections[1].isExcluded).toBe(false);
    expect(sections[2].isExcluded).toBe(false);
    expect(sections[3].isExcluded).toBe(true);
  });

  it('accurately parses all 3 real uploaded .docx theses and auto-excludes Cover, Lời cam đoan, Mục lục, Danh mục & Tài liệu tham khảo', async () => {
    const thesisFiles = [
      'kltn_thai_son_11233561.docx',
      'kltn_ngoc_anh_11220218.docx',
      'bao_cao_phan_duy_cac_11233373.docx',
    ];

    for (const filename of thesisFiles) {
      const file = loadDocxFixtureAsFile(filename);
      const sections = await extractSectionsFromDocx(file);

      expect(sections.length).toBeGreaterThan(4);

      const excludedSections = sections.filter((s) => s.isExcluded);
      const auditedSections = sections.filter((s) => !s.isExcluded);

      expect(excludedSections.length).toBeGreaterThanOrEqual(2);
      expect(auditedSections.length).toBeGreaterThanOrEqual(3);

      // Verify front-matter / cover / Mục lục / Tài liệu tham khảo are excluded
      for (const sec of sections) {
        if (
          /^(?:Trang bìa|LỜI CAM ĐOAN|LỜI CẢM ƠN|MỤC LỤC|DANH MỤC|TÀI LIỆU THAM KHẢO|PHỤ LỤC)/i.test(
            sec.title
          )
        ) {
          expect(sec.isExcluded).toBe(true);
        }
      }

      // Verify zero 0-paragraph ghost sections among audited sections
      for (const auditedSec of auditedSections) {
        expect(auditedSec.paragraphs.length).toBeGreaterThan(0);
      }
    }
  });

  it('filters out HTML <table> cells, deduplicates <li><p>, filters captions/sources, and consolidates empty parent headings', () => {
    const htmlWithTableAndNestedList = `
      <h1>1. KẾT QUẢ HOẠT ĐỘNG KINH DOANH</h1>
      <h2>1.1. Tình hình huy động vốn</h2>
      <p>Bảng 1.1: Tình hình huy động vốn giai đoạn 2022 - 2024</p>
      <table>
        <tr><td><p>Chỉ tiêu</p></td><td><p>2023</p></td><td><p>2024</p></td></tr>
        <tr><td><p>Tổng nguồn vốn</p></td><td><p>17.929</p></td><td><p>19.729</p></td></tr>
      </table>
      <p>Nguồn: Phòng Kế hoạch Tài chính</p>
      <p>Tổng nguồn vốn huy động của chi nhánh tăng trưởng ổn định trong giai đoạn nghiên cứu.</p>
      <ul>
        <li><p>Tiền gửi tiết kiệm dân cư chiếm tỷ trọng lớn nhất trong tổng nguồn vốn.</p></li>
      </ul>
    `;
    const sections = splitRawTextOrHtmlIntoSections(htmlWithTableAndNestedList, true);
    const active = sections.filter((s) => !s.isExcluded);
    expect(active.length).toBe(1);
    expect(active[0].title).toContain('1.1. Tình hình huy động vốn');
    expect(active[0].sectionLabel).toContain('1. KẾT QUẢ');
    // Table cells ("17.929", "19.729"), Bảng caption, and Nguồn line must be excluded; <li><p> must not duplicate
    expect(active[0].paragraphs.length).toBe(2);
    expect(active[0].paragraphs[0]).toContain('Tổng nguồn vốn huy động của chi nhánh');
    expect(active[0].paragraphs[1]).toContain('Tiền gửi tiết kiệm dân cư');
  });

  it('generates a complete standalone HTML audit report with severity summary, reasons, and editorial suggestions', () => {
    const sampleAudit: any = {
      title: 'Luan_van_Thac_si_Tai_chinh.docx',
      sections: [],
      findings: [
        {
          id: 'f1',
          ruleId: 'FOR-01',
          severity: 'critical',
          severityLabel: 'Cần sửa ngay',
          title: 'Trích dẫn chứa ký hiệu hệ thống',
          excerpt: '"contentReference[oaicite:0]"',
          reason: 'Xuất hiện chuỗi ký hiệu hệ thống khi sao chép.',
          suggestion: 'Xóa chuỗi ký hiệu và kiểm tra lại nguồn.',
          chapterTitle: 'Chương 3: Kết quả nghiên cứu',
          status: 'pending',
        },
      ],
      summary: {
        totalWords: 1250,
        totalSentences: 48,
        totalSections: 4,
        auditedSections: 4,
        totalFlags: 1,
        criticalCount: 1,
        warningCount: 0,
        suggestionCount: 0,
        overallAiStyleScore: 35,
        protectedTermsMatched: ['quản trị chuỗi cung ứng'],
      },
    };

    const html = generateStandaloneHtmlReport(sampleAudit);
    expect(html).toContain('<!DOCTYPE html>');
    expect(html).toContain('Luan_van_Thac_si_Tai_chinh.docx');
    expect(html).toContain('Trích dẫn chứa ký hiệu hệ thống');
    expect(html).toContain('Cần sửa ngay');
    expect(html).toContain('Xuất hiện chuỗi ký hiệu hệ thống khi sao chép.');
    expect(html).toContain('Xóa chuỗi ký hiệu và kiểm tra lại nguồn.');
  });
});
