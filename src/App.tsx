import React, { useEffect, useRef, useState } from 'react';
import { DocumentAuditResult } from './types/auditor';
import {
  extractSectionsFromDocx,
  INITIAL_SAMPLE_AUDIT,
} from './utils/docxParser';
import { AppScreen, HeaderBar } from './components/HeaderBar';
import { ChapterSidebar, FindingFilterType } from './components/ChapterSidebar';
import { AuditDocumentViewer } from './components/AuditDocumentViewer';
import { DiagnosticInspector } from './components/DiagnosticInspector';
import {
  ProUpgradeModal,
  ReportPreviewModal,
  ReportPreviewTab,
} from './components/ProUpgradeModal';
import { downloadTurnitinStyleHtmlReport } from './utils/reportExporter';

function formatBytes(bytes: number): string {
  if (!bytes || bytes <= 0) return '1.42 MB';
  const mb = bytes / (1024 * 1024);
  if (mb >= 0.1) return `${mb.toFixed(2)} MB`;
  return `${Math.max(1, Math.round(bytes / 1024))} KB`;
}

export const App: React.FC = () => {
  const [currentScreen, setCurrentScreen] = useState<AppScreen>('home');
  const [theme, setTheme] = useState<'dark' | 'light'>('dark');

  // Audit Document State
  const [auditData, setAuditData] =
    useState<DocumentAuditResult>(INITIAL_SAMPLE_AUDIT);
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [uploadError, setUploadError] = useState<string | null>(null);
  const [isDragging, setIsDragging] = useState(false);
  const [isAuditing, setIsAuditing] = useState(false);
  const [auditProgressText, setAuditProgressText] = useState<string>('');

  // Workspace Navigation & View State
  const [activeSectionId, setActiveSectionId] = useState<string>('sec-1');
  const [activeFindingId, setActiveFindingId] = useState<string>('f2');
  const [activeFilter, setActiveFilter] = useState<FindingFilterType>('all');
  const [largeFont, setLargeFont] = useState(false);
  const [leftColCollapsed, setLeftColCollapsed] = useState(false);
  const [rightColCollapsed, setRightColCollapsed] = useState(false);

  // Modals State
  const [isReportModalOpen, setIsReportModalOpen] = useState(false);
  const [reportInitialTab, setReportInitialTab] =
    useState<ReportPreviewTab>('summary');
  const [isProModalOpen, setIsProModalOpen] = useState(false);

  // Refs for visual effects (Spotlight, Mascot Pupils, File Input)
  const fileInputRef = useRef<HTMLInputElement>(null);
  const spotlightRef = useRef<HTMLDivElement>(null);
  const mascotRef = useRef<SVGSVGElement>(null);
  const pupilLeftRef = useRef<SVGGElement>(null);
  const pupilRightRef = useRef<SVGGElement>(null);
  const [isBlinking, setIsBlinking] = useState(false);

  // Sync theme attribute on <html>
  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
  }, [theme]);

  // Escape key closes modals
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        setIsReportModalOpen(false);
        setIsProModalOpen(false);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  // Periodic mascot blinking & pointermove proximity/magnetic effects
  useEffect(() => {
    const reducedMotion =
      typeof window.matchMedia === 'function' &&
      window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reducedMotion) return;

    const blinkTimer = window.setInterval(() => {
      setIsBlinking(true);
      window.setTimeout(() => setIsBlinking(false), 150);
    }, 4200);

    const handlePointerMove = (e: PointerEvent) => {
      const { clientX, clientY } = e;
      if (spotlightRef.current) {
        spotlightRef.current.style.setProperty('--cursor-x', `${clientX}px`);
        spotlightRef.current.style.setProperty('--cursor-y', `${clientY}px`);
      }

      if (mascotRef.current && pupilLeftRef.current && pupilRightRef.current) {
        const rect = mascotRef.current.getBoundingClientRect();
        const cx = rect.left + rect.width / 2;
        const cy = rect.top + rect.height / 2;
        const angle = Math.atan2(clientY - cy, clientX - cx);
        const dist = Math.min(2.5, Math.hypot(clientX - cx, clientY - cy) / 45);
        const tx = Math.cos(angle) * dist;
        const ty = Math.sin(angle) * dist;
        pupilLeftRef.current.style.transform = `translate(${tx.toFixed(
          2
        )}px, ${ty.toFixed(2)}px)`;
        pupilRightRef.current.style.transform = `translate(${tx.toFixed(
          2
        )}px, ${ty.toFixed(2)}px)`;
      }

      document
        .querySelectorAll<HTMLElement>('.proximity-card')
        .forEach((card) => {
          const rect = card.getBoundingClientRect();
          const x = clientX - rect.left;
          const y = clientY - rect.top;
          const dx = Math.max(rect.left - clientX, 0, clientX - rect.right);
          const dy = Math.max(rect.top - clientY, 0, clientY - rect.bottom);
          const distFromCard = Math.hypot(dx, dy);

          if (distFromCard < 160) {
            const opacity = Math.max(0, 1 - distFromCard / 160);
            card.style.setProperty('--card-mouse-x', `${x}px`);
            card.style.setProperty('--card-mouse-y', `${y}px`);
            card.style.setProperty(
              '--card-proximity-opacity',
              opacity.toFixed(2)
            );
          } else {
            card.style.setProperty('--card-proximity-opacity', '0');
          }
        });

      document
        .querySelectorAll<HTMLElement>('.magnetic-icon')
        .forEach((icon) => {
          const rect = icon.getBoundingClientRect();
          const icx = rect.left + rect.width / 2;
          const icy = rect.top + rect.height / 2;
          const dist = Math.hypot(clientX - icx, clientY - icy);
          const radius = 110;

          if (dist < radius) {
            const pull = 1 - dist / radius;
            const mx = (clientX - icx) * 0.2 * pull;
            const my = (clientY - icy) * 0.2 * pull;
            const scale = 1 + 0.06 * pull;
            icon.style.setProperty('--mag-x', `${mx.toFixed(1)}px`);
            icon.style.setProperty('--mag-y', `${my.toFixed(1)}px`);
            icon.style.setProperty('--mag-scale', scale.toFixed(3));
            icon.style.setProperty('--mag-glow', (pull * 0.5).toFixed(2));
          } else {
            icon.style.setProperty('--mag-x', '0px');
            icon.style.setProperty('--mag-y', '0px');
            icon.style.setProperty('--mag-scale', '1');
            icon.style.setProperty('--mag-glow', '0');
          }
        });
    };

    window.addEventListener('pointermove', handlePointerMove);
    return () => {
      window.clearInterval(blinkTimer);
      window.removeEventListener('pointermove', handlePointerMove);
    };
  }, []);

  const navigateToScreen = (screen: AppScreen) => {
    setCurrentScreen(screen);
    if (
      typeof window !== 'undefined' &&
      typeof window.scrollTo === 'function' &&
      !window.navigator?.userAgent?.includes('jsdom')
    ) {
      window.scrollTo({ top: 0, behavior: 'auto' });
    }
  };

  const handleFileSelection = (file: File | undefined) => {
    if (!file) return;
    const name = file.name || '';
    if (!name.toLowerCase().endsWith('.docx')) {
      setUploadError(
        'Định dạng tệp chưa phù hợp. Vui lòng chọn tài liệu có đuôi .docx.'
      );
      return;
    }
    setUploadError(null);
    setSelectedFile(file);
  };

  const handleExploreSampleDemo = () => {
    setAuditData(INITIAL_SAMPLE_AUDIT);
    setActiveSectionId('sec-1');
    setActiveFindingId('f2');
    navigateToScreen('workspace');
  };

  const handleStartAuditFlow = async () => {
    if (!selectedFile) {
      handleExploreSampleDemo();
      return;
    }

    setIsAuditing(true);
    setAuditProgressText('Đang đọc cấu trúc chương mục từ tệp .docx...');
    try {
      const parsedSections = await extractSectionsFromDocx(selectedFile);
      if (parsedSections.length === 0) {
        throw new Error('Empty docx sections');
      }

      // Send chapters in batches of 20 so entire thesis chapters stay together
      const BATCH_SIZE = 20;
      const mergedSections: DocumentAuditResult['sections'] = [];
      const mergedFindings: DocumentAuditResult['findings'] = [];
      let totalWords = 0;
      let totalSentences = 0;
      const protectedTermsSet = new Set<string>();
      let globalSeq = 1;

      for (let i = 0; i < parsedSections.length; i += BATCH_SIZE) {
        const batch = parsedSections.slice(i, i + BATCH_SIZE);
        const doneCount = Math.min(i + BATCH_SIZE, parsedSections.length);
        setAuditProgressText(
          `Đang rà soát phần ${doneCount}/${parsedSections.length} qua máy chủ kiểm toán...`
        );

        const response = await fetch('/api/audit', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            title: selectedFile.name,
            sections: batch,
          }),
        });

        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`);
        }

        const batchResult: DocumentAuditResult = await response.json();
        batchResult.sections.forEach((sec, sIdx) => {
          const globalChapterNum = i + sIdx + 1;
          const secId = sec.id || `sec-${globalChapterNum}`;
          sec.paragraphs.forEach((para) => {
            para.flags.forEach((flg) => {
              const newId = `f${globalSeq++}`;
              flg.id = newId;
              flg.sectionId = secId;
              flg.chapterNumber = globalChapterNum;
              flg.chapterTitle = sec.title;
              mergedFindings.push(flg);
            });
          });
          mergedSections.push({
            ...sec,
            id: secId,
            chapterNumber: globalChapterNum,
          });
        });

        totalWords += batchResult.summary?.totalWords || 0;
        totalSentences += batchResult.summary?.totalSentences || 0;
        (batchResult.summary?.protectedTermsMatched || []).forEach((t) =>
          protectedTermsSet.add(t)
        );
      }

      const criticalCount = mergedFindings.filter(
        (f) => f.severity === 'critical'
      ).length;
      const warningCount = mergedFindings.filter(
        (f) => f.severity === 'warning'
      ).length;
      const suggestionCount = mergedFindings.filter(
        (f) => f.severity === 'suggestion'
      ).length;
      const activeSecs = mergedSections.filter((s) => !s.isExcluded);
      const nonEmptyActiveSecs = activeSecs.filter(
        (s) => (s.wordCount || 0) > 0 && s.paragraphs.length > 0
      );
      const totalActiveWords = nonEmptyActiveSecs.reduce(
        (acc, s) => acc + Math.max(1, s.wordCount || 0),
        0
      );
      const overallAiStyleScore =
        totalActiveWords > 0
          ? Math.round(
              nonEmptyActiveSecs.reduce(
                (acc, s) =>
                  acc + s.aiStyleScore * Math.max(1, s.wordCount || 0),
                0
              ) / totalActiveWords
            )
          : 0;

      const finalResult: DocumentAuditResult = {
        title: selectedFile.name,
        isDemo: false,
        sections: mergedSections,
        findings: mergedFindings,
        summary: {
          totalWords,
          totalSentences,
          totalSections: mergedSections.length,
          auditedSections: activeSecs.length,
          totalFlags: mergedFindings.length,
          criticalCount,
          warningCount,
          suggestionCount,
          overallAiStyleScore,
          protectedTermsMatched: Array.from(protectedTermsSet),
        },
      };

      setAuditData(finalResult);
      const firstSec = finalResult.sections[0]?.id || 'sec-1';
      const firstFinding = finalResult.findings[0]?.id || '';
      setActiveSectionId(firstSec);
      setActiveFindingId(firstFinding);
      navigateToScreen('workspace');
    } catch {
      const fallback: DocumentAuditResult = {
        ...INITIAL_SAMPLE_AUDIT,
        title: selectedFile.name,
        isDemo: true,
      };
      setAuditData(fallback);
      setActiveSectionId('sec-1');
      setActiveFindingId('f2');
      navigateToScreen('workspace');
    } finally {
      setIsAuditing(false);
      setAuditProgressText('');
    }
  };

  // Workspace Helpers
  const activeSection =
    auditData.sections.find((s) => s.id === activeSectionId) ||
    auditData.sections[0];
  const activeFinding =
    auditData.findings.find((f) => f.id === activeFindingId) ||
    auditData.findings[0] ||
    null;

  const handleSelectSection = (secId: string) => {
    setActiveSectionId(secId);
    const firstInSec = auditData.findings.find((f) => f.sectionId === secId);
    if (firstInSec) {
      setActiveFindingId(firstInSec.id);
    }
  };

  const handleStepFinding = (delta: number) => {
    const list = auditData.findings;
    if (list.length === 0) return;
    const curIdx = Math.max(
      0,
      list.findIndex((f) => f.id === activeFindingId)
    );
    const nextIdx = (curIdx + delta + list.length) % list.length;
    const nextFinding = list[nextIdx];
    setActiveFindingId(nextFinding.id);
    if (nextFinding.sectionId) {
      setActiveSectionId(nextFinding.sectionId);
    }
  };

  const handleToggleResolveCurrentFinding = () => {
    if (!activeFinding) return;
    const nextStatus =
      activeFinding.status === 'resolved' ? 'pending' : 'resolved';
    setAuditData((prev) => ({
      ...prev,
      findings: prev.findings.map((f) =>
        f.id === activeFinding.id ? { ...f, status: nextStatus } : f
      ),
    }));
  };

  const handleIgnoreCurrentFinding = () => {
    if (!activeFinding) return;
    setAuditData((prev) => ({
      ...prev,
      findings: prev.findings.map((f) =>
        f.id === activeFinding.id ? { ...f, status: 'ignored' } : f
      ),
    }));
    handleStepFinding(1);
  };

  // Compute Center Column span class based on collapsed sidebars
  let centerSpanClass = 'lg:col-span-5';
  if (leftColCollapsed && rightColCollapsed) {
    centerSpanClass = 'lg:col-span-12';
  } else if (leftColCollapsed) {
    centerSpanClass = 'lg:col-span-8';
  } else if (rightColCollapsed) {
    centerSpanClass = 'lg:col-span-9';
  }

  // Insights Statistics
  const totalFindingsCount = auditData.findings.length;
  const criticalTotal = auditData.findings.filter(
    (f) => f.severity === 'critical'
  ).length;
  const warningTotal = auditData.findings.filter(
    (f) => f.severity === 'warning'
  ).length;
  const suggestionTotal = auditData.findings.filter(
    (f) => f.severity === 'suggestion'
  ).length;
  const resolvedTotal = auditData.findings.filter(
    (f) => f.status !== 'pending'
  ).length;
  const resolvedRatioPct =
    totalFindingsCount > 0
      ? Math.round((resolvedTotal / totalFindingsCount) * 100)
      : 0;

  return (
    <div className="min-h-screen flex flex-col">
      {/* BACKGROUND ARCHITECTURE */}
      <div className="bg-canvas" aria-hidden="true">
        <div className="ambient-orb orb-1" />
        <div className="ambient-orb orb-2" />
        <div className="ambient-orb orb-3" />
        <div className="bg-grid-pattern" />
        <div className="bg-cross-motif" />
        <div ref={spotlightRef} className="cursor-spotlight" />
      </div>

      {/* GLOBAL HEADER */}
      <HeaderBar
        currentScreen={currentScreen}
        onNavigate={navigateToScreen}
        theme={theme}
        onToggleTheme={() =>
          setTheme((prev) => (prev === 'dark' ? 'light' : 'dark'))
        }
        onOpenProModal={() => setIsProModalOpen(true)}
        mascotRef={mascotRef}
        pupilLeftRef={pupilLeftRef}
        pupilRightRef={pupilRightRef}
        isBlinking={isBlinking}
      />

      {/* ====================================================================
          SCREEN 01: HOME (Streamlined SaaS Landing + Primary DOCX Upload Area)
          ==================================================================== */}
      {currentScreen === 'home' && (
        <main id="screen-home" className="app-screen flex-1">
          <div className="max-w-[1280px] mx-auto px-4 sm:px-6 lg:px-8 py-10 lg:py-16 space-y-16">
            <section className="grid lg:grid-cols-12 gap-10 lg:gap-12 items-center">
              {/* Left Column (7 cols): Value Prop + Interactive Upload Centerpiece */}
              <div className="lg:col-span-7 space-y-6">
                <div className="space-y-3">
                  <p className="text-xs font-semibold uppercase tracking-widest text-blue-400">
                    Academic Writing Review
                  </p>
                  <h1 className="font-display font-extrabold text-3xl sm:text-5xl leading-[1.12] tracking-tight">
                    Rà soát và hoàn thiện{' '}
                    <span className="text-gradient-brand">
                      văn phong học thuật.
                    </span>
                  </h1>
                  <p className="text-base sm:text-lg text-[var(--text-muted)] max-w-xl leading-relaxed">
                    Tải lên tài liệu DOCX để xác định những đoạn cần chú ý, tìm hiểu nguyên nhân và tham khảo các đề xuất biên tập phù hợp.
                  </p>
                </div>

                {/* PRIMARY UPLOAD AREA */}
                <div
                  id="upload-dropzone"
                  onDragEnter={(e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    setIsDragging(true);
                  }}
                  onDragOver={(e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    setIsDragging(true);
                  }}
                  onDragLeave={(e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    setIsDragging(false);
                  }}
                  onDrop={(e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    setIsDragging(false);
                    if (e.dataTransfer?.files?.[0]) {
                      handleFileSelection(e.dataTransfer.files[0]);
                    }
                  }}
                  className={`proximity-card rounded-3xl p-6 sm:p-8 border-2 border-dashed transition-all ${
                    isDragging
                      ? 'border-blue-400 bg-blue-500/5'
                      : 'border-blue-500/35'
                  }`}
                >
                  <input
                    ref={fileInputRef}
                    id="docx-file-input"
                    type="file"
                    accept=".docx,application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    className="sr-only"
                    onChange={(e) => {
                      if (e.target.files?.[0]) {
                        handleFileSelection(e.target.files[0]);
                      }
                    }}
                  />

                  {!selectedFile ? (
                    /* State A: Empty / Unselected File */
                    <div id="upload-state-empty" className="space-y-5">
                      <div className="flex flex-col sm:flex-row items-center gap-5">
                        <div className="magnetic-icon w-16 h-16 rounded-2xl bg-blue-500/15 border border-blue-400/30 flex items-center justify-center text-blue-400 shrink-0">
                          <svg
                            className="w-8 h-8"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                            strokeWidth="1.8"
                          >
                            <path
                              strokeLinecap="round"
                              strokeLinejoin="round"
                              d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
                            />
                          </svg>
                        </div>
                        <div className="flex-1 text-center sm:text-left space-y-1">
                          <div className="flex flex-wrap items-center justify-center sm:justify-start gap-2">
                            <h2 className="font-display font-bold text-lg">
                              Kéo thả tài liệu vào đây hoặc chọn tệp từ máy
                            </h2>
                            <span className="px-2.5 py-0.5 text-[11px] font-mono font-semibold rounded-full bg-blue-500/15 text-blue-400 border border-blue-500/30">
                              .DOCX
                            </span>
                          </div>
                          <p className="text-xs sm:text-sm text-[var(--text-muted)]">
                            Hỗ trợ định dạng Microsoft Word (.docx). Giữ nguyên cấu trúc chương mục khi rà soát.
                          </p>
                        </div>
                      </div>

                      {uploadError && (
                        <div
                          id="upload-error-box"
                          className="p-3 rounded-xl bg-red-500/15 border border-red-500/35 text-xs text-red-300 flex items-center justify-between gap-2"
                          role="alert"
                        >
                          <span>{uploadError}</span>
                          <button
                            type="button"
                            onClick={() => setUploadError(null)}
                            className="text-red-300 hover:text-white font-semibold px-2"
                          >
                            Đóng
                          </button>
                        </div>
                      )}

                      <div className="pt-2 flex flex-wrap items-center justify-center sm:justify-start gap-3">
                        <button
                          type="button"
                          onClick={() => {
                            if (fileInputRef.current) {
                              fileInputRef.current.value = '';
                              fileInputRef.current.click();
                            }
                          }}
                          className="magnetic-icon px-6 py-3 rounded-2xl font-display font-bold text-sm text-white bg-gradient-to-r from-blue-600 to-cyan-500 hover:from-blue-500 hover:to-cyan-400 shadow-lg shadow-blue-500/25"
                        >
                          Browse Files (.docx)
                        </button>
                        <button
                          type="button"
                          onClick={handleExploreSampleDemo}
                          className="px-4 py-3 rounded-2xl text-xs sm:text-sm font-semibold border border-[var(--border-subtle)] bg-[var(--bg-elevated)] text-[var(--text-muted)] hover:text-[var(--text-main)] hover:border-blue-400/40 transition-all"
                        >
                          Explore Demo với bản thảo mẫu
                        </button>
                      </div>
                    </div>
                  ) : (
                    /* State B: File Selected */
                    <div id="upload-state-selected" className="space-y-5">
                      <div className="flex flex-col sm:flex-row items-center justify-between gap-4 p-4 rounded-2xl bg-[var(--bg-elevated)] border border-emerald-500/35">
                        <div className="flex items-center gap-3.5 min-w-0">
                          <div className="w-12 h-12 rounded-xl bg-emerald-500/15 border border-emerald-500/30 flex items-center justify-center text-emerald-400 shrink-0">
                            <svg
                              className="w-6 h-6"
                              fill="none"
                              viewBox="0 0 24 24"
                              stroke="currentColor"
                              strokeWidth="2"
                            >
                              <path
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
                              />
                            </svg>
                          </div>
                          <div className="min-w-0">
                            <p className="font-display font-bold text-sm sm:text-base truncate">
                              {selectedFile.name}
                            </p>
                            <p className="text-xs text-[var(--text-muted)] font-mono mt-0.5">
                              <span>{formatBytes(selectedFile.size)}</span> · Tài liệu DOCX sẵn sàng rà soát
                            </p>
                          </div>
                        </div>
                        <div className="flex items-center gap-2 shrink-0">
                          <button
                            type="button"
                            onClick={() => {
                              if (fileInputRef.current) {
                                fileInputRef.current.value = '';
                                fileInputRef.current.click();
                              }
                            }}
                            className="px-3 py-1.5 rounded-xl text-xs font-semibold border border-[var(--border-subtle)] bg-[var(--bg-card)] hover:border-blue-400/40 transition-all"
                          >
                            Thay thế
                          </button>
                          <button
                            type="button"
                            onClick={() => setSelectedFile(null)}
                            className="px-3 py-1.5 rounded-xl text-xs font-semibold border border-red-500/30 bg-red-500/10 text-red-400 hover:bg-red-500/20 transition-all"
                          >
                            Xóa file
                          </button>
                        </div>
                      </div>

                      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                        <p className="text-xs text-[var(--text-muted)]">
                          {isAuditing
                            ? auditProgressText
                            : 'Hệ thống sẽ tự động tách chương mục và gửi phân tích văn phong.'}
                        </p>
                        <button
                          type="button"
                          id="start-audit-btn"
                          disabled={isAuditing}
                          onClick={handleStartAuditFlow}
                          className="magnetic-icon px-7 py-3.5 rounded-2xl font-display font-extrabold text-sm text-white bg-gradient-to-r from-blue-600 via-cyan-500 to-emerald-500 shadow-xl shadow-blue-500/25 tracking-wide disabled:opacity-60"
                        >
                          {isAuditing ? 'ĐANG RÀ SOÁT...' : 'START AUDIT →'}
                        </button>
                      </div>
                    </div>
                  )}
                </div>
              </div>

              {/* Right Column (5 cols): Visual Interface Preview (Fanned Deck) */}
              <div className="lg:col-span-5 relative">
                <div className="fan-deck proximity-card rounded-3xl h-[360px] sm:h-[390px] flex items-center justify-center p-6 select-none">
                  {/* Left Preview Card */}
                  <div className="fan-card-left absolute w-52 sm:w-56 rounded-2xl border border-[var(--border-subtle)] bg-[var(--bg-elevated)] p-4 shadow-2xl">
                    <div className="flex items-center justify-between text-[11px] font-semibold text-orange-400 mb-2">
                      <span>Chương 1 · Tổng quan</span>
                      <span className="px-2 py-0.5 rounded-full bg-orange-500/15">
                        Nên sửa
                      </span>
                    </div>
                    <p className="text-xs font-semibold mb-1.5">
                      Cấu trúc câu liệt kê lặp lại
                    </p>
                    <p className="text-[11px] text-[var(--text-muted)] leading-relaxed line-clamp-3">
                      "Qua đó góp phần nâng cao hiệu quả vận hành, tối ưu hóa nguồn lực và thúc đẩy tăng trưởng..."
                    </p>
                  </div>

                  {/* Right Preview Card */}
                  <div className="fan-card-right absolute w-52 sm:w-56 rounded-2xl border border-[var(--border-subtle)] bg-[var(--bg-elevated)] p-4 shadow-2xl">
                    <div className="flex items-center justify-between text-[11px] font-semibold text-red-400 mb-2">
                      <span>Chương 3 · Thảo luận</span>
                      <span className="px-2 py-0.5 rounded-full bg-red-500/15">
                        Cần sửa ngay
                      </span>
                    </div>
                    <p className="text-xs font-semibold mb-1.5">
                      Kiểm tra nguồn trích dẫn
                    </p>
                    <p className="text-[11px] text-[var(--text-muted)] leading-relaxed line-clamp-3">
                      Phát hiện ký hiệu trích dẫn hệ thống chưa làm sạch và mã định danh tài liệu cần đối chiếu...
                    </p>
                  </div>

                  {/* Center Main Preview Card */}
                  <div className="fan-card-center relative z-10 w-64 sm:w-72 rounded-2xl border-2 border-blue-500/40 bg-[var(--bg-elevated)] p-5 shadow-2xl space-y-3.5">
                    <div className="flex items-center justify-between">
                      <span className="px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-blue-500/20 text-blue-400">
                        Tổng quan kết quả
                      </span>
                      <span className="text-xs text-[var(--text-muted)]">
                        {auditData.sections.length} Chương
                      </span>
                    </div>
                    <h3 className="font-display font-bold text-sm sm:text-base leading-snug">
                      Bản thảo Nghiên cứu &amp; Phân tích Học thuật
                    </h3>
                    <div className="grid grid-cols-3 gap-2 p-2.5 rounded-xl bg-[var(--bg-base)]/70 border border-[var(--border-subtle)] text-center">
                      <div>
                        <div className="font-mono font-bold text-sm text-red-400">
                          {criticalTotal}
                        </div>
                        <div className="text-[10px] text-[var(--text-muted)]">
                          Cần sửa ngay
                        </div>
                      </div>
                      <div>
                        <div className="font-mono font-bold text-sm text-orange-400">
                          {warningTotal}
                        </div>
                        <div className="text-[10px] text-[var(--text-muted)]">
                          Nên sửa
                        </div>
                      </div>
                      <div>
                        <div className="font-mono font-bold text-sm text-indigo-400">
                          {suggestionTotal}
                        </div>
                        <div className="text-[10px] text-[var(--text-muted)]">
                          Gợi ý
                        </div>
                      </div>
                    </div>
                    <div className="space-y-1.5 text-xs">
                      <div className="flex items-center justify-between">
                        <span className="text-[var(--text-muted)]">
                          Đề xuất biên tập
                        </span>
                        <span className="font-semibold text-emerald-400">
                          Sẵn sàng
                        </span>
                      </div>
                      <div className="flex items-center justify-between">
                        <span className="text-[var(--text-muted)]">
                          Báo cáo kiểm toán
                        </span>
                        <span className="font-semibold text-cyan-400">
                          Xem trực tiếp
                        </span>
                      </div>
                    </div>
                  </div>

                  {/* Subtle Floating Badges */}
                  <div className="animate-float-badge absolute top-4 left-4 z-20 px-3 py-1.5 rounded-full border border-emerald-400/30 bg-[var(--bg-glass)] backdrop-blur-md shadow-lg text-xs font-medium text-emerald-400">
                    Đề xuất biên tập rõ ràng
                  </div>
                  <div className="animate-float-badge-delayed absolute bottom-4 right-4 z-20 px-3 py-1.5 rounded-full border border-cyan-400/30 bg-[var(--bg-glass)] backdrop-blur-md shadow-lg text-xs font-medium text-cyan-400">
                    Phân tích theo từng chương
                  </div>
                </div>
              </div>
            </section>

            {/* 3 Core Benefits */}
            <section className="grid sm:grid-cols-3 gap-5 pt-4">
              <div className="proximity-card rounded-2xl p-6 space-y-2.5">
                <div className="magnetic-icon w-10 h-10 rounded-xl bg-red-500/15 border border-red-500/30 flex items-center justify-center text-red-400">
                  <svg
                    className="w-5 h-5"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    strokeWidth="2"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
                    />
                  </svg>
                </div>
                <h2 className="font-display font-bold text-base">
                  Xác định các điểm cần chú ý
                </h2>
                <p className="text-xs sm:text-sm text-[var(--text-muted)] leading-relaxed">
                  Khoanh vùng các câu văn rập khuôn, trích dẫn cần xác minh hoặc lối diễn đạt thiếu tự nhiên theo ba mức độ ưu tiên.
                </p>
              </div>

              <div className="proximity-card rounded-2xl p-6 space-y-2.5">
                <div className="magnetic-icon w-10 h-10 rounded-xl bg-blue-500/15 border border-blue-500/30 flex items-center justify-center text-blue-400">
                  <svg
                    className="w-5 h-5"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    strokeWidth="2"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"
                    />
                  </svg>
                </div>
                <h2 className="font-display font-bold text-base">
                  Giải thích nguyên nhân cụ thể
                </h2>
                <p className="text-xs sm:text-sm text-[var(--text-muted)] leading-relaxed">
                  Cung cấp nhận xét trực diện cho từng đoạn văn bản để người viết chủ động quyết định giữ nguyên hoặc điều chỉnh.
                </p>
              </div>

              <div className="proximity-card rounded-2xl p-6 space-y-2.5">
                <div className="magnetic-icon w-10 h-10 rounded-xl bg-emerald-500/15 border border-emerald-500/30 flex items-center justify-center text-emerald-400">
                  <svg
                    className="w-5 h-5"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    strokeWidth="2"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"
                    />
                  </svg>
                </div>
                <h2 className="font-display font-bold text-base">
                  Đề xuất biên tập sát ngữ cảnh
                </h2>
                <p className="text-xs sm:text-sm text-[var(--text-muted)] leading-relaxed">
                  Gợi ý phương án viết lại ngắn gọn, khách quan và giữ nguyên nội dung chuyên môn của tài liệu gốc.
                </p>
              </div>
            </section>

            {/* Compact Footer */}
            <footer className="pt-6 border-t border-[var(--border-subtle)] flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-[var(--text-muted)]">
              <div className="flex items-center gap-2">
                <span className="font-display font-bold text-[var(--text-main)]">
                  AI Style Auditor
                </span>
                <span>·</span>
                <span>Academic Writing Review</span>
              </div>
              <div className="flex items-center gap-4">
                <button
                  type="button"
                  onClick={() => navigateToScreen('workspace')}
                  className="hover:text-[var(--text-main)] transition-colors"
                >
                  Workspace
                </button>
                <button
                  type="button"
                  onClick={() => navigateToScreen('insights')}
                  className="hover:text-[var(--text-main)] transition-colors"
                >
                  Insights
                </button>
                <button
                  type="button"
                  onClick={() => setIsReportModalOpen(true)}
                  className="hover:text-[var(--text-main)] transition-colors"
                >
                  Báo cáo kiểm toán
                </button>
              </div>
            </footer>
          </div>
        </main>
      )}

      {/* ====================================================================
          SCREEN 02: WORKSPACE (Dedicated 3-Column SaaS Application View)
          ==================================================================== */}
      {currentScreen === 'workspace' && activeSection && (
        <main
          id="screen-workspace"
          className="app-screen flex-1 lg:h-[calc(100vh-76px)] lg:max-h-[calc(100vh-76px)] lg:overflow-hidden flex flex-col"
        >
          <div className="max-w-[1440px] w-full mx-auto px-4 sm:px-6 lg:px-8 py-4 flex-1 min-h-0 flex flex-col gap-4">
            {/* A. Workspace Header / Application Bar */}
            <div className="shrink-0 proximity-card rounded-2xl px-4 py-3 flex flex-wrap items-center justify-between gap-3">
              <div className="flex flex-wrap items-center gap-2.5 min-w-0">
                <button
                  type="button"
                  onClick={() => navigateToScreen('home')}
                  className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold border border-[var(--border-subtle)] bg-[var(--bg-elevated)] hover:border-blue-400/40 transition-all"
                >
                  <span>←</span>
                  <span>Home</span>
                </button>

                <nav
                  aria-label="Breadcrumb"
                  className="flex items-center gap-1.5 text-xs text-[var(--text-muted)] truncate"
                >
                  <span>Workspace</span>
                  <span>/</span>
                  <span
                    id="workspace-doc-title"
                    className="font-semibold text-[var(--text-main)] truncate max-w-[220px] sm:max-w-[320px]"
                  >
                    {auditData.title}
                  </span>
                </nav>

                {auditData.isDemo && (
                  <span className="px-2.5 py-1 rounded-full text-[11px] font-semibold bg-amber-500/15 text-amber-400 border border-amber-500/30">
                    DEMO PREVIEW – Kết quả minh họa
                  </span>
                )}
              </div>

              {/* Right: Panel Collapse Controls + View Insights + Report Preview */}
              <div className="flex flex-wrap items-center gap-2">
                <button
                  type="button"
                  onClick={() => setLeftColCollapsed((prev) => !prev)}
                  className="hidden lg:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-medium border border-[var(--border-subtle)] bg-[var(--bg-card)] text-[var(--text-muted)] hover:text-[var(--text-main)] transition-all"
                  title="Ẩn hoặc hiện danh sách chương"
                >
                  <span>Ẩn/Hiện Mục lục</span>
                </button>
                <button
                  type="button"
                  onClick={() => setRightColCollapsed((prev) => !prev)}
                  className="hidden lg:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-medium border border-[var(--border-subtle)] bg-[var(--bg-card)] text-[var(--text-muted)] hover:text-[var(--text-main)] transition-all"
                  title="Ẩn hoặc hiện bảng chẩn đoán"
                >
                  <span>Ẩn/Hiện Chẩn đoán</span>
                </button>
                <button
                  type="button"
                  onClick={() => navigateToScreen('insights')}
                  className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl text-xs font-semibold border border-blue-500/35 bg-blue-500/10 text-blue-400 hover:bg-blue-500/20 transition-all"
                >
                  <span>Xem Insights</span>
                </button>
                <button
                  type="button"
                  onClick={() => {
                    setReportInitialTab('turnitin');
                    setIsReportModalOpen(true);
                  }}
                  className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl text-xs font-semibold border border-cyan-500/40 bg-cyan-500/15 text-cyan-300 hover:bg-cyan-500/25 transition-all"
                >
                  <span>Bản thảo Bôi màu (Turnitin)</span>
                </button>
                <button
                  type="button"
                  onClick={() => {
                    setReportInitialTab('summary');
                    setIsReportModalOpen(true);
                  }}
                  className="magnetic-icon inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl text-xs font-semibold text-white bg-gradient-to-r from-blue-600 to-cyan-500 shadow-sm"
                >
                  <span>Xem trước Báo cáo</span>
                </button>
              </div>
            </div>

            {/* B. Three-Column Workspace Grid (Locked height, 3 independent scrollbars) */}
            <div
              id="workspace-grid"
              className="flex-1 min-h-0 grid lg:grid-cols-12 gap-5 items-stretch lg:overflow-hidden"
            >
              <ChapterSidebar
                sections={auditData.sections}
                findings={auditData.findings}
                activeSectionId={activeSection.id}
                onSelectSection={handleSelectSection}
                activeFilter={activeFilter}
                onSelectFilter={setActiveFilter}
                collapsed={leftColCollapsed}
              />

              <AuditDocumentViewer
                section={activeSection}
                allFindings={auditData.findings}
                activeFindingId={activeFindingId}
                onSelectFinding={setActiveFindingId}
                onStepFinding={handleStepFinding}
                activeFilter={activeFilter}
                largeFont={largeFont}
                onToggleFontSize={() => setLargeFont((prev) => !prev)}
                colSpanClass={centerSpanClass}
              />

              <DiagnosticInspector
                finding={activeFinding}
                onToggleResolve={handleToggleResolveCurrentFinding}
                onIgnore={handleIgnoreCurrentFinding}
                onOpenProModal={() => setIsProModalOpen(true)}
                collapsed={rightColCollapsed}
              />
            </div>
          </div>
        </main>
      )}

      {/* ====================================================================
          SCREEN 03: INSIGHTS (Dedicated Audit Overview, Statistics & Report)
          ==================================================================== */}
      {currentScreen === 'insights' && (
        <main id="screen-insights" className="app-screen flex-1">
          <div className="max-w-[1280px] mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
            {/* Insights Header */}
            <div className="proximity-card rounded-2xl p-5 flex flex-wrap items-center justify-between gap-4">
              <div className="space-y-1">
                <div className="flex flex-wrap items-center gap-2.5">
                  <h1 className="font-display font-extrabold text-xl sm:text-2xl">
                    Tổng quan kết quả rà soát
                  </h1>
                  {auditData.isDemo && (
                    <span className="px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-amber-500/15 text-amber-400 border border-amber-500/30">
                      DEMO PREVIEW – Kết quả minh họa
                    </span>
                  )}
                </div>
                <p className="text-xs sm:text-sm text-[var(--text-muted)]">
                  Tài liệu:{' '}
                  <strong className="text-[var(--text-main)]">
                    {auditData.title}
                  </strong>
                </p>
              </div>

              <div className="flex flex-wrap items-center gap-2.5">
                <button
                  type="button"
                  onClick={() => navigateToScreen('workspace')}
                  className="px-4 py-2 rounded-xl text-xs font-semibold border border-[var(--border-subtle)] bg-[var(--bg-elevated)] hover:border-blue-400/40 transition-all"
                >
                  ← Mở Workspace
                </button>
                <button
                  type="button"
                  onClick={() => {
                    setReportInitialTab('turnitin');
                    setIsReportModalOpen(true);
                  }}
                  className="px-4 py-2 rounded-xl text-xs font-semibold border border-cyan-500/40 bg-cyan-500/15 text-cyan-300 hover:bg-cyan-500/25 transition-all"
                >
                  Xem Bản thảo Bôi màu (Turnitin)
                </button>
                <button
                  type="button"
                  onClick={() => {
                    setReportInitialTab('summary');
                    setIsReportModalOpen(true);
                  }}
                  className="magnetic-icon px-4 py-2 rounded-xl text-xs font-bold text-white bg-gradient-to-r from-blue-600 to-cyan-500 shadow-md"
                >
                  Xem trước Báo cáo
                </button>
              </div>
            </div>

            {/* KPI Overview Cards */}
            <section className="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
              <div className="proximity-card rounded-2xl p-5 space-y-1.5">
                <span className="text-xs text-[var(--text-muted)]">
                  Tổng số điểm cần chú ý
                </span>
                <div className="font-display font-extrabold text-3xl text-[var(--text-main)]">
                  {totalFindingsCount}
                </div>
                <p className="text-xs text-[var(--text-muted)]">
                  Trên {auditData.sections.length} phần của tài liệu
                </p>
              </div>

              <div className="proximity-card rounded-2xl p-5 space-y-1.5">
                <span className="text-xs text-[var(--text-muted)]">
                  Cần sửa ngay
                </span>
                <div className="font-display font-extrabold text-3xl text-red-400">
                  {criticalTotal}
                </div>
                <p className="text-xs text-[var(--text-muted)]">
                  Lỗi trích dẫn hoặc ký hiệu lạ
                </p>
              </div>

              <div className="proximity-card rounded-2xl p-5 space-y-1.5">
                <span className="text-xs text-[var(--text-muted)]">
                  Nên sửa &amp; Gợi ý
                </span>
                <div className="font-display font-extrabold text-3xl text-orange-400">
                  {warningTotal + suggestionTotal}
                </div>
                <p className="text-xs text-[var(--text-muted)]">
                  Diễn đạt, cấu trúc câu &amp; liên kết đoạn
                </p>
              </div>

              <div className="proximity-card rounded-2xl p-5 space-y-1.5">
                <span className="text-xs text-[var(--text-muted)]">
                  Tiến độ xử lý
                </span>
                <div className="font-display font-extrabold text-3xl text-emerald-400">
                  {resolvedTotal} / {totalFindingsCount}
                </div>
                <div className="w-full h-1.5 rounded-full bg-slate-700/50 overflow-hidden mt-1">
                  <div
                    className="h-full bg-emerald-500 rounded-full transition-all duration-300"
                    style={{ width: `${resolvedRatioPct}%` }}
                  />
                </div>
              </div>
            </section>

            {/* Priority Breakdown + Chapter Distribution */}
            <section className="grid lg:grid-cols-12 gap-6">
              <div className="lg:col-span-6 proximity-card rounded-3xl p-6 space-y-5">
                <h2 className="font-display font-bold text-base sm:text-lg">
                  Các nhóm vấn đề cần chú ý
                </h2>

                <div className="space-y-4 text-xs sm:text-sm">
                  <div className="space-y-1.5">
                    <div className="flex items-center justify-between">
                      <span className="font-semibold text-red-400">
                        1. Độ chính xác trích dẫn &amp; ký hiệu thừa (Cần sửa ngay)
                      </span>
                      <span className="font-mono">{criticalTotal} phát hiện</span>
                    </div>
                    <div className="w-full h-2 rounded-full bg-slate-700/40 overflow-hidden">
                      <div
                        className="h-full bg-red-500 rounded-full"
                        style={{
                          width: `${
                            totalFindingsCount
                              ? Math.round(
                                  (criticalTotal / totalFindingsCount) * 100
                                )
                              : 0
                          }%`,
                        }}
                      />
                    </div>
                    <p className="text-xs text-[var(--text-muted)]">
                      Cần kiểm tra lại mã định danh nguồn tài liệu và xóa bỏ các ký hiệu phát sinh khi sao chép.
                    </p>
                  </div>

                  <div className="space-y-1.5">
                    <div className="flex items-center justify-between">
                      <span className="font-semibold text-orange-400">
                        2. Cấu trúc câu lặp &amp; cách diễn đạt phóng đại (Nên sửa)
                      </span>
                      <span className="font-mono">{warningTotal} phát hiện</span>
                    </div>
                    <div className="w-full h-2 rounded-full bg-slate-700/40 overflow-hidden">
                      <div
                        className="h-full bg-orange-500 rounded-full"
                        style={{
                          width: `${
                            totalFindingsCount
                              ? Math.round(
                                  (warningTotal / totalFindingsCount) * 100
                                )
                              : 0
                          }%`,
                        }}
                      />
                    </div>
                    <p className="text-xs text-[var(--text-muted)]">
                      Các câu liệt kê ba vế liên tiếp hoặc dùng tính từ tán dương chưa gắn với số liệu thực tế.
                    </p>
                  </div>

                  <div className="space-y-1.5">
                    <div className="flex items-center justify-between">
                      <span className="font-semibold text-indigo-400">
                        3. Câu bị động dài &amp; câu chuyển đoạn chung chung (Gợi ý)
                      </span>
                      <span className="font-mono">
                        {suggestionTotal} phát hiện
                      </span>
                    </div>
                    <div className="w-full h-2 rounded-full bg-slate-700/40 overflow-hidden">
                      <div
                        className="h-full bg-indigo-500 rounded-full"
                        style={{
                          width: `${
                            totalFindingsCount
                              ? Math.round(
                                  (suggestionTotal / totalFindingsCount) * 100
                                )
                              : 0
                          }%`,
                        }}
                      />
                    </div>
                    <p className="text-xs text-[var(--text-muted)]">
                      Có thể rút gọn cụm danh hóa để câu văn chủ động, sáng rõ và dễ theo dõi hơn.
                    </p>
                  </div>
                </div>
              </div>

              <div className="lg:col-span-6 proximity-card rounded-3xl p-6 space-y-5">
                <div className="flex items-center justify-between">
                  <h2 className="font-display font-bold text-base sm:text-lg">
                    Phân bố phát hiện theo chương
                  </h2>
                  <span className="text-xs text-[var(--text-muted)]">
                    Nhấn vào chương để mở trong Workspace
                  </span>
                </div>

                <div className="space-y-2.5 text-xs sm:text-sm max-h-[320px] overflow-y-auto workspace-scroll-area pr-1">
                  {auditData.sections.map((sec) => {
                    const secFindings = auditData.findings.filter(
                      (f) => f.sectionId === sec.id
                    );
                    return (
                      <button
                        key={sec.id}
                        type="button"
                        onClick={() => {
                          handleSelectSection(sec.id);
                          navigateToScreen('workspace');
                        }}
                        className="w-full p-3.5 rounded-2xl border border-[var(--border-subtle)] bg-[var(--bg-elevated)] hover:border-blue-400/50 flex items-center justify-between gap-3 text-left transition-all"
                      >
                        <div>
                          <p className="font-semibold">{sec.title}</p>
                          <p className="text-xs text-[var(--text-muted)] mt-0.5">
                            {sec.isExcluded
                              ? 'Mục tự động loại trừ (Mục lục / Tài liệu tham khảo)'
                              : `${sec.wordCount} từ · Nhấn để rà soát chi tiết`}
                          </p>
                        </div>
                        <span className="px-2.5 py-1 rounded-full text-xs font-mono font-semibold bg-orange-500/15 text-orange-400 shrink-0">
                          {secFindings.length} điểm
                        </span>
                      </button>
                    );
                  })}
                </div>
              </div>
            </section>

            {/* Report Preview & Turnitin Full-Manuscript Export Banner */}
            <section className="proximity-card rounded-3xl p-6 flex flex-col lg:flex-row items-center justify-between gap-5">
              <div className="space-y-1 text-center lg:text-left">
                <h2 className="font-display font-bold text-lg">
                  Báo cáo Kiểm toán &amp; Bản thảo Bôi màu (Turnitin Feedback Studio)
                </h2>
                <p className="text-xs sm:text-sm text-[var(--text-muted)] max-w-2xl">
                  Xem toàn bộ nội dung luận văn đã được bôi màu trực tiếp kèm số thứ tự chú giải theo phong cách Turnitin Feedback Studio, hoặc tải xuống báo cáo tổng hợp định dạng HTML / PDF / JSON.
                </p>
              </div>
              <div className="flex flex-wrap items-center justify-center gap-3 shrink-0">
                <button
                  type="button"
                  onClick={() => downloadTurnitinStyleHtmlReport(auditData)}
                  className="px-4 py-3 rounded-2xl font-display font-bold text-xs sm:text-sm border border-cyan-500/40 bg-cyan-500/15 text-cyan-300 hover:bg-cyan-500/25 transition-all"
                >
                  Tải Bản thảo Bôi màu (.html)
                </button>
                <button
                  type="button"
                  onClick={() => {
                    setReportInitialTab('turnitin');
                    setIsReportModalOpen(true);
                  }}
                  className="magnetic-icon px-5 py-3 rounded-2xl font-display font-bold text-xs sm:text-sm text-white bg-gradient-to-r from-cyan-600 to-blue-600 shadow-lg"
                >
                  Xem Bản thảo Bôi màu
                </button>
                <button
                  type="button"
                  onClick={() => {
                    setReportInitialTab('summary');
                    setIsReportModalOpen(true);
                  }}
                  className="magnetic-icon px-5 py-3 rounded-2xl font-display font-bold text-xs sm:text-sm text-white bg-gradient-to-r from-blue-600 to-indigo-600 shadow-lg"
                >
                  Mở Báo cáo Tổng hợp
                </button>
              </div>
            </section>
          </div>
        </main>
      )}

      {/* MODALS */}
      <ReportPreviewModal
        isOpen={isReportModalOpen}
        onClose={() => setIsReportModalOpen(false)}
        audit={auditData}
        initialTab={reportInitialTab}
      />

      <ProUpgradeModal
        isOpen={isProModalOpen}
        onClose={() => setIsProModalOpen(false)}
      />
    </div>
  );
};

export default App;
