import sys
sys.path.insert(0, '.')
from scripts.writer import write

# 1. variables.css
variables_css = """/* NetWatch AI - Design System Variables */
:root {
    /* Palette */
    --bg-base: #080c14;
    --bg-sidebar: #0b101b;
    --bg-card: #111827;
    --bg-card-hover: #162032;
    --bg-surface: #1e293b;
    --bg-input: #0f172a;
    
    /* Borders */
    --border-color: #1e293b;
    --border-subtle: #192233;
    --border-glow: #3b82f644;

    /* Text Colors */
    --text-primary: #f8fafc;
    --text-secondary: #94a3b8;
    --text-muted: #64748b;
    --text-dim: #475569;

    /* Accent & Brand Colors */
    --accent-blue: #3b82f6;
    --accent-blue-glow: #2563eb;
    --accent-cyan: #06b6d4;
    --accent-purple: #8b5cf6;
    --accent-green: #10b981;
    --accent-amber: #f59e0b;
    --accent-red: #ef4444;
    --accent-orange: #f97316;

    /* Status Colors */
    --status-healthy: #10b981;
    --status-warning: #f59e0b;
    --status-critical: #ef4444;
    --status-offline: #64748b;

    /* Geometry & Shadows */
    --radius-sm: 6px;
    --radius-md: 10px;
    --radius-lg: 14px;
    --radius-full: 9999px;
    --shadow-card: 0 4px 20px -2px rgba(0, 0, 0, 0.4);
    --shadow-glow-blue: 0 0 15px rgba(59, 130, 246, 0.35);
}
"""
write('app/static/css/base/variables.css', variables_css)

# 2. shell.css
shell_css = """/* NetWatch AI - App Shell Layout */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: var(--bg-base);
    color: var(--text-primary);
    min-height: 100vh;
    overflow-x: hidden;
}

.app-shell {
    display: flex;
    min-height: 100vh;
}

/* Sidebar */
.app-sidebar {
    width: 240px;
    background: var(--bg-sidebar);
    border-right: 1px solid var(--border-color);
    display: flex;
    flex-direction: column;
    flex-shrink: 0;
    height: 100vh;
    position: sticky;
    top: 0;
    overflow-y: auto;
    scrollbar-width: thin;
    scrollbar-color: var(--border-color) transparent;
}

.sidebar-header {
    padding: 1.25rem 1rem 1rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.logo-icon-svg {
    width: 36px;
    height: 36px;
    background: linear-gradient(135deg, #6366f1, #3b82f6);
    border-radius: var(--radius-md);
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 12px rgba(99, 102, 241, 0.5);
    flex-shrink: 0;
}

.logo-text-box {
    display: flex;
    flex-direction: column;
}

.logo-title {
    font-size: 1.15rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    color: #ffffff;
    line-height: 1.2;
}

.logo-tagline {
    font-size: 0.65rem;
    color: var(--text-muted);
    font-weight: 500;
}

/* Navigation List */
.sidebar-menu {
    flex: 1;
    padding: 0.5rem 0.75rem;
    display: flex;
    flex-direction: column;
    gap: 0.2rem;
}

.nav-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.55rem 0.75rem;
    border-radius: var(--radius-md);
    color: var(--text-secondary);
    text-decoration: none;
    font-size: 0.85rem;
    font-weight: 500;
    transition: all 0.15s ease;
}

.nav-item:hover {
    color: #ffffff;
    background: var(--bg-surface);
}

.nav-item.active {
    background: var(--accent-blue-glow);
    color: #ffffff;
    font-weight: 600;
    box-shadow: var(--shadow-glow-blue);
}

.nav-item .icon {
    font-size: 1rem;
    width: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0.85;
}

.nav-badge {
    margin-left: auto;
    font-size: 0.65rem;
    font-weight: 700;
    padding: 0.15rem 0.45rem;
    border-radius: var(--radius-full);
}

.nav-badge-green { background: #10b98122; color: #10b981; border: 1px solid #10b98144; }
.nav-badge-red { background: #ef4444; color: #ffffff; min-width: 18px; text-align: center; }
.nav-badge-purple { background: #8b5cf633; color: #c084fc; border: 1px solid #8b5cf655; }

/* Quick Actions */
.sidebar-section-title {
    font-size: 0.65rem;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--text-muted);
    letter-spacing: 0.05em;
    padding: 0.75rem 0.75rem 0.35rem;
}

.quick-action-btn {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    padding: 0.45rem 0.75rem;
    border-radius: var(--radius-md);
    color: var(--text-secondary);
    background: #131d2e;
    border: 1px solid var(--border-subtle);
    font-size: 0.78rem;
    cursor: pointer;
    text-decoration: none;
    margin-bottom: 0.3rem;
    transition: all 0.15s ease;
}

.quick-action-btn:hover {
    background: #1e2b42;
    color: #ffffff;
    border-color: var(--accent-blue);
}

/* Sidebar Footer / User Profile */
.sidebar-footer {
    padding: 0.75rem;
    border-top: 1px solid var(--border-color);
    background: #090e18;
}

.user-profile-bar {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    padding: 0.4rem;
    border-radius: var(--radius-md);
    cursor: pointer;
}

.user-avatar-img {
    width: 32px;
    height: 32px;
    border-radius: var(--radius-full);
    background: #1e293b;
    border: 2px solid var(--accent-blue);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 0.8rem;
}

.user-details {
    flex: 1;
    overflow: hidden;
}

.user-name-title {
    font-size: 0.8rem;
    font-weight: 600;
    color: #ffffff;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.user-role-subtitle {
    font-size: 0.68rem;
    color: var(--text-muted);
}

.sidebar-collapse-btn {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.4rem 0.75rem;
    color: var(--text-muted);
    font-size: 0.75rem;
    cursor: pointer;
    border-top: 1px solid var(--border-subtle);
    margin-top: 0.4rem;
}

/* Main Workspace */
.app-main {
    flex: 1;
    display: flex;
    flex-direction: column;
    min-width: 0;
    background: var(--bg-base);
}

/* Topbar Header */
.app-topbar {
    height: 56px;
    background: var(--bg-sidebar);
    border-bottom: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 1.5rem;
    position: sticky;
    top: 0;
    z-index: 50;
}

.topbar-left {
    display: flex;
    align-items: center;
    gap: 1rem;
    flex: 1;
    max-width: 500px;
}

.topbar-search-box {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    background: var(--bg-input);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    padding: 0.4rem 0.85rem;
    width: 100%;
    color: var(--text-muted);
    font-size: 0.82rem;
}

.topbar-search-box input {
    background: transparent;
    border: none;
    color: #ffffff;
    font-size: 0.82rem;
    width: 100%;
    outline: none;
}

.topbar-shortcut {
    font-size: 0.65rem;
    font-weight: 700;
    background: #1e293b;
    border: 1px solid #334155;
    padding: 0.15rem 0.4rem;
    border-radius: 4px;
    color: var(--text-secondary);
}

.topbar-right {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.status-live-pill {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(16, 185, 129, 0.12);
    border: 1px solid rgba(16, 185, 129, 0.3);
    color: #10b981;
    font-size: 0.75rem;
    font-weight: 600;
    padding: 0.25rem 0.75rem;
    border-radius: var(--radius-full);
}

.status-dot {
    width: 7px;
    height: 7px;
    background: #10b981;
    border-radius: 50%;
    box-shadow: 0 0 8px #10b981;
}

.topbar-icon-btn {
    background: transparent;
    border: none;
    color: var(--text-secondary);
    font-size: 1.1rem;
    cursor: pointer;
    position: relative;
    padding: 0.3rem;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: var(--radius-sm);
}

.topbar-icon-btn:hover {
    color: #ffffff;
    background: var(--bg-surface);
}

.topbar-badge {
    position: absolute;
    top: -2px;
    right: -2px;
    background: #ef4444;
    color: #ffffff;
    font-size: 0.6rem;
    font-weight: 700;
    width: 15px;
    height: 15px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Page Workspace */
.page-container {
    flex: 1;
    padding: 1.5rem 1.75rem;
}

/* App Footer */
.app-footer {
    padding: 1.25rem 1.75rem;
    border-top: 1px solid var(--border-color);
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.75rem;
    color: var(--text-muted);
}

.footer-links {
    display: flex;
    gap: 1.5rem;
}

.footer-links a {
    color: var(--text-muted);
    text-decoration: none;
}

.footer-links a:hover {
    color: var(--text-secondary);
}
"""
write('app/static/css/layout/shell.css', shell_css)

# 3. components.css
components_css = """/* NetWatch AI - Reusable Dashboard Components */
.greeting-header {
    margin-bottom: 1.25rem;
}

.greeting-title {
    font-size: 1.4rem;
    font-weight: 700;
    color: #ffffff;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.greeting-subtitle {
    font-size: 0.82rem;
    color: var(--text-muted);
    margin-top: 0.2rem;
}

/* Card Base */
.nw-card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: 1.15rem;
    position: relative;
    box-shadow: var(--shadow-card);
}

.nw-card:hover {
    border-color: #27354a;
}

.card-title-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.85rem;
}

.card-title-text {
    font-size: 0.88rem;
    font-weight: 600;
    color: #ffffff;
    display: flex;
    align-items: center;
    gap: 0.4rem;
}

.card-header-link {
    font-size: 0.75rem;
    color: var(--accent-blue);
    text-decoration: none;
    font-weight: 500;
}

.card-header-link:hover {
    text-decoration: underline;
}

/* Top 6 KPI Metric Cards */
.kpi-row-grid {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 1rem;
    margin-bottom: 1.25rem;
}

@media (max-width: 1400px) {
    .kpi-row-grid { grid-template-columns: repeat(3, 1fr); }
}

@media (max-width: 900px) {
    .kpi-row-grid { grid-template-columns: repeat(2, 1fr); }
}

.kpi-box {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: 1rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 125px;
    position: relative;
    overflow: hidden;
}

.kpi-top-row {
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.kpi-icon-square {
    width: 32px;
    height: 32px;
    border-radius: var(--radius-sm);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1rem;
    flex-shrink: 0;
}

.kpi-icon-blue { background: rgba(59, 130, 246, 0.15); color: #3b82f6; }
.kpi-icon-red { background: rgba(239, 68, 68, 0.15); color: #ef4444; }
.kpi-icon-purple { background: rgba(139, 92, 246, 0.15); color: #8b5cf6; }
.kpi-icon-amber { background: rgba(245, 158, 11, 0.15); color: #f59e0b; }
.kpi-icon-orange { background: rgba(249, 115, 22, 0.15); color: #f97316; }

.kpi-title-label {
    font-size: 0.75rem;
    color: var(--text-muted);
    font-weight: 500;
}

.kpi-main-val {
    font-size: 1.45rem;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.1;
    margin-top: 0.2rem;
}

.kpi-trend-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 0.7rem;
    margin-top: 0.35rem;
}

.trend-pos { color: #10b981; }
.trend-neg { color: #ef4444; }
.trend-info { color: #3b82f6; }

.kpi-sparkline {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 28px;
    pointer-events: none;
    opacity: 0.7;
}

/* Second Row Grid (Traffic, Top Domains, Topology, IP Lookup) */
.dash-row-2 {
    display: grid;
    grid-template-columns: 2.2fr 1.3fr 1.5fr 1.2fr;
    gap: 1rem;
    margin-bottom: 1.25rem;
}

@media (max-width: 1400px) {
    .dash-row-2 { grid-template-columns: 1fr 1fr; }
}

@media (max-width: 900px) {
    .dash-row-2 { grid-template-columns: 1fr; }
}

/* Metric stats pill strip */
.metrics-strip {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0.5rem;
    padding-top: 0.75rem;
    margin-top: 0.75rem;
    border-top: 1px solid var(--border-subtle);
    text-align: center;
}

.metric-strip-item .val {
    font-size: 0.95rem;
    font-weight: 700;
}

.metric-strip-item .lbl {
    font-size: 0.65rem;
    color: var(--text-muted);
}

/* Domain List Legend */
.domain-legend-list {
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
    font-size: 0.75rem;
}

.domain-legend-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.domain-legend-left {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    color: var(--text-secondary);
}

.color-bullet {
    width: 8px;
    height: 8px;
    border-radius: 2px;
}

/* Third Row Grid (Device Health, Risk Dist, AI Copilot, Maintenance) */
.dash-row-3 {
    display: grid;
    grid-template-columns: 1.2fr 1.2fr 1.6fr 1.2fr;
    gap: 1rem;
    margin-bottom: 1.25rem;
}

@media (max-width: 1400px) {
    .dash-row-3 { grid-template-columns: 1fr 1fr; }
}

@media (max-width: 900px) {
    .dash-row-3 { grid-template-columns: 1fr; }
}

/* AI Copilot Widget */
.copilot-card {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.copilot-chips-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.4rem;
    margin: 0.75rem 0;
}

.copilot-chip {
    background: #141f33;
    border: 1px solid #1e2f4d;
    padding: 0.45rem 0.6rem;
    border-radius: var(--radius-md);
    font-size: 0.72rem;
    color: var(--text-secondary);
    cursor: pointer;
    text-align: left;
    transition: all 0.15s ease;
}

.copilot-chip:hover {
    background: #1b2a47;
    color: #ffffff;
    border-color: var(--accent-blue);
}

.copilot-input-bar {
    display: flex;
    align-items: center;
    background: var(--bg-input);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    padding: 0.35rem 0.6rem;
    margin-top: 0.5rem;
}

.copilot-input-bar input {
    flex: 1;
    background: transparent;
    border: none;
    color: #ffffff;
    font-size: 0.78rem;
    outline: none;
}

.copilot-send-btn {
    background: var(--accent-blue);
    border: none;
    color: #ffffff;
    width: 26px;
    height: 26px;
    border-radius: var(--radius-sm);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
}

/* Fourth Row Grid (Bandwidth Consumers, Incidents, System Status) */
.dash-row-4 {
    display: grid;
    grid-template-columns: 1.4fr 2.6fr 1.2fr;
    gap: 1rem;
}

@media (max-width: 1400px) {
    .dash-row-4 { grid-template-columns: 1fr; }
}

/* Consumers Progress Bars */
.consumer-item {
    margin-bottom: 0.6rem;
}

.consumer-meta {
    display: flex;
    justify-content: space-between;
    font-size: 0.75rem;
    margin-bottom: 0.25rem;
}

.consumer-bar-bg {
    height: 5px;
    background: #1e293b;
    border-radius: 4px;
    overflow: hidden;
}

.consumer-bar-fill {
    height: 100%;
    background: linear-gradient(90deg, #3b82f6, #06b6d4);
    border-radius: 4px;
}

/* Incident Table */
.inc-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.75rem;
}

.inc-table th {
    text-align: left;
    color: var(--text-muted);
    padding: 0.4rem 0.5rem;
    font-weight: 500;
    border-bottom: 1px solid var(--border-subtle);
}

.inc-table td {
    padding: 0.55rem 0.5rem;
    border-bottom: 1px solid var(--border-subtle);
    color: var(--text-secondary);
}

.sev-badge {
    font-size: 0.65rem;
    font-weight: 700;
    padding: 0.15rem 0.45rem;
    border-radius: 4px;
}

.sev-critical { background: rgba(239, 68, 68, 0.2); color: #ef4444; }
.sev-high { background: rgba(249, 115, 22, 0.2); color: #f97316; }
.sev-medium { background: rgba(245, 158, 11, 0.2); color: #f59e0b; }

/* System Status Grid */
.system-status-grid {
    display: flex;
    flex-direction: column;
    gap: 0.6rem;
}

.service-status-pill {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.45rem 0.7rem;
    background: #0f1624;
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-md);
    font-size: 0.75rem;
}

.service-status-healthy {
    color: #10b981;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 0.35rem;
}

.service-status-healthy::before {
    content: '●';
    font-size: 0.7rem;
}
"""
write('app/static/css/components/components.css', components_css)

# 4. app.css
app_css = """/* NetWatch AI Master Stylesheet */
@import url('base/variables.css');
@import url('base/reset.css');
@import url('layout/shell.css');
@import url('components/components.css');
"""
write('app/static/css/app.css', app_css)

print('[+] Redesigned CSS system generated successfully!')
