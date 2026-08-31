# 1. analytics/bandwidth.html
bw_html = """{% extends "base.html" %}

{% block content %}
<div class="page-header">
    <div>
        <h1 class="page-title">Bandwidth Analytics & Throughput</h1>
        <div class="page-subtitle">Real-time interface ingress/egress analysis, top talkers, and protocol distribution</div>
    </div>
</div>

<div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap:1.25rem; margin-bottom:1.5rem;">
    <div class="card kpi-card">
        <div class="kpi-label" style="font-size:0.75rem; color:var(--text-muted); text-transform:uppercase;">Total Ingress Volume</div>
        <div class="kpi-value" id="kpi-bw-in" style="color:var(--accent-cyan); font-size:1.6rem; font-weight:800; margin:0.4rem 0;">-- GB</div>
        <div class="kpi-subtext" style="font-size:0.75rem; color:var(--text-muted);">Inbound Traffic</div>
    </div>
    <div class="card kpi-card">
        <div class="kpi-label" style="font-size:0.75rem; color:var(--text-muted); text-transform:uppercase;">Total Egress Volume</div>
        <div class="kpi-value" id="kpi-bw-out" style="color:var(--accent-blue); font-size:1.6rem; font-weight:800; margin:0.4rem 0;">-- GB</div>
        <div class="kpi-subtext" style="font-size:0.75rem; color:var(--text-muted);">Outbound Traffic</div>
    </div>
    <div class="card kpi-card">
        <div class="kpi-label" style="font-size:0.75rem; color:var(--text-muted); text-transform:uppercase;">Total Bandwidth Exchanged</div>
        <div class="kpi-value" id="kpi-bw-total" style="color:var(--accent-emerald); font-size:1.6rem; font-weight:800; margin:0.4rem 0;">-- GB</div>
        <div class="kpi-subtext" style="font-size:0.75rem; color:var(--text-muted);">Past 24 Hours</div>
    </div>
</div>

<div class="card">
    <div class="card-header" style="margin-bottom:1rem;">
        <div class="card-title" style="font-size:1rem; font-weight:700; color:#fff;">Top Bandwidth Consuming Endpoints</div>
    </div>
    <div class="data-table-container">
        <table class="data-table">
            <thead>
                <tr>
                    <th>Device Name</th>
                    <th>IP Address</th>
                    <th>Device Type</th>
                    <th>Total Transferred</th>
                </tr>
            </thead>
            <tbody id="tbody-top-hogs">
                <tr><td colspan="4" style="text-align:center; padding:2rem;">Loading top bandwidth consumers...</td></tr>
            </tbody>
        </table>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script type="module">
    import { HttpClient } from '/static/js/core/http.js';
    import { Toast } from '/static/js/components/toast.js';

    async function loadBandwidth() {
        try {
            const res = await HttpClient.get('/api/v1/analytics/bandwidth');
            const d = res.data;

            const gbIn = (d.total_ingress_bytes / (1024 * 1024 * 1024)).toFixed(2);
            const gbOut = (d.total_egress_bytes / (1024 * 1024 * 1024)).toFixed(2);
            const gbTot = (d.total_volume_bytes / (1024 * 1024 * 1024)).toFixed(2);

            document.getElementById('kpi-bw-in').textContent = `${gbIn} GB`;
            document.getElementById('kpi-bw-out').textContent = `${gbOut} GB`;
            document.getElementById('kpi-bw-total').textContent = `${gbTot} GB`;

            const tbody = document.getElementById('tbody-top-hogs');
            if (!d.top_consumers || d.top_consumers.length === 0) {
                tbody.innerHTML = '<tr><td colspan="4" style="text-align:center; padding:2rem; color:var(--text-muted);">No bandwidth telemetry collected.</td></tr>';
            } else {
                tbody.innerHTML = d.top_consumers.map(c => `
                    <tr>
                        <td style="font-weight:600; color:var(--text-primary);">${c.device_name || 'Endpoint'}</td>
                        <td><code>${c.ip_address}</code></td>
                        <td style="text-transform:capitalize;">${c.device_type || 'workstation'}</td>
                        <td style="font-weight:700; color:var(--accent-cyan); font-family:monospace;">
                            ${(c.total_bytes / (1024 * 1024 * 1024)).toFixed(2)} GB
                        </td>
                    </tr>
                `).join('');
            }
        } catch (err) {
            Toast.error('Failed to load bandwidth analytics.');
        }
    }
    loadBandwidth();
</script>
{% endblock %}
"""

with open("app/templates/analytics/bandwidth.html", "w", encoding="utf-8") as f:
    f.write(bw_html)

# 2. analytics/office_hours.html
off_html = """{% extends "base.html" %}

{% block content %}
<div class="page-header">
    <div>
        <h1 class="page-title">Office Hours vs Off-Hours Analytics</h1>
        <div class="page-subtitle">Comparative network traffic distribution, baseline compliance, and quiet-hours anomaly inspection</div>
    </div>
</div>

<div style="display:grid; grid-template-columns: 1fr 1fr; gap:1.5rem; margin-bottom:1.5rem;">
    <div class="card kpi-card">
        <div class="kpi-label" style="font-size:0.75rem; color:var(--text-muted); text-transform:uppercase;">Business Hours Volume (09:00 - 18:00)</div>
        <div class="kpi-value" id="kpi-office-pct" style="color:#10b981; font-size:1.6rem; font-weight:800; margin:0.4rem 0;">--%</div>
        <div class="kpi-subtext" id="kpi-office-gb" style="font-size:0.75rem; color:var(--text-muted);">-- GB during working shift</div>
    </div>

    <div class="card kpi-card">
        <div class="kpi-label" style="font-size:0.75rem; color:var(--text-muted); text-transform:uppercase;">Off-Hours Traffic (Night / Weekend)</div>
        <div class="kpi-value" id="kpi-off-pct" style="color:#f59e0b; font-size:1.6rem; font-weight:800; margin:0.4rem 0;">--%</div>
        <div class="kpi-subtext" id="kpi-off-gb" style="font-size:0.75rem; color:var(--text-muted);">-- GB quiet hours volume</div>
    </div>
</div>

<div class="card">
    <div class="card-header" style="margin-bottom:1rem;">
        <div class="card-title" style="font-size:1rem; font-weight:700; color:#fff;">Top Active Devices During Off-Hours</div>
    </div>
    <div class="data-table-container">
        <table class="data-table">
            <thead>
                <tr>
                    <th>Device Name</th>
                    <th>IP Address</th>
                    <th>Assigned User</th>
                    <th>Off-Hours Transferred</th>
                </tr>
            </thead>
            <tbody id="tbody-off-devices">
                <tr><td colspan="4" style="text-align:center; padding:2rem;">Loading off-hours activity...</td></tr>
            </tbody>
        </table>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script type="module">
    import { HttpClient } from '/static/js/core/http.js';
    import { Toast } from '/static/js/components/toast.js';

    async function loadOfficeHours() {
        try {
            const res = await HttpClient.get('/api/v1/analytics/office-hours');
            const d = res.data;

            document.getElementById('kpi-office-pct').textContent = `${d.office_hours_percentage}%`;
            document.getElementById('kpi-office-gb').textContent = `${(d.office_hours_bytes / (1024*1024*1024)).toFixed(2)} GB working shift volume`;
            document.getElementById('kpi-off-pct').textContent = `${d.off_hours_percentage}%`;
            document.getElementById('kpi-off-gb').textContent = `${(d.off_hours_bytes / (1024*1024*1024)).toFixed(2)} GB off-hours volume`;

            const tbody = document.getElementById('tbody-off-devices');
            if (!d.top_off_hours_devices || d.top_off_hours_devices.length === 0) {
                tbody.innerHTML = '<tr><td colspan="4" style="text-align:center; padding:2rem; color:var(--text-muted);">No off-hours activity recorded.</td></tr>';
            } else {
                tbody.innerHTML = d.top_off_hours_devices.map(dev => `
                    <tr>
                        <td style="font-weight:600; color:var(--text-primary);">${dev.device_name || 'Device'}</td>
                        <td><code>${dev.ip_address}</code></td>
                        <td>${dev.assigned_user || 'Unassigned'}</td>
                        <td style="font-weight:700; color:#f59e0b; font-family:monospace;">
                            ${(dev.bytes / (1024*1024)).toFixed(1)} MB
                        </td>
                    </tr>
                `).join('');
            }
        } catch (err) {
            Toast.error('Failed to load office hours analytics.');
        }
    }
    loadOfficeHours();
</script>
{% endblock %}
"""

with open("app/templates/analytics/office_hours.html", "w", encoding="utf-8") as f:
    f.write(off_html)

# 3. diagnostics/slow_network.html
diag_html = """{% extends "base.html" %}

{% block content %}
<div class="page-header">
    <div>
        <h1 class="page-title">Slow Network Diagnostic Wizard</h1>
        <div class="page-subtitle">7-Stage automated diagnostic probe pipeline: Gateway, Latency, Loss, DNS, Bandwidth, Hardware, Root Cause Synthesis</div>
    </div>
    <div>
        <button id="btn-run-diagnosis" class="btn btn-primary btn-sm">⚡ Execute Diagnostic Probe</button>
    </div>
</div>

<!-- Diagnostics Execution Results Card -->
<div class="card" style="margin-bottom:1.5rem;">
    <div class="card-header" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
        <div class="card-title" style="font-size:1rem; font-weight:700; color:#fff;">Probe Pipeline Stages</div>
        <span id="badge-diag-status" class="badge badge-online">READY</span>
    </div>
    
    <div id="diag-steps-container" style="display:flex; flex-direction:column; gap:0.75rem;">
        <div style="text-align:center; padding:3rem; color:var(--text-muted);">
            Click "Execute Diagnostic Probe" to run live 7-stage network health inspection.
        </div>
    </div>
</div>

<!-- Root Cause Synthesis & Playbook -->
<div id="diag-synthesis-card" class="card" style="display:none;">
    <div class="card-header" style="margin-bottom:1rem;">
        <div class="card-title" style="font-size:1rem; font-weight:700; color:#fff;">Root Cause Synthesis & Remediation Playbook</div>
    </div>
    <div style="background:#090f1a; border:1px solid var(--border-subtle); padding:1rem; border-radius:var(--radius-md); margin-bottom:1rem;">
        <div style="font-weight:700; color:var(--accent-cyan); margin-bottom:0.25rem;">Identified Bottleneck:</div>
        <div id="txt-root-cause" style="color:var(--text-primary); font-size:0.9rem;">--</div>
    </div>
    <div>
        <div style="font-weight:700; color:#10b981; margin-bottom:0.25rem;">Actionable Remediation Playbook:</div>
        <div id="txt-playbook" style="color:var(--text-secondary); font-size:0.85rem; line-height:1.6; white-space:pre-line;">--</div>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script type="module">
    import { HttpClient } from '/static/js/core/http.js';
    import { Toast } from '/static/js/components/toast.js';

    document.getElementById('btn-run-diagnosis').addEventListener('click', async () => {
        const btn = document.getElementById('btn-run-diagnosis');
        btn.disabled = true;
        btn.textContent = 'Running 7-Stage Probe...';
        document.getElementById('badge-diag-status').textContent = 'PROBING TELEMETRY';
        document.getElementById('badge-diag-status').className = 'badge badge-degraded';

        try {
            const res = await HttpClient.post('/api/v1/diagnostics/run', { scope: 'Global Gateway' });
            const data = res.data;
            const steps = data.steps;

            const container = document.getElementById('diag-steps-container');
            container.innerHTML = steps.map(s => {
                const borderClr = s.status === 'PASSED' ? '#10b981' : (s.status === 'WARNING' ? '#f59e0b' : '#ef4444');
                const badgeClass = s.status === 'PASSED' ? 'badge-online' : (s.status === 'WARNING' ? 'badge-degraded' : 'badge-unauthorized');
                return `
                <div style="background:#090f1a; padding:1rem; border-radius:var(--radius-md); border-left:4px solid ${borderClr}; border:1px solid var(--border-subtle);">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.25rem;">
                        <div style="font-weight:700; color:var(--text-primary); font-size:0.9rem;">
                            Stage ${s.step_number}: ${s.step_name}
                        </div>
                        <span class="badge ${badgeClass}">${s.status}</span>
                    </div>
                    <div style="font-size:0.8rem; color:var(--text-secondary); margin-bottom:0.25rem;">${s.finding_details}</div>
                    <div style="font-size:0.75rem; color:var(--text-muted);">Observed: <code>${s.metric_value}</code> (Threshold: ${s.threshold_value})</div>
                </div>
                `;
            }).join('');

            // Show synthesis
            document.getElementById('diag-synthesis-card').style.display = 'block';
            document.getElementById('txt-root-cause').textContent = data.session.root_cause_summary || 'All network parameters nominal.';
            document.getElementById('txt-playbook').textContent = data.session.remediation_playbook || 'No action required.';

            document.getElementById('badge-diag-status').textContent = 'COMPLETED';
            document.getElementById('badge-diag-status').className = 'badge badge-online';
            Toast.success('Diagnostic probe completed successfully.');
        } catch (err) {
            Toast.error('Failed to run diagnostics.');
        } finally {
            btn.disabled = false;
            btn.textContent = '⚡ Execute Diagnostic Probe';
        }
    });
</script>
{% endblock %}
"""

with open("app/templates/diagnostics/slow_network.html", "w", encoding="utf-8") as f:
    f.write(diag_html)

# 4. domains/activity.html
dom_html = """{% extends "base.html" %}

{% block content %}
<div class="page-header">
    <div>
        <h1 class="page-title">Authorized Domain Activity Analytics</h1>
        <div class="page-subtitle">Domain resolution queries, category classification, and DNS latency telemetry</div>
    </div>
</div>

<div style="display:grid; grid-template-columns: 2fr 1fr; gap:1.5rem; margin-bottom:1.5rem;">
    <!-- Domain Queries Table -->
    <div class="card">
        <div class="card-header" style="margin-bottom:1rem;">
            <div class="card-title" style="font-size:1rem; font-weight:700; color:#fff;">Live DNS Telemetry Feed</div>
        </div>
        <div class="data-table-container">
            <table class="data-table">
                <thead>
                    <tr>
                        <th>Domain Name</th>
                        <th>Category</th>
                        <th>Status</th>
                        <th>Response Time</th>
                        <th>Office Hours</th>
                    </tr>
                </thead>
                <tbody id="tbody-domains">
                    <tr><td colspan="5" style="text-align:center; padding:2rem;">Loading DNS resolution stream...</td></tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- Top Domains -->
    <div class="card">
        <div class="card-header" style="margin-bottom:1rem;">
            <div class="card-title" style="font-size:1rem; font-weight:700; color:#fff;">Top Queried Domains</div>
        </div>
        <div id="top-domains-list" style="display:flex; flex-direction:column; gap:0.75rem;">
            <div style="text-align:center; color:var(--text-muted); padding:2rem;">Loading rankings...</div>
        </div>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script type="module">
    import { HttpClient } from '/static/js/core/http.js';
    import { Toast } from '/static/js/components/toast.js';

    async function loadDomains() {
        try {
            const res = await HttpClient.get('/api/v1/domains/activity', { limit: 50 });
            const queries = res.data;
            const tbody = document.getElementById('tbody-domains');

            if (!queries || queries.length === 0) {
                tbody.innerHTML = '<tr><td colspan="5" style="text-align:center; padding:2rem; color:var(--text-muted);">No domain queries recorded in current time window.</td></tr>';
            } else {
                tbody.innerHTML = queries.map(q => `
                    <tr>
                        <td style="font-weight:600; color:var(--text-primary); font-family:monospace;">${q.domain}</td>
                        <td><span class="badge badge-online">${q.category || 'General'}</span></td>
                        <td>
                            <span class="badge ${q.is_blocked ? 'badge-unauthorized' : 'badge-online'}">
                                ${q.is_blocked ? 'Blocked' : 'Allowed'}
                            </span>
                        </td>
                        <td><code>${q.response_time_ms} ms</code></td>
                        <td><span class="badge ${q.is_office_hours ? 'badge-online' : 'badge-degraded'}">${q.is_office_hours ? 'Work' : 'Off-Hours'}</span></td>
                    </tr>
                `).join('');
            }

            // Load top domains
            const topRes = await HttpClient.get('/api/v1/domains/top', { limit: 6 });
            const topList = document.getElementById('top-domains-list');
            if (topRes.data && topRes.data.length > 0) {
                topList.innerHTML = topRes.data.map(d => `
                    <div style="display:flex; justify-content:space-between; align-items:center; background:#090f1a; border:1px solid var(--border-subtle); padding:0.6rem 0.85rem; border-radius:var(--radius-md);">
                        <div>
                            <div style="font-weight:600; color:var(--text-primary); font-size:0.85rem;">${d.domain}</div>
                            <div style="font-size:0.7rem; color:var(--text-muted);">${d.category || 'General'}</div>
                        </div>
                        <div style="font-weight:700; color:var(--accent-cyan); font-family:monospace;">${d.count} queries</div>
                    </div>
                `).join('');
            }
        } catch (err) {
            Toast.error('Failed to load domain analytics.');
        }
    }
    loadDomains();
</script>
{% endblock %}
"""

with open("app/templates/domains/activity.html", "w", encoding="utf-8") as f:
    f.write(dom_html)

# 5. network/overview.html
net_html = """{% extends "base.html" %}

{% block content %}
<div class="page-header">
    <div>
        <h1 class="page-title">Network Infrastructure Overview</h1>
        <div class="page-subtitle">Subnets, gateways, sites, and interface telemetry</div>
    </div>
    <div>
        <a href="/topology" class="btn btn-primary btn-sm">🕸 View Topology Canvas</a>
    </div>
</div>

<div class="card" style="margin-bottom:1.5rem;">
    <div class="card-header" style="margin-bottom:1rem;">
        <div class="card-title" style="font-size:1rem; font-weight:700; color:#fff;">Enterprise Subnets & VLAN Allocation</div>
    </div>
    <div class="data-table-container">
        <table class="data-table">
            <thead>
                <tr>
                    <th>Subnet Name</th>
                    <th>CIDR Network</th>
                    <th>Gateway IP</th>
                    <th>VLAN</th>
                    <th>Active Devices</th>
                    <th>Network Zone</th>
                </tr>
            </thead>
            <tbody id="tbody-subnets">
                <tr><td colspan="6" style="text-align:center; padding:2rem;">Loading subnets...</td></tr>
            </tbody>
        </table>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script type="module">
    import { HttpClient } from '/static/js/core/http.js';
    import { Toast } from '/static/js/components/toast.js';

    async function loadNetwork() {
        try {
            const res = await HttpClient.get('/api/v1/network/overview');
            const subnets = res.data.subnets;
            const tbody = document.getElementById('tbody-subnets');
            
            if (!subnets || subnets.length === 0) {
                tbody.innerHTML = '<tr><td colspan="6" style="text-align:center; padding:2rem; color:var(--text-muted);">No subnets found.</td></tr>';
            } else {
                tbody.innerHTML = subnets.map(s => `
                    <tr>
                        <td style="font-weight:600; color:var(--text-primary);">${s.name}</td>
                        <td><code>${s.cidr}</code></td>
                        <td><code>${s.gateway_ip}</code></td>
                        <td><span class="badge badge-online">VLAN ${s.vlan_id || '1'}</span></td>
                        <td style="font-weight:700;">${s.device_count || 0} endpoints</td>
                        <td>
                            <span class="badge badge-online">
                                ${s.zone || 'Internal LAN'}
                            </span>
                        </td>
                    </tr>
                `).join('');
            }
        } catch (err) {
            Toast.error('Failed to load network subnets.');
        }
    }
    loadNetwork();
</script>
{% endblock %}
"""

with open("app/templates/network/overview.html", "w", encoding="utf-8") as f:
    f.write(net_html)

print("[+] All 5 templates fixed!")
