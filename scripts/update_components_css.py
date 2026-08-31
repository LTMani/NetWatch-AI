with open("app/static/css/components/components.css", "a", encoding="utf-8") as f:
    f.write("""
/* ==========================================================================
   GLOBAL BUTTON SYSTEM
   ========================================================================== */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.4rem;
    padding: 0.45rem 0.9rem;
    font-size: 0.8rem;
    font-weight: 600;
    border-radius: var(--radius-md);
    cursor: pointer;
    transition: all var(--transition-fast);
    border: 1px solid transparent;
    text-decoration: none;
    line-height: 1.2;
    background: #1e293b;
    color: #f8fafc;
}

.btn:hover {
    filter: brightness(1.1);
    transform: translateY(-1px);
}

.btn:active {
    transform: translateY(0);
}

.btn-primary {
    background: linear-gradient(135deg, #2563eb, #0284c7) !important;
    color: #ffffff !important;
    border: 1px solid #38bdf8 !important;
    box-shadow: 0 0 12px rgba(37, 99, 235, 0.35);
}

.btn-primary:hover {
    background: linear-gradient(135deg, #1d4ed8, #0369a1) !important;
    box-shadow: 0 0 16px rgba(56, 189, 248, 0.5);
}

.btn-secondary {
    background: #151f30 !important;
    color: #f1f5f9 !important;
    border: 1px solid #27354a !important;
}

.btn-secondary:hover {
    background: #1e2d42 !important;
    border-color: #3b82f6 !important;
}

.btn-danger {
    background: rgba(220, 38, 38, 0.2) !important;
    color: #ef4444 !important;
    border: 1px solid rgba(239, 68, 68, 0.4) !important;
}

.btn-danger:hover {
    background: #dc2626 !important;
    color: #ffffff !important;
}

.btn-sm {
    padding: 0.3rem 0.65rem;
    font-size: 0.72rem;
}

.btn-lg {
    padding: 0.65rem 1.35rem;
    font-size: 0.95rem;
}

/* ==========================================================================
   MODAL DIALOGUE SYSTEM
   ========================================================================== */
.modal-overlay {
    display: none !important;
    position: fixed;
    inset: 0;
    background: rgba(4, 7, 13, 0.82);
    backdrop-filter: blur(5px);
    -webkit-backdrop-filter: blur(5px);
    z-index: 99999;
    justify-content: center;
    align-items: center;
    padding: 1.5rem;
}

.modal-overlay.active {
    display: flex !important;
}

.modal-box {
    background: #0d1524;
    border: 1px solid #1e2d42;
    border-radius: var(--radius-lg);
    width: 100%;
    max-width: 540px;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.75), 0 0 20px rgba(56, 189, 248, 0.1);
    overflow: hidden;
    animation: modalFadeIn 0.15s ease-out;
}

@keyframes modalFadeIn {
    from { opacity: 0; transform: scale(0.96) translateY(8px); }
    to { opacity: 1; transform: scale(1) translateY(0); }
}

.modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 1.25rem;
    border-bottom: 1px solid var(--border-subtle);
    background: #090f1a;
}

.modal-body {
    padding: 1.25rem;
}

.modal-footer {
    display: flex;
    justify-content: flex-end;
    gap: 0.75rem;
    padding: 0.85rem 1.25rem;
    border-top: 1px solid var(--border-subtle);
    background: #090f1a;
}

/* ==========================================================================
   PAGE HEADERS, CARDS & DATA TABLES
   ========================================================================== */
.page-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.25rem;
    flex-wrap: wrap;
    gap: 1rem;
}

.page-title {
    font-size: 1.35rem;
    font-weight: 700;
    color: #ffffff;
}

.page-subtitle {
    font-size: 0.8rem;
    color: var(--text-muted);
    margin-top: 0.2rem;
}

.card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: 1.25rem;
    box-shadow: var(--shadow-card);
}

.data-table-container {
    overflow-x: auto;
    width: 100%;
}

.data-table {
    width: 100%;
    border-collapse: collapse;
    text-align: left;
    font-size: 0.8rem;
}

.data-table th {
    padding: 0.75rem 1rem;
    border-bottom: 1px solid var(--border-color);
    color: var(--text-muted);
    font-weight: 600;
    text-transform: uppercase;
    font-size: 0.68rem;
    letter-spacing: 0.05em;
    background: #090e17;
}

.data-table td {
    padding: 0.85rem 1rem;
    border-bottom: 1px solid var(--border-subtle);
    color: var(--text-primary);
    vertical-align: middle;
}

.data-table tr:hover td {
    background: rgba(255, 255, 255, 0.02);
}

/* Badge States */
.badge {
    display: inline-flex;
    align-items: center;
    padding: 0.15rem 0.5rem;
    font-size: 0.68rem;
    font-weight: 600;
    border-radius: var(--radius-full);
    text-transform: capitalize;
}

.badge-online { background: rgba(16, 185, 129, 0.15); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.3); }
.badge-offline { background: rgba(100, 116, 139, 0.15); color: #94a3b8; border: 1px solid rgba(100, 116, 139, 0.3); }
.badge-degraded { background: rgba(245, 158, 11, 0.15); color: #f59e0b; border: 1px solid rgba(245, 158, 11, 0.3); }
.badge-unauthorized { background: rgba(239, 68, 68, 0.15); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.3); }
""")
print("[+] Appended component styles to components.css")
