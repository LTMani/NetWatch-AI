// NetWatch AI - HTTP Client Wrapper
export class HttpClient {
    static async request(url, options = {}) {
        const headers = {
            'Content-Type': 'application/json',
            ...(options.headers || {})
        };
        
        const token = localStorage.getItem('nw_token');
        if (token) {
            headers['Authorization'] = `Bearer ${token}`;
        }

        try {
            const response = await fetch(url, {
                ...options,
                headers
            });

            if (response.status === 401 && !url.includes('/api/v1/auth/login')) {
                localStorage.removeItem('nw_token');
                window.location.href = '/login';
                return null;
            }

            const data = await response.json().catch(() => ({}));
            if (!response.ok) {
                const errorMsg = data.message || `Request failed with status ${response.status}`;
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
        const fullUrl = queryString ? `${url}?${queryString}` : url;
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
