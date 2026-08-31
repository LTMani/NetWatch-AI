import sys
sys.path.insert(0, '.')
from scripts.writer import write

# 1. core/http.js
http_js = '''// NetWatch AI - HTTP Client Wrapper
export class HttpClient {
    static async request(url, options = {}) {
        const headers = {
            'Content-Type': 'application/json',
            ...(options.headers || {})
        };
        
        const token = localStorage.getItem('nw_token');
        if (token) {
            headers['Authorization'] = Bearer ;
        }

        try {
            const response = await fetch(url, {
                ...options,
                headers
            });

            if (response.status === 401 && !url.includes('/api/v1/auth/login')) {
                // Clear session and redirect to login if session expired
                window.location.href = '/login';
                return null;
            }

            const data = await response.json().catch(() => ({}));
            if (!response.ok) {
                const errorMsg = data.message || Request failed with status ;
                throw new Error(errorMsg);
            }
            return data;
        } catch (err) {
            console.error('[HttpClient Error]', err);
            throw err;
        }
    }

    static get(url, params = {}) {
        const queryString = new URLSearchParams(params).toString();
        const fullUrl = queryString ? ${url}? : url;
        return this.request(fullUrl, { method: 'GET' });
    }

    static post(url, body = {}) {
        return this.request(url, {
            method: 'POST',
            body: JSON.stringify(body)
        });
    }

    static patch(url, body = {}) {
        return this.request(url, {
            method: 'PATCH',
            body: JSON.stringify(body)
        });
    }

    static delete(url) {
        return this.request(url, { method: 'DELETE' });
    }
}
'''
write('app/static/js/core/http.js', http_js)

# 2. components/toast.js
toast_js = '''// NetWatch AI - Notification Toast Manager
export class Toast {
    static getContainer() {
        let container = document.getElementById('toast-container');
        if (!container) {
            container = document.createElement('div');
            container.id = 'toast-container';
            container.className = 'toast-container';
            document.body.appendChild(container);
        }
        return container;
    }

    static show(message, type = 'info', durationMs = 4000) {
        const container = this.getContainer();
        const toast = document.createElement('div');
        toast.className = 	oast toast-;
        
        const icons = {
            success: '✓',
            error: '✕',
            warning: '⚠',
            info: 'ℹ'
        };

        toast.innerHTML = 
            <span style="font-weight:bold; font-size:1.1rem;"></span>
            <span style="flex:1;"></span>
        ;
        container.appendChild(toast);

        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transform = 'translateX(100%)';
            toast.style.transition = 'all 0.3s ease';
            setTimeout(() => toast.remove(), 300);
        }, durationMs);
    }

    static success(msg) { this.show(msg, 'success'); }
    static error(msg) { this.show(msg, 'error', 5000); }
    static warning(msg) { this.show(msg, 'warning'); }
    static info(msg) { this.show(msg, 'info'); }
}
'''
write('app/static/js/components/toast.js', toast_js)

# 3. components/modal.js
modal_js = '''// NetWatch AI - Modal Dialogue Controller
export class Modal {
    static open(modalId) {
        const el = document.getElementById(modalId);
        if (el) {
            el.classList.add('active');
            document.body.style.overflow = 'hidden';
        }
    }

    static close(modalId) {
        const el = document.getElementById(modalId);
        if (el) {
            el.classList.remove('active');
            document.body.style.overflow = '';
        }
    }

    static init() {
        document.addEventListener('click', (e) => {
            if (e.target.dataset.modalClose) {
                this.close(e.target.dataset.modalClose);
            }
            if (e.target.classList.contains('modal-overlay')) {
                e.target.classList.remove('active');
                document.body.style.overflow = '';
            }
        });
    }
}
'''
write('app/static/js/components/modal.js', modal_js)

# 4. components/charts.js (Pure Canvas High-Performance Chart Renderer)
charts_js = '''// NetWatch AI - Pure HTML5 Canvas Cyber Chart Renderer
export class ChartRenderer {
    static renderLineChart(canvasId, labels, dataPoints, color = '#00f0ff', fillGradient = true) {
        const canvas = document.getElementById(canvasId);
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        const w = canvas.width = canvas.parentElement.clientWidth;
        const h = canvas.height = canvas.parentElement.clientHeight || 200;

        ctx.clearRect(0, 0, w, h);
        if (!dataPoints || dataPoints.length === 0) return;

        const maxVal = Math.max(...dataPoints, 10) * 1.15;
        const minVal = Math.min(...dataPoints, 0);
        const padding = { top: 20, right: 20, bottom: 30, left: 40 };
        const plotW = w - padding.left - padding.right;
        const plotH = h - padding.top - padding.bottom;

        // Draw grid lines
        ctx.strokeStyle = '#1e293b';
        ctx.lineWidth = 1;
        ctx.beginPath();
        for (let i = 0; i <= 4; i++) {
            const y = padding.top + (plotH / 4) * i;
            ctx.moveTo(padding.left, y);
            ctx.lineTo(w - padding.right, y);
            ctx.fillStyle = '#64748b';
            ctx.font = '10px sans-serif';
            const val = (maxVal - (maxVal / 4) * i).toFixed(0);
            ctx.fillText(val, 5, y + 3);
        }
        ctx.stroke();

        // Calculate coordinates
        const pts = dataPoints.map((val, idx) => {
            const x = padding.left + (plotW / (dataPoints.length - 1)) * idx;
            const y = padding.top + plotH - ((val - minVal) / (maxVal - minVal)) * plotH;
            return { x, y, val };
        });

        // Draw area gradient
        if (fillGradient) {
            const grad = ctx.createLinearGradient(0, padding.top, 0, h - padding.bottom);
            grad.addColorStop(0, ${color}44);
            grad.addColorStop(1, ${color}00);

            ctx.beginPath();
            ctx.moveTo(pts[0].x, pts[0].y);
            for (let i = 1; i < pts.length; i++) {
                ctx.lineTo(pts[i].x, pts[i].y);
            }
            ctx.lineTo(pts[pts.length - 1].x, h - padding.bottom);
            ctx.lineTo(pts[0].x, h - padding.bottom);
            ctx.closePath();
            ctx.fillStyle = grad;
            ctx.fill();
        }

        // Draw line
        ctx.beginPath();
        ctx.strokeStyle = color;
        ctx.lineWidth = 2.5;
        ctx.moveTo(pts[0].x, pts[0].y);
        for (let i = 1; i < pts.length; i++) {
            ctx.lineTo(pts[i].x, pts[i].y);
        }
        ctx.stroke();

        // Draw points
        pts.forEach(p => {
            ctx.beginPath();
            ctx.arc(p.x, p.y, 4, 0, Math.PI * 2);
            ctx.fillStyle = '#0a0e17';
            ctx.fill();
            ctx.strokeStyle = color;
            ctx.lineWidth = 2;
            ctx.stroke();
        });
    }

    static renderDonutChart(canvasId, dataObject, colorPalette = ['#38bdf8', '#6366f1', '#10b981', '#f59e0b', '#f43f5e', '#a855f7']) {
        const canvas = document.getElementById(canvasId);
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        const w = canvas.width = canvas.parentElement.clientWidth;
        const h = canvas.height = canvas.parentElement.clientHeight || 200;

        ctx.clearRect(0, 0, w, h);
        const entries = Object.entries(dataObject);
        const total = entries.reduce((acc, [_, v]) => acc + v, 0);
        if (total === 0) return;

        const cx = w / 2;
        const cy = h / 2;
        const radius = Math.min(cx, cy) - 20;
        const innerRadius = radius * 0.65;

        let startAngle = -Math.PI / 2;
        entries.forEach(([label, val], idx) => {
            const sliceAngle = (val / total) * Math.PI * 2;
            const color = colorPalette[idx % colorPalette.length];

            ctx.beginPath();
            ctx.arc(cx, cy, radius, startAngle, startAngle + sliceAngle);
            ctx.arc(cx, cy, innerRadius, startAngle + sliceAngle, startAngle, true);
            ctx.closePath();
            ctx.fillStyle = color;
            ctx.fill();

            startAngle += sliceAngle;
        });

        // Center total text
        ctx.fillStyle = '#f8fafc';
        ctx.font = 'bold 16px sans-serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(total.toLocaleString(), cx, cy - 6);
        ctx.fillStyle = '#64748b';
        ctx.font = '10px sans-serif';
        ctx.fillText('QUERIES', cx, cy + 12);
    }
}
'''
write('app/static/js/components/charts.js', charts_js)

# 5. Core app.js bootstrap
app_js = '''// NetWatch AI - Master Application Orchestrator
import { Modal } from './components/modal.js';
import { Toast } from './components/toast.js';
import { HttpClient } from './core/http.js';

document.addEventListener('DOMContentLoaded', () => {
    Modal.init();
    
    // Command Palette Trigger (Ctrl+K or Cmd+K)
    document.addEventListener('keydown', (e) => {
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            Toast.info('Quick Command Palette: Type to search assets, diagnostics, or policies.');
        }
    });

    // Global Logout Handler
    const logoutBtn = document.getElementById('btn-logout');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', async (e) => {
            e.preventDefault();
            try {
                await HttpClient.post('/api/v1/auth/logout');
                localStorage.removeItem('nw_token');
                window.location.href = '/login';
            } catch (err) {
                window.location.href = '/login';
            }
        });
    }
});
'''
write('app/static/js/app.js', app_js)

print('Frontend JavaScript core engine generated.')
