// NetWatch AI - Modal Dialogue Controller
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
