import sys
sys.path.insert(0, '.')
from scripts.writer import write

# Variables & Theme
vars_css = '''/* NetWatch AI - Enterprise Cyber Design System Variables */
:root {
    --bg-primary: #0a0e17;
    --bg-secondary: #111827;
    --bg-card: #162032;
    --bg-card-hover: #1c2940;
    --bg-surface: #1f2d47;
    --bg-input: #0e1524;
    
    --border-color: #24344d;
    --border-subtle: #1b263b;
    --border-focus: #38bdf8;
    
    --text-primary: #f8fafc;
    --text-secondary: #94a3b8;
    --text-muted: #64748b;
    --text-disabled: #475569;
    
    /* Cyber Accents */
    --accent-cyan: #00f0ff;
    --accent-blue: #38bdf8;
    --accent-indigo: #6366f1;
    --accent-emerald: #10b981;
    --accent-amber: #f59e0b;
    --accent-rose: #f43f5e;
    --accent-purple: #a855f7;
    
    /* Status Colors */
    --status-optimal: #10b981;
    --status-healthy: #06b6d4;
    --status-degraded: #f59e0b;
    --status-warning: #f97316;
    --status-critical: #ef4444;
    
    /* Risk Levels */
    --risk-negligible: #10b981;
    --risk-low: #38bdf8;
    --risk-moderate: #f59e0b;
    --risk-elevated: #f97316;
    --risk-high: #ef4444;
    --risk-critical: #dc2626;
    
    --sidebar-width: 260px;
    --sidebar-collapsed-width: 72px;
    --topbar-height: 64px;
    --radius-sm: 4px;
    --radius-md: 8px;
    --radius-lg: 12px;
    --radius-xl: 16px;
    --radius-full: 9999px;
    
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.4);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.5), 0 2px 4px -1px rgba(0, 0, 0, 0.4);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.6), 0 4px 6px -2px rgba(0, 0, 0, 0.5);
    --shadow-glow-cyan: 0 0 15px rgba(0, 240, 255, 0.35);
    --shadow-glow-rose: 0 0 15px rgba(244, 63, 94, 0.35);
    --shadow-glow-emerald: 0 0 15px rgba(16, 185, 129, 0.35);
    
    --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    --font-mono: 'JetBrains Mono', 'Fira Code', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    
    --transition-fast: 0.15s ease;
    --transition-normal: 0.25s ease;
    --transition-slow: 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
'''
write('app/static/css/base/variables.css', vars_css)

# Reset & Typography
reset_css = '''*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html, body {
    height: 100%;
    background-color: var(--bg-primary);
    color: var(--text-primary);
    font-family: var(--font-sans);
    font-size: 14px;
    line-height: 1.5;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    overflow-x: hidden;
}

a {
    color: var(--accent-blue);
    text-decoration: none;
    transition: color var(--transition-fast);
}

a:hover {
    color: var(--accent-cyan);
}

button, input, select, textarea {
    font-family: inherit;
    font-size: inherit;
    color: inherit;
    outline: none;
}

ul, ol {
    list-style: none;
}

table {
    border-collapse: collapse;
    width: 100%;
}

img, svg {
    display: inline-block;
    vertical-align: middle;
}

/* Custom Scrollbars */
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}
::-webkit-scrollbar-track {
    background: var(--bg-primary);
}
::-webkit-scrollbar-thumb {
    background: var(--border-color);
    border-radius: var(--radius-full);
}
::-webkit-scrollbar-thumb:hover {
    background: var(--text-muted);
}
'''
write('app/static/css/base/reset.css', reset_css)

# Layout: Shell, Topbar, Sidebar
layout_css = '''/* Main App Layout Grid */
.app-shell {
    display: flex;
    min-height: 100vh;
    background-color: var(--bg-primary);
}

/* Sidebar Navigation */
.app-sidebar {
    width: var(--sidebar-width);
    background-color: var(--bg-secondary);
    border-right: 1px solid var(--border-color);
    display: flex;
    flex-direction: column;
    flex-shrink: 0;
    position: sticky;
    top: 0;
    height: 100vh;
    z-index: 50;
    transition: width var(--transition-normal);
}

.sidebar-header {
    height: var(--topbar-height);
    display: flex;
    align-items: center;
    padding: 0 1.25rem;
    border-bottom: 1px solid var(--border-color);
    gap: 0.75rem;
}

.logo-icon {
    width: 32px;
    height: 32px;
    border-radius: var(--radius-md);
    background: linear-gradient(135deg, var(--accent-cyan), var(--accent-indigo));
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    font-weight: 800;
    font-size: 1.1rem;
    box-shadow: var(--shadow-glow-cyan);
}

.logo-text {
    font-size: 1.1rem;
    font-weight: 700;
    letter-spacing: -0.02em;
    color: var(--text-primary);
}

.logo-tag {
    font-size: 0.65rem;
    padding: 2px 6px;
    border-radius: var(--radius-sm);
    background-color: rgba(0, 240, 255, 0.15);
    color: var(--accent-cyan);
    font-weight: 600;
    text-transform: uppercase;
}

.sidebar-menu {
    flex: 1;
    overflow-y: auto;
    padding: 1rem 0.75rem;
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
}

.menu-section-header {
    font-size: 0.7rem;
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding: 0.75rem 0.5rem 0.25rem 0.5rem;
}

.nav-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.6rem 0.75rem;
    border-radius: var(--radius-md);
    color: var(--text-secondary);
    font-weight: 500;
    transition: all var(--transition-fast);
}

.nav-item:hover {
    background-color: var(--bg-card);
    color: var(--text-primary);
}

.nav-item.active {
    background-color: rgba(56, 189, 248, 0.15);
    color: var(--accent-blue);
    font-weight: 600;
    border-left: 3px solid var(--accent-cyan);
}

.nav-item .icon {
    font-size: 1.1rem;
    width: 20px;
    text-align: center;
}

.sidebar-footer {
    padding: 1rem 1.25rem;
    border-top: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.user-avatar {
    width: 36px;
    height: 36px;
    border-radius: var(--radius-full);
    background: var(--bg-surface);
    border: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    color: var(--accent-cyan);
}

.user-meta {
    flex: 1;
    overflow: hidden;
}

.user-name {
    font-weight: 600;
    font-size: 0.85rem;
    color: var(--text-primary);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.user-role {
    font-size: 0.7rem;
    color: var(--text-muted);
    text-transform: capitalize;
}

/* Main Content Wrapper */
.app-main {
    flex: 1;
    display: flex;
    flex-direction: column;
    min-width: 0;
}

/* Top Navigation Bar */
.app-topbar {
    height: var(--topbar-height);
    background-color: var(--bg-secondary);
    border-bottom: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 1.75rem;
    position: sticky;
    top: 0;
    z-index: 40;
}

.topbar-search {
    display: flex;
    align-items: center;
    background-color: var(--bg-input);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    padding: 0.4rem 0.75rem;
    width: 320px;
    gap: 0.5rem;
    color: var(--text-muted);
    cursor: pointer;
}

.search-shortcut {
    margin-left: auto;
    font-size: 0.7rem;
    background-color: var(--bg-surface);
    padding: 2px 6px;
    border-radius: var(--radius-sm);
    color: var(--text-secondary);
    border: 1px solid var(--border-color);
}

.topbar-actions {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.live-health-pill {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.35rem 0.75rem;
    border-radius: var(--radius-full);
    background-color: rgba(16, 185, 129, 0.12);
    border: 1px solid rgba(16, 185, 129, 0.3);
    color: var(--status-optimal);
    font-size: 0.8rem;
    font-weight: 600;
}

.pulse-dot {
    width: 8px;
    height: 8px;
    border-radius: var(--radius-full);
    background-color: var(--status-optimal);
    box-shadow: 0 0 8px var(--status-optimal);
    animation: pulseGlow 2s infinite;
}

@keyframes pulseGlow {
    0% { transform: scale(0.95); opacity: 0.8; }
    50% { transform: scale(1.2); opacity: 1; }
    100% { transform: scale(0.95); opacity: 0.8; }
}

/* Page Container */
.page-container {
    padding: 1.75rem;
    flex: 1;
    max-width: 1600px;
    margin: 0 auto;
    width: 100%;
}

.page-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1.5rem;
}

.page-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-primary);
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.page-subtitle {
    font-size: 0.85rem;
    color: var(--text-muted);
    margin-top: 0.25rem;
}
'''
write('app/static/css/layout/shell.css', layout_css)

# Components: Cards, Buttons, Tables, Badges, Modals, Gauges
comp_css = '''/* Cyber Defense UI Components */

/* Cards */
.card {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: 1.25rem;
    box-shadow: var(--shadow-sm);
    transition: border-color var(--transition-fast), box-shadow var(--transition-fast);
}

.card:hover {
    border-color: rgba(56, 189, 248, 0.3);
}

.card-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1rem;
}

.card-title {
    font-size: 1rem;
    font-weight: 600;
    color: var(--text-primary);
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

/* Metric KPI Card */
.kpi-card {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.kpi-label {
    font-size: 0.75rem;
    font-weight: 600;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.kpi-value {
    font-size: 1.75rem;
    font-weight: 800;
    color: var(--text-primary);
    font-family: var(--font-mono);
}

.kpi-subtext {
    font-size: 0.75rem;
    display: flex;
    align-items: center;
    gap: 0.35rem;
}

.trend-up { color: var(--status-optimal); }
.trend-down { color: var(--status-critical); }
.trend-neutral { color: var(--text-muted); }

/* Buttons */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.55rem 1rem;
    border-radius: var(--radius-md);
    font-weight: 600;
    font-size: 0.85rem;
    cursor: pointer;
    border: 1px solid transparent;
    transition: all var(--transition-fast);
}

.btn-primary {
    background: linear-gradient(135deg, #0284c7, #0ea5e9);
    color: #fff;
    border-color: #38bdf8;
    box-shadow: 0 0 10px rgba(14, 165, 233, 0.3);
}

.btn-primary:hover {
    background: linear-gradient(135deg, #0369a1, #0284c7);
    box-shadow: 0 0 15px rgba(14, 165, 233, 0.5);
}

.btn-secondary {
    background-color: var(--bg-surface);
    color: var(--text-primary);
    border-color: var(--border-color);
}

.btn-secondary:hover {
    background-color: var(--bg-card-hover);
    border-color: var(--text-muted);
}

.btn-danger {
    background-color: rgba(239, 68, 68, 0.15);
    color: #f87171;
    border-color: rgba(239, 68, 68, 0.3);
}

.btn-danger:hover {
    background-color: #ef4444;
    color: #fff;
}

.btn-sm {
    padding: 0.35rem 0.65rem;
    font-size: 0.75rem;
}

/* Badges */
.badge {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    padding: 0.2rem 0.55rem;
    border-radius: var(--radius-sm);
    font-size: 0.7rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
}

.badge-critical { background: rgba(220, 38, 38, 0.2); color: #f87171; border: 1px solid rgba(220, 38, 38, 0.4); }
.badge-high { background: rgba(249, 115, 22, 0.2); color: #fb923c; border: 1px solid rgba(249, 115, 22, 0.4); }
.badge-medium { background: rgba(245, 158, 11, 0.2); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.4); }
.badge-low { background: rgba(56, 189, 248, 0.2); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); }
.badge-optimal { background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); }

/* Tables */
.data-table-container {
    overflow-x: auto;
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    background-color: var(--bg-card);
}

.data-table th {
    background-color: var(--bg-surface);
    padding: 0.75rem 1rem;
    text-align: left;
    font-size: 0.75rem;
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-bottom: 1px solid var(--border-color);
}

.data-table td {
    padding: 0.85rem 1rem;
    border-bottom: 1px solid var(--border-subtle);
    color: var(--text-secondary);
    font-size: 0.85rem;
}

.data-table tr:hover td {
    background-color: rgba(255, 255, 255, 0.02);
    color: var(--text-primary);
}

/* Modals */
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(10, 14, 23, 0.8);
    backdrop-filter: blur(4px);
    display: none;
    align-items: center;
    justify-content: center;
    z-index: 100;
}

.modal-overlay.active {
    display: flex;
}

.modal-box {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-xl);
    width: 90%;
    max-width: 600px;
    box-shadow: var(--shadow-lg);
    overflow: hidden;
    animation: modalPop 0.25s ease;
}

@keyframes modalPop {
    from { transform: scale(0.95); opacity: 0; }
    to { transform: scale(1); opacity: 1; }
}

.modal-header {
    padding: 1.25rem 1.5rem;
    border-bottom: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.modal-body {
    padding: 1.5rem;
    max-height: 75vh;
    overflow-y: auto;
}

.modal-footer {
    padding: 1rem 1.5rem;
    border-top: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    justify-content: flex-end;
    gap: 0.75rem;
    background-color: var(--bg-secondary);
}

/* Toasts */
.toast-container {
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    z-index: 200;
}

.toast {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 0.75rem 1.25rem;
    border-radius: var(--radius-md);
    box-shadow: var(--shadow-lg);
    display: flex;
    align-items: center;
    gap: 0.75rem;
    min-width: 280px;
    animation: toastSlide 0.3s ease;
}

@keyframes toastSlide {
    from { transform: translateX(100%); opacity: 0; }
    to { transform: translateX(0); opacity: 1; }
}
'''
write('app/static/css/components/components.css', comp_css)

# Master CSS bundle
master_css = '''@import 'base/variables.css';
@import 'base/reset.css';
@import 'layout/shell.css';
@import 'components/components.css';
'''
write('app/static/css/app.css', master_css)

print('Frontend CSS Design System generated.')
