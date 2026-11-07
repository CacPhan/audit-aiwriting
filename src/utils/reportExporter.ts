import {
  AuditedParagraph,
  AuditFlag,
  DocumentAuditResult,
} from '../types/auditor';

function escapeHtml(text: string): string {
  return String(text || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function getSafeBaseFilename(title: string): string {
  return (
    String(title || 'Bao_cao_kiem_toan')
      .replace(/\.docx$/i, '')
      .replace(/[^\p{L}\p{N}_-]+/gu, '_')
      .replace(/^_+|_+$/g, '') || 'Bao_cao_kiem_toan'
  );
}

/**
 * Palette of distinct Feedback Studio highlight color schemes
 * mapped deterministically by severity and finding index so adjacent/varied rules
 * stand out clearly (Red, Rose, Amber, Blue, Purple, Emerald).
 */
export interface FeedbackColorTheme {
  bg: string;
  border: string;
  badgeBg: string;
  text: string;
}

const FEEDBACK_PALETTE: Record<string, FeedbackColorTheme[]> = {
  critical: [
    {
      bg: '#fde2e4',
      border: '#e63946',
      badgeBg: '#d90429',
      text: '#641220',
    },
    {
      bg: '#ffd6e0',
      border: '#d81159',
      badgeBg: '#b5179e',
      text: '#590d22',
    },
  ],
  warning: [
    {
      bg: '#ffe5d9',
      border: '#f77f00',
      badgeBg: '#e85d04',
      text: '#7f4f24',
    },
    {
      bg: '#fae1dd',
      border: '#e07a5f',
      badgeBg: '#c9184a',
      text: '#6b2d5c',
    },
    {
      bg: '#e0fbfc',
      border: '#0096c7',
      badgeBg: '#0077b6',
      text: '#023e8a',
    },
  ],
  suggestion: [
    {
      bg: '#e2eafc',
      border: '#4361ee',
      badgeBg: '#3f37c9',
      text: '#1d3557',
    },
    {
      bg: '#ede0d4',
      border: '#7f5539',
      badgeBg: '#6c757d',
      text: '#343a40',
    },
    {
      bg: '#d8f3dc',
      border: '#40916c',
      badgeBg: '#2d6a4f',
      text: '#1b4332',
    },
    {
      bg: '#f3d9fa',
      border: '#9c36b5',
      badgeBg: '#862e9c',
      text: '#49111c',
    },
  ],
};

export function getFeedbackColorTheme(
  severity: string,
  badgeNumber: number
): FeedbackColorTheme {
  const list = FEEDBACK_PALETTE[severity] || FEEDBACK_PALETTE.suggestion;
  return list[(Math.max(1, badgeNumber) - 1) % list.length];
}

/**
 * Generates a standalone, print-ready HTML document for the Summary Audit Report.
 */
export function generateStandaloneHtmlReport(
  audit: DocumentAuditResult
): string {
  const criticalCount = audit.findings.filter(
    (f) => f.severity === 'critical'
  ).length;
  const warningCount = audit.findings.filter(
    (f) => f.severity === 'warning'
  ).length;
  const suggestionCount = audit.findings.filter(
    (f) => f.severity === 'suggestion'
  ).length;

  const findingsHtml =
    audit.findings.length === 0
      ? `<div style="padding:24px;border:1px solid #cbd5e1;border-radius:12px;text-align:center;color:#475569;">
          Không phát hiện điểm cần lưu ý nào trong tài liệu này.
         </div>`
      : audit.findings
          .map((f, index) => {
            const badgeColor =
              f.severity === 'critical'
                ? '#dc2626'
                : f.severity === 'warning'
                ? '#ea580c'
                : '#4f46e5';
            const badgeBg =
              f.severity === 'critical'
                ? '#fef2f2'
                : f.severity === 'warning'
                ? '#fff7ed'
                : '#eef2ff';
            const sectionObj = audit.sections.find(
              (s) => s.id === f.sectionId
            );
            const sectionTitle = sectionObj ? sectionObj.title : '';

            return `
        <div class="finding-card">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:12px;margin-bottom:8px;">
            <div>
              <strong style="font-size:15px;color:#0f172a;">#${index + 1}. ${escapeHtml(
              f.title
            )}</strong>
              ${
                sectionTitle
                  ? `<div style="font-size:12px;color:#64748b;margin-top:2px;">Chương/Mục: ${escapeHtml(
                      sectionTitle
                    )}</div>`
                  : ''
              }
            </div>
            <span style="font-size:12px;font-weight:700;color:${badgeColor};background:${badgeBg};border:1px solid ${badgeColor}40;padding:3px 10px;border-radius:999px;white-space:nowrap;">
              ${escapeHtml(f.severityLabel)}
            </span>
          </div>
          <blockquote style="margin:8px 0;padding:10px 14px;background:#f8fafc;border-left:3px solid ${badgeColor};font-style:italic;color:#334155;border-radius:0 8px 8px 0;">
            ${escapeHtml(f.excerpt || f.matchedText || '')}
          </blockquote>
          <p style="margin:6px 0;font-size:13.5px;color:#475569;">
            <strong>Nguyên nhân:</strong> ${escapeHtml(f.reason)}
          </p>
          <p style="margin:6px 0 0;font-size:13.5px;color:#047857;background:#ecfdf5;padding:8px 12px;border-radius:8px;border:1px solid #a7f3d0;">
            <strong>Đề xuất biên tập:</strong> ${escapeHtml(f.suggestion)}
          </p>
        </div>
      `;
          })
          .join('\n');

  return `<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Báo cáo Kiểm toán Văn phong - ${escapeHtml(audit.title)}</title>
  <style>
    * { box-sizing: border-box; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      max-width: 900px;
      margin: 28px auto;
      padding: 0 24px 40px;
      color: #0f172a;
      background: #ffffff;
      line-height: 1.65;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }
    .summary-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 14px;
      margin: 22px 0 28px;
    }
    .summary-box {
      padding: 16px;
      border: 1px solid #cbd5e1;
      border-radius: 12px;
      text-align: center;
      background: #f8fafc;
    }
    .finding-card {
      padding: 16px 18px;
      border: 1px solid #cbd5e1;
      border-radius: 12px;
      margin-bottom: 14px;
      background: #ffffff;
      page-break-inside: avoid;
      break-inside: avoid;
    }
    @page {
      size: A4 portrait;
      margin: 15mm 14mm;
    }
    @media print {
      body {
        margin: 0;
        padding: 0;
        max-width: 100%;
      }
      .no-print {
        display: none !important;
      }
    }
  </style>
</head>
<body>
  <header style="border-bottom:2px solid #0f172a;padding-bottom:14px;">
    <div style="font-size:11px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#2563eb;">
      AI STYLE AUDITOR · ACADEMIC WRITING REVIEW
    </div>
    <h1 style="margin:6px 0 4px;font-size:22px;">Báo cáo Kiểm toán Văn phong Học thuật</h1>
    <p style="color:#475569;margin:0;font-size:14px;">
      Tài liệu: <strong>${escapeHtml(audit.title)}</strong> · Tổng số từ: <strong>${
    audit.summary?.totalWords ?? 0
  }</strong> · Tổng phát hiện: <strong>${audit.findings.length}</strong>
    </p>
  </header>

  <div class="summary-grid">
    <div class="summary-box">
      <div style="font-size:12px;color:#64748b;font-weight:600;">Cần sửa ngay</div>
      <div style="font-size:26px;font-weight:800;color:#dc2626;margin-top:2px;">${criticalCount}</div>
    </div>
    <div class="summary-box">
      <div style="font-size:12px;color:#64748b;font-weight:600;">Nên sửa</div>
      <div style="font-size:26px;font-weight:800;color:#ea580c;margin-top:2px;">${warningCount}</div>
    </div>
    <div class="summary-box">
      <div style="font-size:12px;color:#64748b;font-weight:600;">Gợi ý</div>
      <div style="font-size:26px;font-weight:800;color:#4f46e5;margin-top:2px;">${suggestionCount}</div>
    </div>
  </div>

  <main>
    ${findingsHtml}
  </main>
</body>
</html>`;
}

/**
 * Helper that slices a paragraph's text and wraps each flagged span in a
 * Feedback Studio colored highlight with a superscript badge number.
 */
function renderParagraphFeedbackHtml(
  para: AuditedParagraph,
  findingNumberMap: Map<string, number>,
  allFindingsMap: Map<string, AuditFlag>
): string {
  const text = para.text || '';
  const paraFlags = (para.flags || [])
    .map((f) => allFindingsMap.get(f.id) || f)
    .filter(
      (f) =>
        typeof f.start === 'number' &&
        typeof f.end === 'number' &&
        f.end > f.start
    )
    .sort((a, b) => a.start - b.start);

  if (paraFlags.length === 0) {
    return escapeHtml(text);
  }

  const parts: string[] = [];
  let cursor = 0;

  for (const flag of paraFlags) {
    const start = Math.max(cursor, Math.min(flag.start, text.length));
    const end = Math.max(start, Math.min(flag.end, text.length));

    if (start > cursor) {
      parts.push(escapeHtml(text.slice(cursor, start)));
    }

    if (end > start) {
      const badgeNum = findingNumberMap.get(flag.id) || 1;
      const theme = getFeedbackColorTheme(flag.severity, badgeNum);
      const snippet = escapeHtml(text.slice(start, end));
      const tooltip = escapeHtml(
        `[#${badgeNum} - ${flag.severityLabel}] ${flag.title}: ${flag.suggestion}`
      );

      parts.push(
        `<a href="#feedback-note-${badgeNum}" class="t-hl" style="background:${theme.bg};border-bottom:2px solid ${theme.border};color:${theme.text};" title="${tooltip}">` +
          `<sup class="t-badge" style="background:${theme.badgeBg};">${badgeNum}</sup>` +
          `${snippet}` +
          `</a>`
      );
      cursor = end;
    }
  }

  if (cursor < text.length) {
    parts.push(escapeHtml(text.slice(cursor)));
  }

  return parts.join('');
}

/**
 * Classifies a paragraph line or section heading so that Feedback Studio preserves
 * the original .docx hierarchy (Chapter H1, Section H2, Subheading H3/H4, List item, Body paragraph).
 */
export function classifyManuscriptBlock(
  text: string,
  isExcludedSection = false
): 'subheading' | 'bullet' | 'toc-or-ref' | 'body' {
  const trimmed = (text || '').trim();
  if (
    trimmed.length <= 150 &&
    !/[.!?]$/.test(trimmed) &&
    /^(?:\d+\.\d+\.\d+(?:\.\d+)*\.?\s+|[a-zđ]\)\s+|[IVXLC]+\.\s+)/i.test(
      trimmed
    )
  ) {
    return 'subheading';
  }
  if (/^(?:[-•+]\s+|\d+\.\s+\S+)/.test(trimmed) && isExcludedSection) {
    return 'toc-or-ref';
  }
  if (/^[-•+]\s+/.test(trimmed)) {
    return 'bullet';
  }
  if (isExcludedSection) {
    return 'toc-or-ref';
  }
  return 'body';
}

/**
 * Generates a full-manuscript Feedback Studio HTML document:
 * - Preserves the original .docx chapter/section/subheading hierarchy & formatting
 * - Highlights every AI-style span inline with colored backgrounds and top-left numbered badges (1, 2, 3...)
 * - Includes a numbered Feedback Studio Annotation Key linking each badge number
 *   to its diagnosis, reason, and editorial rewrite suggestion.
 */
export function generateFeedbackHtmlReport(audit: DocumentAuditResult): string {
  const findingNumberMap = new Map<string, number>();
  const allFindingsMap = new Map<string, AuditFlag>();

  audit.findings.forEach((f, idx) => {
    findingNumberMap.set(f.id, idx + 1);
    allFindingsMap.set(f.id, f);
  });

  const criticalCount = audit.findings.filter(
    (f) => f.severity === 'critical'
  ).length;
  const warningCount = audit.findings.filter(
    (f) => f.severity === 'warning'
  ).length;
  const suggestionCount = audit.findings.filter(
    (f) => f.severity === 'suggestion'
  ).length;

  // Render full manuscript sections preserving original .docx heading levels & paragraph formatting
  const sectionsHtml = audit.sections
    .map((sec) => {
      const secFindingsCount = audit.findings.filter(
        (f) => f.sectionId === sec.id
      ).length;

      const isTopChapter =
        /^(?:CHƯƠNG\s*(?:\d+|[IVXLC]+)|PHẦN\s+|MỞ\s+ĐẦU|LỜI\s+MỞ\s+ĐẦU|KẾT\s+LUẬN|DANH\s+MỤC|TÀI\s+LIỆU\s+THAM\s+KHẢO|MỤC\s+LỤC|PHỤ\s+LỤC)/i.test(
          sec.title.trim()
        );
      const headingClass = isTopChapter
        ? 'section-heading-h1'
        : 'section-heading-h2';

      // If a parent chapter title was attached to sectionLabel (e.g. "CHƯƠNG 1: ... · 1.1..."), show it above
      const hasParentChapterLabel =
        sec.sectionLabel &&
        !sec.sectionLabel.startsWith('Phần ') &&
        !sec.sectionLabel.startsWith('Mục loại trừ') &&
        sec.sectionLabel.includes('·');
      const parentChapterBanner = hasParentChapterLabel
        ? `<div class="parent-chapter-label">${escapeHtml(
            sec.sectionLabel.split('·')[0].trim()
          )}</div>`
        : '';

      const paragraphsHtml = sec.paragraphs
        .map((para) => {
          const innerHtml = renderParagraphFeedbackHtml(
            para,
            findingNumberMap,
            allFindingsMap
          );
          const prefixHtml = para.prefix
            ? `<h3 class="manuscript-subheading">${escapeHtml(
                para.prefix
              )}</h3>`
            : '';
          const blockKind = classifyManuscriptBlock(para.text, sec.isExcluded);

          if (blockKind === 'subheading') {
            return `${prefixHtml}<h4 class="manuscript-subheading">${innerHtml}</h4>`;
          }
          if (blockKind === 'bullet') {
            return `${prefixHtml}<p class="manuscript-bullet">${innerHtml}</p>`;
          }
          if (blockKind === 'toc-or-ref') {
            return `${prefixHtml}<p class="manuscript-ref-line">${innerHtml}</p>`;
          }
          return `${prefixHtml}<p class="manuscript-para">${innerHtml}</p>`;
        })
        .join('\n');

      return `
      <section class="manuscript-section" id="sec-${escapeHtml(sec.id)}">
        ${parentChapterBanner}
        <div class="section-heading-bar">
          <h2 class="${headingClass}">${escapeHtml(sec.title)}</h2>
          <span class="section-meta-badge">
            ${
              sec.isExcluded
                ? 'Mục tự động bỏ qua'
                : `${secFindingsCount} đánh dấu`
            }
          </span>
        </div>
        ${paragraphsHtml}
      </section>`;
    })
    .join('\n');

  // Render numbered Feedback Studio annotation cards
  const feedbackCardsHtml =
    audit.findings.length === 0
      ? `<div style="padding:18px;text-align:center;color:#64748b;border:1px dashed #cbd5e1;border-radius:10px;">
          Không có đánh dấu văn phong nào trong bản thảo.
         </div>`
      : audit.findings
          .map((f, idx) => {
            const num = idx + 1;
            const theme = getFeedbackColorTheme(f.severity, num);
            const secObj = audit.sections.find((s) => s.id === f.sectionId);
            const secName = secObj ? secObj.shortTitle || secObj.title : '';

            return `
        <div class="feedback-note-card" id="feedback-note-${num}" style="border-left:4px solid ${
              theme.badgeBg
            };">
          <div style="display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:6px;">
            <div style="display:flex;align-items:center;gap:8px;">
              <span class="note-num-pill" style="background:${
                theme.badgeBg
              };">${num}</span>
              <strong style="font-size:13.5px;color:#0f172a;">${escapeHtml(
                f.title
              )}</strong>
            </div>
            <span style="font-size:11px;font-weight:700;padding:2px 8px;border-radius:999px;background:${
              theme.bg
            };color:${theme.text};border:1px solid ${theme.border};">
              ${escapeHtml(f.severityLabel)}
            </span>
          </div>
          ${
            secName
              ? `<div style="font-size:11.5px;color:#64748b;margin-bottom:4px;">Vị trí: <strong>${escapeHtml(
                  secName
                )}</strong></div>`
              : ''
          }
          <div style="font-size:12.5px;font-style:italic;color:#334155;background:#f8fafc;padding:6px 10px;border-radius:6px;margin-bottom:6px;">
            ${escapeHtml(f.excerpt || f.matchedText || '')}
          </div>
          <div style="font-size:12.5px;color:#475569;margin-bottom:4px;">
            <strong>Nhận xét:</strong> ${escapeHtml(f.reason)}
          </div>
          <div style="font-size:12.5px;color:#047857;background:#ecfdf5;padding:6px 10px;border-radius:6px;border:1px solid #a7f3d0;">
            <strong>Gợi ý sửa:</strong> ${escapeHtml(f.suggestion)}
          </div>
        </div>`;
          })
          .join('\n');

  return `<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Feedback - ${escapeHtml(audit.title)}</title>
  <style>
    * { box-sizing: border-box; }
    body {
      margin: 0;
      padding: 0;
      background: #eef2f6;
      color: #1e293b;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }
    /* Feedback Studio Top Bar */
    .studio-topbar {
      position: sticky;
      top: 0;
      z-index: 30;
      background: #ffffff;
      border-bottom: 3px solid #0284c7;
      padding: 10px 24px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      box-shadow: 0 2px 8px rgba(15, 23, 42, 0.06);
    }
    .studio-brand {
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 800;
      font-size: 16px;
      color: #0369a1;
      letter-spacing: -0.02em;
    }
    .studio-doc-info {
      font-size: 13.5px;
      color: #334155;
      font-weight: 600;
    }
    .studio-stats {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
    }
    .stat-pill {
      padding: 3px 10px;
      border-radius: 6px;
      font-weight: 700;
      border: 1px solid #cbd5e1;
      background: #f8fafc;
    }
    /* Main Layout Container */
    .studio-workspace {
      max-width: 1320px;
      margin: 24px auto;
      padding: 0 18px 48px;
      display: grid;
      grid-template-columns: minmax(0, 1fr) 370px;
      gap: 24px;
      align-items: start;
    }
    @media (max-width: 1024px) {
      .studio-workspace {
        grid-template-columns: 1fr;
      }
    }
    /* A4 Thesis Manuscript Sheet */
    .a4-paper {
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      box-shadow: 0 6px 24px rgba(15, 23, 42, 0.08);
      padding: 48px 56px;
      font-family: "Times New Roman", "Noto Serif", Georgia, serif;
      font-size: 17px;
      line-height: 1.95;
      color: #111827;
    }
    @media (max-width: 640px) {
      .a4-paper {
        padding: 24px 20px;
        font-size: 15.5px;
      }
    }
    .manuscript-section {
      margin-bottom: 34px;
      padding-bottom: 18px;
      border-bottom: 1px dashed #e2e8f0;
    }
    .parent-chapter-label {
      font-family: "Times New Roman", Georgia, serif;
      font-size: 15px;
      font-weight: 700;
      text-transform: uppercase;
      color: #334155;
      margin-bottom: 6px;
      letter-spacing: 0.02em;
    }
    .section-heading-bar {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 16px;
    }
    .section-heading-h1 {
      font-family: "Times New Roman", Georgia, serif;
      font-size: 20px;
      font-weight: 700;
      text-transform: uppercase;
      color: #0f172a;
      margin: 0;
      line-height: 1.4;
    }
    .section-heading-h2 {
      font-family: "Times New Roman", Georgia, serif;
      font-size: 18px;
      font-weight: 700;
      color: #0f172a;
      margin: 0;
      line-height: 1.45;
    }
    .manuscript-subheading {
      font-family: "Times New Roman", Georgia, serif;
      font-size: 17px;
      font-weight: 700;
      color: #1e293b;
      margin: 18px 0 8px 0;
      text-indent: 0;
    }
    .section-meta-badge {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 11px;
      font-weight: 600;
      color: #475569;
      background: #f1f5f9;
      padding: 2px 9px;
      border-radius: 999px;
      white-space: nowrap;
      flex-shrink: 0;
    }
    .manuscript-para {
      margin: 0 0 14px 0;
      text-align: justify;
      text-indent: 28px;
    }
    .manuscript-bullet {
      margin: 0 0 10px 0;
      padding-left: 24px;
      text-align: justify;
      text-indent: 0;
    }
    .manuscript-ref-line {
      margin: 0 0 8px 0;
      text-align: left;
      text-indent: 0;
      font-size: 15.5px;
    }
    /* Inline Highlight & Top-Left Badge */
    .t-hl {
      position: relative;
      display: inline;
      padding: 2px 3px 2px 4px;
      border-radius: 3px;
      text-decoration: none;
      box-decoration-break: clone;
      -webkit-box-decoration-break: clone;
      transition: filter 0.15s ease;
    }
    .t-hl:hover {
      filter: brightness(0.93);
    }
    .t-badge {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-width: 17px;
      height: 15px;
      padding: 0 4px;
      margin-right: 2px;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      font-size: 10px;
      font-weight: 800;
      line-height: 1;
      color: #ffffff;
      border-radius: 3px 3px 3px 0;
      vertical-align: super;
      transform: translateY(-4px);
      box-shadow: 0 1px 2px rgba(0,0,0,0.22);
      text-indent: 0;
    }
    /* Right Side Feedback Studio Margin Panel */
    .studio-sidebar {
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      padding: 18px;
      box-shadow: 0 4px 16px rgba(15, 23, 42, 0.05);
      position: sticky;
      top: 68px;
      max-height: calc(100vh - 90px);
      overflow-y: auto;
    }
    .feedback-note-card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 12px;
      margin-bottom: 12px;
      page-break-inside: avoid;
      break-inside: avoid;
    }
    .note-num-pill {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-width: 22px;
      height: 20px;
      padding: 0 6px;
      border-radius: 4px;
      color: #ffffff;
      font-size: 11px;
      font-weight: 800;
    }
    @page {
      size: A4 portrait;
      margin: 14mm 14mm;
    }
    @media print {
      body {
        background: #ffffff !important;
      }
      .studio-topbar {
        position: static;
        box-shadow: none;
        padding: 0 0 10px 0;
        margin-bottom: 16px;
      }
      .studio-workspace {
        display: block;
        max-width: 100%;
        margin: 0;
        padding: 0;
      }
      .a4-paper {
        border: none;
        box-shadow: none;
        padding: 0;
      }
      .studio-sidebar {
        position: static;
        max-height: none;
        overflow: visible;
        border: none;
        box-shadow: none;
        padding: 20px 0 0 0;
        margin-top: 24px;
        border-top: 2px solid #0f172a;
      }
    }
  </style>
</head>
<body>
  <header class="studio-topbar">
    <div class="studio-brand">
      <span>feedback studio</span>
      <span style="color:#cbd5e1;font-weight:400;">|</span>
      <span class="studio-doc-info">${escapeHtml(audit.title)}</span>
    </div>
    <div class="studio-stats">
      <span class="stat-pill" style="color:#dc2626;border-color:#fecaca;background:#fef2f2;">
        Cần sửa ngay: ${criticalCount}
      </span>
      <span class="stat-pill" style="color:#ea580c;border-color:#fed7aa;background:#fff7ed;">
        Nên sửa: ${warningCount}
      </span>
      <span class="stat-pill" style="color:#4f46e5;border-color:#c7d2fe;background:#eef2ff;">
        Gợi ý: ${suggestionCount}
      </span>
      <span class="stat-pill">
        Tổng: ${audit.findings.length} vị trí
      </span>
    </div>
  </header>

  <div class="studio-workspace">
    <article class="a4-paper">
      ${sectionsHtml}
    </article>

    <aside class="studio-sidebar">
      <h3 style="margin:0 0 12px 0;font-size:14px;text-transform:uppercase;letter-spacing:0.05em;color:#334155;">
        Danh mục Chú giải (${audit.findings.length} đánh dấu)
      </h3>
      ${feedbackCardsHtml}
    </aside>
  </div>
</body>
</html>`;
}

/**
 * Helper to trigger a browser file download from a Blob.
 */
function triggerBlobDownload(blob: Blob, filename: string): void {
  if (typeof URL === 'undefined' || typeof URL.createObjectURL !== 'function') {
    return;
  }
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  a.style.display = 'none';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  setTimeout(() => {
    try {
      URL.revokeObjectURL(url);
    } catch {
      // ignore cleanup error
    }
  }, 1500);
}

export function downloadStandaloneHtmlReport(audit: DocumentAuditResult): void {
  const htmlContent = generateStandaloneHtmlReport(audit);
  const blob = new Blob([htmlContent], { type: 'text/html;charset=utf-8' });
  const safeName = getSafeBaseFilename(audit.title);
  triggerBlobDownload(blob, `${safeName}_Audit_Report.html`);
}

export function downloadFeedbackHtmlReport(audit: DocumentAuditResult): void {
  const htmlContent = generateFeedbackHtmlReport(audit);
  const blob = new Blob([htmlContent], { type: 'text/html;charset=utf-8' });
  const safeName = getSafeBaseFilename(audit.title);
  triggerBlobDownload(blob, `${safeName}_Feedback.html`);
}

export function downloadJsonAuditReport(audit: DocumentAuditResult): void {
  const publicPayload = {
    documentTitle: audit.title,
    totalWords: audit.summary?.totalWords ?? 0,
    totalSentences: audit.summary?.totalSentences ?? 0,
    overallScore: audit.summary?.overallAiStyleScore ?? 0,
    summaryCounts: {
      critical: audit.findings.filter((f) => f.severity === 'critical').length,
      warning: audit.findings.filter((f) => f.severity === 'warning').length,
      suggestion: audit.findings.filter((f) => f.severity === 'suggestion')
        .length,
      resolved: audit.findings.filter((f) => f.status !== 'pending').length,
    },
    findings: audit.findings.map((f, index) => ({
      number: index + 1,
      severity: f.severityLabel,
      title: f.title,
      excerpt: f.excerpt || f.matchedText || '',
      reason: f.reason,
      suggestion: f.suggestion,
      status: f.status,
    })),
  };

  const blob = new Blob([JSON.stringify(publicPayload, null, 2)], {
    type: 'application/json;charset=utf-8',
  });
  const safeName = getSafeBaseFilename(audit.title);
  triggerBlobDownload(blob, `${safeName}_Audit_Report.json`);
}

/**
 * Prints either the Summary Report or the Feedback Full-Manuscript view
 * inside a clean hidden iframe so Chrome/Edge Print-to-PDF renders crisp A4 pages.
 */
export function printAuditDocument(
  audit: DocumentAuditResult,
  mode: 'summary' | 'feedback' = 'summary'
): void {
  const htmlContent =
    mode === 'feedback'
      ? generateFeedbackHtmlReport(audit)
      : generateStandaloneHtmlReport(audit);

  if (typeof document === 'undefined') return;

  const existingIframe = document.getElementById(
    'audit-print-iframe'
  ) as HTMLIFrameElement | null;
  if (existingIframe && existingIframe.parentNode) {
    existingIframe.parentNode.removeChild(existingIframe);
  }

  const iframe = document.createElement('iframe');
  iframe.id = 'audit-print-iframe';
  iframe.title = 'Bản in báo cáo kiểm toán';
  iframe.style.position = 'fixed';
  iframe.style.right = '0';
  iframe.style.bottom = '0';
  iframe.style.width = '0';
  iframe.style.height = '0';
  iframe.style.border = '0';
  iframe.style.visibility = 'hidden';
  document.body.appendChild(iframe);

  const iframeDoc = iframe.contentWindow?.document || iframe.contentDocument;
  if (!iframeDoc || !iframe.contentWindow) {
    if (typeof window !== 'undefined' && typeof window.print === 'function') {
      window.print();
    }
    return;
  }

  iframeDoc.open();
  iframeDoc.write(htmlContent);
  iframeDoc.close();

  const triggerPrint = () => {
    try {
      iframe.contentWindow?.focus();
      if (typeof iframe.contentWindow?.print === 'function') {
        iframe.contentWindow.print();
      } else if (typeof window.print === 'function') {
        window.print();
      }
    } catch {
      if (typeof window.print === 'function') {
        window.print();
      }
    }
  };

  setTimeout(triggerPrint, 180);
}
