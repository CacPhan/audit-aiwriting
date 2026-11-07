export type SeverityLevel = 'critical' | 'warning' | 'suggestion';
export type FindingStatus = 'pending' | 'resolved' | 'ignored';

export interface ParagraphMetrics {
  cvLength: number;
  deltaLength: number;
  isi: number;
  opr: number;
  svci: number;
  sicd: number;
  bcr: number;
}

export interface AuditFlag {
  id: string;
  ruleId: string;
  ruleName?: string;
  category?: string;
  priorityStage?: string;
  severity: SeverityLevel;
  severityLabel: string;
  title: string;
  excerpt: string;
  matchedText?: string;
  reason: string;
  suggestion: string;
  start: number;
  end: number;
  sectionId?: string;
  chapterNumber?: number;
  chapterTitle?: string;
  paragraphIndex?: number;
  status: FindingStatus;
}

export type ManuscriptBlockType =
  | 'prose'
  | 'subheading'
  | 'caption'
  | 'list-item';

export interface AuditedParagraph {
  index: number;
  text: string;
  prefix?: string;
  blockType?: ManuscriptBlockType;
  wordCount: number;
  sentenceCount: number;
  metrics: ParagraphMetrics;
  flags: AuditFlag[];
  protectedTerms: string[];
  aiStyleScore: number;
}

export interface AuditedSection {
  id: string;
  chapterNumber: number;
  title: string;
  shortTitle: string;
  sectionLabel: string;
  parentHeading?: string;
  isExcluded: boolean;
  wordCount: number;
  flagCount: number;
  aiStyleScore: number;
  paragraphs: AuditedParagraph[];
}

export interface DocumentAuditSummary {
  totalWords: number;
  totalSentences: number;
  totalSections: number;
  auditedSections: number;
  totalFlags: number;
  criticalCount: number;
  warningCount: number;
  suggestionCount: number;
  overallAiStyleScore: number;
  protectedTermsMatched: string[];
  lexiconSize?: number;
  totalRulesCount?: number;
}

export interface DocumentAuditResult {
  title: string;
  sections: AuditedSection[];
  findings: AuditFlag[];
  summary: DocumentAuditSummary;
  isDemo?: boolean;
}

export interface ParsedThesisSection {
  id: string;
  title: string;
  shortTitle: string;
  sectionLabel: string;
  parentHeading?: string;
  paragraphs: string[];
  paragraphTypes?: ManuscriptBlockType[];
  isExcluded: boolean;
}
