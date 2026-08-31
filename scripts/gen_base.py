import sys
sys.path.insert(0, '.')
from scripts.writer import write

base_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title or 'NetWatch AI -- Enterprise Network Usage & Intelligence' }}</title>
    <link rel="stylesheet" href="/static/css/app.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="app-shell">
        <!-- Sidebar Navigation -->
        <aside class="app-sidebar" id="main-sidebar">
            <div class="sidebar-header">
                <div class="logo-icon-svg">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M12 2L3 7v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-9-5z"/>
                        <circle cx="12" cy="12" r="3"/>
                    </svg>
                </div>
                <div class="logo-text-box">
                    <div class="logo-title">NetWatch <span style="color:#38bdf8;">AI</span></div>
                    <div class="logo-tagline">Watch Smarter. Detect Faster.</div>
                </div>
            </div>

            <nav class="sidebar-menu">
                <a href="/dashboard" class="nav-item {% if active_page == 'dashboard' or not active_page %}active{% endif %}">
                    <span class="icon">⊞</span><span>Dashboard</span>
                </a>
                <a href="/network/overview" class="nav-item {% if active_page == 'network' %}active{% endif %}">
                    <span class="icon">☷</span><span>Network</span>
                </a>
                <a href="/devices" class="nav-item {% if active_page == 'devices' %}active{% endif %}">
                    <span class="icon">💻</span><span>Devices</span>
                </a>
                <a href="/devices" class="nav-item">
                    <span class="icon">🔍</span><span>IP Lookup</span>
                    <span class="nav-badge nav-badge-green">NEW</span>
                </a>
                <a href="/domains/activity" class="nav-item {% if active_page == 'domains' %}active{% endif %}">
                    <span class="icon">📈</span><span>Activity</span>
                </a>
                <a href="/analytics/bandwidth" class="nav-item {% if active_page == 'analytics' %}active{% endif %}">
                    <span class="icon">📊</span><span>Analytics</span>
                </a>
                <a href="/alerts" class="nav-item {% if active_page == 'alerts' %}active{% endif %}">
                    <span class="icon">🔔</span><span>Alerts</span>
                    <span class="nav-badge nav-badge-red">7</span>
                </a>
                <a href="/incidents" class="nav-item {% if active_page == 'incidents' %}active{% endif %}">
                    <span class="icon">🛡</span><span>Incidents</span>
                    <span class="nav-badge nav-badge-red">3</span>
                </a>
                <a href="/copilot" class="nav-item {% if active_page == 'copilot' %}active{% endif %}">
                    <span class="icon">🤖</span><span>AI Copilot</span>
                    <span class="nav-badge nav-badge-purple">Beta</span>
                </a>
                <a href="/topology" class="nav-item {% if active_page == 'topology' %}active{% endif %}">
                    <span class="icon">🕸</span><span>Topology</span>
                </a>
                <a href="/forecasting" class="nav-item {% if active_page == 'forecasting' %}active{% endif %}">
                    <span class="icon">📉</span><span>Forecasting</span>
                </a>
                <a href="/digital-twin" class="nav-item {% if active_page == 'digital_twin' %}active{% endif %}">
                    <span class="icon">⚙</span><span>Digital Twin</span>
                </a>
                <a href="/reports" class="nav-item {% if active_page == 'reports' %}active{% endif %}">
                    <span class="icon">📑</span><span>Reports</span>
                </a>
                <a href="/policies" class="nav-item {% if active_page == 'policies' %}active{% endif %}">
                    <span class="icon">📜</span><span>Policies</span>
                </a>
                <a href="/audit-logs" class="nav-item {% if active_page == 'audit' %}active{% endif %}">
                    <span class="icon">🔒</span><span>Audit Logs</span>
                </a>
                <a href="/settings" class="nav-item {% if active_page == 'settings' %}active{% endif %}">
                    <span class="icon">⚙</span><span>Settings</span>
                </a>

                <div class="sidebar-section-title">Quick Actions</div>
                <a href="/devices" class="quick-action-btn"><span>➕</span> Add Device</a>
                <a href="/policies" class="quick-action-btn"><span>📄</span> Create Policy</a>
                <a href="/diagnostics/slow-network" class="quick-action-btn"><span>⚡</span> Run Diagnostic</a>
                <a href="/reports" class="quick-action-btn"><span>📊</span> Generate Report</a>
            </nav>

            <div class="sidebar-footer">
                <div class="user-profile-bar" id="profile-dropdown-toggle">
                    <div class="user-avatar-img">
                        <span style="font-weight:700; color:#fff;">AD</span>
                    </div>
                    <div class="user-details">
                        <div class="user-name-title">{{ current_user.full_name if current_user else 'Admin' }}</div>
                        <div class="user-role-subtitle">{{ (current_user.primary_role if current_user else 'Super Administrator') | replace('_', ' ') | title }}</div>
                    </div>
                    <span style="color:var(--text-muted); font-size:0.7rem;">▾</span>
                </div>
                <div class="sidebar-collapse-btn" onclick="toggleSidebar()">
                    <span>≡ Collapse</span>
                    <span>&lt;</span>
                </div>
            </div>
        </aside>

        <!-- Main Content Area -->
        <main class="app-main">
            <!-- Topbar Header -->
            <header class="app-topbar">
                <div class="topbar-left">
                    <button class="topbar-icon-btn" onclick="toggleSidebar()" title="Toggle Navigation">☰</button>
                    <div class="topbar-search-box">
                        <span>🔍</span>
                        <input type="text" id="global-search-input" placeholder="Search for devices, IPs, users, domains, alerts...">
                        <span class="topbar-shortcut">Ctrl + K</span>
                    </div>
                </div>

                <div class="topbar-right">
                    <div class="status-live-pill">
                        <span class="status-dot"></span>
                        <span>Live All systems operational</span>
                    </div>

                    <a href="/alerts" class="topbar-icon-btn" title="Alerts">
                        🔔
                        <span class="topbar-badge">7</span>
                    </a>

                    <a href="/incidents" class="topbar-icon-btn" title="Messages">
                        ✉
                    </a>

                    <a href="/diagnostics/slow-network" class="topbar-icon-btn" title="Help & Diagnostics">
                        ❓
                    </a>

                    <button class="topbar-icon-btn" onclick="toggleFullscreen()" title="Fullscreen">
                        ⛶
                    </button>

                    <button class="topbar-icon-btn" title="Theme Toggle">
                        ☀
                    </button>

                    <div style="display:flex; align-items:center; gap:0.5rem; margin-left:0.5rem; cursor:pointer;" id="topbar-user-menu">
                        <div style="width:28px; height:28px; border-radius:50%; overflow:hidden; border:1.5px solid var(--accent-blue); background:#1e293b; display:flex; align-items:center; justify-content:center; font-size:0.75rem; font-weight:bold; color:#fff;">
                            AD
                        </div>
                        <span style="font-size:0.8rem; font-weight:600;">Admin</span>
                        <span style="font-size:0.65rem; color:var(--text-muted);">▾</span>
                    </div>
                </div>
            </header>

            <!-- Page Container -->
            <section class="page-container">
                {% block content %}{% endblock %}
            </section>

            <!-- App Footer -->
            <footer class="app-footer">
                <div>© 2025 NetWatch AI. All rights reserved.</div>
                <div class="footer-links">
                    <a href="#">Privacy Policy</a>
                    <a href="#">Terms of Service</a>
                    <a href="#">Support</a>
                </div>
            </footer>
        </main>
    </div>

    <!-- Global Toast Container -->
    <div id="toast-container" class="toast-container"></div>

    <script>
        function toggleSidebar() {
            const sb = document.getElementById('main-sidebar');
            if (sb) {
                sb.style.display = (sb.style.display === 'none') ? 'flex' : 'none';
            }
        }
        function toggleFullscreen() {
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen().catch(() => {});
            } else {
                document.exitFullscreen().catch(() => {});
            }
        }
    </script>
    <script type="module" src="/static/js/app.js"></script>
    {% block scripts %}{% endblock %}
</body>
</html>
"""
write('app/templates/base.html', base_html)
print('[+] base.html written!')
