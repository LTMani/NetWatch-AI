import sys
sys.path.insert(0, '.')
from scripts.writer import write

# policies/index.html
policies_html = '''{% extends "base.html" %}

{% block content %}
<div class="page-header">
    <div>
        <h1 class="page-title">Traffic Policies & Rule Builder</h1>
        <div class="page-subtitle">Define automated threshold triggers, domain category restrictions, and violation actions</div>
    </div>
    <div>
        <button id="btn-create-policy" class="btn btn-primary btn-sm">+ Create Policy</button>
    </div>
</div>

<div class="card">
    <div class="data-table-container">
        <table class="data-table">
            <thead>
                <tr>
                    <th>Policy Name</th>
                    <th>Category</th>
                    <th>Action</th>
                    <th>Severity</th>
                    <th>Violations</th>
                    <th>State</th>
                    <th>Toggle</th>
                </tr>
            </thead>
            <tbody id="tbody-policies">
                <tr><td colspan="7" style="text-align:center; padding:2rem;">Loading policies...</td></tr>
            </tbody>
        </table>
    </div>
</div>

<!-- Create Policy Modal -->
<div id="modal-create-pol" class="modal-overlay">
    <div class="modal-box">
        <div class="modal-header">
            <h3 style="font-size:1.1rem; font-weight:700;">Define Traffic Policy</h3>
            <button data-modal-close="modal-create-pol" style="background:none; border:none; color:var(--text-muted); cursor:pointer; font-size:1.2rem;">✕</button>
        </div>
        <form id="form-create-pol">
            <div class="modal-body">
                <div style="margin-bottom:1rem;">
                    <label class="form-label" style="display:block; font-size:0.8rem; margin-bottom:0.3rem;">Policy Name</label>
                    <input type="text" id="pol-name" class="form-input" required placeholder="Restrict Heavy P2P & Streaming During Office Hours" style="width:100%; padding:0.55rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;">
                </div>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-bottom:1rem;">
                    <div>
                        <label class="form-label" style="display:block; font-size:0.8rem; margin-bottom:0.3rem;">Category</label>
                        <select id="pol-cat" class="form-input" style="width:100%; padding:0.55rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;">
                            <option value="BANDWIDTH">Bandwidth Threshold</option>
                            <option value="DOMAIN">Domain Category</option>
                            <option value="SECURITY">Security Posture</option>
                        </select>
                    </div>
                    <div>
                        <label class="form-label" style="display:block; font-size:0.8rem; margin-bottom:0.3rem;">Action</label>
                        <select id="pol-act" class="form-input" style="width:100%; padding:0.55rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;">
                            <option value="create_incident">Create Incident & Alert</option>
                            <option value="alert_only">Alert Only</option>
                            <option value="quarantine_device">Auto-Quarantine Device</option>
                        </select>
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" data-modal-close="modal-create-pol" class="btn btn-secondary btn-sm">Cancel</button>
                <button type="submit" class="btn btn-primary btn-sm">Save Policy</button>
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

    async function loadPolicies() {
        try {
            const res = await HttpClient.get('/api/v1/policies');
            const items = res.data;
            const tbody = document.getElementById('tbody-policies');

            if (items.length === 0) {
                tbody.innerHTML = '<tr><td colspan="7" style="text-align:center; padding:2rem; color:var(--text-muted);">No policies configured.</td></tr>';
                return;
            }

            tbody.innerHTML = items.map(p => `
                <tr>
                    <td>
                        <div style="font-weight:600; color:var(--text-primary);">${p.name}</div>
                        <div style="font-size:0.75rem; color:var(--text-muted);">${p.description || 'Enterprise rule'}</div>
                    </td>
                    <td><span class="badge badge-low">${p.category}</span></td>
                    <td><code>${p.action}</code></td>
                    <td><span class="badge badge-${p.severity === 'critical' ? 'critical' : 'high'}">${p.severity.toUpperCase()}</span></td>
                    <td style="font-weight:700; color:${p.violation_count > 0 ? 'var(--status-critical)' : 'var(--text-muted)'};">${p.violation_count}</td>
                    <td>
                        <span class="badge badge-${p.is_enabled ? 'optimal' : 'medium'}">
                            ${p.is_enabled ? 'ACTIVE' : 'DISABLED'}
                        </span>
                    </td>
                    <td>
                        <button class="btn btn-secondary btn-sm btn-toggle-pol" data-id="${p.id}">
                            ${p.is_enabled ? 'Disable' : 'Enable'}
                        </button>
                    </td>
                </tr>
            `).join('');

            document.querySelectorAll('.btn-toggle-pol').forEach(btn => {
                btn.addEventListener('click', async (e) => {
                    const id = e.target.dataset.id;
                    try {
                        await HttpClient.patch(`/api/v1/policies/${id}/toggle`);
                        Toast.success('Policy state updated.');
                        loadPolicies();
                    } catch (err) {
                        Toast.error('Action failed.');
                    }
                });
            });
        } catch (err) {
            Toast.error('Failed to load policies.');
        }
    }

    document.getElementById('btn-create-policy').addEventListener('click', () => Modal.open('modal-create-pol'));

    document.getElementById('form-create-pol').addEventListener('submit', async (e) => {
        e.preventDefault();
        const payload = {
            name: document.getElementById('pol-name').value.trim(),
            category: document.getElementById('pol-cat').value,
            action: document.getElementById('pol-act').value
        };
        try {
            await HttpClient.post('/api/v1/policies', payload);
            Toast.success('Policy created.');
            Modal.close('modal-create-pol');
            loadPolicies();
        } catch (err) {
            Toast.error(err.message || 'Creation failed.');
        }
    });

    loadPolicies();
</script>
{% endblock %}
'''
write('app/templates/policies/index.html', policies_html)

# topology/index.html
topo_html = '''{% extends "base.html" %}

{% block content %}
<div class="page-header">
    <div>
        <h1 class="page-title">Interactive Network Topology Graph</h1>
        <div class="page-subtitle">Force-directed hierarchical layout: Edge Firewall ➔ Core Router ➔ Distribution Switches ➔ Endpoints</div>
    </div>
    <div>
        <a href="/digital-twin" class="btn btn-primary btn-sm">⚇ Launch What-If Sandbox</a>
    </div>
</div>

<div class="card" style="padding:0; overflow:hidden; position:relative; height:620px; background:#070a10;">
    <div style="position:absolute; top:1rem; left:1.5rem; z-index:10; display:flex; gap:0.5rem;">
        <span class="badge badge-optimal">Link Flow: Live NetFlow</span>
        <span class="badge badge-low">Layout: Hierarchical Tier</span>
    </div>

    <canvas id="canvas-topology" style="width:100%; height:100%; display:block;"></canvas>
</div>
{% endblock %}

{% block scripts %}
<script type="module">
    import { HttpClient } from '/static/js/core/http.js';
    import { Toast } from '/static/js/components/toast.js';

    async function renderTopology() {
        const canvas = document.getElementById('canvas-topology');
        const ctx = canvas.getContext('2d');
        const w = canvas.width = canvas.parentElement.clientWidth;
        const h = canvas.height = canvas.parentElement.clientHeight;

        try {
            const res = await HttpClient.get('/api/v1/topology/graph');
            const nodes = res.data.nodes;
            const links = res.data.links;

            // Draw Background Grid
            ctx.strokeStyle = '#0f172a';
            ctx.lineWidth = 1;
            for (let x = 0; x < w; x += 40) {
                ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke();
            }
            for (let y = 0; y < h; y += 40) {
                ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
            }

            // Map nodes by key
            const nodeMap = {};
            nodes.forEach(n => {
                nodeMap[n.node_key] = n;
            });

            // Draw Links
            links.forEach(l => {
                const src = nodeMap[l.source_node_key];
                const tgt = nodeMap[l.target_node_key];
                if (src && tgt) {
                    ctx.beginPath();
                    ctx.strokeStyle = l.status === 'UP' ? 'rgba(0, 240, 255, 0.4)' : 'rgba(239, 68, 68, 0.6)';
                    ctx.lineWidth = 2;
                    ctx.moveTo(src.pos_x, src.pos_y);
                    ctx.lineTo(tgt.pos_x, tgt.pos_y);
                    ctx.stroke();

                    // Bandwidth label
                    const mx = (src.pos_x + tgt.pos_x) / 2;
                    const my = (src.pos_y + tgt.pos_y) / 2;
                    ctx.fillStyle = '#64748b';
                    ctx.font = '10px monospace';
                    ctx.fillText(`${l.current_traffic_mbps} Mbps`, mx + 4, my - 4);
                }
            });

            // Draw Nodes
            nodes.forEach(n => {
                ctx.beginPath();
                ctx.arc(n.pos_x, n.pos_y, 22, 0, Math.PI * 2);
                ctx.fillStyle = '#162032';
                ctx.fill();
                ctx.strokeStyle = n.tier_level <= 1 ? '#00f0ff' : '#38bdf8';
                ctx.lineWidth = 2.5;
                ctx.stroke();

                // Icon / Label
                ctx.fillStyle = '#f8fafc';
                ctx.font = 'bold 10px sans-serif';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText(n.node_type.substring(0, 4).toUpperCase(), n.pos_x, n.pos_y);

                // Label below
                ctx.fillStyle = '#94a3b8';
                ctx.font = '11px sans-serif';
                ctx.fillText(n.label, n.pos_x, n.pos_y + 34);
            });
        } catch (err) {
            Toast.error('Failed to load topology.');
        }
    }

    renderTopology();
</script>
{% endblock %}
'''
write('app/templates/topology/index.html', topo_html)

# copilot/index.html
copilot_html = '''{% extends "base.html" %}

{% block content %}
<div class="page-header">
    <div>
        <h1 class="page-title">Grounded AI Network Copilot</h1>
        <div class="page-subtitle">Natural language telemetry investigation grounded in real database records with zero hallucination</div>
    </div>
</div>

<div class="card" style="display:flex; flex-direction:column; height:680px; padding:0; overflow:hidden;">
    <!-- Chat Messages Feed -->
    <div id="chat-feed" style="flex:1; overflow-y:auto; padding:1.5rem; display:flex; flex-direction:column; gap:1.25rem;">
        <!-- Welcome Message -->
        <div style="display:flex; gap:1rem; max-width:80%;">
            <div class="logo-icon" style="width:36px; height:36px; flex-shrink:0;">🤖</div>
            <div style="background:var(--bg-surface); padding:1rem 1.25rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
                <div style="font-weight:700; color:var(--accent-cyan); margin-bottom:0.4rem;">NetWatch AI Copilot</div>
                <div style="font-size:0.88rem; color:var(--text-primary); line-height:1.6;">
                    Hello Administrator. I am connected to all live network flows, DNS logs, asset risk scores, and health telemetry. How can I assist your investigation today?
                </div>
                <!-- Suggested Questions Chips -->
                <div style="display:flex; gap:0.5rem; flex-wrap:wrap; margin-top:1rem;">
                    <button class="btn btn-secondary btn-sm chip-q" data-q="Why is the network slow today?">⚡ Why is the network slow?</button>
                    <button class="btn btn-secondary btn-sm chip-q" data-q="Which devices have the highest risk scores?">🛡 High-risk devices</button>
                    <button class="btn btn-secondary btn-sm chip-q" data-q="Show recent bandwidth anomalies.">⚠ Recent anomalies</button>
                    <button class="btn btn-secondary btn-sm chip-q" data-q="What is the status of active incidents?">🚨 Active incidents</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Query Input Bar -->
    <div style="padding:1rem 1.5rem; border-top:1px solid var(--border-color); background:var(--bg-secondary);">
        <form id="form-copilot-query" style="display:flex; gap:0.75rem;">
            <input type="text" id="input-copilot" class="form-input" placeholder="Ask anything about network performance, security risks, or anomalies..." required style="flex:1; padding:0.75rem 1rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff; font-size:0.9rem;">
            <button type="submit" id="btn-copilot-submit" class="btn btn-primary" style="padding:0.75rem 1.5rem;">Ask Copilot ➔</button>
        </form>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script type="module">
    import { HttpClient } from '/static/js/core/http.js';
    import { Toast } from '/static/js/components/toast.js';

    const feed = document.getElementById('chat-feed');

    function appendUserMessage(text) {
        const div = document.createElement('div');
        div.style.cssText = 'display:flex; justify-content:flex-end;';
        div.innerHTML = `
            <div style="background:linear-gradient(135deg, #0284c7, #0ea5e9); color:#fff; padding:0.85rem 1.25rem; border-radius:var(--radius-lg); max-width:70%; font-size:0.9rem; font-weight:500;">
                ${text}
            </div>
        `;
        feed.appendChild(div);
        feed.scrollTop = feed.scrollHeight;
    }

    function appendCopilotMessage(text, actions = []) {
        const div = document.createElement('div');
        div.style.cssText = 'display:flex; gap:1rem; max-width:85%;';
        
        let actionsHtml = '';
        if (actions && actions.length > 0) {
            actionsHtml = `
                <div style="display:flex; gap:0.5rem; flex-wrap:wrap; margin-top:0.75rem;">
                    ${actions.map(a => `<a href="${a.url}" class="btn btn-secondary btn-sm">${a.label} ➔</a>`).join('')}
                </div>
            `;
        }

        div.innerHTML = `
            <div class="logo-icon" style="width:36px; height:36px; flex-shrink:0;">🤖</div>
            <div style="background:var(--bg-surface); padding:1rem 1.25rem; border-radius:var(--radius-lg); border:1px solid var(--border-color); flex:1;">
                <div style="font-weight:700; color:var(--accent-cyan); margin-bottom:0.4rem;">NetWatch AI Copilot</div>
                <div style="font-size:0.88rem; color:var(--text-primary); line-height:1.6; white-space:pre-line;">
                    ${text}
                </div>
                ${actionsHtml}
            </div>
        `;
        feed.appendChild(div);
        feed.scrollTop = feed.scrollHeight;
    }

    async function sendQuery(q) {
        appendUserMessage(q);
        const btn = document.getElementById('btn-copilot-submit');
        btn.disabled = true;

        try {
            const res = await HttpClient.post('/api/v1/copilot/ask', { query: q });
            appendCopilotMessage(res.data.response, res.data.actions);
        } catch (err) {
            Toast.error('Copilot query failed.');
        } finally {
            btn.disabled = false;
            document.getElementById('input-copilot').value = '';
        }
    }

    document.getElementById('form-copilot-query').addEventListener('submit', (e) => {
        e.preventDefault();
        const q = document.getElementById('input-copilot').value.trim();
        if (q) sendQuery(q);
    });

    document.querySelectorAll('.chip-q').forEach(chip => {
        chip.addEventListener('click', (e) => {
            sendQuery(e.target.dataset.q);
        });
    });
</script>
{% endblock %}
'''
write('app/templates/copilot/index.html', copilot_html)

# forecasting/index.html
forecasting_html = '''{% extends "base.html" %}

{% block content %}
<div class="page-header">
    <div>
        <h1 class="page-title">Bandwidth Capacity Forecasting</h1>
        <div class="page-subtitle">Holt-Winters time-series projections, growth rate modeling, and saturation bottleneck prediction</div>
    </div>
</div>

<div class="card">
    <div class="data-table-container">
        <table class="data-table">
            <thead>
                <tr>
                    <th>Target Scope</th>
                    <th>Horizon</th>
                    <th>Current Usage</th>
                    <th>Projected Peak</th>
                    <th>Capacity Limit</th>
                    <th>Risk Level</th>
                    <th>Strategic Recommendation</th>
                </tr>
            </thead>
            <tbody id="tbody-forecasts">
                <tr><td colspan="7" style="text-align:center; padding:2rem;">Calculating forecast projections...</td></tr>
            </tbody>
        </table>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script type="module">
    import { HttpClient } from '/static/js/core/http.js';
    import { Toast } from '/static/js/components/toast.js';

    async function loadForecasts() {
        try {
            const res = await HttpClient.get('/api/v1/forecasting/projections');
            const items = res.data;
            const tbody = document.getElementById('tbody-forecasts');

            tbody.innerHTML = items.map(f => `
                <tr>
                    <td style="font-weight:600; color:var(--text-primary);">${f.target_scope}</td>
                    <td><span class="badge badge-low">${f.forecast_horizon_days} Days</span></td>
                    <td><code>${f.current_usage_mbps} Mbps</code></td>
                    <td style="font-weight:700; color:var(--accent-cyan); font-family:var(--font-mono);">${f.projected_usage_mbps} Mbps</td>
                    <td><code>${f.capacity_limit_mbps} Mbps</code></td>
                    <td><span class="badge badge-${f.saturation_risk_level === 'CRITICAL' ? 'critical' : (f.saturation_risk_level === 'HIGH' ? 'high' : 'optimal')}">${f.saturation_risk_level}</span></td>
                    <td style="font-size:0.8rem; color:var(--text-secondary); max-width:320px;">${f.recommendation}</td>
                </tr>
            `).join('');
        } catch (err) {
            Toast.error('Failed to load forecasts.');
        }
    }
    loadForecasts();
</script>
{% endblock %}
'''
write('app/templates/forecasting/index.html', forecasting_html)

# digital_twin/index.html
twin_html = '''{% extends "base.html" %}

{% block content %}
<div class="page-header">
    <div>
        <h1 class="page-title">Digital Twin Sandbox Simulator</h1>
        <div class="page-subtitle">Inject What-If failures (Node outage, link cuts, DDoS surges) to test failover resilience</div>
    </div>
</div>

<div style="display:grid; grid-template-columns: 1fr 2fr; gap:1.5rem;">
    <!-- Simulation Control Card -->
    <div class="card">
        <div class="card-header">
            <div class="card-title">Scenario Parameters</div>
        </div>
        <form id="form-run-sim">
            <div style="margin-bottom:1rem;">
                <label class="form-label" style="display:block; font-size:0.8rem; margin-bottom:0.3rem;">Failure Target Node</label>
                <select id="sim-node" class="form-input" style="width:100%; padding:0.55rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;">
                    <option value="NODE_ROUTER_CORE">Core Gateway Router (NODE_ROUTER_CORE)</option>
                    <option value="NODE_FIREWALL_CORE">Edge Firewall 01 (NODE_FIREWALL_CORE)</option>
                    <option value="NODE_SWITCH_CORP">Distribution Switch (Building A)</option>
                </select>
            </div>

            <div style="margin-bottom:1.5rem;">
                <label class="form-label" style="display:block; font-size:0.8rem; margin-bottom:0.3rem;">Failure Type</label>
                <select id="sim-type" class="form-input" style="width:100%; padding:0.55rem; background:var(--bg-input); border:1px solid var(--border-color); border-radius:var(--radius-md); color:#fff;">
                    <option value="NODE_FAILURE">Complete Node Outage</option>
                    <option value="LINK_CUT">Primary Fiber Cut</option>
                    <option value="DDOS_SURGE">10x DDoS Traffic Spike</option>
                </select>
            </div>

            <button type="submit" id="btn-submit-sim" class="btn btn-primary" style="width:100%; padding:0.65rem;">⚇ Run Sandbox Simulation</button>
        </form>
    </div>

    <!-- Simulation Results Card -->
    <div class="card">
        <div class="card-header">
            <div class="card-title">Resilience & Impact Analysis</div>
            <span id="badge-sim-status" class="badge badge-optimal">READY</span>
        </div>

        <div id="sim-results-body" style="display:flex; flex-direction:column; gap:1rem; padding:0.5rem 0;">
            <div style="text-align:center; padding:3rem; color:var(--text-muted);">
                Select failure parameters and run simulation to evaluate network failover tolerance.
            </div>
        </div>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script type="module">
    import { HttpClient } from '/static/js/core/http.js';
    import { Toast } from '/static/js/components/toast.js';

    document.getElementById('form-run-sim').addEventListener('submit', async (e) => {
        e.preventDefault();
        const btn = document.getElementById('btn-submit-sim');
        btn.disabled = true;
        btn.textContent = 'Simulating Dijkstra Rerouting...';

        const node = document.getElementById('sim-node').value;
        const type = document.getElementById('sim-type').value;

        try {
            const res = await HttpClient.post('/api/v1/digital-twin/simulate', {
                node_key: node,
                simulation_type: type,
                name: `Simulation: ${type} on ${node}`
            });
            const s = res.data;

            document.getElementById('badge-sim-status').textContent = 'SIMULATED';
            document.getElementById('sim-results-body').innerHTML = `
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem;">
                    <div style="background:var(--bg-surface); padding:1rem; border-radius:var(--radius-md);">
                        <div style="font-size:0.75rem; color:var(--text-muted);">Simulated Resilience Score</div>
                        <div style="font-size:2rem; font-weight:800; color:${s.simulated_resilience_score >= 80 ? 'var(--status-optimal)' : 'var(--status-critical)'}; font-family:var(--font-mono);">
                            ${s.simulated_resilience_score}/100
                        </div>
                    </div>
                    <div style="background:var(--bg-surface); padding:1rem; border-radius:var(--radius-md);">
                        <div style="font-size:0.75rem; color:var(--text-muted);">Impacted Endpoints</div>
                        <div style="font-size:2rem; font-weight:800; color:var(--accent-amber); font-family:var(--font-mono);">
                            ${s.impacted_devices_count} devices
                        </div>
                    </div>
                </div>

                <div style="background:var(--bg-surface); padding:1rem; border-radius:var(--radius-md);">
                    <div style="font-weight:700; color:var(--accent-cyan); margin-bottom:0.25rem;">Mitigation Advisory:</div>
                    <div style="font-size:0.85rem; color:var(--text-secondary);">${s.mitigation_recommendation}</div>
                </div>
            `;
            Toast.success('Simulation executed.');
        } catch (err) {
            Toast.error('Simulation failed.');
        } finally {
            btn.disabled = false;
            btn.textContent = '⚇ Run Sandbox Simulation';
        }
    });
</script>
{% endblock %}
'''
write('app/templates/digital_twin/index.html', twin_html)

print('Policies, Topology, Copilot, Forecasting, and Digital Twin templates created.')
