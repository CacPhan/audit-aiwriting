import React from 'react';
import { AuditedSection, AuditFlag } from '../types/auditor';

export type FindingFilterType =
  | 'all'
  | 'critical'
  | 'warning'
  | 'suggestion'
  | 'resolved';

interface ChapterSidebarProps {
  sections: AuditedSection[];
  findings: AuditFlag[];
  activeSectionId: string;
  onSelectSection: (sectionId: string) => void;
  activeFilter: FindingFilterType;
  onSelectFilter: (filter: FindingFilterType) => void;
  collapsed: boolean;
}

export const ChapterSidebar: React.FC<ChapterSidebarProps> = ({
  sections,
  findings,
  activeSectionId,
  onSelectSection,
  activeFilter,
  onSelectFilter,
  collapsed,
}) => {
  const resolvedCount = findings.filter((f) => f.status !== 'pending').length;
  const criticalCount = findings.filter(
    (f) => f.severity === 'critical' && f.status === 'pending'
  ).length;
  const warningCount = findings.filter(
    (f) => f.severity === 'warning' && f.status === 'pending'
  ).length;
  const suggestionCount = findings.filter(
    (f) => f.severity === 'suggestion' && f.status === 'pending'
  ).length;

  return (
    <aside
      id="workspace-col-left"
      className={`lg:col-span-3 space-y-4 ${collapsed ? 'lg:hidden' : ''}`}
    >
      {/* Document Chapters */}
      <div className="proximity-card rounded-2xl p-4 space-y-3">
        <div className="flex items-center justify-between">
          <h2 className="font-display font-bold text-xs uppercase tracking-wider text-[var(--text-muted)]">
            Cấu trúc tài liệu
          </h2>
          <span
            id="workspace-progress-badge"
            className="text-[11px] font-mono text-emerald-400"
          >
            Đã xử lý {resolvedCount}/{findings.length}
          </span>
        </div>

        <div id="chapter-list" className="space-y-1.5 text-xs">
          {sections.map((sec) => {
            const secFindings = findings.filter((f) => f.sectionId === sec.id);
            const unresolvedCount = secFindings.filter(
              (f) => f.status === 'pending'
            ).length;
            const isCurrent = sec.id === activeSectionId;

            return (
              <button
                key={sec.id}
                type="button"
                onClick={() => onSelectSection(sec.id)}
                className={
                  isCurrent
                    ? 'w-full flex items-center justify-between px-3 py-2.5 rounded-xl bg-blue-600/15 border border-blue-500/40 text-left font-semibold transition-all'
                    : 'w-full flex items-center justify-between px-3 py-2.5 rounded-xl hover:bg-[var(--bg-base)]/60 border border-transparent text-left transition-all'
                }
              >
                <span className="truncate pr-2">{sec.shortTitle}</span>
                {sec.isExcluded ? (
                  <span className="px-2 py-0.5 rounded-full text-[10px] font-mono bg-slate-500/20 text-slate-400 shrink-0">
                    Bỏ qua
                  </span>
                ) : unresolvedCount === 0 ? (
                  <span className="px-2 py-0.5 rounded-full text-[10px] font-mono bg-emerald-500/20 text-emerald-400 shrink-0">
                    Hoàn tất
                  </span>
                ) : (
                  <span className="px-2 py-0.5 rounded-full text-[10px] font-mono bg-amber-500/20 text-amber-400 shrink-0">
                    {unresolvedCount} điểm
                  </span>
                )}
              </button>
            );
          })}
        </div>
      </div>

      {/* Severity & Resolution Status Filter */}
      <div className="proximity-card rounded-2xl p-4 space-y-3">
        <h2 className="font-display font-bold text-xs uppercase tracking-wider text-[var(--text-muted)]">
          Bộ lọc điểm cần chú ý
        </h2>
        <div
          className="flex flex-col gap-1.5 text-xs"
          role="group"
          aria-label="Bộ lọc mức độ ưu tiên"
        >
          <button
            type="button"
            onClick={() => onSelectFilter('all')}
            className={
              activeFilter === 'all'
                ? 'filter-btn active flex items-center justify-between px-3 py-2 rounded-xl font-semibold bg-blue-600 text-white transition-all'
                : 'filter-btn flex items-center justify-between px-3 py-2 rounded-xl border border-transparent hover:bg-[var(--bg-base)]/60 text-left transition-all'
            }
          >
            <span>Tất cả phát hiện</span>
            <span className="font-mono text-[11px]">{findings.length}</span>
          </button>

          <button
            type="button"
            onClick={() => onSelectFilter('critical')}
            className={
              activeFilter === 'critical'
                ? 'filter-btn active flex items-center justify-between px-3 py-2 rounded-xl font-semibold bg-blue-600 text-white transition-all'
                : 'filter-btn flex items-center justify-between px-3 py-2 rounded-xl border border-transparent hover:bg-[var(--bg-base)]/60 text-left transition-all'
            }
          >
            <span className="inline-flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-red-500" />
              <span>Cần sửa ngay</span>
            </span>
            <span className="font-mono text-[11px] text-red-400">
              {criticalCount}
            </span>
          </button>

          <button
            type="button"
            onClick={() => onSelectFilter('warning')}
            className={
              activeFilter === 'warning'
                ? 'filter-btn active flex items-center justify-between px-3 py-2 rounded-xl font-semibold bg-blue-600 text-white transition-all'
                : 'filter-btn flex items-center justify-between px-3 py-2 rounded-xl border border-transparent hover:bg-[var(--bg-base)]/60 text-left transition-all'
            }
          >
            <span className="inline-flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-orange-500" />
              <span>Nên sửa</span>
            </span>
            <span className="font-mono text-[11px] text-orange-400">
              {warningCount}
            </span>
          </button>

          <button
            type="button"
            onClick={() => onSelectFilter('suggestion')}
            className={
              activeFilter === 'suggestion'
                ? 'filter-btn active flex items-center justify-between px-3 py-2 rounded-xl font-semibold bg-blue-600 text-white transition-all'
                : 'filter-btn flex items-center justify-between px-3 py-2 rounded-xl border border-transparent hover:bg-[var(--bg-base)]/60 text-left transition-all'
            }
          >
            <span className="inline-flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-indigo-400" />
              <span>Gợi ý</span>
            </span>
            <span className="font-mono text-[11px] text-indigo-400">
              {suggestionCount}
            </span>
          </button>

          <button
            type="button"
            onClick={() => onSelectFilter('resolved')}
            className={
              activeFilter === 'resolved'
                ? 'filter-btn active flex items-center justify-between px-3 py-2 rounded-xl font-semibold bg-blue-600 text-white transition-all'
                : 'filter-btn flex items-center justify-between px-3 py-2 rounded-xl border border-transparent hover:bg-[var(--bg-base)]/60 text-left transition-all'
            }
          >
            <span className="inline-flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-emerald-400" />
              <span>Đã xử lý</span>
            </span>
            <span className="font-mono text-[11px] text-emerald-400">
              {resolvedCount}
            </span>
          </button>
        </div>
      </div>
    </aside>
  );
};
