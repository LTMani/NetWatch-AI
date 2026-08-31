import sys
sys.path.insert(0, '.')
from scripts.writer import write

# devices/list.html
devices_list_html = '''{% extends "base.html" %}

{% block content %}
<div class="page-header">
    <div>
        <h1 class="page-title">Authorized Device Inventory</h1>
        <div class="page-subtitle">Hardware tracking, IP/MAC bindings, OS signatures, and asset risk scoring</div>
    </div>
    <div style="display:flex; gap:0.75rem;">
        <a href="/api/v1/devices/export" class="btn btn-secondary btn-sm">⬇ Export CSV</a>
        <button id="btn-open-add-device" class="btn btn-primary btn-sm">+ Register Device</button>
    </div>
</div>

<!-- Search & Filter Bar -->
<div class="card" style="margin-bottom:1.25rem; padding:1rem;">
    <div style="display:flex; gap:1rem; flex-wrap:wrap; align-items:center;">
        <input type="text" id="filter-search" class="form-input" placeholder="Search by name, IP, MAC, or user..." style="flex:1; min-width:240px; padding:0.5rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;">
        
        <select id="filter-status" class="form-input" style="width:140px; padding:0.5rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;">
            <option value="">All Statuses</option>
            <option value="online">Online</option>
            <option value="offline">Offline</option>
            <option value="degraded">Degraded</option>
            <option value="unauthorized">Quarantined</option>
        </select>

        <select id="filter-type" class="form-input" style="width:160px; padding:0.5rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;">
            <option value="">All Device Types</option>
            <option value="workstation">Workstation</option>
            <option value="laptop">Laptop</option>
            <option value="server">Server</option>
            <option value="router">Router</option>
            <option value="switch">Switch</option>
            <option value="printer">Printer</option>
        </select>

        <button id="btn-apply-filters" class="btn btn-secondary btn-sm">Filter</button>
    </div>
</div>

<!-- Devices Table -->
<div class="card">
    <div class="data-table-container">
        <table class="data-table">
            <thead>
                <tr>
                    <th>Device / Hostname</th>
                    <th>IP & MAC Address</th>
                    <th>Type & OS</th>
                    <th>Status</th>
                    <th>Risk Score</th>
                    <th>Assigned User</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody id="tbody-devices">
                <tr><td colspan="7" style="text-align:center; padding:2rem;">Loading device inventory...</td></tr>
            </tbody>
        </table>
    </div>
</div>

<!-- Add Device Modal -->
<div id="modal-add-device" class="modal-overlay">
    <div class="modal-box">
        <div class="modal-header">
            <h3 style="font-size:1.1rem; font-weight:700;">Register New Network Asset</h3>
            <button data-modal-close="modal-add-device" style="background:none; border:none; color:var(--text-muted); cursor:pointer; font-size:1.2rem;">✕</button>
        </div>
        <form id="form-add-device">
            <div class="modal-body">
                <div style="margin-bottom:1rem;">
                    <label class="form-label" style="display:block; font-size:0.8rem; margin-bottom:0.3rem;">Device Name</label>
                    <input type="text" id="dev-name" class="form-input" required placeholder="ENG-WORKSTATION-42" style="width:100%; padding:0.55rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;">
                </div>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-bottom:1rem;">
                    <div>
                        <label class="form-label" style="display:block; font-size:0.8rem; margin-bottom:0.3rem;">IP Address</label>
                        <input type="text" id="dev-ip" class="form-input" required placeholder="192.168.10.45" style="width:100%; padding:0.55rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;">
                    </div>
                    <div>
                        <label class="form-label" style="display:block; font-size:0.8rem; margin-bottom:0.3rem;">MAC Address</label>
                        <input type="text" id="dev-mac" class="form-input" required placeholder="00:50:56:AB:CD:EF" style="width:100%; padding:0.55rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;">
                    </div>
                </div>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-bottom:1rem;">
                    <div>
                        <label class="form-label" style="display:block; font-size:0.8rem; margin-bottom:0.3rem;">Device Type</label>
                        <select id="dev-type" class="form-input" style="width:100%; padding:0.55rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;">
                            <option value="workstation">Workstation</option>
                            <option value="laptop">Laptop</option>
                            <option value="server">Server</option>
                            <option value="router">Router</option>
                            <option value="switch">Switch</option>
                        </select>
                    </div>
                    <div>
                        <label class="form-label" style="display:block; font-size:0.8rem; margin-bottom:0.3rem;">Operating System</label>
                        <input type="text" id="dev-os" class="form-input" placeholder="Ubuntu 24.04 LTS" style="width:100%; padding:0.55rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;">
                    </div>
                </div>
                <div>
                    <label class="form-label" style="display:block; font-size:0.8rem; margin-bottom:0.3rem;">Assigned User Email</label>
                    <input type="email" id="dev-user" class="form-input" placeholder="engineer@netwatch.internal" style="width:100%; padding:0.55rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;">
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" data-modal-close="modal-add-device" class="btn btn-secondary btn-sm">Cancel</button>
                <button type="submit" class="btn btn-primary btn-sm">Register Asset</button>
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

    async function loadDevices() {
        const search = document.getElementById('filter-search').value;
        const status = document.getElementById('filter-status').value;
        const type = document.getElementById('filter-type').value;

        try {
            const res = await HttpClient.get('/api/v1/devices', { search, status, type, per_page: 50 });
            const items = res.data.items;
            const tbody = document.getElementById('tbody-devices');

            if (items.length === 0) {
                tbody.innerHTML = '<tr><td colspan="7" style="text-align:center; padding:2rem; color:var(--text-muted);">No devices matching filter criteria.</td></tr>';
                return;
            }

            tbody.innerHTML = items.map(d => 
                <tr>
                    <td>
                        <div style="font-weight:600; color:var(--text-primary);"></div>
                        <div style="font-size:0.75rem; color:var(--text-muted);"></div>
                    </td>
                    <td>
                        <div><code></code></div>
                        <div style="font-size:0.75rem; color:var(--text-muted);"></div>
                    </td>
                    <td>
                        <div style="text-transform:capitalize;"></div>
                        <div style="font-size:0.75rem; color:var(--text-muted);"></div>
                    </td>
                    <td>
                        <span class="badge badge-">
                            
                        </span>
                    </td>
                    <td>
                        <span style="font-weight:700; color:;">
                            
                        </span>
                        <span style="font-size:0.75rem; color:var(--text-muted);">()</span>
                    </td>
                    <td>
                        <div></div>
                        <div style="font-size:0.75rem; color:var(--text-muted);"></div>
                    </td>
                    <td>
                        <div style="display:flex; gap:0.4rem;">
                            <a href="/devices/" class="btn btn-secondary btn-sm" style="padding:0.25rem 0.5rem;">360°</a>
                            <button class="btn btn-danger btn-sm btn-quarantine" data-id="" data-quarantined="" style="padding:0.25rem 0.5rem;">
                                
                            </button>
                        </div>
                    </td>
                </tr>
            ).join('');

            document.querySelectorAll('.btn-quarantine').forEach(btn => {
                btn.addEventListener('click', async (e) => {
                    const devId = e.target.dataset.id;
                    const isQ = e.target.dataset.quarantined === 'true';
                    try {
                        await HttpClient.post(/api/v1/devices//quarantine, { quarantine: !isQ });
                        Toast.success('Device quarantine state toggled.');
                        loadDevices();
                    } catch (err) {
                        Toast.error(err.message || 'Action failed.');
                    }
                });
            });
        } catch (err) {
            Toast.error('Failed to load device inventory.');
        }
    }

    document.getElementById('btn-apply-filters').addEventListener('click', loadDevices);
    document.getElementById('btn-open-add-device').addEventListener('click', () => Modal.open('modal-add-device'));

    document.getElementById('form-add-device').addEventListener('submit', async (e) => {
        e.preventDefault();
        const payload = {
            name: document.getElementById('dev-name').value.trim(),
            ip_address: document.getElementById('dev-ip').value.trim(),
            mac_address: document.getElementById('dev-mac').value.trim(),
            device_type: document.getElementById('dev-type').value,
            operating_system: document.getElementById('dev-os').value.trim(),
            assigned_email: document.getElementById('dev-user').value.trim()
        };

        try {
            await HttpClient.post('/api/v1/devices', payload);
            Toast.success('Device registered successfully.');
            Modal.close('modal-add-device');
            loadDevices();
        } catch (err) {
            Toast.error(err.message || 'Registration failed.');
        }
    });

    loadDevices();
</script>
{% endblock %}
'''
write('app/templates/devices/list.html', devices_list_html)

# devices/detail.html
dev_detail_html = '''{% extends "base.html" %}

{% block content %}
<div class="page-header">
    <div>
        <h1 class="page-title">Device 360: {{ device.name if device else 'Endpoint' }}</h1>
        <div class="page-subtitle">IP: <code>{{ device.ip_address if device else 'N/A' }}</code> | MAC: <code>{{ device.mac_address if device else 'N/A' }}</code></div>
    </div>
    <div>
        <a href="/devices" class="btn btn-secondary btn-sm">⬅ Back to Inventory</a>
    </div>
</div>

<div style="display:grid; grid-template-columns: 1fr 2fr; gap:1.5rem;">
    <!-- Asset Metadata Card -->
    <div class="card">
        <div class="card-header">
            <div class="card-title">Asset Specification</div>
            <span class="badge badge-{{ 'critical' if device and device.risk_score >= 50 else 'optimal' }}">
                Risk Score: {{ device.risk_score if device else 0 }}
            </span>
        </div>
        <div style="display:flex; flex-direction:column; gap:0.85rem; font-size:0.85rem;">
            <div style="display:flex; justify-content:space-between; border-bottom:1px solid var(--border-subtle); padding-bottom:0.5rem;">
                <span style="color:var(--text-muted);">Hardware Vendor</span>
                <span>{{ device.vendor if device else 'Enterprise Hardware' }}</span>
            </div>
            <div style="display:flex; justify-content:space-between; border-bottom:1px solid var(--border-subtle); padding-bottom:0.5rem;">
                <span style="color:var(--text-muted);">Device Type</span>
                <span style="text-transform:capitalize;">{{ device.device_type if device else 'Workstation' }}</span>
            </div>
            <div style="display:flex; justify-content:space-between; border-bottom:1px solid var(--border-subtle); padding-bottom:0.5rem;">
                <span style="color:var(--text-muted);">Operating System</span>
                <span>{{ device.operating_system if device else 'Linux' }}</span>
            </div>
            <div style="display:flex; justify-content:space-between; border-bottom:1px solid var(--border-subtle); padding-bottom:0.5rem;">
                <span style="color:var(--text-muted);">Assigned User</span>
                <span>{{ device.assigned_user or 'Unassigned' }}</span>
            </div>
            <div style="display:flex; justify-content:space-between;">
                <span style="color:var(--text-muted);">Authorization</span>
                <span class="badge badge-{{ 'optimal' if device and device.is_authorized else 'critical' }}">
                    {{ 'Authorized' if device and device.is_authorized else 'Unauthorized' }}
                </span>
            </div>
        </div>
    </div>

    <!-- Live Telemetry Stream -->
    <div class="card">
        <div class="card-header">
            <div class="card-title">Real-Time Bandwidth Utilization</div>
            <span class="badge badge-low">Live NetFlow Stream</span>
        </div>
        <div style="height:220px;">
            <canvas id="canvas-device-telemetry"></canvas>
        </div>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script type="module">
    import { ChartRenderer } from '/static/js/components/charts.js';
    const sampleData = [12, 18, 25, 42, 68, 55, 32, 28, 45, 52, 60, 48];
    const labels = ['-55m', '-50m', '-45m', '-40m', '-35m', '-30m', '-25m', '-20m', '-15m', '-10m', '-5m', 'Now'];
    ChartRenderer.renderLineChart('canvas-device-telemetry', labels, sampleData, '#38bdf8');
</script>
{% endblock %}
'''
write('app/templates/devices/detail.html', dev_detail_html)

# domains/activity.html
dom_act_html = '''{% extends "base.html" %}

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
        <div class="card-header">
            <div class="card-title">Live DNS Telemetry Feed</div>
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
        <div class="card-header">
            <div class="card-title">Top Queried Domains</div>
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

            if (queries.length === 0) {
                tbody.innerHTML = '<tr><td colspan="5" style="text-align:center; padding:2rem; color:var(--text-muted);">No domain queries recorded in current time window.</td></tr>';
            } else {
                tbody.innerHTML = queries.map(q => 
                    <tr>
                        <td style="font-weight:600; color:var(--text-primary); font-family:var(--font-mono);"></td>
                        <td><span class="badge badge-low"></span></td>
                        <td>
                            <span class="badge badge-">
                                
                            </span>
                        </td>
                        <td><code> ms</code></td>
                        <td><span class="badge badge-"></span></td>
                    </tr>
                ).join('');
            }

            // Load top domains
            const topRes = await HttpClient.get('/api/v1/domains/top', { limit: 6 });
            const topList = document.getElementById('top-domains-list');
            topList.innerHTML = topRes.data.map(d => 
                <div style="display:flex; justify-content:space-between; align-items:center; background:var(--bg-surface); padding:0.6rem 0.85rem; border-radius:var(--radius-md);">
                    <div>
                        <div style="font-weight:600; color:var(--text-primary); font-size:0.85rem;"></div>
                        <div style="font-size:0.7rem; color:var(--text-muted);"></div>
                    </div>
                    <div style="font-weight:700; color:var(--accent-cyan); font-family:var(--font-mono);"></div>
                </div>
            ).join('');
        } catch (err) {
            Toast.error('Failed to load domain analytics.');
        }
    }
    loadDomains();
</script>
{% endblock %}
'''
write('app/templates/domains/activity.html', dom_act_html)

print('Device list, Device detail, and Domain activity templates created.')
