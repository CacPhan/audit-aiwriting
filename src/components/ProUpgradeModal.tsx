import React, { useMemo, useState } from 'react';
import {
  AuditedParagraph,
  AuditFlag,
  DocumentAuditResult,
} from '../types/auditor';
import {
  downloadJsonAuditReport,
  downloadStandaloneHtmlReport,
  downloadTurnitinStyleHtmlReport,
  getTurnitinColorTheme,
  printAuditDocument,
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

export type ReportPreviewTab = 'summary' | 'turnitin';

interface ReportPreviewModalProps {
  isOpen: boolean;
  onClose: () => void;
  audit: DocumentAuditResult;
  initialTab?: ReportPreviewTab;
}

function getSeverityBadgeStyle(severity: string): string {
  if (severity === 'critical')
    return 'bg-red-500/20 text-red-400 border border-red-500/35';
  if (severity === 'warning')
    return 'bg-orange-500/20 text-orange-400 border border-orange-500/35';
  return 'bg-indigo-500/20 text-indigo-300 border border-indigo-500/35';
}

function renderTurnitinParagraphNodes(
  para: AuditedParagraph,
  findingNumberMap: Map<string, number>,
  allFindingsMap: Map<string, AuditFlag>,
  activeBadgeNum: number | null,
  onSelectBadge: (num: number) => void
): React.ReactNode {
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
    return text;
  }

  const nodes: React.ReactNode[] = [];
  let cursor = 0;

  paraFlags.forEach((flag, idx) => {
    const start = Math.max(cursor, Math.min(flag.start, text.length));
    const end = Math.max(start, Math.min(flag.end, text.length));

    if (start > cursor) {
      nodes.push(
        <React.Fragment key={`t-txt-${idx}`}>
          {text.slice(cursor, start)}
        </React.Fragment>
      );
    }

    if (end > start) {
      const badgeNum = findingNumberMap.get(flag.id) || 1;
      const theme = getTurnitinColorTheme(flag.severity, badgeNum);
      const isSelected = activeBadgeNum === badgeNum;

      nodes.push(
        <span
          key={`t-hl-${flag.id}-${idx}`}
          className="turnitin-hl"
          style={{
            backgroundColor: theme.bg,
            borderBottom: `2px solid ${theme.border}`,
            color: theme.text,
            outline: isSelected ? `2px solid ${theme.badgeBg}` : 'none',
            outlineOffset: '1px',
          }}
          title={`[#${badgeNum} - ${flag.severityLabel}] ${flag.title}`}
          onClick={() => onSelectBadge(badgeNum)}
          role="button"
          tabIndex={0}
          onKeyDown={(e) => {
            if (e.key === 'Enter' || e.key === ' ') {
              e.preventDefault();
              onSelectBadge(badgeNum);
            }
          }}
        >
          <sup
            className="turnitin-badge"
            style={{ backgroundColor: theme.badgeBg }}
          >
            {badgeNum}
          </sup>
          {text.slice(start, end)}
        </span>
      );
      cursor = end;
    }
  });

  if (cursor < text.length) {
    nodes.push(
      <React.Fragment key="t-tail">{text.slice(cursor)}</React.Fragment>
    );
  }

  return nodes;
}

export const ReportPreviewModal: React.FC<ReportPreviewModalProps> = ({
  isOpen,
  onClose,
  audit,
  initialTab = 'summary',
}) => {
  const [activeTab, setActiveTab] = useState<ReportPreviewTab>(initialTab);
  const [selectedBadgeNum, setSelectedBadgeNum] = useState<number | null>(1);

  React.useEffect(() => {
    if (isOpen) {
      setActiveTab(initialTab);
    }
  }, [isOpen, initialTab]);

  const { findingNumberMap, allFindingsMap } = useMemo(() => {
    const numMap = new Map<string, number>();
    const flagMap = new Map<string, AuditFlag>();
    audit.findings.forEach((f, idx) => {
      numMap.set(f.id, idx + 1);
      flagMap.set(f.id, f);
    });
    return { findingNumberMap: numMap, allFindingsMap: flagMap };
  }, [audit.findings]);

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

  const handleSelectBadge = (num: number) => {
    setSelectedBadgeNum(num);
    if (typeof document !== 'undefined') {
      const noteEl = document.getElementById(`modal-turnitin-note-${num}`);
      if (noteEl && typeof noteEl.scrollIntoView === 'function') {
        noteEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }
  };

  return (
    <div
      id="report-modal"
      className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-black/75 backdrop-blur-md"
      role="dialog"
      aria-modal="true"
      aria-labelledby="report-modal-title"
    >
      <div className="proximity-card max-w-6xl w-full max-h-[92vh] flex flex-col rounded-3xl border border-cyan-500/40 overflow-hidden">
        {/* Modal Header */}
        <div className="p-4 sm:p-5 border-b border-[var(--border-subtle)] flex flex-wrap items-center justify-between gap-4 bg-[var(--bg-elevated)]">
          <div>
            <div className="flex flex-wrap items-center gap-2">
              {audit.isDemo ? (
                <span className="px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-amber-500/15 text-amber-400 border border-amber-500/30">
                  DEMO PREVIEW – Kết quả minh họa
                </span>
              ) : (
                <span className="px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-emerald-500/15 text-emerald-400 border border-emerald-500/30">
                  BÁO CÁO KIỂM TOÁN THỰC TẾ
                </span>
              )}
              <span className="text-xs text-[var(--text-muted)]">
                · {audit.summary?.totalWords ?? 0} từ · {audit.findings.length}{' '}
                đánh dấu
              </span>
            </div>
            <h2
              id="report-modal-title"
              className="font-display font-extrabold text-lg sm:text-xl mt-1.5"
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

          {/* Mode Switcher Tabs: Summary vs Turnitin Feedback Studio */}
          <div className="flex items-center gap-2">
            <div
              className="inline-flex p-1 rounded-2xl bg-[var(--bg-base)] border border-[var(--border-subtle)] text-xs"
              role="tablist"
              aria-label="Chế độ xem báo cáo"
            >
              <button
                type="button"
                role="tab"
                aria-selected={activeTab === 'summary'}
                onClick={() => setActiveTab('summary')}
                className={
                  activeTab === 'summary'
                    ? 'px-3.5 py-1.5 rounded-xl font-bold bg-blue-600 text-white shadow-sm transition-all'
                    : 'px-3.5 py-1.5 rounded-xl font-medium text-[var(--text-muted)] hover:text-[var(--text-main)] transition-all'
                }
              >
                Danh sách Chẩn đoán
              </button>
              <button
                type="button"
                role="tab"
                id="tab-turnitin-studio"
                aria-selected={activeTab === 'turnitin'}
                onClick={() => setActiveTab('turnitin')}
                className={
                  activeTab === 'turnitin'
                    ? 'px-3.5 py-1.5 rounded-xl font-bold bg-gradient-to-r from-cyan-600 to-blue-600 text-white shadow-sm transition-all'
                    : 'px-3.5 py-1.5 rounded-xl font-medium text-[var(--text-muted)] hover:text-[var(--text-main)] transition-all'
                }
              >
                Bản thảo Bôi màu (Feedback Studio)
              </button>
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
        </div>

        {/* Modal Scrollable Report Body */}
        {activeTab === 'summary' ? (
          <div className="flex-1 min-h-0 p-5 sm:p-6 overflow-y-auto workspace-scroll-area space-y-5 text-xs sm:text-sm">
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
                <div className="text-[11px] text-[var(--text-muted)]">
                  Gợi ý
                </div>
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
        ) : (
          /* TURNITIN FEEDBACK STUDIO FULL-MANUSCRIPT VIEW */
          <div
            id="turnitin-studio-preview"
            className="flex-1 min-h-0 grid lg:grid-cols-12 overflow-hidden bg-slate-100 text-slate-900"
          >
            {/* Left/Center: Full Thesis A4 Paper with Colored Inline Highlights & Numbered Badges */}
            <div className="lg:col-span-8 h-full overflow-y-auto workspace-scroll-area p-4 sm:p-6">
              {/* Feedback Studio Top Banner */}
              <div className="mb-4 px-4 py-2.5 rounded-xl bg-white border-b-2 border-sky-600 shadow-sm flex flex-wrap items-center justify-between gap-2 text-xs">
                <div className="flex items-center gap-2">
                  <span className="font-display font-extrabold text-sky-700 tracking-tight text-sm">
                    feedback studio
                  </span>
                  <span className="text-slate-300">|</span>
                  <span className="font-semibold text-slate-700 truncate max-w-[260px]">
                    {audit.title}
                  </span>
                </div>
                <div className="flex items-center gap-2 text-[11px]">
                  <span className="px-2 py-0.5 rounded bg-red-50 text-red-700 border border-red-200 font-semibold">
                    Cần sửa ngay: {criticalCount}
                  </span>
                  <span className="px-2 py-0.5 rounded bg-orange-50 text-orange-700 border border-orange-200 font-semibold">
                    Nên sửa: {warningCount}
                  </span>
                  <span className="px-2 py-0.5 rounded bg-indigo-50 text-indigo-700 border border-indigo-200 font-semibold">
                    Gợi ý: {suggestionCount}
                  </span>
                </div>
              </div>

              {/* A4 Academic Manuscript Sheet */}
              <div
                className="bg-white border border-slate-300 rounded shadow-md px-6 sm:px-12 py-8 sm:py-10 space-y-7 text-slate-900"
                style={{
                  fontFamily:
                    '"Times New Roman", "Noto Serif", Georgia, Cambria, serif',
                  fontSize: '16.5px',
                  lineHeight: 1.92,
                }}
              >
                {audit.sections.map((sec) => (
                  <section
                    key={sec.id}
                    className="space-y-3.5 pb-5 border-b border-dashed border-slate-200 last:border-none"
                  >
                    <div className="flex items-center justify-between gap-2">
                      <h3 className="font-bold text-base sm:text-lg uppercase text-slate-900">
                        {sec.title}
                      </h3>
                      <span
                        className="text-[11px] font-sans font-semibold px-2.5 py-0.5 rounded-full bg-slate-100 text-slate-600 shrink-0"
                        style={{ fontFamily: 'Plus Jakarta Sans, sans-serif' }}
                      >
                        {sec.isExcluded
                          ? 'Mục tự động loại trừ'
                          : `${
                              audit.findings.filter(
                                (f) => f.sectionId === sec.id
                              ).length
                            } vị trí`}
                      </span>
                    </div>

                    {sec.paragraphs.map((para) => (
                      <p
                        key={para.index}
                        className="text-justify"
                        style={{ textIndent: '26px' }}
                      >
                        {renderTurnitinParagraphNodes(
                          para,
                          findingNumberMap,
                          allFindingsMap,
                          selectedBadgeNum,
                          handleSelectBadge
                        )}
                      </p>
                    ))}
                  </section>
                ))}
              </div>
            </div>

            {/* Right Column: Turnitin Feedback Studio Numbered Margin Cards */}
            <aside className="lg:col-span-4 h-full overflow-y-auto workspace-scroll-area bg-white border-l border-slate-300 p-4 space-y-3">
              <div className="sticky top-0 z-10 bg-white pb-2 border-b border-slate-200 flex items-center justify-between">
                <h3 className="font-display font-bold text-xs uppercase tracking-wider text-slate-700">
                  Danh mục Chú giải ({audit.findings.length})
                </h3>
                <span className="text-[11px] text-slate-500">
                  Nhấn số trên bài để đối chiếu
                </span>
              </div>

              {audit.findings.map((f, idx) => {
                const num = idx + 1;
                const theme = getTurnitinColorTheme(f.severity, num);
                const isSelected = selectedBadgeNum === num;
                const secObj = audit.sections.find((s) => s.id === f.sectionId);

                return (
                  <div
                    key={f.id}
                    id={`modal-turnitin-note-${num}`}
                    onClick={() => setSelectedBadgeNum(num)}
                    className={`p-3 rounded-xl border transition-all cursor-pointer space-y-1.5 text-xs ${
                      isSelected
                        ? 'bg-sky-50/70 border-sky-500 shadow-sm'
                        : 'bg-white border-slate-200 hover:border-slate-300'
                    }`}
                    style={{ borderLeft: `4px solid ${theme.badgeBg}` }}
                  >
                    <div className="flex items-center justify-between gap-2">
                      <div className="flex items-center gap-2 min-w-0">
                        <span
                          className="inline-flex items-center justify-center min-w-[22px] h-5 px-1.5 rounded text-[11px] font-extrabold text-white shrink-0"
                          style={{ backgroundColor: theme.badgeBg }}
                        >
                          {num}
                        </span>
                        <span className="font-bold text-slate-900 truncate">
                          {f.title}
                        </span>
                      </div>
                      <span
                        className="px-2 py-0.5 rounded-full text-[10px] font-bold shrink-0"
                        style={{
                          backgroundColor: theme.bg,
                          color: theme.text,
                          border: `1px solid ${theme.border}`,
                        }}
                      >
                        {f.severityLabel}
                      </span>
                    </div>

                    {secObj && (
                      <div className="text-[11px] text-slate-500">
                        Phần: <strong>{secObj.shortTitle}</strong>
                      </div>
                    )}

                    <p className="italic text-slate-600 bg-slate-50 p-2 rounded border border-slate-200/80">
                      {f.excerpt}
                    </p>
                    <p className="text-slate-700">
                      <strong>Nhận xét:</strong> {f.reason}
                    </p>
                    <p className="text-emerald-800 bg-emerald-50 border border-emerald-200 p-2 rounded font-medium">
                      <strong>Gợi ý sửa:</strong> {f.suggestion}
                    </p>
                  </div>
                );
              })}
            </aside>
          </div>
        )}

        {/* Modal Footer with Complete Export Actions */}
        <div className="p-4 sm:p-5 border-t border-[var(--border-subtle)] flex flex-wrap items-center justify-between gap-3 bg-[var(--bg-elevated)]">
          <div className="flex flex-wrap items-center gap-2">
            <button
              type="button"
              onClick={() => downloadTurnitinStyleHtmlReport(audit)}
              className="px-3.5 py-2 rounded-xl text-xs font-bold text-white bg-gradient-to-r from-cyan-600 to-blue-600 hover:opacity-95 shadow-sm transition-all"
            >
              Tải Bản thảo Bôi màu (Turnitin HTML)
            </button>
            <button
              type="button"
              onClick={() => printAuditDocument(audit, 'turnitin')}
              className="px-3.5 py-2 rounded-xl text-xs font-semibold border border-cyan-500/40 bg-cyan-500/10 text-cyan-300 hover:bg-cyan-500/20 transition-all"
            >
              In / Lưu PDF Bản thảo Bôi màu
            </button>
            <button
              type="button"
              onClick={() => downloadStandaloneHtmlReport(audit)}
              className="px-3.5 py-2 rounded-xl text-xs font-semibold border border-[var(--border-subtle)] bg-[var(--bg-card)] hover:border-blue-400/50 transition-all"
            >
              Tải Báo cáo HTML
            </button>
            <button
              type="button"
              onClick={() => printAuditDocument(audit, 'summary')}
              className="px-3.5 py-2 rounded-xl text-xs font-semibold border border-[var(--border-subtle)] bg-[var(--bg-card)] hover:border-blue-400/50 transition-all"
            >
              In / Lưu PDF Báo cáo
            </button>
            <button
              type="button"
              onClick={() => downloadJsonAuditReport(audit)}
              className="px-3.5 py-2 rounded-xl text-xs font-semibold border border-[var(--border-subtle)] bg-[var(--bg-card)] hover:border-blue-400/50 transition-all"
            >
              Tải JSON
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
