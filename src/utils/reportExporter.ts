import { DocumentAuditResult } from '../types/auditor';

function escapeHtml(raw: string): string {
  return (raw || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

export function generateStandaloneHtmlReport(audit: DocumentAuditResult): string {
  const { title, findings, summary } = audit;
  const criticalCount = findings.filter((f) => f.severity === 'critical').length;
  const warningCount = findings.filter((f) => f.severity === 'warning').length;
  const suggestionCount = findings.filter((f) => f.severity === 'suggestion').length;
  const resolvedCount = findings.filter((f) => f.status === 'resolved').length;

  const findingsHtml = findings
    .map((f, idx) => {
      const badgeColor =
        f.severity === 'critical'
          ? 'background:#fee2e2;color:#991b1b;border:1px solid #fca5a5;'
          : f.severity === 'warning'
          ? 'background:#ffedd5;color:#9a3412;border:1px solid #fdba74;'
          : 'background:#e0e7ff;color:#3730a3;border:1px solid #a5b4fc;';

      return `
        <div class="finding-card">
          <div class="finding-header">
            <strong>${idx + 1}. ${escapeHtml(f.title)}</strong>
            <span class="badge" style="${badgeColor}">${escapeHtml(f.severityLabel)}</span>
          </div>
          ${f.chapterTitle ? `<div class="chapter-tag">${escapeHtml(f.chapterTitle)}</div>` : ''}
          <blockquote class="excerpt">${escapeHtml(f.excerpt)}</blockquote>
          <p class="reason"><strong>Nguyên nhân cần lưu ý:</strong> ${escapeHtml(f.reason)}</p>
          <p class="suggestion"><strong>Đề xuất biên tập:</strong> ${escapeHtml(f.suggestion)}</p>
        </div>
      `;
    })
    .join('\n');

  return `<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <title>Báo cáo Kiểm toán Văn phong Học thuật — ${escapeHtml(title)}</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      color: #0f172a;
      background: #f8fafc;
      margin: 0;
      padding: 32px 20px;
      line-height: 1.65;
    }
    .container {
      max-width: 920px;
      margin: 0 auto;
      background: #ffffff;
      border-radius: 16px;
      padding: 32px;
      box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
      border: 1px solid #e2e8f0;
    }
    h1 { margin: 0 0 8px 0; font-size: 24px; color: #0f172a; }
    .subtitle { color: #475569; font-size: 14px; margin-bottom: 24px; }
    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      margin-bottom: 28px;
    }
    .kpi-box {
      padding: 14px;
      border-radius: 12px;
      background: #f1f5f9;
      text-align: center;
    }
    .kpi-val { font-size: 22px; font-weight: 800; }
    .kpi-label { font-size: 12px; color: #64748b; }
    .finding-card {
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 18px;
      margin-bottom: 14px;
      background: #ffffff;
    }
    .finding-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      margin-bottom: 8px;
    }
    .badge {
      padding: 3px 10px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 600;
    }
    .chapter-tag { font-size: 12px; color: #64748b; margin-bottom: 8px; }
    .excerpt {
      margin: 8px 0;
      padding: 10px 14px;
      background: #f8fafc;
      border-left: 3px solid #3b82f6;
      font-style: italic;
      color: #334155;
    }
    .reason { font-size: 13.5px; color: #475569; margin: 6px 0; }
    .suggestion { font-size: 13.5px; color: #047857; margin: 6px 0 0 0; }
    @media print {
      body { background: #fff; padding: 0; }
      .container { box-shadow: none; border: none; }
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Báo cáo Kiểm toán Văn phong Học thuật</h1>
    <div class="subtitle">Tài liệu: <strong>${escapeHtml(title)}</strong> · Tổng số từ: ${summary?.totalWords ?? 0} · Đã xử lý: ${resolvedCount}/${findings.length}</div>
    <div class="kpi-grid">
      <div class="kpi-box">
        <div class="kpi-val" style="color:#dc2626;">${criticalCount}</div>
        <div class="kpi-label">Cần sửa ngay</div>
      </div>
      <div class="kpi-box">
        <div class="kpi-val" style="color:#ea580c;">${warningCount}</div>
        <div class="kpi-label">Nên sửa</div>
      </div>
      <div class="kpi-box">
        <div class="kpi-val" style="color:#4f46e5;">${suggestionCount}</div>
        <div class="kpi-label">Gợi ý</div>
      </div>
      <div class="kpi-box">
        <div class="kpi-val" style="color:#059669;">${resolvedCount}/${findings.length}</div>
        <div class="kpi-label">Đã xử lý</div>
      </div>
    </div>
    ${findingsHtml}
  </div>
</body>
</html>`;
}

export function downloadStandaloneHtmlReport(audit: DocumentAuditResult): void {
  const html = generateStandaloneHtmlReport(audit);
  const blob = new Blob([html], { type: 'text/html;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  const safeName = (audit.title || 'Bao_cao_kiem_toan').replace(/\.docx$/i, '');
  a.href = url;
  a.download = `${safeName}_Audit_Report.html`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

export function downloadJsonAuditReport(audit: DocumentAuditResult): void {
  const jsonStr = JSON.stringify(audit, null, 2);
  const blob = new Blob([jsonStr], { type: 'application/json;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  const safeName = (audit.title || 'Bao_cao_kiem_toan').replace(/\.docx$/i, '');
  a.href = url;
  a.download = `${safeName}_Audit_Report.json`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}
