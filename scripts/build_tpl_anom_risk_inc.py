import sys
sys.path.insert(0, '.')
from scripts.writer import write

# anomalies/index.html
anom_html = '''{% extends "base.html" %}

{% block content %}
<div class="page-header">
    <div>
        <h1 class="page-title">Anomaly Detection Center</h1>
        <div class="page-subtitle">Z-Score bandwidth spikes, EWMA off-hours exfiltration, and high-frequency DNS beaconing</div>
    </div>
    <div>
        <button id="btn-trigger-scan" class="btn btn-primary btn-sm">⚡ Run Anomaly Scan</button>
    </div>
</div>

<div class="card">
    <div class="data-table-container">
        <table class="data-table">
            <thead>
                <tr>
                    <th>Anomaly Type</th>
                    <th>Device / Subnet</th>
                    <th>Algorithm</th>
                    <th>Observed vs Baseline</th>
                    <th>Severity</th>
                    <th>Status</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody id="tbody-anomalies">
                <tr><td colspan="7" style="text-align:center; padding:2rem;">Loading detected anomalies...</td></tr>
            </tbody>
        </table>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script type="module">
    import { HttpClient } from '/static/js/core/http.js';
    import { Toast } from '/static/js/components/toast.js';

    async function loadAnomalies() {
        try {
            const res = await HttpClient.get('/api/v1/anomalies');
            const items = res.data.items;
            const tbody = document.getElementById('tbody-anomalies');

            if (items.length === 0) {
                tbody.innerHTML = '<tr><td colspan="7" style="text-align:center; padding:2rem; color:var(--text-muted);">No active anomalies detected across network flows.</td></tr>';
                return;
            }

            tbody.innerHTML = items.map(a => `
                <tr>
                    <td style="font-weight:600; color:var(--text-primary);">
                        ${a.anomaly_type.replace(/_/g, ' ').toUpperCase()}
                    </td>
                    <td><code>${a.device_id ? 'Device' : 'Subnet'}</code></td>
                    <td><span class="badge badge-low">${a.algorithm_used}</span></td>
                    <td>
                        <div>Observed: <code>${(a.observed_value / (1024*1024)).toFixed(1)} MB</code></div>
                        <div style="font-size:0.75rem; color:var(--text-muted);">Baseline: ${(a.baseline_value / (1024*1024)).toFixed(1)} MB</div>
                    </td>
                    <td><span class="badge badge-${a.severity === 'critical' ? 'critical' : (a.severity === 'high' ? 'high' : 'medium')}">${a.severity}</span></td>
                    <td>
                        <span class="badge badge-${a.is_acknowledged ? 'optimal' : 'medium'}">
                            ${a.is_acknowledged ? 'ACKNOWLEDGED' : 'ACTIVE'}
                        </span>
                    </td>
                    <td>
                        ${!a.is_acknowledged ? `
                            <button class="btn btn-secondary btn-sm btn-ack-anom" data-id="${a.id}">Ack</button>
                        ` : '<span style="color:var(--text-muted); font-size:0.8rem;">Reviewed</span>'}
                    </td>
                </tr>
            `).join('');

            document.querySelectorAll('.btn-ack-anom').forEach(btn => {
                btn.addEventListener('click', async (e) => {
                    const id = e.target.dataset.id;
                    try {
                        await HttpClient.post(`/api/v1/anomalies/${id}/acknowledge`);
                        Toast.success('Anomaly acknowledged.');
                        loadAnomalies();
                    } catch (err) {
                        Toast.error('Action failed.');
                    }
                });
            });
        } catch (err) {
            Toast.error('Failed to load anomalies.');
        }
    }

    document.getElementById('btn-trigger-scan').addEventListener('click', async () => {
        try {
            const res = await HttpClient.post('/api/v1/anomalies/detect');
            Toast.success(res.message);
            loadAnomalies();
        } catch (err) {
            Toast.error('Scan failed.');
        }
    });

    loadAnomalies();
</script>
{% endblock %}
'''
write('app/templates/anomalies/index.html', anom_html)

# risk/index.html
risk_html = '''{% extends "base.html" %}

{% block content %}
<div class="page-header">
    <div>
        <h1 class="page-title">Asset Risk Posture & Scoring</h1>
        <div class="page-subtitle">Dynamic Bayesian half-life decay risk calculation and multi-factor penalty attribution</div>
    </div>
    <div>
        <button id="btn-recalc-risk" class="btn btn-primary btn-sm">⟳ Recalculate Posture</button>
    </div>
</div>

<div class="card">
    <div class="card-header">
        <div class="card-title">Asset Risk Leaderboard</div>
    </div>
    <div class="data-table-container">
        <table class="data-table">
            <thead>
                <tr>
                    <th>Device Name</th>
                    <th>IP Address</th>
                    <th>Assigned User</th>
                    <th>Risk Score (0-100)</th>
                    <th>Classification</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody id="tbody-risk">
                <tr><td colspan="6" style="text-align:center; padding:2rem;">Loading asset risk evaluations...</td></tr>
            </tbody>
        </table>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script type="module">
    import { HttpClient } from '/static/js/core/http.js';
    import { Toast } from '/static/js/components/toast.js';

    async function loadRisk() {
        try {
            const res = await HttpClient.get('/api/v1/risk/leaderboard');
            const devs = res.data;
            const tbody = document.getElementById('tbody-risk');

            if (devs.length === 0) {
                tbody.innerHTML = '<tr><td colspan="6" style="text-align:center; padding:2rem; color:var(--text-muted);">All assets operating within nominal safety margins.</td></tr>';
                return;
            }

            tbody.innerHTML = devs.map(d => `
                <tr>
                    <td style="font-weight:600; color:var(--text-primary);">${d.name}</td>
                    <td><code>${d.ip_address}</code></td>
                    <td>${d.assigned_user || 'Unassigned'}</td>
                    <td style="font-weight:800; font-family:var(--font-mono); font-size:1.1rem; color:${d.risk_score >= 50 ? 'var(--status-critical)' : 'var(--status-optimal)'};">
                        ${d.risk_score}
                    </td>
                    <td><span class="badge badge-${d.risk_level === 'critical' ? 'critical' : (d.risk_level === 'high' ? 'high' : 'medium')}">${d.risk_level}</span></td>
                    <td><a href="/devices/${d.id}" class="btn btn-secondary btn-sm">Inspect Risk ➔</a></td>
                </tr>
            `).join('');
        } catch (err) {
            Toast.error('Failed to load risk leaderboard.');
        }
    }

    document.getElementById('btn-recalc-risk').addEventListener('click', async () => {
        try {
            const res = await HttpClient.post('/api/v1/risk/recalculate');
            Toast.success(res.message);
            loadRisk();
        } catch (err) {
            Toast.error('Recalculation failed.');
        }
    });

    loadRisk();
</script>
{% endblock %}
'''
write('app/templates/risk/index.html', risk_html)

# alerts/index.html
alerts_html = '''{% extends "base.html" %}

{% block content %}
<div class="page-header">
    <div>
        <h1 class="page-title">Correlated Alerts Center</h1>
        <div class="page-subtitle">Temporal and topological correlation groups reducing alert floods into actionable clusters</div>
    </div>
</div>

<div class="card">
    <div class="data-table-container">
        <table class="data-table">
            <thead>
                <tr>
                    <th>Alert Title</th>
                    <th>Category</th>
                    <th>Severity</th>
                    <th>Source</th>
                    <th>Status</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody id="tbody-alerts">
                <tr><td colspan="6" style="text-align:center; padding:2rem;">Loading alert telemetry...</td></tr>
            </tbody>
        </table>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script type="module">
    import { HttpClient } from '/static/js/core/http.js';
    import { Toast } from '/static/js/components/toast.js';

    async function loadAlerts() {
        try {
            const res = await HttpClient.get('/api/v1/alerts');
            const items = res.data.items;
            const tbody = document.getElementById('tbody-alerts');

            if (items.length === 0) {
                tbody.innerHTML = '<tr><td colspan="6" style="text-align:center; padding:2rem; color:var(--text-muted);">No active network alerts.</td></tr>';
                return;
            }

            tbody.innerHTML = items.map(a => `
                <tr>
                    <td>
                        <div style="font-weight:600; color:var(--text-primary);">${a.title}</div>
                        <div style="font-size:0.75rem; color:var(--text-secondary);">${a.message}</div>
                    </td>
                    <td><span class="badge badge-low">${a.category}</span></td>
                    <td><span class="badge badge-${a.severity === 'critical' ? 'critical' : (a.severity === 'high' ? 'high' : 'medium')}">${a.severity}</span></td>
                    <td><code>${a.source}</code></td>
                    <td>
                        <span class="badge badge-${a.is_acknowledged ? 'optimal' : 'medium'}">
                            ${a.is_acknowledged ? 'ACKNOWLEDGED' : 'ACTIVE'}
                        </span>
                    </td>
                    <td>
                        ${!a.is_acknowledged ? `
                            <button class="btn btn-secondary btn-sm btn-ack-alert" data-id="${a.id}">Ack</button>
                        ` : '<span style="color:var(--text-muted); font-size:0.8rem;">Reviewed</span>'}
                    </td>
                </tr>
            `).join('');

            document.querySelectorAll('.btn-ack-alert').forEach(btn => {
                btn.addEventListener('click', async (e) => {
                    const id = e.target.dataset.id;
                    try {
                        await HttpClient.post(`/api/v1/alerts/${id}/acknowledge`);
                        Toast.success('Alert acknowledged.');
                        loadAlerts();
                    } catch (err) {
                        Toast.error('Action failed.');
                    }
                });
            });
        } catch (err) {
            Toast.error('Failed to load alerts.');
        }
    }
    loadAlerts();
</script>
{% endblock %}
'''
write('app/templates/alerts/index.html', alerts_html)

# incidents/list.html
inc_list_html = '''{% extends "base.html" %}

{% block content %}
<div class="page-header">
    <div>
        <h1 class="page-title">Incident Response Board</h1>
        <div class="page-subtitle">Track, investigate, and resolve enterprise network outages and security breaches</div>
    </div>
    <div>
        <button id="btn-create-inc" class="btn btn-primary btn-sm">+ Create Incident</button>
    </div>
</div>

<div class="card">
    <div class="data-table-container">
        <table class="data-table">
            <thead>
                <tr>
                    <th>Incident #</th>
                    <th>Title & Summary</th>
                    <th>Severity</th>
                    <th>Status</th>
                    <th>Lead Investigator</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody id="tbody-incidents">
                <tr><td colspan="6" style="text-align:center; padding:2rem;">Loading incidents...</td></tr>
            </tbody>
        </table>
    </div>
</div>

<!-- Create Incident Modal -->
<div id="modal-create-inc" class="modal-overlay">
    <div class="modal-box">
        <div class="modal-header">
            <h3 style="font-size:1.1rem; font-weight:700;">Open Network Incident</h3>
            <button data-modal-close="modal-create-inc" style="background:none; border:none; color:var(--text-muted); cursor:pointer; font-size:1.2rem;">✕</button>
        </div>
        <form id="form-create-inc">
            <div class="modal-body">
                <div style="margin-bottom:1rem;">
                    <label class="form-label" style="display:block; font-size:0.8rem; margin-bottom:0.3rem;">Incident Title</label>
                    <input type="text" id="inc-title" class="form-input" required placeholder="Core Switch Trunk Link Flap in Building B" style="width:100%; padding:0.55rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;">
                </div>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-bottom:1rem;">
                    <div>
                        <label class="form-label" style="display:block; font-size:0.8rem; margin-bottom:0.3rem;">Severity</label>
                        <select id="inc-sev" class="form-input" style="width:100%; padding:0.55rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;">
                            <option value="sev2_high">SEV-2 High</option>
                            <option value="sev1_critical">SEV-1 Critical</option>
                            <option value="sev3_medium">SEV-3 Medium</option>
                            <option value="sev4_low">SEV-4 Low</option>
                        </select>
                    </div>
                    <div>
                        <label class="form-label" style="display:block; font-size:0.8rem; margin-bottom:0.3rem;">Category</label>
                        <input type="text" id="inc-cat" class="form-input" value="Network Performance" style="width:100%; padding:0.55rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;">
                    </div>
                </div>
                <div>
                    <label class="form-label" style="display:block; font-size:0.8rem; margin-bottom:0.3rem;">Incident Summary</label>
                    <textarea id="inc-summary" class="form-input" rows="3" placeholder="Describe the symptom, affected subnets, and customer impact..." style="width:100%; padding:0.55rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;"></textarea>
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" data-modal-close="modal-create-inc" class="btn btn-secondary btn-sm">Cancel</button>
                <button type="submit" class="btn btn-primary btn-sm">Open Incident</button>
            </div>
        </form>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script type="module">
    import { HttpClient } from '/static/js/core/http.js';
    import { Modal } from '/static/js/components/modal.js';
    import { Toast } from '/static/js/components/toast.js';

    async function loadIncidents() {
        try {
            const res = await HttpClient.get('/api/v1/incidents');
            const items = res.data.items;
            const tbody = document.getElementById('tbody-incidents');

            if (items.length === 0) {
                tbody.innerHTML = '<tr><td colspan="6" style="text-align:center; padding:2rem; color:var(--text-muted);">No open incidents. All services operational.</td></tr>';
                return;
            }

            tbody.innerHTML = items.map(inc => `
                <tr>
                    <td><code style="font-weight:700; color:var(--accent-cyan);">${inc.incident_number}</code></td>
                    <td>
                        <div style="font-weight:600; color:var(--text-primary);">${inc.title}</div>
                        <div style="font-size:0.75rem; color:var(--text-secondary);">${inc.summary}</div>
                    </td>
                    <td><span class="badge badge-${inc.severity.includes('critical') ? 'critical' : 'high'}">${inc.severity.toUpperCase()}</span></td>
                    <td><span class="badge badge-${inc.status === 'resolved' ? 'optimal' : 'medium'}">${inc.status.toUpperCase()}</span></td>
                    <td>${inc.lead_investigator || 'admin'}</td>
                    <td><a href="/incidents/${inc.id}" class="btn btn-secondary btn-sm">War Room ➔</a></td>
                </tr>
            `).join('');
        } catch (err) {
            Toast.error('Failed to load incidents.');
        }
    }

    document.getElementById('btn-create-inc').addEventListener('click', () => Modal.open('modal-create-inc'));

    document.getElementById('form-create-inc').addEventListener('submit', async (e) => {
        e.preventDefault();
        const payload = {
            title: document.getElementById('inc-title').value.trim(),
            severity: document.getElementById('inc-sev').value,
            category: document.getElementById('inc-cat').value.trim(),
            summary: document.getElementById('inc-summary').value.trim()
        };

        try {
            await HttpClient.post('/api/v1/incidents', payload);
            Toast.success('Incident opened successfully.');
            Modal.close('modal-create-inc');
            loadIncidents();
        } catch (err) {
            Toast.error(err.message || 'Creation failed.');
        }
    });

    loadIncidents();
</script>
{% endblock %}
'''
write('app/templates/incidents/list.html', inc_list_html)

# incidents/detail.html
inc_detail_html = '''{% extends "base.html" %}

{% block content %}
<div class="page-header">
    <div>
        <h1 class="page-title">War Room: {{ incident.incident_number if incident else 'INC-2026-0001' }}</h1>
        <div class="page-subtitle">{{ incident.title if incident else 'Core Performance Incident' }}</div>
    </div>
    <div style="display:flex; gap:0.75rem;">
        <select id="select-inc-status" class="form-input" style="padding:0.4rem 0.75rem; background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;">
            <option value="open" {% if incident and incident.status == 'open' %}selected{% endif %}>Open</option>
            <option value="investigating" {% if incident and incident.status == 'investigating' %}selected{% endif %}>Investigating</option>
            <option value="identified" {% if incident and incident.status == 'identified' %}selected{% endif %}>Identified</option>
            <option value="monitoring" {% if incident and incident.status == 'monitoring' %}selected{% endif %}>Monitoring</option>
            <option value="resolved" {% if incident and incident.status == 'resolved' %}selected{% endif %}>Resolved</option>
        </select>
        <button id="btn-save-status" class="btn btn-primary btn-sm">Update State</button>
    </div>
</div>

<div style="display:grid; grid-template-columns: 2fr 1fr; gap:1.5rem;">
    <!-- Investigation Timeline -->
    <div class="card">
        <div class="card-header">
            <div class="card-title">Investigation Activity Timeline</div>
        </div>
        <div id="timeline-container" style="display:flex; flex-direction:column; gap:1rem; padding:0.5rem 0;">
            {% if incident and incident.timeline_entries %}
                {% for entry in incident.timeline_entries %}
                    <div style="border-left:2px solid var(--accent-cyan); padding-left:1rem;">
                        <div style="font-size:0.75rem; color:var(--text-muted);">{{ entry.timestamp.strftime('%Y-%m-%d %H:%M UTC') }} by <b>{{ entry.author }}</b></div>
                        <div style="font-size:0.85rem; color:var(--text-primary); margin-top:0.25rem;">{{ entry.message }}</div>
                    </div>
                {% endfor %}
            {% else %}
                <div style="color:var(--text-muted); text-align:center; padding:2rem;">No timeline entries recorded yet.</div>
            {% endif %}
        </div>

        <form id="form-add-timeline" style="margin-top:1.5rem; display:flex; gap:0.5rem;">
            <input type="text" id="input-timeline-note" class="form-input" placeholder="Add investigation note or finding..." required style="flex:1; padding:0.55rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;">
            <button type="submit" class="btn btn-secondary btn-sm">+ Post Note</button>
        </form>
    </div>

    <!-- Metadata Panel -->
    <div class="card">
        <div class="card-header">
            <div class="card-title">Incident Meta</div>
            <span class="badge badge-high">{{ incident.severity if incident else 'SEV-2' }}</span>
        </div>
        <div style="font-size:0.85rem; display:flex; flex-direction:column; gap:0.75rem;">
            <div>
                <span style="color:var(--text-muted);">Summary:</span>
                <p style="color:var(--text-primary); margin-top:0.25rem;">{{ incident.summary if incident else 'No summary' }}</p>
            </div>
            <div>
                <span style="color:var(--text-muted);">Lead Investigator:</span>
                <p style="color:var(--text-primary);">{{ incident.lead_investigator if incident else 'admin' }}</p>
            </div>
            <div>
                <span style="color:var(--text-muted);">Category:</span>
                <p style="color:var(--text-primary);">{{ incident.category if incident else 'Network Performance' }}</p>
            </div>
        </div>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script type="module">
    import { HttpClient } from '/static/js/core/http.js';
    import { Toast } from '/static/js/components/toast.js';

    const incId = '{{ incident.id if incident else "" }}';

    document.getElementById('btn-save-status').addEventListener('click', async () => {
        const newStatus = document.getElementById('select-inc-status').value;
        try {
            await HttpClient.patch(`/api/v1/incidents/${incId}/status`, { status: newStatus });
            Toast.success('Incident status updated.');
            setTimeout(() => window.location.reload(), 400);
        } catch (err) {
            Toast.error('Failed to update status.');
        }
    });

    document.getElementById('form-add-timeline').addEventListener('submit', async (e) => {
        e.preventDefault();
        const note = document.getElementById('input-timeline-note').value.trim();
        try {
            await HttpClient.post(`/api/v1/incidents/${incId}/timeline`, { message: note, entry_type: 'NOTE' });
            Toast.success('Timeline note added.');
            setTimeout(() => window.location.reload(), 400);
        } catch (err) {
            Toast.error('Failed to post note.');
        }
    });
</script>
{% endblock %}
'''
write('app/templates/incidents/detail.html', inc_detail_html)

print('Anomalies, Risk, Alerts, and Incident templates created.')
