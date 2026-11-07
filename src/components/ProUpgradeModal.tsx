import React from 'react';
import { DocumentAuditResult } from '../types/auditor';
import {
  downloadJsonAuditReport,
  downloadStandaloneHtmlReport,
} from '../utils/reportExporter';

interface ProUpgradeModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export const ProUpgradeModal: React.FC<ProUpgradeModalProps> = ({
  isOpen,
  onClose,
}) => {
  if (!isOpen) return null;

  return (
    <div
      id="pro-modal"
      className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/75 backdrop-blur-md"
      role="dialog"
      aria-modal="true"
      aria-labelledby="pro-modal-title"
    >
      <div className="proximity-card max-w-md w-full rounded-3xl p-6 sm:p-7 border border-violet-500/40 space-y-4">
        <div className="flex items-center justify-between">
          <span className="px-3 py-1 rounded-full text-xs font-semibold bg-violet-500/20 text-violet-300 border border-violet-500/35">
            Upgrade Pro (Coming soon)
          </span>
          <button
            type="button"
            onClick={onClose}
            className="w-8 h-8 rounded-full border border-[var(--border-subtle)] bg-[var(--bg-base)] flex items-center justify-center text-[var(--text-muted)] hover:text-[var(--text-main)]"
            aria-label="Đóng cửa sổ"
          >
            ✕
          </button>
        </div>
        <h2
          id="pro-modal-title"
          className="font-display font-extrabold text-xl"
        >
          Tính năng Nâng cao đang được phát triển
        </h2>
        <p className="text-xs sm:text-sm text-[var(--text-muted)] leading-relaxed">
          Phiên bản Pro với không gian biên tập trực tiếp kèm chấm điểm thời gian thực và xuất tài liệu Microsoft Word (.docx) giữ nguyên định dạng đang trong quá trình hoàn thiện. Hiện tại bạn có thể trải nghiệm đầy đủ luồng duyệt bản thảo, xem đề xuất biên tập và tải báo cáo kiểm toán.
        </p>
        <div className="pt-2 flex justify-end">
          <button
            type="button"
            onClick={onClose}
            className="px-5 py-2.5 rounded-xl text-xs font-semibold border border-[var(--border-subtle)] bg-[var(--bg-elevated)] text-[var(--text-main)]"
          >
            Đã hiểu
          </button>
        </div>
      </div>
    </div>
  );
};

interface ReportPreviewModalProps {
  isOpen: boolean;
  onClose: () => void;
  audit: DocumentAuditResult;
}

function getSeverityBadgeStyle(severity: string): string {
  if (severity === 'critical')
    return 'bg-red-500/20 text-red-400 border border-red-500/35';
  if (severity === 'warning')
    return 'bg-orange-500/20 text-orange-400 border border-orange-500/35';
  return 'bg-indigo-500/20 text-indigo-300 border border-indigo-500/35';
}

export const ReportPreviewModal: React.FC<ReportPreviewModalProps> = ({
  isOpen,
  onClose,
  audit,
}) => {
  if (!isOpen) return null;

  const criticalCount = audit.findings.filter(
    (f) => f.severity === 'critical'
  ).length;
  const warningCount = audit.findings.filter(
    (f) => f.severity === 'warning'
  ).length;
  const suggestionCount = audit.findings.filter(
    (f) => f.severity === 'suggestion'
  ).length;

  return (
    <div
      id="report-modal"
      className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/75 backdrop-blur-md"
      role="dialog"
      aria-modal="true"
      aria-labelledby="report-modal-title"
    >
      <div className="proximity-card max-w-3xl w-full max-h-[88vh] flex flex-col rounded-3xl border border-cyan-500/40 overflow-hidden">
        {/* Modal Header */}
        <div className="p-5 sm:p-6 border-b border-[var(--border-subtle)] flex items-center justify-between gap-4">
          <div>
            {audit.isDemo ? (
              <span className="px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-amber-500/15 text-amber-400 border border-amber-500/30">
                DEMO PREVIEW – Kết quả minh họa
              </span>
            ) : (
              <span className="px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-emerald-500/15 text-emerald-400 border border-emerald-500/30">
                BÁO CÁO KIỂM TOÁN THỰC TẾ
              </span>
            )}
            <h2
              id="report-modal-title"
              className="font-display font-extrabold text-lg sm:text-xl mt-2"
            >
              Báo cáo Kiểm toán Văn phong Học thuật
            </h2>
            <p
              id="report-doc-name"
              className="text-xs text-[var(--text-muted)] mt-0.5"
            >
              Tài liệu: {audit.title}
            </p>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="w-9 h-9 rounded-full border border-[var(--border-subtle)] bg-[var(--bg-base)] flex items-center justify-center text-[var(--text-muted)] hover:text-[var(--text-main)]"
            aria-label="Đóng cửa sổ"
          >
            ✕
          </button>
        </div>

        {/* Modal Scrollable Report Body */}
        <div className="p-5 sm:p-6 overflow-y-auto space-y-5 text-xs sm:text-sm">
          <div className="grid grid-cols-3 gap-3 p-3.5 rounded-2xl bg-[var(--bg-elevated)] border border-[var(--border-subtle)] text-center">
            <div>
              <div className="text-[11px] text-[var(--text-muted)]">
                Cần sửa ngay
              </div>
              <div className="font-display font-bold text-lg text-red-400">
                {criticalCount}
              </div>
            </div>
            <div>
              <div className="text-[11px] text-[var(--text-muted)]">
                Nên sửa
              </div>
              <div className="font-display font-bold text-lg text-orange-400">
                {warningCount}
              </div>
            </div>
            <div>
              <div className="text-[11px] text-[var(--text-muted)]">Gợi ý</div>
              <div className="font-display font-bold text-lg text-indigo-400">
                {suggestionCount}
              </div>
            </div>
          </div>

          <div id="report-findings-list" className="space-y-3">
            {audit.findings.map((f, index) => (
              <div
                key={f.id}
                className="p-4 rounded-2xl border border-[var(--border-subtle)] bg-[var(--bg-card)] space-y-2"
              >
                <div className="flex flex-wrap items-center justify-between gap-2">
                  <span className="font-display font-bold text-sm">
                    {index + 1}. {f.title}
                  </span>
                  <span
                    className={`px-2.5 py-0.5 rounded-full text-[11px] font-semibold ${getSeverityBadgeStyle(
                      f.severity
                    )}`}
                  >
                    {f.severityLabel}
                  </span>
                </div>
                <p className="text-xs italic text-[var(--text-muted)]">
                  {f.excerpt}
                </p>
                <p className="text-xs text-[var(--text-muted)]">
                  <strong>Nguyên nhân:</strong> {f.reason}
                </p>
                <p className="text-xs text-emerald-400">
                  <strong>Đề xuất biên tập:</strong> {f.suggestion}
                </p>
              </div>
            ))}
          </div>
        </div>

        {/* Modal Footer with Export Actions */}
        <div className="p-4 sm:p-5 border-t border-[var(--border-subtle)] flex flex-wrap items-center justify-between gap-3 bg-[var(--bg-elevated)]">
          <div className="flex flex-wrap items-center gap-2">
            <button
              type="button"
              onClick={() => downloadStandaloneHtmlReport(audit)}
              className="px-3.5 py-2 rounded-xl text-xs font-semibold border border-[var(--border-subtle)] bg-[var(--bg-card)] hover:border-blue-400/50 transition-all"
            >
              Tải Báo cáo HTML
            </button>
            <button
              type="button"
              onClick={() => downloadJsonAuditReport(audit)}
              className="px-3.5 py-2 rounded-xl text-xs font-semibold border border-[var(--border-subtle)] bg-[var(--bg-card)] hover:border-blue-400/50 transition-all"
            >
              Tải JSON
            </button>
            <button
              type="button"
              onClick={() => window.print()}
              className="px-3.5 py-2 rounded-xl text-xs font-semibold border border-[var(--border-subtle)] bg-[var(--bg-card)] hover:border-blue-400/50 transition-all"
            >
              In / Lưu PDF
            </button>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="px-5 py-2.5 rounded-xl text-xs font-bold bg-blue-600 text-white hover:bg-blue-500 transition-all"
          >
            Đóng bản xem trước
          </button>
        </div>
      </div>
    </div>
  );
};
