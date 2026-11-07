import React from 'react';
import { AuditedParagraph, AuditedSection, AuditFlag } from '../types/auditor';
import { FindingFilterType } from './ChapterSidebar';

interface AuditDocumentViewerProps {
  section: AuditedSection;
  allFindings: AuditFlag[];
  activeFindingId: string;
  onSelectFinding: (findingId: string) => void;
  onStepFinding: (delta: number) => void;
  activeFilter: FindingFilterType;
  largeFont: boolean;
  onToggleFontSize: () => void;
  colSpanClass: string;
}

function getSeverityClass(severity: string): string {
  if (severity === 'critical') return 'span-critical';
  if (severity === 'warning') return 'span-warning';
  return 'span-suggestion';
}

function renderParagraphWithHighlights(
  para: AuditedParagraph,
  allFindings: AuditFlag[],
  activeFindingId: string,
  activeFilter: FindingFilterType,
  onSelectFinding: (id: string) => void
): React.ReactNode {
  const text = para.text || '';
  const paraFlags = (para.flags || [])
    .map((f) => allFindings.find((af) => af.id === f.id) || f)
    .filter((f) => typeof f.start === 'number' && typeof f.end === 'number' && f.end > f.start)
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
        <React.Fragment key={`txt-${idx}`}>
          {text.slice(cursor, start)}
        </React.Fragment>
      );
    }

    if (end > start) {
      const isResolved = flag.status !== 'pending';
      const matchesFilter =
        activeFilter === 'all' ||
        (activeFilter === 'resolved' && isResolved) ||
        (activeFilter === flag.severity && !isResolved);

      let cls = `audit-span ${getSeverityClass(flag.severity)}`;
      if (isResolved) cls += ' is-resolved';
      if (activeFindingId === flag.id) cls += ' active-span';

      nodes.push(
        <span
          key={flag.id}
          className={cls}
          style={{ opacity: matchesFilter ? 1 : 0.25 }}
          tabIndex={0}
          role="button"
          aria-label={`${flag.severityLabel}: ${flag.title}`}
          onClick={() => onSelectFinding(flag.id)}
          onKeyDown={(e) => {
            if (e.key === 'Enter' || e.key === ' ') {
              e.preventDefault();
              onSelectFinding(flag.id);
            }
          }}
        >
          {text.slice(start, end)}
        </span>
      );
      cursor = end;
    }
  });

  if (cursor < text.length) {
    nodes.push(
      <React.Fragment key="txt-tail">{text.slice(cursor)}</React.Fragment>
    );
  }

  return nodes;
}

export const AuditDocumentViewer: React.FC<AuditDocumentViewerProps> = ({
  section,
  allFindings,
  activeFindingId,
  onSelectFinding,
  onStepFinding,
  activeFilter,
  largeFont,
  onToggleFontSize,
  colSpanClass,
}) => {
  const currentIdx = Math.max(
    0,
    allFindings.findIndex((f) => f.id === activeFindingId)
  );
  const totalCount = allFindings.length;

  return (
    <section
      id="workspace-col-center"
      className={`${colSpanClass} proximity-card rounded-3xl p-6 sm:p-8 bg-[var(--manuscript-bg)] space-y-5`}
    >
      {/* Viewer Top Bar */}
      <div className="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-[var(--border-subtle)]">
        <div>
          <span
            id="viewer-section-label"
            className="text-[11px] font-mono uppercase tracking-wider text-blue-400"
          >
            {section.sectionLabel}
          </span>
          <h2
            id="viewer-chapter-heading"
            className="font-display font-bold text-base sm:text-lg mt-0.5"
          >
            {section.title}
          </h2>
        </div>

        {/* Prev/Next Finding Stepper + Font Scale Toggle */}
        <div className="flex items-center gap-1.5">
          <button
            type="button"
            onClick={() => onStepFinding(-1)}
            disabled={totalCount === 0}
            className="px-2.5 py-1.5 rounded-lg text-xs font-semibold border border-[var(--border-subtle)] bg-[var(--bg-card)] hover:border-blue-400/40 disabled:opacity-40"
            title="Điểm cần chú ý trước"
          >
            ← Trước
          </button>
          <span
            id="finding-stepper-label"
            className="px-2 text-xs font-mono text-[var(--text-muted)]"
          >
            {totalCount > 0 ? `${currentIdx + 1} / ${totalCount}` : '0 / 0'}
          </span>
          <button
            type="button"
            onClick={() => onStepFinding(1)}
            disabled={totalCount === 0}
            className="px-2.5 py-1.5 rounded-lg text-xs font-semibold border border-[var(--border-subtle)] bg-[var(--bg-card)] hover:border-blue-400/40 disabled:opacity-40"
            title="Điểm cần chú ý tiếp theo"
          >
            Tiếp →
          </button>
          <button
            type="button"
            onClick={onToggleFontSize}
            id="font-size-btn"
            className="ml-1 px-2.5 py-1.5 rounded-lg text-xs font-mono border border-[var(--border-subtle)] bg-[var(--bg-card)] hover:border-blue-400/40"
            title="Đổi cỡ chữ vùng đọc"
          >
            Aa
          </button>
        </div>
      </div>

      {/* Manuscript Content Container */}
      <article
        id="manuscript-content"
        style={{ fontSize: largeFont ? '17px' : '15px' }}
        className="space-y-5 leading-[1.88] text-[var(--text-main)] min-h-[360px]"
      >
        {section.isExcluded && (
          <div className="p-4 rounded-2xl bg-slate-500/10 border border-[var(--border-subtle)] text-xs text-[var(--text-muted)]">
            Phần này ({section.title}) thuộc nhóm Mục lục hoặc Danh mục Tài liệu tham khảo nên được tự động loại trừ khỏi quá trình kiểm toán văn phong.
          </div>
        )}
        {section.paragraphs.map((para) => (
          <div key={para.index} className="space-y-2">
            {para.prefix && (
              <p className="text-xs font-mono text-[var(--text-muted)]">
                {para.prefix}
              </p>
            )}
            <p>
              {renderParagraphWithHighlights(
                para,
                allFindings,
                activeFindingId,
                activeFilter,
                onSelectFinding
              )}
            </p>
          </div>
        ))}
      </article>

      {/* Accessible Underline Legend */}
      <div className="pt-4 border-t border-[var(--border-subtle)] flex flex-wrap items-center gap-4 text-xs text-[var(--text-muted)]">
        <span className="inline-flex items-center gap-1.5">
          <span
            className="inline-block w-4 border-b-2 border-red-500"
            style={{
              borderBottomStyle:
                'wavy' as React.CSSProperties['borderBottomStyle'],
            }}
          />
          <span>Cần sửa ngay</span>
        </span>
        <span className="inline-flex items-center gap-1.5">
          <span className="inline-block w-4 border-b-2 border-orange-500" />
          <span>Nên sửa</span>
        </span>
        <span className="inline-flex items-center gap-1.5">
          <span className="inline-block w-4 border-b-2 border-dashed border-indigo-400" />
          <span>Gợi ý</span>
        </span>
        <span className="inline-flex items-center gap-1.5">
          <span className="inline-block w-4 border-b-2 border-dotted border-emerald-400" />
          <span>Đã xử lý</span>
        </span>
      </div>
    </section>
  );
};
