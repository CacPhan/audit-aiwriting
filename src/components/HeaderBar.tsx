import React from 'react';

export type AppScreen = 'home' | 'workspace' | 'insights';

interface HeaderBarProps {
  currentScreen: AppScreen;
  onNavigate: (screen: AppScreen) => void;
  theme: 'dark' | 'light';
  onToggleTheme: () => void;
  onOpenProModal: () => void;
  mascotRef: React.RefObject<SVGSVGElement>;
  pupilLeftRef: React.RefObject<SVGGElement>;
  pupilRightRef: React.RefObject<SVGGElement>;
  isBlinking: boolean;
}

export const HeaderBar: React.FC<HeaderBarProps> = ({
  currentScreen,
  onNavigate,
  theme,
  onToggleTheme,
  onOpenProModal,
  mascotRef,
  pupilLeftRef,
  pupilRightRef,
  isBlinking,
}) => {
  return (
    <header className="glass-nav sticky top-0 z-40">
      <div className="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
        {/* Brand Logo + Mascot */}
        <button
          type="button"
          onClick={() => onNavigate('home')}
          className="group flex items-center gap-3 text-left rounded-xl focus:outline-none"
        >
          <div className="magnetic-icon w-10 h-10 rounded-xl bg-gradient-to-br from-blue-500/20 via-cyan-500/15 to-emerald-500/20 border border-blue-400/30 flex items-center justify-center shadow-md">
            <svg
              ref={mascotRef}
              id="auditor-mascot"
              className={`auditor-mascot w-8 h-8 ${isBlinking ? 'blinking' : ''}`}
              viewBox="0 0 64 64"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
              role="img"
              aria-label="AI Style Auditor"
            >
              <defs>
                <linearGradient
                  id="uvBeamGrad"
                  x1="32"
                  y1="32"
                  x2="64"
                  y2="8"
                  gradientUnits="userSpaceOnUse"
                >
                  <stop offset="0%" stopColor="#38bdf8" stopOpacity="0.55" />
                  <stop offset="60%" stopColor="#10b981" stopOpacity="0.18" />
                  <stop offset="100%" stopColor="#10b981" stopOpacity="0" />
                </linearGradient>
                <clipPath id="eyeClipLeft">
                  <ellipse cx="23" cy="30" rx="7.5" ry="8.5" />
                </clipPath>
                <clipPath id="eyeClipRight">
                  <ellipse cx="41" cy="30" rx="7.5" ry="8.5" />
                </clipPath>
              </defs>
              <polygon
                className="uv-beam"
                points="32,26 64,2 64,46"
                fill="url(#uvBeamGrad)"
              />
              <rect
                x="8"
                y="14"
                width="48"
                height="34"
                rx="17"
                fill="#0f172a"
                stroke="#38bdf8"
                strokeWidth="2.5"
              />
              <ellipse cx="23" cy="30" rx="7.5" ry="8.5" fill="#fffdf9" />
              <g clipPath="url(#eyeClipLeft)">
                <g ref={pupilLeftRef} className="pupil-group" id="pupil-left">
                  <circle cx="23" cy="30" r="4.3" fill="#0284c7" />
                  <circle cx="23" cy="30" r="2.4" fill="#0f172a" />
                  <circle cx="21.5" cy="28.3" r="1.2" fill="#ffffff" />
                </g>
                <rect
                  className="eyelid"
                  x="14"
                  y="20"
                  width="18"
                  height="19"
                  fill="#1e293b"
                  style={{ transform: 'scaleY(0.08)' }}
                />
              </g>
              <ellipse
                cx="23"
                cy="30"
                rx="7.5"
                ry="8.5"
                stroke="#0f172a"
                strokeWidth="1.8"
              />
              <ellipse cx="41" cy="30" rx="7.5" ry="8.5" fill="#fffdf9" />
              <g clipPath="url(#eyeClipRight)">
                <g ref={pupilRightRef} className="pupil-group" id="pupil-right">
                  <circle cx="41" cy="30" r="4.3" fill="#10b981" />
                  <circle cx="41" cy="30" r="2.4" fill="#0f172a" />
                  <circle cx="39.5" cy="28.3" r="1.2" fill="#ffffff" />
                </g>
                <rect
                  className="eyelid"
                  x="32"
                  y="20"
                  width="18"
                  height="19"
                  fill="#1e293b"
                  style={{ transform: 'scaleY(0.08)' }}
                />
              </g>
              <ellipse
                cx="41"
                cy="30"
                rx="7.5"
                ry="8.5"
                stroke="#0f172a"
                strokeWidth="1.8"
              />
              <path
                d="M30.5 30H33.5"
                stroke="#38bdf8"
                strokeWidth="2.2"
                strokeLinecap="round"
              />
              <path d="M32 6L48 12L32 18L16 12L32 6Z" fill="#3b82f6" />
            </svg>
          </div>
          <div>
            <span className="font-display font-extrabold text-base sm:text-lg tracking-tight block leading-none">
              AI Style Auditor
            </span>
            <span className="text-[11px] text-[var(--text-muted)] block mt-1">
              Academic Writing Review
            </span>
          </div>
        </button>

        {/* Center Navigation: 3 Independent Screens (Hidden on Mobile) */}
        <nav
          className="hidden md:flex items-center gap-1 p-1 rounded-full border border-[var(--border-subtle)] bg-[var(--bg-card)] backdrop-blur-md"
          aria-label="Điều hướng chính"
        >
          {(['home', 'workspace', 'insights'] as AppScreen[]).map((scr) => {
            const isActive = currentScreen === scr;
            const label =
              scr === 'home'
                ? 'Home'
                : scr === 'workspace'
                ? 'Workspace'
                : 'Insights';
            return (
              <button
                key={scr}
                type="button"
                onClick={() => onNavigate(scr)}
                className={
                  isActive
                    ? 'main-nav-btn px-4 py-1.5 rounded-full text-xs font-semibold transition-all bg-blue-600 text-white shadow-sm'
                    : 'main-nav-btn px-4 py-1.5 rounded-full text-xs font-semibold text-[var(--text-muted)] hover:text-[var(--text-main)] transition-all'
                }
              >
                {label}
              </button>
            );
          })}
        </nav>

        {/* Right Actions: Theme Switcher + Upgrade Pro (Coming soon) */}
        <div className="flex items-center gap-2.5">
          <button
            id="theme-toggle-btn"
            type="button"
            onClick={onToggleTheme}
            className="magnetic-icon w-9 h-9 rounded-full border border-[var(--border-subtle)] bg-[var(--bg-card)] text-[var(--text-main)] hover:border-blue-400/50 shadow-sm"
            aria-label="Chuyển đổi giao diện Sáng hoặc Tối"
            title="Đổi giao diện Sáng / Tối"
          >
            {theme === 'dark' ? (
              <svg
                id="icon-sun"
                className="w-4 h-4 text-amber-400"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                strokeWidth="2"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"
                />
              </svg>
            ) : (
              <svg
                id="icon-moon"
                className="w-4 h-4 text-orange-600"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                strokeWidth="2"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"
                />
              </svg>
            )}
          </button>

          <button
            type="button"
            onClick={onOpenProModal}
            className="magnetic-icon inline-flex items-center gap-2 px-3.5 py-2 rounded-full text-xs font-semibold text-white bg-gradient-to-r from-violet-600/90 via-indigo-600/90 to-blue-600/90 hover:from-violet-500 hover:to-blue-500 shadow-md shadow-indigo-500/20"
          >
            <span>Upgrade Pro (Coming soon)</span>
          </button>
        </div>
      </div>
    </header>
  );
};
