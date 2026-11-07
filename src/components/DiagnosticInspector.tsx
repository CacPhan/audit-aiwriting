import React, { useState } from 'react';
import { AuditFlag } from '../types/auditor';

interface DiagnosticInspectorProps {
  finding: AuditFlag | null;
  onToggleResolve: () => void;
  onIgnore: () => void;
  onOpenProModal: () => void;
  collapsed: boolean;
}

function getSeverityBadgeStyle(severity: string): string {
  if (severity === 'critical')
    return 'bg-red-500/20 text-red-400 border border-red-500/35';
  if (severity === 'warning')
    return 'bg-orange-500/20 text-orange-400 border border-orange-500/35';
  return 'bg-indigo-500/20 text-indigo-300 border border-indigo-500/35';
}

export const DiagnosticInspector: React.FC<DiagnosticInspectorProps> = ({
  finding,
  onToggleResolve,
  onIgnore,
  onOpenProModal,
  collapsed,
}) => {
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    if (!finding) return;
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(finding.suggestion).catch(() => {});
    }
    setCopied(true);
    setTimeout(() => setCopied(false), 1500);
  };

  return (
    <aside
      id="workspace-col-right"
      className={`lg:col-span-4 lg:h-full lg:max-h-full lg:overflow-y-auto overscroll-contain workspace-scroll-area lg:pr-1 space-y-4 ${
        collapsed ? 'lg:hidden' : ''
      }`}
    >
      <div
        id="diagnostic-panel"
        className="proximity-card rounded-3xl p-6 space-y-5 border-blue-500/35"
      >
        {finding ? (
          <>
            {/* Priority & Status Header */}
            <div className="flex items-center justify-between gap-2">
              <span
                id="diag-severity-badge"
                className={`px-3 py-1 rounded-full text-xs font-bold ${getSeverityBadgeStyle(
                  finding.severity
                )}`}
              >
                {finding.severityLabel}
              </span>
              {finding.status === 'resolved' ? (
                <span
                  id="diag-status-badge"
                  className="px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-emerald-500/20 text-emerald-400 border border-emerald-500/35"
                >
                  Đã đánh dấu xử lý
                </span>
              ) : finding.status === 'ignored' ? (
                <span
                  id="diag-status-badge"
                  className="px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-slate-500/20 text-slate-300 border border-slate-500/35"
                >
                  Đã bỏ qua
                </span>
              ) : (
                <span
                  id="diag-status-badge"
                  className="px-2.5 py-0.5 rounded-full text-[11px] font-medium bg-slate-500/15 text-[var(--text-muted)] border border-[var(--border-subtle)]"
                >
                  Chưa xử lý
                </span>
              )}
            </div>

            {/* Finding Title & Highlighted Excerpt */}
            <div className="space-y-2.5">
              <h3
                id="diag-title"
                className="font-display font-bold text-lg leading-snug"
              >
                {finding.title}
              </h3>
              <div className="space-y-1">
                <span className="text-[11px] font-semibold uppercase tracking-wider text-[var(--text-muted)]">
                  Đoạn văn bằng chứng
                </span>
                <blockquote
                  id="diag-excerpt"
                  className="p-3.5 rounded-2xl bg-[var(--bg-base)]/80 border border-[var(--border-subtle)] text-xs sm:text-sm italic leading-relaxed"
                >
                  {finding.excerpt}
                </blockquote>
              </div>
            </div>

            {/* Explanation */}
            <div className="space-y-1.5">
              <h4 className="text-xs font-semibold uppercase tracking-wider text-blue-400">
                Nguyên nhân cần lưu ý
              </h4>
              <p
                id="diag-reason"
                className="text-xs sm:text-sm text-[var(--text-muted)] leading-relaxed"
              >
                {finding.reason}
              </p>
            </div>

            {/* Concrete Editorial Suggestion */}
            <div className="space-y-2">
              <h4 className="text-xs font-semibold uppercase tracking-wider text-emerald-400">
                Đề xuất biên tập
              </h4>
              <div className="p-4 rounded-2xl bg-emerald-500/10 border border-emerald-500/30 space-y-2">
                <p
                  id="diag-suggestion"
                  className="text-xs sm:text-sm text-[var(--text-main)] font-medium leading-relaxed"
                >
                  {finding.suggestion}
                </p>
              </div>
            </div>

            {/* Action Buttons: Copy, Mark Resolved, Ignore */}
            <div className="pt-2 flex flex-wrap items-center gap-2">
              <button
                type="button"
                id="copy-suggestion-btn"
                onClick={handleCopy}
                className="flex-1 py-2.5 px-3.5 rounded-xl text-xs font-semibold border border-[var(--border-subtle)] bg-[var(--bg-elevated)] hover:border-blue-400/50 transition-all"
              >
                {copied ? 'Đã sao chép' : 'Sao chép gợi ý'}
              </button>
              <button
                type="button"
                id="resolve-finding-btn"
                onClick={onToggleResolve}
                className={
                  finding.status === 'resolved'
                    ? 'flex-1 py-2.5 px-3.5 rounded-xl text-xs font-bold border border-emerald-500/40 bg-emerald-500/15 text-emerald-300 hover:bg-emerald-500/25 transition-all'
                    : 'flex-1 py-2.5 px-3.5 rounded-xl text-xs font-bold text-white bg-emerald-600 hover:bg-emerald-500 transition-all'
                }
              >
                {finding.status === 'resolved'
                  ? 'Hoàn tác trạng thái'
                  : 'Đánh dấu đã xử lý'}
              </button>
              <button
                type="button"
                onClick={onIgnore}
                className="py-2.5 px-3.5 rounded-xl text-xs font-semibold border border-[var(--border-subtle)] text-[var(--text-muted)] hover:text-[var(--text-main)] transition-all"
              >
                Bỏ qua
              </button>
            </div>

            {/* Pro Feature Hook: Direct Web Editing & Formatted .DOCX Export */}
            <div className="pt-3 border-t border-[var(--border-subtle)]">
              <button
                type="button"
                onClick={onOpenProModal}
                className="w-full py-2.5 px-3.5 rounded-xl text-xs font-semibold border border-violet-500/35 bg-violet-500/10 text-violet-300 hover:bg-violet-500/20 flex items-center justify-between transition-all"
              >
                <span>[PRO] Chỉnh sửa trực tiếp &amp; Xuất .docx</span>
                <span className="px-2 py-0.5 rounded-full text-[10px] bg-violet-500/25">
                  Upgrade Pro
                </span>
              </button>
            </div>
          </>
        ) : (
          <div className="py-8 text-center space-y-2">
            <p className="font-display font-bold text-sm">
              Chưa chọn điểm cần chú ý
            </p>
            <p className="text-xs text-[var(--text-muted)]">
              Nhấn vào bất kỳ cụm từ được gạch chân trong vùng bản thảo để xem nguyên nhân và đề xuất biên tập.
            </p>
          </div>
        )}
      </div>
    </aside>
  );
};
