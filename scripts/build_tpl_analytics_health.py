import sys
sys.path.insert(0, '.')
from scripts.writer import write

# analytics/bandwidth.html
bw_html = '''{% extends "base.html" %}

{% block content %}
<div class="page-header">
    <div>
        <h1 class="page-title">Bandwidth Analytics & Throughput</h1>
        <div class="page-subtitle">Real-time interface ingress/egress analysis, top talkers, and protocol distribution</div>
    </div>
</div>

<div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap:1.25rem; margin-bottom:1.5rem;">
    <div class="card kpi-card">
        <div class="kpi-label">Total Ingress Volume</div>
        <div class="kpi-value" id="kpi-bw-in" style="color:var(--accent-cyan);">-- GB</div>
        <div class="kpi-subtext">Inbound Traffic</div>
    </div>
    <div class="card kpi-card">
        <div class="kpi-label">Total Egress Volume</div>
        <div class="kpi-value" id="kpi-bw-out" style="color:var(--accent-blue);">-- GB</div>
        <div class="kpi-subtext">Outbound Traffic</div>
    </div>
    <div class="card kpi-card">
        <div class="kpi-label">Total Bandwidth Exchanged</div>
        <div class="kpi-value" id="kpi-bw-total" style="color:var(--accent-emerald);">-- GB</div>
        <div class="kpi-subtext">Past 24 Hours</div>
    </div>
</div>

<div class="card">
    <div class="card-header">
        <div class="card-title">Top Bandwidth Consuming Endpoints</div>
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

            document.getElementById('kpi-bw-in').textContent = ${gbIn} GB;
            document.getElementById('kpi-bw-out').textContent = ${gbOut} GB;
            document.getElementById('kpi-bw-total').textContent = ${gbTot} GB;

            const tbody = document.getElementById('tbody-top-hogs');
            if (d.top_consumers.length === 0) {
                tbody.innerHTML = '<tr><td colspan="4" style="text-align:center; padding:2rem; color:var(--text-muted);">No bandwidth telemetry collected.</td></tr>';
            } else {
                tbody.innerHTML = d.top_consumers.map(c => 
                    <tr>
                        <td style="font-weight:600; color:var(--text-primary);"></td>
                        <td><code></code></td>
                        <td style="text-transform:capitalize;"></td>
                        <td style="font-weight:700; color:var(--accent-cyan); font-family:var(--font-mono);">
                             GB
                        </td>
                    </tr>
                ).join('');
            }
        } catch (err) {
            Toast.error('Failed to load bandwidth analytics.');
        }
    }
    loadBandwidth();
</script>
{% endblock %}
'''
write('app/templates/analytics/bandwidth.html', bw_html)

# analytics/office_hours.html
office_html = '''{% extends "base.html" %}

{% block content %}
<div class="page-header">
    <div>
        <h1 class="page-title">Office Hours vs Off-Hours Analytics</h1>
        <div class="page-subtitle">Comparative network traffic distribution, baseline compliance, and quiet-hours anomaly inspection</div>
    </div>
</div>

<div style="display:grid; grid-template-columns: 1fr 1fr; gap:1.5rem; margin-bottom:1.5rem;">
    <div class="card kpi-card">
        <div class="kpi-label">Business Hours Volume (09:00 - 18:00)</div>
        <div class="kpi-value" id="kpi-office-pct" style="color:var(--status-optimal);">--%</div>
        <div class="kpi-subtext" id="kpi-office-gb">-- GB during working shift</div>
    </div>

    <div class="card kpi-card">
        <div class="kpi-label">Off-Hours Traffic (Night / Weekend)</div>
        <div class="kpi-value" id="kpi-off-pct" style="color:var(--accent-amber);">--%</div>
        <div class="kpi-subtext" id="kpi-off-gb">-- GB quiet hours volume</div>
    </div>
</div>

<div class="card">
    <div class="card-header">
        <div class="card-title">Top Active Devices During Off-Hours</div>
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

            document.getElementById('kpi-office-pct').textContent = ${d.office_hours_percentage}%;
            document.getElementById('kpi-office-gb').textContent = ${(d.office_hours_bytes / (1024*1024*1024)).toFixed(2)} GB working shift volume;
            document.getElementById('kpi-off-pct').textContent = ${d.off_hours_percentage}%;
            document.getElementById('kpi-off-gb').textContent = ${(d.off_hours_bytes / (1024*1024*1024)).toFixed(2)} GB off-hours volume;

            const tbody = document.getElementById('tbody-off-devices');
            if (d.top_off_hours_devices.length === 0) {
                tbody.innerHTML = '<tr><td colspan="4" style="text-align:center; padding:2rem; color:var(--text-muted);">No off-hours activity recorded.</td></tr>';
            } else {
                tbody.innerHTML = d.top_off_hours_devices.map(dev => 
                    <tr>
                        <td style="font-weight:600; color:var(--text-primary);"></td>
                        <td><code></code></td>
                        <td></td>
                        <td style="font-weight:700; color:var(--accent-amber); font-family:var(--font-mono);">
                             MB
                        </td>
                    </tr>
                ).join('');
            }
        } catch (err) {
            Toast.error('Failed to load office hours analytics.');
        }
    }
    loadOfficeHours();
</script>
{% endblock %}
'''
write('app/templates/analytics/office_hours.html', office_html)

# health/index.html
health_html = '''{% extends "base.html" %}

{% block content %}
<div class="page-header">
    <div>
        <h1 class="page-title">Enterprise Network Health Engine</h1>
        <div class="page-subtitle">Composite health scoring model across path latency, packet drop, jitter, saturation, and link reliability</div>
    </div>
    <div>
        <a href="/diagnostics/slow-network" class="btn btn-primary btn-sm">⚡ Run Diagnostic Wizard</a>
    </div>
</div>

<div style="display:grid; grid-template-columns: 1fr 2fr; gap:1.5rem; margin-bottom:1.5rem;">
    <!-- Composite Score Card -->
    <div class="card" style="text-align:center; padding:2rem;">
        <div style="font-size:0.85rem; font-weight:700; color:var(--text-muted); text-transform:uppercase; margin-bottom:1rem;">Overall Network Health</div>
        <div id="health-big-score" style="font-size:4.5rem; font-weight:900; color:var(--status-optimal); font-family:var(--font-mono); line-height:1;">
            --
        </div>
        <div id="health-big-status" class="badge badge-optimal" style="margin-top:1rem; font-size:0.85rem; padding:0.4rem 1rem;">
            OPTIMAL
        </div>
        <div id="health-big-explanation" style="font-size:0.85rem; color:var(--text-secondary); margin-top:1.25rem; line-height:1.5;">
            Loading health model explanation...
        </div>
    </div>

    <!-- Health Vectors Card -->
    <div class="card">
        <div class="card-header">
            <div class="card-title">Telemetry Vector Scores (0-100)</div>
        </div>
        <div style="display:flex; flex-direction:column; gap:1.25rem; padding:0.5rem 0;">
            <div>
                <div style="display:flex; justify-content:space-between; font-size:0.85rem; margin-bottom:0.35rem;">
                    <span>Round-Trip Path Latency</span>
                    <span id="score-lat" style="font-weight:700; color:var(--accent-cyan);">--/100</span>
                </div>
                <div style="height:8px; background:var(--bg-surface); border-radius:var(--radius-full); overflow:hidden;">
                    <div id="bar-lat" style="width:0%; height:100%; background:var(--accent-cyan); transition:width 0.5s ease;"></div>
                </div>
            </div>

            <div>
                <div style="display:flex; justify-content:space-between; font-size:0.85rem; margin-bottom:0.35rem;">
                    <span>Packet Loss Rate</span>
                    <span id="score-loss" style="font-weight:700; color:var(--accent-emerald);">--/100</span>
                </div>
                <div style="height:8px; background:var(--bg-surface); border-radius:var(--radius-full); overflow:hidden;">
                    <div id="bar-loss" style="width:0%; height:100%; background:var(--accent-emerald); transition:width 0.5s ease;"></div>
                </div>
            </div>

            <div>
                <div style="display:flex; justify-content:space-between; font-size:0.85rem; margin-bottom:0.35rem;">
                    <span>Jitter Stability</span>
                    <span id="score-jitter" style="font-weight:700; color:var(--accent-blue);">--/100</span>
                </div>
                <div style="height:8px; background:var(--bg-surface); border-radius:var(--radius-full); overflow:hidden;">
                    <div id="bar-jitter" style="width:0%; height:100%; background:var(--accent-blue); transition:width 0.5s ease;"></div>
                </div>
            </div>

            <div>
                <div style="display:flex; justify-content:space-between; font-size:0.85rem; margin-bottom:0.35rem;">
                    <span>Bandwidth Saturation</span>
                    <span id="score-bw" style="font-weight:700; color:var(--accent-purple);">--/100</span>
                </div>
                <div style="height:8px; background:var(--bg-surface); border-radius:var(--radius-full); overflow:hidden;">
                    <div id="bar-bw" style="width:0%; height:100%; background:var(--accent-purple); transition:width 0.5s ease;"></div>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script type="module">
    import { HttpClient } from '/static/js/core/http.js';
    import { Toast } from '/static/js/components/toast.js';

    async function loadHealth() {
        try {
            const res = await HttpClient.get('/api/v1/health/current');
            const h = res.data;

            document.getElementById('health-big-score').textContent = h.overall_score;
            document.getElementById('health-big-score').style.color = h.overall_score >= 80 ? 'var(--status-optimal)' : (h.overall_score >= 60 ? 'var(--status-degraded)' : 'var(--status-critical)');
            document.getElementById('health-big-status').textContent = h.health_status.toUpperCase();
            document.getElementById('health-big-explanation').textContent = h.explanation;

            document.getElementById('score-lat').textContent = ${h.latency_score}/100;
            document.getElementById('bar-lat').style.width = ${h.latency_score}%;

            document.getElementById('score-loss').textContent = ${h.packet_loss_score}/100;
            document.getElementById('bar-loss').style.width = ${h.packet_loss_score}%;

            document.getElementById('score-jitter').textContent = ${h.jitter_score}/100;
            document.getElementById('bar-jitter').style.width = ${h.jitter_score}%;

            document.getElementById('score-bw').textContent = ${h.bandwidth_score}/100;
            document.getElementById('bar-bw').style.width = ${h.bandwidth_score}%;
        } catch (err) {
            Toast.error('Failed to load health metrics.');
        }
    }
    loadHealth();
</script>
{% endblock %}
'''
write('app/templates/health/index.html', health_html)

# diagnostics/slow_network.html
diag_html = '''{% extends "base.html" %}

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
    <div class="card-header">
        <div class="card-title">Probe Pipeline Stages</div>
        <span id="badge-diag-status" class="badge badge-optimal">READY</span>
    </div>
    
    <div id="diag-steps-container" style="display:flex; flex-direction:column; gap:0.75rem;">
        <div style="text-align:center; padding:3rem; color:var(--text-muted);">
            Click "Execute Diagnostic Probe" to run live 7-stage network health inspection.
        </div>
    </div>
</div>

<!-- Root Cause Synthesis & Playbook -->
<div id="diag-synthesis-card" class="card" style="display:none;">
    <div class="card-header">
        <div class="card-title">Root Cause Synthesis & Remediation Playbook</div>
    </div>
    <div style="background:var(--bg-surface); padding:1rem; border-radius:var(--radius-md); margin-bottom:1rem;">
        <div style="font-weight:700; color:var(--accent-cyan); margin-bottom:0.25rem;">Identified Bottleneck:</div>
        <div id="txt-root-cause" style="color:var(--text-primary); font-size:0.9rem;">--</div>
    </div>
    <div>
        <div style="font-weight:700; color:var(--status-optimal); margin-bottom:0.25rem;">Actionable Remediation Playbook:</div>
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
        document.getElementById('badge-diag-status').className = 'badge badge-medium';

        try {
            const res = await HttpClient.post('/api/v1/diagnostics/run', { scope: 'Global Gateway' });
            const data = res.data;
            const steps = data.steps;

            const container = document.getElementById('diag-steps-container');
            container.innerHTML = steps.map(s => 
                <div style="background:var(--bg-surface); padding:1rem; border-radius:var(--radius-md); border-left:4px solid ;">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.25rem;">
                        <div style="font-weight:700; color:var(--text-primary); font-size:0.9rem;">
                            Stage : 
                        </div>
                        <span class="badge badge-"></span>
                    </div>
                    <div style="font-size:0.8rem; color:var(--text-secondary); margin-bottom:0.25rem;"></div>
                    <div style="font-size:0.75rem; color:var(--text-muted);">Observed: <code></code> (Threshold: )</div>
                </div>
            ).join('');

            // Show synthesis
            document.getElementById('diag-synthesis-card').style.display = 'block';
            document.getElementById('txt-root-cause').textContent = data.session.root_cause_summary;
            document.getElementById('txt-playbook').textContent = data.session.remediation_playbook;

            document.getElementById('badge-diag-status').textContent = 'COMPLETED';
            document.getElementById('badge-diag-status').className = 'badge badge-optimal';
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
'''
write('app/templates/diagnostics/slow_network.html', diag_html)

print('Analytics, Health, and Diagnostics templates created.')
