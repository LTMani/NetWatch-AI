import sys
sys.path.insert(0, '.')
from scripts.writer import write

# base.html
base_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title or 'NetWatch AI -- Enterprise Network Intelligence' }}</title>
    <link rel="stylesheet" href="/static/css/app.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;800&display=swap" rel="stylesheet">
</head>
<body>
    <div class="app-shell">
        <!-- Sidebar Navigation -->
        <aside class="app-sidebar">
            <div class="sidebar-header">
                <div class="logo-icon">NW</div>
                <div class="logo-text">NetWatch <span style="color:var(--accent-cyan);">AI</span></div>
                <span class="logo-tag">PRO</span>
            </div>

            <nav class="sidebar-menu">
                <div class="menu-section-header">Command & Telemetry</div>
                <a href="/dashboard" class="nav-item {% if active_page == 'dashboard' %}active{% endif %}">
                    <span class="icon">⊞</span><span>Dashboard</span>
                </a>
                <a href="/network/overview" class="nav-item {% if active_page == 'network' %}active{% endif %}">
                    <span class="icon">☷</span><span>Network Overview</span>
                </a>
                <a href="/devices" class="nav-item {% if active_page == 'devices' %}active{% endif %}">
                    <span class="icon">💻</span><span>Device Inventory</span>
                </a>
                <a href="/topology" class="nav-item {% if active_page == 'topology' %}active{% endif %}">
                    <span class="icon">🕸</span><span>Network Topology</span>
                </a>

                <div class="menu-section-header">Analytics & Traffic</div>
                <a href="/domains/activity" class="nav-item {% if active_page == 'domains' %}active{% endif %}">
                    <span class="icon">🌐</span><span>Domain Activity</span>
                </a>
                <a href="/analytics/bandwidth" class="nav-item {% if active_page == 'analytics' %}active{% endif %}">
                    <span class="icon">📊</span><span>Bandwidth Analytics</span>
                </a>
                <a href="/analytics/office-hours" class="nav-item {% if active_page == 'office_hours' %}active{% endif %}">
                    <span class="icon">⏱</span><span>Office Hours</span>
                </a>

                <div class="menu-section-header">Intelligence & Diagnostics</div>
                <a href="/health" class="nav-item {% if active_page == 'health' %}active{% endif %}">
                    <span class="icon">♥</span><span>Health Engine</span>
                </a>
                <a href="/diagnostics/slow-network" class="nav-item {% if active_page == 'diagnostics' %}active{% endif %}">
                    <span class="icon">⚡</span><span>Slow Network Wizard</span>
                </a>
                <a href="/anomalies" class="nav-item {% if active_page == 'anomalies' %}active{% endif %}">
                    <span class="icon">⚠</span><span>Anomaly Center</span>
                </a>
                <a href="/risk" class="nav-item {% if active_page == 'risk' %}active{% endif %}">
                    <span class="icon">🛡</span><span>Asset Risk Posture</span>
                </a>
                <a href="/copilot" class="nav-item {% if active_page == 'copilot' %}active{% endif %}">
                    <span class="icon">🤖</span><span>AI Copilot</span>
                </a>

                <div class="menu-section-header">Response & Security</div>
                <a href="/alerts" class="nav-item {% if active_page == 'alerts' %}active{% endif %}">
                    <span class="icon">🔔</span><span>Correlated Alerts</span>
                </a>
                <a href="/incidents" class="nav-item {% if active_page == 'incidents' %}active{% endif %}">
                    <span class="icon">🚨</span><span>Incident Board</span>
                </a>
                <a href="/policies" class="nav-item {% if active_page == 'policies' %}active{% endif %}">
                    <span class="icon">📜</span><span>Traffic Policies</span>
                </a>
                <a href="/digital-twin" class="nav-item {% if active_page == 'digital_twin' %}active{% endif %}">
                    <span class="icon">⚇</span><span>Digital Twin Simulator</span>
                </a>
                <a href="/forecasting" class="nav-item {% if active_page == 'forecasting' %}active{% endif %}">
                    <span class="icon">📈</span><span>Capacity Forecast</span>
                </a>

                <div class="menu-section-header">Governance & System</div>
                <a href="/reports" class="nav-item {% if active_page == 'reports' %}active{% endif %}">
                    <span class="icon">📑</span><span>Executive Reports</span>
                </a>
                <a href="/audit-logs" class="nav-item {% if active_page == 'audit' %}active{% endif %}">
                    <span class="icon">🔒</span><span>Audit Trail</span>
                </a>
                <a href="/users" class="nav-item {% if active_page == 'users' %}active{% endif %}">
                    <span class="icon">👥</span><span>User Management</span>
                </a>
                <a href="/settings" class="nav-item {% if active_page == 'settings' %}active{% endif %}">
                    <span class="icon">⚙</span><span>Settings & Privacy</span>
                </a>
            </nav>

            <div class="sidebar-footer">
                <div class="user-avatar">{{ (current_user.full_name[0] if current_user else 'A') | upper }}</div>
                <div class="user-meta">
                    <div class="user-name">{{ current_user.full_name if current_user else 'Administrator' }}</div>
                    <div class="user-role">{{ (current_user.primary_role if current_user else 'Super Admin') | replace('_', ' ') }}</div>
                </div>
                <button id="btn-logout" title="Sign Out" style="background:none; border:none; color:var(--text-muted); cursor:pointer; font-size:1.1rem;">⎋</button>
            </div>
        </aside>

        <!-- Main Workspace -->
        <main class="app-main">
            <!-- Topbar Header -->
            <header class="app-topbar">
                <div class="topbar-search">
                    <span>🔍</span>
                    <span>Search devices, IPs, policies...</span>
                    <span class="search-shortcut">Ctrl+K</span>
                </div>

                <div class="topbar-actions">
                    <div class="live-health-pill">
                        <span class="pulse-dot"></span>
                        <span id="topbar-health-score">Health: 98/100</span>
                    </div>
                    <a href="/copilot" class="btn btn-secondary btn-sm">🤖 AI Copilot</a>
                    <a href="/reports" class="btn btn-primary btn-sm">Export Report</a>
                </div>
            </header>

            <!-- Page Content Injection -->
            <section class="page-container">
                {% block content %}{% endblock %}
            </section>
        </main>
    </div>

    <!-- Global Toast Container -->
    <div id="toast-container" class="toast-container"></div>

    <script type="module" src="/static/js/app.js"></script>
    {% block scripts %}{% endblock %}
</body>
</html>
'''
write('app/templates/base.html', base_html)

# landing.html
landing_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NetWatch AI -- Watch Smarter. Detect Faster.</title>
    <link rel="stylesheet" href="/static/css/app.css">
    <style>
        .landing-hero {
            padding: 6rem 2rem 4rem;
            text-align: center;
            max-width: 1000px;
            margin: 0 auto;
        }
        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.4rem 1rem;
            border-radius: var(--radius-full);
            background: rgba(0, 240, 255, 0.1);
            border: 1px solid rgba(0, 240, 255, 0.3);
            color: var(--accent-cyan);
            font-weight: 600;
            font-size: 0.85rem;
            margin-bottom: 1.5rem;
        }
        .hero-title {
            font-size: 3.5rem;
            font-weight: 800;
            line-height: 1.15;
            letter-spacing: -0.03em;
            margin-bottom: 1.5rem;
            background: linear-gradient(135deg, #ffffff 30%, #38bdf8 70%, #00f0ff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .hero-desc {
            font-size: 1.25rem;
            color: var(--text-secondary);
            margin-bottom: 2.5rem;
            line-height: 1.6;
        }
        .hero-cta-group {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1.25rem;
        }
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            max-width: 1200px;
            margin: 4rem auto;
            padding: 0 2rem;
        }
        .feature-card {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-xl);
            padding: 2rem;
            transition: all var(--transition-normal);
        }
        .feature-card:hover {
            border-color: var(--accent-cyan);
            transform: translateY(-4px);
            box-shadow: var(--shadow-glow-cyan);
        }
        .feature-icon {
            font-size: 2rem;
            margin-bottom: 1rem;
            display: inline-block;
        }
    </style>
</head>
<body style="background: radial-gradient(circle at 50% 10%, #162032 0%, #0a0e17 60%);">
    <header style="display:flex; justify-content:space-between; align-items:center; padding: 1.5rem 3rem; border-bottom: 1px solid var(--border-subtle);">
        <div style="display:flex; align-items:center; gap:0.75rem;">
            <div class="logo-icon">NW</div>
            <div style="font-size:1.3rem; font-weight:800; color:var(--text-primary);">NetWatch <span style="color:var(--accent-cyan);">AI</span></div>
        </div>
        <div>
            <a href="/login" class="btn btn-primary">Launch Console ➔</a>
        </div>
    </header>

    <section class="landing-hero">
        <div class="hero-badge">⚡ Next-Gen Enterprise Network Intelligence</div>
        <h1 class="hero-title">Watch Smarter.<br>Detect Faster.</h1>
        <p class="hero-desc">
            AI-driven network monitoring, 7-stage automated slow network diagnostics, anomaly detection, real-time risk scoring, and grounded copilot intelligence built strictly for authorized enterprise environments.
        </p>
        <div class="hero-cta-group">
            <a href="/login" class="btn btn-primary" style="padding:0.85rem 2rem; font-size:1rem;">Access Live Platform</a>
            <a href="/dashboard" class="btn btn-secondary" style="padding:0.85rem 2rem; font-size:1rem;">Interactive Demo</a>
        </div>
    </section>

    <section class="feature-grid">
        <div class="feature-card">
            <div class="feature-icon">♥</div>
            <h3 style="font-size:1.2rem; font-weight:700; margin-bottom:0.5rem;">Network Health Engine</h3>
            <p style="color:var(--text-secondary); line-height:1.6;">Composite health score (0-100) combining path latency, jitter, packet drop clusters, error rates, and link flaps.</p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <h3 style="font-size:1.2rem; font-weight:700; margin-bottom:0.5rem;">7-Stage Slow Network Wizard</h3>
            <p style="color:var(--text-secondary); line-height:1.6;">Automated step-by-step diagnostic pipeline pinpointing bottlenecks across gateways, DNS resolvers, and bandwidth saturations.</p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">🛡</div>
            <h3 style="font-size:1.2rem; font-weight:700; margin-bottom:0.5rem;">Asset Risk Posture</h3>
            <p style="color:var(--text-secondary); line-height:1.6;">Dynamic Bayesian-decay risk scoring identifying vulnerable devices, policy infractions, and threat intelligence matches.</p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <h3 style="font-size:1.2rem; font-weight:700; margin-bottom:0.5rem;">Grounded AI Copilot</h3>
            <p style="color:var(--text-secondary); line-height:1.6;">Natural language query engine grounded in real database telemetry. Answers "Why is the network slow?" with verified evidence.</p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">🕸</div>
            <h3 style="font-size:1.2rem; font-weight:700; margin-bottom:0.5rem;">Interactive Topology</h3>
            <p style="color:var(--text-secondary); line-height:1.6;">Hierarchical force-directed network topology canvas with live link bandwidth overlays and node inspection modals.</p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">🔒</div>
            <h3 style="font-size:1.2rem; font-weight:700; margin-bottom:0.5rem;">Zero Payload Privacy</h3>
            <p style="color:var(--text-secondary); line-height:1.6;">Strict enterprise privacy boundaries inspecting only metadata, domains, and bandwidth without capturing private messages or keystrokes.</p>
        </div>
    </section>

    <footer style="text-align:center; padding:3rem; border-top:1px solid var(--border-subtle); color:var(--text-muted); font-size:0.85rem;">
        NetWatch AI Enterprise Platform. Authorized Corporate Network Monitoring.
    </footer>
</body>
</html>
'''
write('app/templates/landing.html', landing_html)

# auth/login.html
login_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign In -- NetWatch AI</title>
    <link rel="stylesheet" href="/static/css/app.css">
    <style>
        .auth-container {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background: radial-gradient(circle at 50% 20%, #162032 0%, #0a0e17 70%);
            padding: 1.5rem;
        }
        .auth-card {
            width: 100%;
            max-width: 440px;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-xl);
            padding: 2.5rem;
            box-shadow: var(--shadow-lg);
        }
        .form-group {
            margin-bottom: 1.25rem;
        }
        .form-label {
            display: block;
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--text-secondary);
            margin-bottom: 0.4rem;
        }
        .form-input {
            width: 100%;
            padding: 0.65rem 0.85rem;
            background-color: var(--bg-input);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            color: var(--text-primary);
            font-size: 0.9rem;
            transition: border-color var(--transition-fast);
        }
        .form-input:focus {
            border-color: var(--accent-cyan);
            box-shadow: 0 0 8px rgba(0, 240, 255, 0.2);
        }
        .demo-accounts {
            margin-top: 1.5rem;
            padding: 1rem;
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-md);
            font-size: 0.75rem;
        }
    </style>
</head>
<body>
    <div class="auth-container">
        <div class="auth-card">
            <div style="text-align:center; margin-bottom:2rem;">
                <div class="logo-icon" style="margin:0 auto 0.75rem; width:44px; height:44px; font-size:1.3rem;">NW</div>
                <h2 style="font-size:1.5rem; font-weight:800; color:var(--text-primary);">NetWatch <span style="color:var(--accent-cyan);">AI</span></h2>
                <p style="color:var(--text-muted); font-size:0.85rem; margin-top:0.25rem;">Enterprise Telemetry & Intelligence Console</p>
            </div>

            <form id="form-login">
                <div class="form-group">
                    <label class="form-label" for="identifier">Username or Corporate Email</label>
                    <input type="text" id="identifier" name="identifier" class="form-input" placeholder="admin@netwatch.internal" required autofocus value="admin@netwatch.internal">
                </div>

                <div class="form-group">
                    <label class="form-label" for="password">Security Password</label>
                    <input type="password" id="password" name="password" class="form-input" placeholder="••••••••••••" required value="Admin@NetWatch2026!">
                </div>

                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem; font-size:0.8rem;">
                    <label style="display:flex; align-items:center; gap:0.4rem; cursor:pointer; color:var(--text-secondary);">
                        <input type="checkbox" id="remember_me" name="remember_me" checked> Remember Device
                    </label>
                    <a href="#" style="color:var(--accent-blue);">Forgot Key?</a>
                </div>

                <button type="submit" id="btn-submit-login" class="btn btn-primary" style="width:100%; padding:0.75rem;">Authorize & Sign In</button>
            </form>

            <div class="demo-accounts">
                <div style="font-weight:700; color:var(--accent-cyan); margin-bottom:0.4rem;">🔑 Enterprise Pre-Loaded Credentials:</div>
                <div style="color:var(--text-secondary);">Super Admin: <code>admin@netwatch.internal</code> / <code>Admin@NetWatch2026!</code></div>
                <div style="color:var(--text-secondary);">Analyst: <code>analyst@netwatch.internal</code> / <code>Analyst@2026!</code></div>
            </div>
        </div>
    </div>

    <div id="toast-container" class="toast-container"></div>

    <script type="module">
        import { HttpClient } from '/static/js/core/http.js';
        import { Toast } from '/static/js/components/toast.js';

        document.getElementById('form-login').addEventListener('submit', async (e) => {
            e.preventDefault();
            const btn = document.getElementById('btn-submit-login');
            btn.disabled = true;
            btn.textContent = 'Authenticating...';

            const identifier = document.getElementById('identifier').value.trim();
            const password = document.getElementById('password').value;
            const remember_me = document.getElementById('remember_me').checked;

            try {
                const res = await HttpClient.post('/api/v1/auth/login', {
                    identifier, password, remember_me
                });
                if (res.status === 'success') {
                    localStorage.setItem('nw_token', res.data.access_token);
                    Toast.success('Authentication granted. Redirecting to console...');
                    setTimeout(() => window.location.href = '/dashboard', 600);
                }
            } catch (err) {
                Toast.error(err.message || 'Login failed. Please check credentials.');
                btn.disabled = false;
                btn.textContent = 'Authorize & Sign In';
            }
        });
    </script>
</body>
</html>
'''
write('app/templates/auth/login.html', login_html)

# auth/register.html
register_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Enterprise Account -- NetWatch AI</title>
    <link rel="stylesheet" href="/static/css/app.css">
</head>
<body style="min-height:100vh; display:flex; align-items:center; justify-content:center; background: radial-gradient(circle at 50% 20%, #162032 0%, #0a0e17 70%);">
    <div style="width:100%; max-width:480px; background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-xl); padding:2.5rem;">
        <div style="text-align:center; margin-bottom:2rem;">
            <div class="logo-icon" style="margin:0 auto 0.75rem;">NW</div>
            <h2 style="font-size:1.5rem; font-weight:800; color:var(--text-primary);">Register Account</h2>
            <p style="color:var(--text-muted); font-size:0.85rem;">Authorized Personnel Access Provisioning</p>
        </div>

        <form id="form-register">
            <div style="margin-bottom:1.25rem;">
                <label style="display:block; font-size:0.8rem; font-weight:600; margin-bottom:0.4rem; color:var(--text-secondary);">Full Name</label>
                <input type="text" id="full_name" class="form-input" style="width:100%; padding:0.65rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;" required placeholder="Jane Doe">
            </div>

            <div style="margin-bottom:1.25rem;">
                <label style="display:block; font-size:0.8rem; font-weight:600; margin-bottom:0.4rem; color:var(--text-secondary);">Username</label>
                <input type="text" id="username" class="form-input" style="width:100%; padding:0.65rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;" required placeholder="janedoe">
            </div>

            <div style="margin-bottom:1.25rem;">
                <label style="display:block; font-size:0.8rem; font-weight:600; margin-bottom:0.4rem; color:var(--text-secondary);">Corporate Email</label>
                <input type="email" id="email" class="form-input" style="width:100%; padding:0.65rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;" required placeholder="jane@netwatch.internal">
            </div>

            <div style="margin-bottom:1.5rem;">
                <label style="display:block; font-size:0.8rem; font-weight:600; margin-bottom:0.4rem; color:var(--text-secondary);">Password (8+ chars)</label>
                <input type="password" id="password" class="form-input" style="width:100%; padding:0.65rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;" required placeholder="••••••••••••">
            </div>

            <button type="submit" class="btn btn-primary" style="width:100%; padding:0.75rem;">Create Account</button>
            <div style="text-align:center; margin-top:1rem; font-size:0.85rem;">
                <a href="/login" style="color:var(--accent-blue);">Already registered? Sign In</a>
            </div>
        </form>
    </div>
</body>
</html>
'''
write('app/templates/auth/register.html', register_html)

print('Template Batch 1 (Base, Landing, Auth) created.')
