import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import App from '../../App';

describe('AI Style Auditor Multi-Screen SaaS & 3-Column Workspace Integration', () => {
  it('renders Home screen with .docx upload dropzone, switches to 3-column Workspace, inspects findings, and opens Report & Pro modals', () => {
    render(<App />);

    // 1. Home screen is rendered by default with upload dropzone
    expect(
      screen.getByText(/Kéo thả tài liệu vào đây hoặc chọn tệp từ máy/i)
    ).toBeTruthy();

    // 2. Navigate to Workspace via demo button or nav
    const demoBtn = screen.getByRole('button', {
      name: /Explore Demo với bản thảo mẫu/i,
    });
    fireEvent.click(demoBtn);

    // 3. Verify 3-Column Workspace renders chapter tree, highlighted spans, and diagnostic inspector
    expect(screen.getByText(/Cấu trúc tài liệu/i)).toBeTruthy();
    expect(
      screen.getByText(/Chương 1: Cơ sở lý luận và Tổng quan nghiên cứu/i)
    ).toBeTruthy();
    expect(
      screen.getByText(/Diễn đạt phóng đại thiếu thước đo cụ thể/i)
    ).toBeTruthy();

    // 4. Click another highlighted span in Chapter 1 and verify DiagnosticInspector updates
    const firstSpan = screen.getByText(
      /Trong bối cảnh toàn cầu hóa và cuộc cách mạng công nghiệp diễn ra mạnh mẽ hiện nay,/i
    );
    fireEvent.click(firstSpan);
    expect(
      screen.getByText(/Mở đầu đoạn bằng nhận định vĩ mô chung chung/i)
    ).toBeTruthy();

    // 5. Mark finding as resolved and check progress badge updates
    const resolveBtn = screen.getByRole('button', {
      name: /Đánh dấu đã xử lý/i,
    });
    fireEvent.click(resolveBtn);
    expect(screen.getByText(/Đã xử lý 1\/7/i)).toBeTruthy();

    // 6. Open Report Preview Modal
    const reportBtn = screen.getByRole('button', {
      name: /Xem trước Báo cáo/i,
    });
    fireEvent.click(reportBtn);
    expect(
      screen.getByText(/Báo cáo Kiểm toán Văn phong Học thuật/i)
    ).toBeTruthy();

    // Close Report Modal
    const closeReportBtn = screen.getByRole('button', {
      name: /Đóng bản xem trước/i,
    });
    fireEvent.click(closeReportBtn);

    // 7. Open ProUpgradeModal via Upgrade Pro button
    const proBtn = screen.getByRole('button', {
      name: /Upgrade Pro \(Coming soon\)/i,
    });
    fireEvent.click(proBtn);
    expect(
      screen.getByText(/Tính năng Nâng cao đang được phát triển/i)
    ).toBeTruthy();
  });
});
