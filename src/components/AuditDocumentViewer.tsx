import React, { useEffect, useRef } from 'react';
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

function getSeverityRank(severity: string): number {
  if (severity === 'critical') return 3;
  if (severity === 'warning') return 2;
  return 1;
}

function getSeverityClass(severity: string): string {
  if (severity === 'critical') return 'span-critical';
  if (severity === 'warning') return 'span-warning';
  return 'span-suggestion';
}

/**
 * Interval-splitting renderer that handles both disjoint and nested/overlapping flags
 * (e.g., a narrow lexical/connective flag inside a whole-paragraph RHY-01 or DIS-01 flag).
 * Narrower / more specific spans take visual & click priority on their sub-interval,
 * while clicking a multi-flag segment cycles through the covering flags!
 */
function renderParagraphWithHighlights(
  para: AuditedParagraph,
  allFindings: AuditFlag[],
  activeFindingId: string,
  activeFilter: FindingFilterType,
  onSelectFinding: (id: string) => void
): React.ReactNode {
  const text = para.text || '';
  if (!text) return text;

  const paraFlags = (para.flags || [])
    .map((f) => allFindings.find((af) => af.id === f.id) || f)
    .filter(
      (f) =>
        typeof f.start === 'number' &&
        typeof f.end === 'number' &&
        f.end > f.start
    );

  if (paraFlags.length === 0) {
    return text;
  }

  // Collect all unique boundary points across all flags in this paragraph
  const boundariesSet = new Set<number>([0, text.length]);
  paraFlags.forEach((f) => {
    const s = Math.max(0, Math.min(f.start, text.length));
    const e = Math.max(s, Math.min(f.end, text.length));
    boundariesSet.add(s);
    boundariesSet.add(e);
  });

  const boundaries = Array.from(boundariesSet).sort((a, b) => a - b);
  const nodes: React.ReactNode[] = [];

  for (let i = 0; i < boundaries.length - 1; i++) {
    const segStart = boundaries[i];
    const segEnd = boundaries[i + 1];
    if (segEnd <= segStart) continue;

    const covering = paraFlags.filter((f) => {
      const s = Math.max(0, Math.min(f.start, text.length));
      const e = Math.max(s, Math.min(f.end, text.length));
      return s <= segStart && e >= segEnd;
    });

    if (covering.length === 0) {
      nodes.push(
        <React.Fragment key={`txt-${segStart}-${segEnd}`}>
          {text.slice(segStart, segEnd)}
        </React.Fragment>
      );
      continue;
    }

    // Sort covering flags so narrowest (most specific phrase/clause) comes first,
    // then higher severity, then earlier start
    const sortedCovering = [...covering].sort((a, b) => {
      const lenA = a.end - a.start;
      const lenB = b.end - b.start;
      if (lenA !== lenB) return lenA - lenB;
      const rankDiff = getSeverityRank(b.severity) - getSeverityRank(a.severity);
      if (rankDiff !== 0) return rankDiff;
      return a.start - b.start;
    });

    const primaryFlag = sortedCovering[0];
    const isAnyCoveringActive = sortedCovering.some(
      (f) => f.id === activeFindingId
    );
    const displayFlag =
      sortedCovering.find((f) => f.id === activeFindingId) || primaryFlag;

    const isResolved = displayFlag.status !== 'pending';
    const matchesFilter =
      activeFilter === 'all' ||
      (activeFilter === 'resolved' && isResolved) ||
      (activeFilter === displayFlag.severity && !isResolved);

    let cls = `audit-span ${getSeverityClass(displayFlag.severity)}`;
    if (isResolved) cls += ' is-resolved';
    if (isAnyCoveringActive) cls += ' active-span';

    const handleSpanClick = () => {
      if (sortedCovering.length > 1 && isAnyCoveringActive) {
        const curIdx = sortedCovering.findIndex(
          (f) => f.id === activeFindingId
        );
        const nextFlag =
          sortedCovering[(curIdx + 1) % sortedCovering.length] || primaryFlag;
        onSelectFinding(nextFlag.id);
      } else {
        onSelectFinding(primaryFlag.id);
      }
    };

    nodes.push(
      <span
        key={`seg-${segStart}-${segEnd}-${displayFlag.id}`}
        data-finding-id={displayFlag.id}
        data-covering-ids={sortedCovering.map((f) => f.id).join(',')}
        className={cls}
        style={{ opacity: matchesFilter ? 1 : 0.25 }}
        tabIndex={0}
        role="button"
        aria-label={`${displayFlag.severityLabel}: ${displayFlag.title}`}
        onClick={handleSpanClick}
        onKeyDown={(e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            handleSpanClick();
          }
        }}
      >
        {text.slice(segStart, segEnd)}
      </span>
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
  const articleRef = useRef<HTMLElement>(null);

  // Filter findings according to activeFilter so the stepper counter matches what the user is filtering
  const filteredGlobalFindings = allFindings.filter((f) => {
    const isResolved = f.status !== 'pending';
    if (activeFilter === 'all') return true;
    if (activeFilter === 'resolved') return isResolved;
    return f.severity === activeFilter && !isResolved;
  });

  const activeList =
    filteredGlobalFindings.length > 0 ? filteredGlobalFindings : allFindings;

  const currentGlobalIdx = Math.max(
    0,
    activeList.findIndex((f) => f.id === activeFindingId)
  );
  const totalGlobalCount = activeList.length;

  // Section-local findings count for clear orientation
  const sectionFindings = activeList.filter((f) => f.sectionId === section.id);
  const currentSecIdx = sectionFindings.findIndex(
    (f) => f.id === activeFindingId
  );

  // Auto-scroll the manuscript container when activeFindingId changes
  useEffect(() => {
    if (!activeFindingId || !articleRef.current) return;
    const container = articleRef.current;
    const targetSpan = container.querySelector<HTMLElement>(
      `[data-covering-ids*="${activeFindingId}"]`
    );
    if (targetSpan && typeof targetSpan.scrollIntoView === 'function') {
      targetSpan.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  }, [activeFindingId, section.id]);

  return (
    <section
      id="workspace-col-center"
      className={`${colSpanClass} lg:h-full lg:max-h-full lg:overflow-hidden flex flex-col proximity-card rounded-3xl px-5 sm:px-7 py-4 bg-[var(--manuscript-bg)]`}
    >
      {/* Compact Viewer Top Bar */}
      <div className="shrink-0 flex flex-wrap items-center justify-between gap-2.5 pb-3 border-b border-[var(--border-subtle)]">
        <div className="min-w-0 flex-1">
          <div className="flex items-center gap-2">
            <span
              id="viewer-section-label"
              className="text-[11px] font-mono uppercase tracking-wider text-blue-400"
            >
              {section.sectionLabel}
            </span>
            {sectionFindings.length > 0 && (
              <span className="px-2 py-0.5 rounded-full text-[10px] font-mono font-semibold bg-blue-500/15 text-blue-300 border border-blue-500/30">
                Mục này:{' '}
                {currentSecIdx >= 0
                  ? `${currentSecIdx + 1}/${sectionFindings.length}`
                  : `${sectionFindings.length} điểm`}
              </span>
            )}
          </div>
          <h2
            id="viewer-chapter-heading"
            className="font-display font-bold text-sm sm:text-base mt-0.5 truncate"
            title={section.title}
          >
            {section.title}
          </h2>
        </div>

        {/* Prev/Next Finding Stepper + Font Scale Toggle */}
        <div className="flex items-center gap-1.5 shrink-0">
          <button
            type="button"
            onClick={() => onStepFinding(-1)}
            disabled={totalGlobalCount === 0}
            className="px-2.5 py-1.5 rounded-lg text-xs font-semibold border border-[var(--border-subtle)] bg-[var(--bg-card)] hover:border-blue-400/40 disabled:opacity-40"
            title="Điểm cần chú ý trước"
          >
            ← Trước
          </button>
          <span
            id="finding-stepper-label"
            className="px-2 text-xs font-mono text-[var(--text-muted)] whitespace-nowrap"
            title="Thứ tự điểm cần chú ý trên toàn tài liệu"
          >
            {totalGlobalCount > 0
              ? `${currentGlobalIdx + 1} / ${totalGlobalCount}`
              : '0 / 0'}
          </span>
          <button
            type="button"
            onClick={() => onStepFinding(1)}
            disabled={totalGlobalCount === 0}
            className="px-2.5 py-1.5 rounded-lg text-xs font-semibold border border-[var(--border-subtle)] bg-[var(--bg-card)] hover:border-blue-400/40 disabled:opacity-40"
            title="Điểm cần chú ý tiếp theo"
          >
            Tiếp →
          </button>
          <button
            type="button"
            onClick={onToggleFontSize}
            id="font-size-btn"
            className="ml-0.5 px-2.5 py-1.5 rounded-lg text-xs font-mono border border-[var(--border-subtle)] bg-[var(--bg-card)] hover:border-blue-400/40"
            title="Đổi cỡ chữ vùng đọc"
          >
            Aa
          </button>
        </div>
      </div>

      {/* Expanded Manuscript Scrollable Content Container */}
      <article
        ref={articleRef}
        id="manuscript-content"
        style={{ fontSize: largeFont ? '17px' : '15.5px' }}
        className="flex-1 min-h-0 overflow-y-auto overscroll-contain workspace-scroll-area py-3.5 pr-2 space-y-4 leading-[1.88] text-[var(--text-main)]"
      >
        {section.parentHeading && (
          <div className="pb-2 border-b border-dashed border-[var(--border-subtle)]">
            <p className="text-xs font-display font-bold uppercase tracking-wide text-blue-400">
              {section.parentHeading}
            </p>
          </div>
        )}
        {section.isExcluded && (
          <div className="p-4 rounded-2xl bg-slate-500/10 border border-[var(--border-subtle)] text-xs text-[var(--text-muted)]">
            Phần này ({section.title}) thuộc nhóm Mục lục hoặc Danh mục Tài liệu tham khảo nên được tự động loại trừ khỏi quá trình kiểm toán văn phong.
          </div>
        )}
        {section.paragraphs.map((para) => (
          <div key={para.index} className="space-y-1.5">
            {para.prefix && (
              <p className="text-xs font-mono font-semibold text-blue-400/90">
                {para.prefix}
              </p>
            )}
            <p className="text-justify">
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

      {/* Compact Accessible Underline Legend */}
      <div className="shrink-0 pt-2.5 border-t border-[var(--border-subtle)] flex flex-wrap items-center gap-4 text-[11px] text-[var(--text-muted)]">
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
