import sys
sys.path.insert(0, '.')
from app import create_app
from app.models.base import db

app = create_app('testing')

endpoints = [
    '/',
    '/landing',
    '/login',
    '/register',
    '/dashboard',
    '/network/overview',
    '/devices',
    '/domains/activity',
    '/analytics/office-hours',
    '/analytics/bandwidth',
    '/health',
    '/diagnostics/slow-network',
    '/anomalies',
    '/risk',
    '/alerts',
    '/incidents',
    '/policies',
    '/topology',
    '/copilot',
    '/forecasting',
    '/digital-twin',
    '/reports',
    '/audit-logs',
    '/users',
    '/settings'
]

with app.app_context():
    db.create_all()
    client = app.test_client()
    passed = 0
    for ep in endpoints:
        res = client.get(ep, follow_redirects=True)
        if res.status_code in (200, 302):
            passed += 1
        else:
            print(f'FAIL on {ep}: Status {res.status_code}')
            sys.exit(1)

    print(f'All {passed}/{len(endpoints)} view endpoints tested and verified cleanly (Status 200/302)!')
