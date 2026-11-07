import { describe, it, expect } from 'vitest';
import { splitRawTextOrHtmlIntoSections } from '../docxParser';
import { generateStandaloneHtmlReport } from '../reportExporter';

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
      '1. Nguyễn Văn A (2024), Quản trị học, NXB Kinh tế Quốc dân.'
    ].join('\n\n');

    const sections = splitRawTextOrHtmlIntoSections(rawThesis, false);
    expect(sections.length).toBe(4);
    expect(sections[0].isExcluded).toBe(true);
    expect(sections[1].isExcluded).toBe(false);
    expect(sections[3].isExcluded).toBe(true);
  });

  it('generates a complete standalone HTML audit report with severity summary and findings', () => {
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
  });
});
