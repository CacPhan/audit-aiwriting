import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { describe, it, expect, vi, afterEach } from 'vitest';
import App from '../../App';

const FORBIDDEN_INTERNAL_JARGON = [
  '8 ngành Kinh tế',
  '2.400+ thuật ngữ miễn trừ',
  'ECON-26',
  'Rule-Based Engine',
  '26 Signs',
  '26 quy tắc',
  '6 chỉ số',
  'CV_L',
  'ISI',
  'OPR',
  'SVCI',
  'SICD',
  'BCR',
  'P0',
  'P1',
  'P2',
  'P3',
  '70–90+ trang',
  '84 trang',
  '99.000đ',
  'rê chuột',
  'di chuột',
];

describe('AI Style Auditor Multi-Screen SaaS, UI Jargon Non-Disclosure & E2E Flow', () => {
  afterEach(() => {
    vi.restoreAllMocks();
  });

  it('verifies 3 independent screens (Home, Workspace, Insights), severity filters, column collapse, theme toggle, and Escape modal close', () => {
    const { container } = render(<App />);

    // 1. Home screen is rendered by default; Workspace and Insights are NOT in the DOM (no vertical scroll single-page)
    expect(container.querySelector('#screen-home')).toBeTruthy();
    expect(container.querySelector('#screen-workspace')).toBeNull();
    expect(container.querySelector('#screen-insights')).toBeNull();

    // 2. Test non-.docx file upload validation on Home
    const fileInput = container.querySelector(
      '#docx-file-input'
    ) as HTMLInputElement;
    const invalidFile = new File(['invalid pdf content'], 'tai_lieu.pdf', {
      type: 'application/pdf',
    });
    fireEvent.change(fileInput, { target: { files: [invalidFile] } });
    expect(
      screen.getByText(
        /Định dạng tệp chưa phù hợp\. Vui lòng chọn tài liệu có đuôi \.docx\./i
      )
    ).toBeTruthy();

    // 3. Switch to Workspace via Explore Demo button
    const demoBtn = screen.getByRole('button', {
      name: /Explore Demo với bản thảo mẫu/i,
    });
    fireEvent.click(demoBtn);

    expect(container.querySelector('#screen-home')).toBeNull();
    expect(container.querySelector('#screen-workspace')).toBeTruthy();

    // 4. Verify 3-column Workspace, chapter switching, and 3 underline classes (wavy, solid, dashed)
    expect(screen.getByText(/Cấu trúc tài liệu/i)).toBeTruthy();
    expect(container.querySelector('.span-warning')).toBeTruthy();
    expect(container.querySelector('.span-suggestion')).toBeTruthy();

    // Switch to Chapter 3 to verify critical wavy span
    const ch3Btn = screen.getByRole('button', {
      name: /Chương 3: Kết quả và Thảo luận/i,
    });
    fireEvent.click(ch3Btn);
    expect(container.querySelector('.span-critical')).toBeTruthy();

    // 5. Test severity filters ("Cần sửa ngay", "Nên sửa", "Gợi ý")
    const filterGroup = screen.getByRole('group', {
      name: /Bộ lọc mức độ ưu tiên/i,
    });
    expect(filterGroup).toBeTruthy();
    fireEvent.click(
      screen.getAllByRole('button', { name: /Cần sửa ngay/i })[0]
    );
    fireEvent.click(screen.getByRole('button', { name: /Tất cả phát hiện/i }));

    // 6. Test collapsing Left and Right columns
    const toggleLeftBtn = screen.getByRole('button', {
      name: /Ẩn\/Hiện Mục lục/i,
    });
    const toggleRightBtn = screen.getByRole('button', {
      name: /Ẩn\/Hiện Chẩn đoán/i,
    });
    fireEvent.click(toggleLeftBtn);
    expect(
      container
        .querySelector('#workspace-col-left')
        ?.className.includes('lg:hidden')
    ).toBe(true);
    fireEvent.click(toggleLeftBtn);

    fireEvent.click(toggleRightBtn);
    expect(
      container
        .querySelector('#workspace-col-right')
        ?.className.includes('lg:hidden')
    ).toBe(true);
    fireEvent.click(toggleRightBtn);

    // 7. Copy suggestion & Mark finding as Resolved
    const copyBtn = screen.getByRole('button', { name: /Sao chép gợi ý/i });
    fireEvent.click(copyBtn);
    expect(screen.getByText(/Đã sao chép/i)).toBeTruthy();

    const resolveBtn = screen.getByRole('button', {
      name: /Đánh dấu đã xử lý/i,
    });
    fireEvent.click(resolveBtn);
    expect(screen.getByText(/Đã xử lý 1\/7/i)).toBeTruthy();

    // 8. Navigate to Insights screen and verify synchronized resolution progress
    const insightsBtn = screen.getByRole('button', { name: /Xem Insights/i });
    fireEvent.click(insightsBtn);
    expect(container.querySelector('#screen-workspace')).toBeNull();
    expect(container.querySelector('#screen-insights')).toBeTruthy();
    expect(screen.getByText(/Tổng quan kết quả rà soát/i)).toBeTruthy();
    expect(screen.getByText('1 / 7')).toBeTruthy();

    // 9. Open Report Preview Modal, switch to Turnitin Feedback Studio tab, and close with Escape key
    const openReportBtn = screen.getAllByRole('button', {
      name: /Xem trước Báo cáo/i,
    })[0];
    fireEvent.click(openReportBtn);
    expect(
      screen.getByText(/Báo cáo Kiểm toán Văn phong Học thuật/i)
    ).toBeTruthy();
    const turnitinTabBtn = container.querySelector(
      '#tab-turnitin-studio'
    ) as HTMLButtonElement;
    expect(turnitinTabBtn).toBeTruthy();
    fireEvent.click(turnitinTabBtn);
    expect(container.querySelector('#turnitin-studio-preview')).toBeTruthy();
    expect(container.querySelectorAll('.turnitin-hl').length).toBeGreaterThan(
      0
    );
    expect(
      container.querySelectorAll('.turnitin-badge').length
    ).toBeGreaterThan(0);

    fireEvent.keyDown(window, { key: 'Escape' });
    expect(container.querySelector('#report-modal')).toBeNull();

    // 10. Open ProUpgradeModal and close with Escape key
    const proBtn = screen.getByRole('button', {
      name: /Upgrade Pro \(Coming soon\)/i,
    });
    fireEvent.click(proBtn);
    expect(
      screen.getByText(/Tính năng Nâng cao đang được phát triển/i)
    ).toBeTruthy();
    fireEvent.keyDown(window, { key: 'Escape' });
    expect(container.querySelector('#pro-modal')).toBeNull();

    // 11. Toggle Dark / Light Theme
    const themeBtn = container.querySelector(
      '#theme-toggle-btn'
    ) as HTMLButtonElement;
    expect(document.documentElement.getAttribute('data-theme')).toBe('dark');
    fireEvent.click(themeBtn);
    expect(document.documentElement.getAttribute('data-theme')).toBe('light');
  });

  it('scans Frontend source files and rendered DOM to guarantee zero internal technical jargon leakage and accessibility support', () => {
    const srcDir = path.resolve(process.cwd(), 'src');
    const uiFilesToScan = [
      path.resolve(process.cwd(), 'index.html'),
      path.join(srcDir, 'App.tsx'),
      path.join(srcDir, 'components', 'HeaderBar.tsx'),
      path.join(srcDir, 'components', 'ChapterSidebar.tsx'),
      path.join(srcDir, 'components', 'AuditDocumentViewer.tsx'),
      path.join(srcDir, 'components', 'DiagnosticInspector.tsx'),
      path.join(srcDir, 'components', 'ProUpgradeModal.tsx'),
      path.join(srcDir, 'utils', 'reportExporter.ts'),
    ];

    for (const filePath of uiFilesToScan) {
      const content = fs.readFileSync(filePath, 'utf-8');
      for (const term of FORBIDDEN_INTERNAL_JARGON) {
        // Use word-boundary check for short codes like P0..P3, ISI, OPR, BCR
        if (/^[A-Z0-9_]{2,4}$/.test(term)) {
          const regex = new RegExp(`\\b${term}\\b`);
          expect(
            regex.test(content),
            `Forbidden internal code "${term}" found in ${path.basename(filePath)}`
          ).toBe(false);
        } else {
          expect(
            content.includes(term),
            `Forbidden phrase "${term}" found in ${path.basename(filePath)}`
          ).toBe(false);
        }
      }
    }

    // Verify CSS accessibility rules (:focus-visible and prefers-reduced-motion: reduce)
    const cssContent = fs.readFileSync(path.join(srcDir, 'index.css'), 'utf-8');
    expect(cssContent).toContain(':focus-visible');
    expect(cssContent).toContain('prefers-reduced-motion: reduce');
  });

  it('executes End-to-End flow: uploads real .docx thesis -> extracts chapters -> calls Python /api/audit engine -> renders Workspace & Insights', async () => {
    // Route fetch('/api/audit') directly to the real Python serverless engine (api/audit.py)
    vi.spyOn(globalThis, 'fetch').mockImplementation(
      async (_input, init?: RequestInit) => {
        const bodyStr = typeof init?.body === 'string' ? init.body : '{}';
        const py = spawnSync('python', ['api/audit.py'], {
          cwd: process.cwd(),
          input: Buffer.from(bodyStr, 'utf-8'),
          maxBuffer: 15 * 1024 * 1024,
        });
        const outJson = py.stdout.toString('utf-8');
        return new Response(outJson, {
          status: py.status === 0 ? 200 : 500,
          headers: { 'Content-Type': 'application/json' },
        });
      }
    );

    const { container } = render(<App />);

    // Load real thesis .docx fixture
    const docxPath = path.resolve(
      process.cwd(),
      'tests',
      'fixtures',
      'kltn_thai_son_11233561.docx'
    );
    const buffer = fs.readFileSync(docxPath);
    const docxFile = new File(
      [new Uint8Array(buffer)],
      'KLTN_Nguyen_Le_Thai_Son_11233561.docx',
      {
        type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
      }
    );
    Object.defineProperty(docxFile, 'arrayBuffer', {
      value: async () =>
        buffer.buffer.slice(
          buffer.byteOffset,
          buffer.byteOffset + buffer.byteLength
        ),
    });

    // 1. Select valid .docx file on Home screen
    const fileInput = container.querySelector(
      '#docx-file-input'
    ) as HTMLInputElement;
    fireEvent.change(fileInput, { target: { files: [docxFile] } });

    // Verify filename and size are displayed on Home screen
    expect(
      screen.getByText('KLTN_Nguyen_Le_Thai_Son_11233561.docx')
    ).toBeTruthy();
    expect(screen.getByText(/0\.31 MB/i)).toBeTruthy();

    // 2. Click START AUDIT -> triggers mammoth extraction + Python /api/audit + transitions to Workspace
    const startBtn = container.querySelector(
      '#start-audit-btn'
    ) as HTMLButtonElement;
    fireEvent.click(startBtn);

    await waitFor(
      () => {
        expect(container.querySelector('#screen-workspace')).toBeTruthy();
      },
      { timeout: 15000 }
    );

    // Verify real thesis title is active in Workspace breadcrumb and DEMO badge is hidden
    expect(
      container.querySelector('#workspace-doc-title')?.textContent
    ).toBe('KLTN_Nguyen_Le_Thai_Son_11233561.docx');
    expect(screen.queryByText(/DEMO PREVIEW/i)).toBeNull();

    // 3. Switch to Insights screen and verify real audited thesis title & chapters
    fireEvent.click(screen.getByRole('button', { name: /Xem Insights/i }));
    expect(container.querySelector('#screen-insights')).toBeTruthy();
    expect(
      screen.getByText('KLTN_Nguyen_Le_Thai_Son_11233561.docx')
    ).toBeTruthy();
  }, 20000);
});
