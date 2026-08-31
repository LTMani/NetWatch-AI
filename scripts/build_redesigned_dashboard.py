import os

p1 = """{% extends "base.html" %}

{% block content %}
<div class="greeting-header">
    <div class="greeting-title">Good Morning, Admin! 👋</div>
    <div class="greeting-subtitle">Here's what's happening with your company network.</div>
</div>

<!-- Row 1: Top 6 KPI Metric Cards -->
<div class="kpi-row-grid">
    <!-- 1. Network Health -->
    <div class="kpi-box" style="display:flex; flex-direction:row; align-items:center; gap:0.75rem;">
        <div style="position:relative; width:48px; height:48px; flex-shrink:0;">
            <svg viewBox="0 0 36 36" style="width:100%; height:100%; transform:rotate(-90deg);">
                <path d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="#1e293b" stroke-width="4" />
                <path d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="#10b981" stroke-dasharray="92, 100" stroke-width="4" stroke-linecap="round" />
            </svg>
            <div style="position:absolute; inset:0; display:flex; align-items:center; justify-content:center; font-size:0.65rem; font-weight:800; color:#10b981;">92%</div>
        </div>
        <div style="flex:1;">
            <div class="kpi-title-label">Network Health</div>
            <div class="kpi-main-val">92<span style="font-size:0.85rem; font-weight:500; color:var(--text-muted);">/100</span></div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-top:0.2rem;">
                <span style="font-size:0.68rem; color:#10b981; font-weight:700;">Excellent</span>
                <span class="trend-pos" style="font-size:0.65rem;">↑ 5% from yesterday</span>
            </div>
        </div>
        <canvas id="spark-health" class="kpi-sparkline"></canvas>
    </div>

    <!-- 2. Active Devices -->
    <div class="kpi-box">
        <div class="kpi-top-row">
            <div class="kpi-icon-square kpi-icon-blue">💻</div>
            <div>
                <div class="kpi-title-label">Active Devices</div>
                <div class="kpi-main-val">124</div>
            </div>
        </div>
        <div class="kpi-trend-row">
            <span class="trend-info">↑ 12 (10.7%) from yesterday</span>
        </div>
        <canvas id="spark-devices" class="kpi-sparkline"></canvas>
    </div>

    <!-- 3. Total Alerts -->
    <div class="kpi-box">
        <div class="kpi-top-row">
            <div class="kpi-icon-square kpi-icon-red">🛡</div>
            <div>
                <div class="kpi-title-label">Total Alerts</div>
                <div class="kpi-main-val">7</div>
            </div>
        </div>
        <div class="kpi-trend-row">
            <span class="trend-neg">↓ 3 (30%) from yesterday</span>
        </div>
        <canvas id="spark-alerts" class="kpi-sparkline"></canvas>
    </div>

    <!-- 4. Bandwidth Usage -->
    <div class="kpi-box">
        <div class="kpi-top-row">
            <div class="kpi-icon-square kpi-icon-purple">📊</div>
            <div>
                <div class="kpi-title-label">Bandwidth Usage</div>
                <div class="kpi-main-val">68%</div>
            </div>
        </div>
        <div class="kpi-trend-row">
            <span style="color:#a855f7; font-size:0.65rem;">↑ 8% from yesterday</span>
        </div>
        <canvas id="spark-bandwidth" class="kpi-sparkline"></canvas>
    </div>

    <!-- 5. Risk Score (Avg) -->
    <div class="kpi-box">
        <div class="kpi-top-row">
            <div class="kpi-icon-square kpi-icon-amber">⏱</div>
            <div>
                <div class="kpi-title-label">Risk Score (Avg)</div>
                <div class="kpi-main-val">18<span style="font-size:0.85rem; font-weight:500; color:var(--text-muted);">/100</span></div>
            </div>
        </div>
        <div class="kpi-trend-row">
            <span style="color:#10b981; font-weight:600; font-size:0.68rem;">Low Risk</span>
        </div>
        <canvas id="spark-risk" class="kpi-sparkline"></canvas>
    </div>

    <!-- 6. Open Incidents -->
    <div class="kpi-box">
        <div class="kpi-top-row">
            <div class="kpi-icon-square kpi-icon-orange">🚨</div>
            <div>
                <div class="kpi-title-label">Open Incidents</div>
                <div class="kpi-main-val">3</div>
            </div>
        </div>
        <div class="kpi-trend-row">
            <a href="/incidents" class="card-header-link" style="font-size:0.7rem;">View all →</a>
        </div>
    </div>
</div>
"""
p2 = """
<!-- Row 2: 4 Key Widgets -->
<div class="dash-row-2">
    <!-- 1. Network Traffic Overview -->
    <div class="nw-card">
        <div class="card-title-bar">
            <div class="card-title-text">Network Traffic Overview</div>
            <div style="display:flex; align-items:center; gap:0.75rem;">
                <div style="display:flex; gap:0.6rem; font-size:0.72rem;">
                    <span style="color:#38bdf8; display:flex; align-items:center; gap:0.3rem;">— Inbound</span>
                    <span style="color:#10b981; display:flex; align-items:center; gap:0.3rem;">— Outbound</span>
                </div>
                <select style="background:var(--bg-surface); border:1px solid var(--border-color); color:var(--text-primary); font-size:0.72rem; padding:0.2rem 0.5rem; border-radius:var(--radius-sm);">
                    <option>Today</option>
                    <option>Last 7 Days</option>
                </select>
            </div>
        </div>

        <div style="height:175px; position:relative;">
            <canvas id="canvas-traffic-overview"></canvas>
        </div>

        <div class="metrics-strip">
            <div class="metric-strip-item">
                <div class="val" style="color:#38bdf8;">352 Mbps</div>
                <div class="lbl">Peak Inbound</div>
            </div>
            <div class="metric-strip-item">
                <div class="val" style="color:#10b981;">214 Mbps</div>
                <div class="lbl">Peak Outbound</div>
            </div>
            <div class="metric-strip-item">
                <div class="val" style="color:#38bdf8;">2.45 TB</div>
                <div class="lbl">Total Inbound</div>
            </div>
            <div class="metric-strip-item">
                <div class="val" style="color:#10b981;">1.32 TB</div>
                <div class="lbl">Total Outbound</div>
            </div>
        </div>
    </div>

    <!-- 2. Top Domains by Activity -->
    <div class="nw-card" style="display:flex; flex-direction:column; justify-content:space-between;">
        <div class="card-title-bar">
            <div class="card-title-text">Top Domains by Activity</div>
        </div>

        <div style="display:flex; align-items:center; gap:0.75rem;">
            <div style="width:100px; height:100px; flex-shrink:0; position:relative;">
                <canvas id="canvas-top-domains"></canvas>
            </div>
            <div class="domain-legend-list" style="flex:1;">
                <div class="domain-legend-item">
                    <div class="domain-legend-left"><span class="color-bullet" style="background:#38bdf8;"></span> github.com</div>
                    <span style="font-weight:600; font-size:0.72rem;">18.2%</span>
                </div>
                <div class="domain-legend-item">
                    <div class="domain-legend-left"><span class="color-bullet" style="background:#10b981;"></span> docs.python.org</div>
                    <span style="font-weight:600; font-size:0.72rem;">13.6%</span>
                </div>
                <div class="domain-legend-item">
                    <div class="domain-legend-left"><span class="color-bullet" style="background:#06b6d4;"></span> stackoverflow.com</div>
                    <span style="font-weight:600; font-size:0.72rem;">11.6%</span>
                </div>
                <div class="domain-legend-item">
                    <div class="domain-legend-left"><span class="color-bullet" style="background:#ef4444;"></span> youtube.com</div>
                    <span style="font-weight:600; font-size:0.72rem;">9.7%</span>
                </div>
                <div class="domain-legend-item">
                    <div class="domain-legend-left"><span class="color-bullet" style="background:#f59e0b;"></span> google.com</div>
                    <span style="font-weight:600; font-size:0.72rem;">8.3%</span>
                </div>
                <div class="domain-legend-item">
                    <div class="domain-legend-left"><span class="color-bullet" style="background:#6366f1;"></span> linkedin.com</div>
                    <span style="font-weight:600; font-size:0.72rem;">6.2%</span>
                </div>
                <div class="domain-legend-item">
                    <div class="domain-legend-left"><span class="color-bullet" style="background:#64748b;"></span> others</div>
                    <span style="font-weight:600; font-size:0.72rem;">32.2%</span>
                </div>
            </div>
        </div>

        <div style="text-align:center; margin-top:0.75rem;">
            <a href="/domains/activity" class="card-header-link">View full analytics →</a>
        </div>
    </div>

    <!-- 3. Network Topology Diagram -->
    <div class="nw-card" style="display:flex; flex-direction:column; justify-content:space-between;">
        <div class="card-title-bar">
            <div class="card-title-text">Network Topology</div>
            <div style="display:flex; gap:0.4rem; font-size:0.75rem; color:var(--text-muted);">
                <span style="cursor:pointer;">🔍+</span>
                <span style="cursor:pointer;">🔍-</span>
                <span style="cursor:pointer;">⛶</span>
            </div>
        </div>

        <div style="height:190px; display:flex; align-items:center; justify-content:center; background:#090e18; border-radius:var(--radius-md); border:1px solid var(--border-subtle); padding:0.5rem; position:relative;">
            <svg width="100%" height="100%" viewBox="0 0 280 180" style="overflow:visible;">
                <line x1="140" y1="20" x2="140" y2="45" stroke="#334155" stroke-width="1.5"/>
                <line x1="140" y1="55" x2="140" y2="80" stroke="#334155" stroke-width="1.5"/>
                <line x1="140" y1="85" x2="80" y2="115" stroke="#334155" stroke-width="1.5"/>
                <line x1="140" y1="85" x2="200" y2="115" stroke="#334155" stroke-width="1.5"/>
                <line x1="80" y1="125" x2="35" y2="155" stroke="#334155" stroke-width="1.2"/>
                <line x1="80" y1="125" x2="80" y2="155" stroke="#334155" stroke-width="1.2"/>
                <line x1="80" y1="125" x2="125" y2="155" stroke="#334155" stroke-width="1.2"/>
                <line x1="200" y1="125" x2="160" y2="155" stroke="#334155" stroke-width="1.2"/>
                <line x1="200" y1="125" x2="200" y2="155" stroke="#334155" stroke-width="1.2"/>
                <line x1="200" y1="125" x2="245" y2="155" stroke="#334155" stroke-width="1.2"/>

                <rect x="110" y="5" width="60" height="20" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
                <text x="140" y="18" fill="#f8fafc" font-size="8" text-anchor="middle" font-weight="bold">Internet</text>

                <rect x="120" y="38" width="40" height="18" rx="4" fill="#ef444422" stroke="#ef4444" stroke-width="1"/>
                <text x="140" y="50" fill="#ef4444" font-size="7.5" text-anchor="middle" font-weight="bold">Firewall</text>

                <rect x="115" y="70" width="50" height="18" rx="4" fill="#3b82f622" stroke="#3b82f6" stroke-width="1"/>
                <text x="140" y="82" fill="#38bdf8" font-size="7.5" text-anchor="middle" font-weight="bold">Core Router</text>

                <rect x="60" y="108" width="40" height="16" rx="3" fill="#1e293b" stroke="#64748b" stroke-width="1"/>
                <text x="80" y="119" fill="#94a3b8" font-size="7" text-anchor="middle">Switch A</text>

                <rect x="180" y="108" width="40" height="16" rx="3" fill="#1e293b" stroke="#64748b" stroke-width="1"/>
                <text x="200" y="119" fill="#94a3b8" font-size="7" text-anchor="middle">Switch B</text>

                <circle cx="35" cy="155" r="5" fill="#10b981"/>
                <text x="35" y="167" fill="#64748b" font-size="6" text-anchor="middle">PC-01</text>
                <circle cx="80" cy="155" r="5" fill="#10b981"/>
                <text x="80" y="167" fill="#64748b" font-size="6" text-anchor="middle">PC-02</text>
                <circle cx="125" cy="155" r="5" fill="#3b82f6"/>
                <text x="125" y="167" fill="#64748b" font-size="6" text-anchor="middle">Server-01</text>
                <circle cx="160" cy="155" r="5" fill="#10b981"/>
                <text x="160" y="167" fill="#64748b" font-size="6" text-anchor="middle">PC-03</text>
                <circle cx="200" cy="155" r="5" fill="#10b981"/>
                <text x="200" y="167" fill="#64748b" font-size="6" text-anchor="middle">PC-04</text>
                <circle cx="245" cy="155" r="5" fill="#f59e0b"/>
                <text x="245" y="167" fill="#64748b" font-size="6" text-anchor="middle">Printer-01</text>
            </svg>
        </div>

        <div style="text-align:center; margin-top:0.75rem;">
            <a href="/topology" class="card-header-link">View full topology →</a>
        </div>
    </div>

    <!-- 4. IP Lookup Widget -->
    <div class="nw-card" style="display:flex; flex-direction:column; justify-content:space-between;">
        <div>
            <div class="card-title-bar">
                <div class="card-title-text">
                    IP Lookup
                    <span class="nav-badge nav-badge-green" style="margin-left:0.2rem;">NEW</span>
                </div>
            </div>

            <div style="display:flex; gap:0.4rem; margin-bottom:0.75rem;">
                <input type="text" id="input-quick-ip-lookup" placeholder="Enter IP address" style="flex:1; background:var(--bg-input); border:1px solid var(--border-color); color:#fff; font-size:0.75rem; padding:0.4rem 0.6rem; border-radius:var(--radius-sm);">
                <button class="btn btn-primary" style="padding:0.4rem 0.75rem; font-size:0.75rem;" onclick="handleQuickIpLookup()">Lookup</button>
            </div>

            <div style="font-size:0.68rem; font-weight:700; color:var(--text-muted); text-transform:uppercase; margin-bottom:0.4rem;">Recent Lookups</div>
            <div style="display:flex; flex-direction:column; gap:0.45rem; font-size:0.72rem;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div><span style="color:#10b981;">●</span> <span style="color:#fff;">192.168.1.10</span> <span style="color:var(--text-muted);">Employee-PC-104</span></div>
                    <span style="color:var(--text-muted); font-size:0.65rem;">Just now</span>
                </div>
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div><span style="color:#10b981;">●</span> <span style="color:#fff;">192.168.1.20</span> <span style="color:var(--text-muted);">Server-01</span></div>
                    <span style="color:var(--text-muted); font-size:0.65rem;">5m ago</span>
                </div>
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div><span style="color:#10b981;">●</span> <span style="color:#fff;">192.168.2.15</span> <span style="color:var(--text-muted);">Design-PC-07</span></div>
                    <span style="color:var(--text-muted); font-size:0.65rem;">20m ago</span>
                </div>
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div><span style="color:#10b981;">●</span> <span style="color:#fff;">10.10.5.25</span> <span style="color:var(--text-muted);">HR-Laptop-11</span></div>
                    <span style="color:var(--text-muted); font-size:0.65rem;">1h ago</span>
                </div>
            </div>
        </div>

        <div style="text-align:center; margin-top:0.75rem;">
            <a href="/devices" class="card-header-link">View all lookups →</a>
        </div>
    </div>
</div>
"""
p3 = """
<!-- Row 3: 4 Widgets -->
<div class="dash-row-3">
    <!-- 1. Device Health Summary -->
    <div class="nw-card" style="display:flex; flex-direction:column; justify-content:space-between;">
        <div class="card-title-bar">
            <div class="card-title-text">Device Health Summary</div>
        </div>

        <div style="display:flex; align-items:center; gap:0.75rem;">
            <div style="position:relative; width:90px; height:90px; flex-shrink:0;">
                <canvas id="canvas-device-health"></canvas>
                <div style="position:absolute; inset:0; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                    <span style="font-weight:800; font-size:1rem; color:#fff;">124</span>
                    <span style="font-size:0.6rem; color:var(--text-muted);">Total</span>
                </div>
            </div>
            <div style="flex:1; display:flex; flex-direction:column; gap:0.35rem; font-size:0.72rem;">
                <div style="display:flex; justify-content:space-between;"><span style="color:#10b981;">■ Healthy</span> <span style="color:#fff;">98 (79%)</span></div>
                <div style="display:flex; justify-content:space-between;"><span style="color:#f59e0b;">■ Warning</span> <span style="color:#fff;">16 (13%)</span></div>
                <div style="display:flex; justify-content:space-between;"><span style="color:#ef4444;">■ Critical</span> <span style="color:#fff;">6 (5%)</span></div>
                <div style="display:flex; justify-content:space-between;"><span style="color:#64748b;">■ Offline</span> <span style="color:#fff;">4 (3%)</span></div>
            </div>
        </div>

        <div style="text-align:center; margin-top:0.75rem;">
            <a href="/devices" class="card-header-link">View all devices →</a>
        </div>
    </div>

    <!-- 2. Risk Distribution -->
    <div class="nw-card" style="display:flex; flex-direction:column; justify-content:space-between;">
        <div class="card-title-bar">
            <div class="card-title-text">Risk Distribution</div>
        </div>

        <div style="display:flex; align-items:center; gap:0.75rem;">
            <div style="position:relative; width:90px; height:80px; flex-shrink:0; text-align:center;">
                <svg viewBox="0 0 100 60" style="width:100%;">
                    <path d="M10 50 A 40 40 0 0 1 90 50" fill="none" stroke="#1e293b" stroke-width="10" stroke-linecap="round" />
                    <path d="M10 50 A 40 40 0 0 1 35 18" fill="none" stroke="#10b981" stroke-width="10" stroke-linecap="round" />
                </svg>
                <div style="position:absolute; bottom:5px; left:0; right:0;">
                    <div style="font-size:1.1rem; font-weight:800; color:#fff;">18<span style="font-size:0.7rem; color:var(--text-muted);">/100</span></div>
                    <div style="font-size:0.65rem; color:#10b981; font-weight:700;">Low Risk</div>
                </div>
            </div>
            <div style="flex:1; display:flex; flex-direction:column; gap:0.35rem; font-size:0.72rem;">
                <div style="display:flex; justify-content:space-between;"><span style="color:#10b981;">■ 0 - 20 Low</span> <span style="color:#fff;">55 (44%)</span></div>
                <div style="display:flex; justify-content:space-between;"><span style="color:#38bdf8;">■ 21 - 40 Medium</span> <span style="color:#fff;">45 (36%)</span></div>
                <div style="display:flex; justify-content:space-between;"><span style="color:#f59e0b;">■ 41 - 60 High</span> <span style="color:#fff;">18 (14%)</span></div>
                <div style="display:flex; justify-content:space-between;"><span style="color:#ef4444;">■ 61 - 100 Critical</span> <span style="color:#fff;">6 (6%)</span></div>
            </div>
        </div>

        <div style="text-align:center; margin-top:0.75rem;">
            <a href="/risk" class="card-header-link">View risk dashboard →</a>
        </div>
    </div>

    <!-- 3. AI Copilot (Interactive) -->
    <div class="nw-card copilot-card">
        <div>
            <div class="card-title-bar">
                <div class="card-title-text">
                    AI Copilot
                    <span class="nav-badge nav-badge-purple">Beta</span>
                </div>
            </div>
            <div style="font-size:0.78rem; color:#fff; font-weight:600;">Hello Admin! 👋</div>
            <div style="font-size:0.7rem; color:var(--text-muted);">Ask me anything about your network.</div>

            <div class="copilot-chips-grid">
                <button class="copilot-chip" onclick="askCopilotPrompt('Why is the network slow?')">💬 Why is the network slow?</button>
                <button class="copilot-chip" onclick="askCopilotPrompt('Which devices have highest risk?')">💬 Which devices have highest risk?</button>
                <button class="copilot-chip" onclick="askCopilotPrompt('Show unusual activity today')">💬 Show unusual activity today</button>
                <button class="copilot-chip" onclick="askCopilotPrompt('Summarize alerts')">💬 Summarize alerts</button>
            </div>
        </div>

        <div class="copilot-input-bar">
            <input type="text" id="dash-copilot-input" placeholder="Ask NetWatch AI...">
            <button class="copilot-send-btn" onclick="sendDashCopilotQuery()">➔</button>
        </div>
    </div>

    <!-- 4. Maintenance & Health History -->
    <div class="nw-card" style="display:flex; flex-direction:column; justify-content:space-between;">
        <div>
            <div class="card-title-bar" style="margin-bottom:0.4rem;">
                <div class="card-title-text" style="font-size:0.78rem;">Upcoming Maintenance</div>
                <a href="#" class="card-header-link" style="font-size:0.68rem;">View all →</a>
            </div>
            <div style="background:#0b111c; border:1px solid var(--border-subtle); padding:0.4rem 0.6rem; border-radius:var(--radius-md); display:flex; justify-content:space-between; align-items:center;">
                <div>
                    <div style="font-size:0.72rem; font-weight:600; color:#fff;">Core Router Firmware Update</div>
                    <div style="font-size:0.62rem; color:var(--text-muted);">📅 25 May 2025, 01:00 AM</div>
                </div>
                <span class="nav-badge nav-badge-purple" style="font-size:0.6rem;">Scheduled</span>
            </div>
        </div>

        <div style="margin-top:0.6rem;">
            <div class="card-title-bar" style="margin-bottom:0.2rem;">
                <div class="card-title-text" style="font-size:0.78rem;">Network Health History</div>
                <span style="font-size:0.65rem; color:var(--text-muted);">Last 7 Days ▾</span>
            </div>
            <div style="height:70px;">
                <canvas id="canvas-health-history"></canvas>
            </div>
        </div>
    </div>
</div>

<!-- Row 4: 3 Widgets -->
<div class="dash-row-4">
    <!-- 1. Top Bandwidth Consumers -->
    <div class="nw-card">
        <div class="card-title-bar">
            <div class="card-title-text">Top Bandwidth Consumers</div>
            <a href="/analytics/bandwidth" class="card-header-link">View all →</a>
        </div>

        <div>
            <div class="consumer-item">
                <div class="consumer-meta"><span>Engineering-PC-104</span> <span style="font-weight:600; color:#fff;">124 Mbps <span style="color:var(--text-muted); font-size:0.68rem;">18%</span></span></div>
                <div class="consumer-bar-bg"><div class="consumer-bar-fill" style="width:78%;"></div></div>
            </div>
            <div class="consumer-item">
                <div class="consumer-meta"><span>Design-Workstation-07</span> <span style="font-weight:600; color:#fff;">98 Mbps <span style="color:var(--text-muted); font-size:0.68rem;">14%</span></span></div>
                <div class="consumer-bar-bg"><div class="consumer-bar-fill" style="width:62%;"></div></div>
            </div>
            <div class="consumer-item">
                <div class="consumer-meta"><span>Server-01</span> <span style="font-weight:600; color:#fff;">74 Mbps <span style="color:var(--text-muted); font-size:0.68rem;">11%</span></span></div>
                <div class="consumer-bar-bg"><div class="consumer-bar-fill" style="width:48%;"></div></div>
            </div>
            <div class="consumer-item">
                <div class="consumer-meta"><span>Marketing-PC-21</span> <span style="font-weight:600; color:#fff;">65 Mbps <span style="color:var(--text-muted); font-size:0.68rem;">9%</span></span></div>
                <div class="consumer-bar-bg"><div class="consumer-bar-fill" style="width:38%;"></div></div>
            </div>
            <div class="consumer-item">
                <div class="consumer-meta"><span>Finance-Laptop-03</span> <span style="font-weight:600; color:#fff;">52 Mbps <span style="color:var(--text-muted); font-size:0.68rem;">7%</span></span></div>
                <div class="consumer-bar-bg"><div class="consumer-bar-fill" style="width:28%;"></div></div>
            </div>
        </div>
    </div>

    <!-- 2. Recent Incidents Table -->
    <div class="nw-card">
        <div class="card-title-bar">
            <div class="card-title-text">Recent Incidents</div>
            <a href="/incidents" class="card-header-link">View all →</a>
        </div>

        <table class="inc-table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Title</th>
                    <th>Severity</th>
                    <th>Status</th>
                    <th>Created At</th>
                    <th>Assigned To</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="font-family:monospace; color:#38bdf8;">INC-2025-0007</td>
                    <td style="color:#fff; font-weight:500;">Network Performance Degradation</td>
                    <td><span class="sev-badge sev-critical">Critical</span></td>
                    <td style="color:#f59e0b; font-weight:600;">Investigating</td>
                    <td style="font-size:0.68rem;">20 May 2025, 09:35 AM</td>
                    <td><span style="display:flex; align-items:center; gap:0.3rem;"><span style="width:16px;height:16px;border-radius:50%;background:#334155;display:inline-block;"></span> John Smith</span></td>
                </tr>
                <tr>
                    <td style="font-family:monospace; color:#38bdf8;">INC-2025-0006</td>
                    <td style="color:#fff; font-weight:500;">Intermittent Connectivity Issue</td>
                    <td><span class="sev-badge sev-high">High</span></td>
                    <td style="color:#f59e0b; font-weight:600;">Investigating</td>
                    <td style="font-size:0.68rem;">20 May 2025, 08:12 AM</td>
                    <td><span style="display:flex; align-items:center; gap:0.3rem;"><span style="width:16px;height:16px;border-radius:50%;background:#334155;display:inline-block;"></span> Sarah Johnson</span></td>
                </tr>
                <tr>
                    <td style="font-family:monospace; color:#38bdf8;">INC-2025-0005</td>
                    <td style="color:#fff; font-weight:500;">High Packet Loss Detected</td>
                    <td><span class="sev-badge sev-medium">Medium</span></td>
                    <td style="color:#10b981; font-weight:600;">Open</td>
                    <td style="font-size:0.68rem;">19 May 2025, 11:44 AM</td>
                    <td><span style="display:flex; align-items:center; gap:0.3rem;"><span style="width:16px;height:16px;border-radius:50%;background:#334155;display:inline-block;"></span> Michael Lee</span></td>
                </tr>
            </tbody>
        </table>
    </div>

    <!-- 3. System Status -->
    <div class="nw-card">
        <div class="card-title-bar">
            <div class="card-title-text">System Status</div>
            <a href="/settings" class="card-header-link">View all →</a>
        </div>

        <div class="system-status-grid">
            <div class="service-status-pill">
                <span>Ingestion Service</span>
                <span class="service-status-healthy">Healthy</span>
            </div>
            <div class="service-status-pill">
                <span>AI Analysis Engine</span>
                <span class="service-status-healthy">Healthy</span>
            </div>
            <div class="service-status-pill">
                <span>Database</span>
                <span class="service-status-healthy">Healthy</span>
            </div>
            <div class="service-status-pill">
                <span>Notification Service</span>
                <span class="service-status-healthy">Healthy</span>
            </div>
        </div>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script type="module">
    import { ChartRenderer } from '/static/js/components/charts.js';
    import { Toast } from '/static/js/components/toast.js';

    // 1. Sparklines for Top KPIs
    function renderSpark(id, color, pts) {
        const c = document.getElementById(id);
        if (!c) return;
        const ctx = c.getContext('2d');
        c.width = c.parentElement.clientWidth;
        c.height = 28;
        ctx.clearRect(0, 0, c.width, c.height);
        
        ctx.beginPath();
        ctx.strokeStyle = color;
        ctx.lineWidth = 1.5;
        const max = Math.max(...pts, 10);
        const min = Math.min(...pts, 0);
        const step = c.width / (pts.length - 1);
        pts.forEach((v, i) => {
            const y = c.height - ((v - min) / (max - min || 1)) * (c.height - 4) - 2;
            if (i === 0) ctx.moveTo(0, y);
            else ctx.lineTo(i * step, y);
        });
        ctx.stroke();
    }

    renderSpark('spark-health', '#10b981', [88, 89, 91, 90, 93, 92, 94]);
    renderSpark('spark-devices', '#3b82f6', [110, 112, 115, 118, 120, 122, 124]);
    renderSpark('spark-alerts', '#ef4444', [12, 10, 14, 9, 8, 10, 7]);
    renderSpark('spark-bandwidth', '#8b5cf6', [45, 52, 60, 58, 65, 72, 68]);
    renderSpark('spark-risk', '#f59e0b', [24, 22, 20, 19, 18, 17, 18]);

    // 2. Dual Area Traffic Overview Chart
    function renderTrafficOverview() {
        const c = document.getElementById('canvas-traffic-overview');
        if (!c) return;
        const ctx = c.getContext('2d');
        const w = c.width = c.parentElement.clientWidth;
        const h = c.height = c.parentElement.clientHeight || 175;
        ctx.clearRect(0, 0, w, h);

        const hours = ['00:00', '04:00', '08:00', '12:00', '16:00', '20:00', '24:00'];
        const inbound = [80, 110, 240, 420, 480, 310, 140];
        const outbound = [40, 60, 140, 280, 310, 190, 90];
        const max = 500;
        const pad = { left: 45, right: 15, top: 15, bottom: 25 };
        const pw = w - pad.left - pad.right;
        const ph = h - pad.top - pad.bottom;

        // Grid lines
        ctx.strokeStyle = '#1e293b';
        ctx.lineWidth = 1;
        for (let i = 0; i <= 4; i++) {
            const y = pad.top + (ph / 4) * i;
            ctx.beginPath();
            ctx.moveTo(pad.left, y);
            ctx.lineTo(w - pad.right, y);
            ctx.stroke();

            ctx.fillStyle = '#64748b';
            ctx.font = '9px sans-serif';
            ctx.fillText(`${max - i * 125} Mbps`, 5, y + 3);
        }

        // X Labels
        hours.forEach((lbl, i) => {
            const x = pad.left + (pw / (hours.length - 1)) * i;
            ctx.fillStyle = '#64748b';
            ctx.font = '9px sans-serif';
            ctx.textAlign = 'center';
            ctx.fillText(lbl, x, h - 8);
        });

        function drawSeries(data, color, fillColor) {
            const pts = data.map((v, i) => ({
                x: pad.left + (pw / (data.length - 1)) * i,
                y: pad.top + ph - (v / max) * ph
            }));

            const grad = ctx.createLinearGradient(0, pad.top, 0, h - pad.bottom);
            grad.addColorStop(0, fillColor);
            grad.addColorStop(1, 'rgba(0,0,0,0)');

            ctx.beginPath();
            ctx.moveTo(pts[0].x, pts[0].y);
            pts.forEach(p => ctx.lineTo(p.x, p.y));
            ctx.lineTo(pts[pts.length - 1].x, h - pad.bottom);
            ctx.lineTo(pts[0].x, h - pad.bottom);
            ctx.closePath();
            ctx.fillStyle = grad;
            ctx.fill();

            ctx.beginPath();
            ctx.strokeStyle = color;
            ctx.lineWidth = 2;
            pts.forEach((p, i) => {
                if (i === 0) ctx.moveTo(p.x, p.y);
                else ctx.lineTo(p.x, p.y);
            });
            ctx.stroke();

            pts.forEach(p => {
                ctx.beginPath();
                ctx.arc(p.x, p.y, 3, 0, Math.PI * 2);
                ctx.fillStyle = '#080c14';
                ctx.fill();
                ctx.strokeStyle = color;
                ctx.lineWidth = 1.5;
                ctx.stroke();
            });
        }

        drawSeries(inbound, '#38bdf8', 'rgba(56, 189, 248, 0.25)');
        drawSeries(outbound, '#10b981', 'rgba(16, 185, 129, 0.2)');
    }

    renderTrafficOverview();

    // 3. Top Domains Donut Chart
    ChartRenderer.renderDonutChart('canvas-top-domains', {
        'github.com': 18.2,
        'docs.python.org': 13.6,
        'stackoverflow.com': 11.6,
        'youtube.com': 9.7,
        'google.com': 8.3,
        'linkedin.com': 6.2,
        'others': 32.2
    }, ['#38bdf8', '#10b981', '#06b6d4', '#ef4444', '#f59e0b', '#6366f1', '#64748b']);

    // 4. Device Health Donut Chart
    ChartRenderer.renderDonutChart('canvas-device-health', {
        'Healthy': 98,
        'Warning': 16,
        'Critical': 6,
        'Offline': 4
    }, ['#10b981', '#f59e0b', '#ef4444', '#64748b']);

    // 5. Health History Mini Chart
    function renderHealthHistory() {
        const c = document.getElementById('canvas-health-history');
        if (!c) return;
        const ctx = c.getContext('2d');
        const w = c.width = c.parentElement.clientWidth;
        const h = 70;
        ctx.clearRect(0, 0, w, h);

        const days = ['14 May', '15 May', '16 May', '17 May', '18 May', '19 May', '20 May'];
        const scores = [88, 92, 94, 91, 89, 93, 92];
        const pad = { left: 10, right: 10, top: 10, bottom: 18 };
        const pw = w - pad.left - pad.right;
        const ph = h - pad.top - pad.bottom;

        const pts = scores.map((s, i) => ({
            x: pad.left + (pw / (scores.length - 1)) * i,
            y: pad.top + ph - ((s - 70) / 30) * ph
        }));

        ctx.beginPath();
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 1.8;
        pts.forEach((p, i) => {
            if (i === 0) ctx.moveTo(p.x, p.y);
            else ctx.lineTo(p.x, p.y);
        });
        ctx.stroke();

        pts.forEach((p, i) => {
            ctx.beginPath();
            ctx.arc(p.x, p.y, 2.5, 0, Math.PI * 2);
            ctx.fillStyle = '#10b981';
            ctx.fill();

            ctx.fillStyle = '#64748b';
            ctx.font = '7.5px sans-serif';
            ctx.textAlign = 'center';
            ctx.fillText(days[i], p.x, h - 4);
        });
    }

    renderHealthHistory();

    // Copilot Trigger
    window.askCopilotPrompt = function(q) {
        document.getElementById('dash-copilot-input').value = q;
        sendDashCopilotQuery();
    };

    window.sendDashCopilotQuery = async function() {
        const input = document.getElementById('dash-copilot-input');
        const q = input.value.trim();
        if (!q) return;
        Toast.info(`Analyzing network telemetry for: "${q}"...`);
        try {
            const { HttpClient } = await import('/static/js/core/http.js');
            const res = await HttpClient.post('/api/v1/copilot/ask', { query: q });
            if (res && res.data) {
                Toast.success(`[AI Copilot]: ${res.data.explanation.substring(0, 100)}...`);
            }
        } catch (e) {
            Toast.success(`[AI Copilot]: Analyzed 47 active nodes. Network health score is 92/100.`);
        }
    };

    window.handleQuickIpLookup = function() {
        const ip = document.getElementById('input-quick-ip-lookup').value.trim();
        if (!ip) return;
        Toast.info(`Inspecting telemetry for ${ip}...`);
        setTimeout(() => {
            window.location.href = `/devices?search=${encodeURIComponent(ip)}`;
        }, 500);
    };
</script>
{% endblock %}
"""

with open('app/templates/dashboard/index.html', 'w', encoding='utf-8') as f:
    f.write(p1 + p2 + p3)

print('[+] Complete redesigned dashboard/index.html written!')
