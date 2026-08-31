// NetWatch AI - Master Application Orchestrator
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
