html_content = """{% extends "base.html" %}

{% block content %}
<div class="page-header">
    <div>
        <h1 class="page-title">Authorized Device Inventory</h1>
        <div class="page-subtitle">Hardware tracking, router-connected discovery, IP/MAC bindings, and asset risk scoring</div>
    </div>
    <div style="display:flex; gap:0.6rem; flex-wrap:wrap;">
        <button id="btn-discover-devices" class="btn btn-primary btn-sm">⚡ Discover Devices</button>
        <a href="/settings/data-sources" class="btn btn-secondary btn-sm">🔌 Add Data Source</a>
        <button id="btn-open-add-device" class="btn btn-secondary btn-sm">+ Register Manually</button>
        <a href="/api/v1/devices/export" class="btn btn-secondary btn-sm">⬇ Export CSV</a>
    </div>
</div>

<!-- Search & Filter Bar -->
<div class="card" style="margin-bottom:1.25rem; padding:1rem;">
    <div style="display:flex; gap:1rem; flex-wrap:wrap; align-items:center;">
        <input type="text" id="filter-search" class="form-input" placeholder="Search by name, IP, MAC, user, or vendor..." style="flex:1; min-width:240px; padding:0.5rem 0.75rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff; font-size:0.8rem;">
        
        <select id="filter-status" class="form-input" style="width:140px; padding:0.5rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff; font-size:0.8rem;">
            <option value="">All Statuses</option>
            <option value="online">Online</option>
            <option value="offline">Offline</option>
            <option value="degraded">Degraded</option>
            <option value="unauthorized">Quarantined</option>
        </select>

        <select id="filter-type" class="form-input" style="width:160px; padding:0.5rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff; font-size:0.8rem;">
            <option value="">All Device Types</option>
            <option value="workstation">Workstation</option>
            <option value="laptop">Laptop</option>
            <option value="server">Server</option>
            <option value="router">Router</option>
            <option value="switch">Switch</option>
            <option value="iot">IoT / Sensor</option>
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
                    <th>Status & Freshness</th>
                    <th>Discovery Source</th>
                    <th>Risk Score</th>
                    <th>Assigned User</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody id="tbody-devices">
                <tr><td colspan="8" style="text-align:center; padding:2rem;">Loading authorized device inventory...</td></tr>
            </tbody>
        </table>
    </div>
</div>

<!-- Optional Manual Fallback Modal -->
<div id="modal-add-device" class="modal-overlay">
    <div class="modal-box">
        <div class="modal-header">
            <h3 style="font-size:1.1rem; font-weight:700; color:#fff;">Register Manual Network Asset</h3>
            <button data-modal-close="modal-add-device" style="background:none; border:none; color:var(--text-muted); cursor:pointer; font-size:1.2rem;">✕</button>
        </div>
        <form id="form-add-device">
            <div class="modal-body">
                <div style="background:#090f1a; border:1px solid var(--border-subtle); padding:0.6rem 0.85rem; border-radius:var(--radius-md); font-size:0.75rem; color:var(--text-muted); margin-bottom:1rem;">
                    💡 <strong>Pro-Tip:</strong> Use <strong>Discover Devices</strong> to automatically ingest connected endpoints from your router/DHCP data source. Use this form only for manual asset registration.
                </div>
                <div style="margin-bottom:1rem;">
                    <label class="form-label" style="display:block; font-size:0.8rem; color:var(--text-muted); margin-bottom:0.3rem;">Device Name</label>
                    <input type="text" id="dev-name" class="form-input" required placeholder="ENG-WORKSTATION-42" style="width:100%; padding:0.55rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff; font-size:0.8rem;">
                </div>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-bottom:1rem;">
                    <div>
                        <label class="form-label" style="display:block; font-size:0.8rem; color:var(--text-muted); margin-bottom:0.3rem;">IP Address</label>
                        <input type="text" id="dev-ip" class="form-input" required placeholder="10.0.10.45" style="width:100%; padding:0.55rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff; font-size:0.8rem; font-family:monospace;">
                    </div>
                    <div>
                        <label class="form-label" style="display:block; font-size:0.8rem; color:var(--text-muted); margin-bottom:0.3rem;">MAC Address</label>
                        <input type="text" id="dev-mac" class="form-input" required placeholder="00:50:56:AB:CD:EF" style="width:100%; padding:0.55rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff; font-size:0.8rem; font-family:monospace;">
                    </div>
                </div>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-bottom:1rem;">
                    <div>
                        <label class="form-label" style="display:block; font-size:0.8rem; color:var(--text-muted); margin-bottom:0.3rem;">Device Type</label>
                        <select id="dev-type" class="form-input" style="width:100%; padding:0.55rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff; font-size:0.8rem;">
                            <option value="workstation">Workstation</option>
                            <option value="laptop">Laptop</option>
                            <option value="server">Server</option>
                            <option value="router">Router</option>
                            <option value="switch">Switch</option>
                            <option value="iot">IoT</option>
                        </select>
                    </div>
                    <div>
                        <label class="form-label" style="display:block; font-size:0.8rem; color:var(--text-muted); margin-bottom:0.3rem;">Operating System</label>
                        <input type="text" id="dev-os" class="form-input" placeholder="Ubuntu 24.04 LTS" style="width:100%; padding:0.55rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff; font-size:0.8rem;">
                    </div>
                </div>
                <div>
                    <label class="form-label" style="display:block; font-size:0.8rem; color:var(--text-muted); margin-bottom:0.3rem;">Assigned User Email</label>
                    <input type="email" id="dev-user" class="form-input" placeholder="engineer@netwatch.internal" style="width:100%; padding:0.55rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff; font-size:0.8rem;">
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" data-modal-close="modal-add-device" class="btn btn-secondary btn-sm">Cancel</button>
                <button type="submit" class="btn btn-primary btn-sm">Register Manual Asset</button>
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

    Modal.init();

    const urlParams = new URLSearchParams(window.location.search);
    const initialSearch = urlParams.get('search');
    if (initialSearch) {
        document.getElementById('filter-search').value = initialSearch;
    }

    async function loadDevices() {
        const search = document.getElementById('filter-search').value.trim();
        const status = document.getElementById('filter-status').value;
        const type = document.getElementById('filter-type').value;

        try {
            const res = await HttpClient.get('/api/v1/devices', { search, status, type, per_page: 50 });
            const items = (res && res.data && res.data.items) ? res.data.items : [];
            const tbody = document.getElementById('tbody-devices');

            if (items.length === 0) {
                tbody.innerHTML = `
                    <tr>
                        <td colspan="8" style="text-align:center; padding:3rem;">
                            <div style="font-size:2rem; margin-bottom:0.5rem;">🔌</div>
                            <div style="font-weight:700; color:#fff; font-size:1rem; margin-bottom:0.25rem;">No Devices Matching Filter</div>
                            <p style="font-size:0.75rem; color:var(--text-muted); margin-bottom:1rem;">Click "Discover Devices" to poll your authorized router/DHCP source.</p>
                            <button class="btn btn-primary btn-sm" onclick="triggerDiscovery()">⚡ Run Device Discovery</button>
                        </td>
                    </tr>
                `;
                return;
            }

            tbody.innerHTML = items.map(d => {
                const statusClass = `badge-${d.status || 'offline'}`;
                const riskColor = (d.risk_score > 60) ? '#ef4444' : ((d.risk_score > 30) ? '#f59e0b' : '#10b981');
                const srcLabel = (d.discovery_source || 'DISCOVERED_DHCP').replace('DISCOVERED_', '').replace('_', ' ');
                const freshnessClass = d.data_freshness === 'LIVE' ? '#10b981' : '#f59e0b';

                return `
                <tr>
                    <td>
                        <div style="font-weight:600; color:var(--text-primary);">${d.name}</div>
                        <div style="font-size:0.75rem; color:var(--text-muted); font-family:monospace;">${d.hostname || 'None'}</div>
                    </td>
                    <td>
                        <div><code style="color:#38bdf8;">${d.ip_address}</code></div>
                        <div style="font-size:0.72rem; color:var(--text-muted); font-family:monospace;">${d.mac_address}</div>
                    </td>
                    <td>
                        <div style="text-transform:capitalize; font-weight:500;">${d.device_type}</div>
                        <div style="font-size:0.72rem; color:var(--text-muted);">${d.operating_system || d.vendor || 'Generic'}</div>
                    </td>
                    <td>
                        <div style="display:flex; flex-direction:column; gap:0.2rem; align-items:flex-start;">
                            <span class="badge ${statusClass}">${d.status}</span>
                            <span style="font-size:0.65rem; color:${freshnessClass}; font-weight:700;">● ${d.data_freshness || 'LIVE'}</span>
                        </div>
                    </td>
                    <td>
                        <span class="badge badge-online" style="font-size:0.65rem; text-transform:uppercase;">${srcLabel}</span>
                    </td>
                    <td>
                        <span style="font-weight:700; color:${riskColor};">
                            ${d.risk_score ? d.risk_score.toFixed(1) : '0.0'}
                        </span>
                        <span style="font-size:0.7rem; color:var(--text-muted);">(${d.risk_level || 'LOW'})</span>
                    </td>
                    <td>
                        <div style="color:var(--text-primary); font-size:0.78rem;">${d.assigned_user || 'Unassigned'}</div>
                        <div style="font-size:0.7rem; color:var(--text-muted);">${d.assigned_email || ''}</div>
                    </td>
                    <td>
                        <div style="display:flex; gap:0.4rem;">
                            <a href="/ip-lookup?ip=${encodeURIComponent(d.ip_address)}" class="btn btn-primary btn-sm" style="padding:0.25rem 0.5rem;" title="Investigate in IP Center">🔍 Inspect</a>
                            <a href="/devices/${d.id}" class="btn btn-secondary btn-sm" style="padding:0.25rem 0.5rem;">360°</a>
                            <button class="btn btn-danger btn-sm btn-quarantine" data-id="${d.id}" data-quarantined="${d.is_quarantined}" style="padding:0.25rem 0.5rem;">
                                ${d.is_quarantined ? 'Unquarantine' : 'Quarantine'}
                            </button>
                        </div>
                    </td>
                </tr>
                `;
            }).join('');

            document.querySelectorAll('.btn-quarantine').forEach(btn => {
                btn.addEventListener('click', async (e) => {
                    const devId = e.currentTarget.dataset.id;
                    const isQ = e.currentTarget.dataset.quarantined === 'true';
                    try {
                        await HttpClient.post(`/api/v1/devices/${devId}/quarantine`, { quarantine: !isQ });
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

    window.triggerDiscovery = async function() {
        const btn = document.getElementById('btn-discover-devices');
        if (btn) {
            btn.disabled = true;
            btn.textContent = '⚡ Ingesting Network Sources...';
        }
        Toast.info('Connecting to authorized network controllers & DHCP lease tables...');

        try {
            const res = await HttpClient.post('/api/v1/data-sources/discover-all');
            Toast.success(res.data.message || 'Discovery sync completed.');
            loadDevices();
        } catch (e) {
            Toast.error(e.message || 'Discovery failed.');
        } finally {
            if (btn) {
                btn.disabled = false;
                btn.textContent = '⚡ Discover Devices';
            }
        }
    };

    document.getElementById('btn-discover-devices').addEventListener('click', window.triggerDiscovery);
    document.getElementById('btn-apply-filters').addEventListener('click', loadDevices);
    document.getElementById('filter-search').addEventListener('keyup', (e) => {
        if (e.key === 'Enter') loadDevices();
    });

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
            Toast.success('Manual asset registered.');
            Modal.close('modal-add-device');
            loadDevices();
        } catch (err) {
            Toast.error(err.message || 'Registration failed.');
        }
    });

    loadDevices();
</script>
{% endblock %}
"""

with open("app/templates/devices/list.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("[+] Updated app/templates/devices/list.html with Discover Devices, Add Data Source, and Register Manually!")
