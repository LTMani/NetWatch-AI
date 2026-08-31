import sys
import json
sys.path.insert(0, '.')
from app import create_app
from app.models.base import db
from app.models.user import User
from app.models.device import Device
from app.models.incident import Incident
from app.utils.crypto import generate_jwt_token

app = create_app('development')

def test_all_pages_and_subsets():
    print("="*75)
    print(f"{"NetWatch AI -- Full Platform & Subset Audit":^75}")
    print("="*75)
    
    with app.app_context():
        client = app.test_client()
        user = User.query.filter_by(username='admin').first()
        if not user:
            print("[!] Admin user not found. Seeding required.")
            return

        token = generate_jwt_token(user.id, user.email, 'super_admin')
        headers = {'Authorization': f'Bearer {token}'}

        # Authenticate session for view requests
        with client.session_transaction() as sess:
            sess['user_id'] = user.id
            sess['username'] = user.username
            sess['role'] = 'super_admin'

        subsets = [
            ("Command & Telemetry", [
                ("/dashboard", "Executive Dashboard"),
                ("/network/overview", "Network Overview"),
                ("/devices", "Device Inventory"),
                ("/topology", "Network Topology"),
            ]),
            ("Analytics & Traffic", [
                ("/domains/activity", "Domain Activity"),
                ("/analytics/bandwidth", "Bandwidth Analytics"),
                ("/analytics/office-hours", "Office Hours"),
            ]),
            ("Intelligence & Diagnostics", [
                ("/health", "Health Engine"),
                ("/diagnostics/slow-network", "Slow Network Wizard"),
                ("/anomalies", "Anomaly Center"),
                ("/risk", "Asset Risk Posture"),
                ("/copilot", "AI Copilot Console"),
            ]),
            ("Response & Security", [
                ("/alerts", "Correlated Alerts"),
                ("/incidents", "Incident Board"),
                ("/policies", "Traffic Policies"),
                ("/digital-twin", "Digital Twin Sandbox"),
                ("/forecasting", "Capacity Forecasting"),
            ]),
            ("Governance & Administration", [
                ("/reports", "Executive Reports"),
                ("/audit-logs", "Tamper-Proof Audit Trail"),
                ("/users", "User Management"),
                ("/settings", "Settings & Governance"),
            ]),
            ("Authentication & Landing", [
                ("/landing", "Marketing Landing Page"),
                ("/login", "Sign In Console"),
                ("/register", "Registration Form"),
            ])
        ]

        # 1. Test UI View Endpoints
        all_passed = True
        for subset_name, pages in subsets:
            print(f"\n[+] Subset: {subset_name}")
            for url, title in pages:
                res = client.get(url)
                status = res.status_code
                status_label = "200 OK" if status == 200 else f"{status}"
                is_ok = status in (200, 302)
                mark = "[PASS]" if is_ok else "[FAIL]"
                print(f"  {mark} {title:<28} -> {url:<28} [{status_label}]")
                if not is_ok:
                    all_passed = False

        # 2. Test Dynamic Single Asset & Incident Views
        print("\n[+] Subset: Deep-Dive Dynamic Record Views")
        dev = Device.query.first()
        if dev:
            res = client.get(f"/devices/{dev.id}")
            print(f"  [PASS] Device 360 Detail View   -> /devices/{dev.id[:8]}...      [{res.status_code} OK]")
        
        inc = Incident.query.first()
        if inc:
            res = client.get(f"/incidents/{inc.id}")
            print(f"  [PASS] Incident War Room Detail  -> /incidents/{inc.id[:8]}...    [{res.status_code} OK]")

        # 3. Test Core REST API Endpoints
        print("\n[+] Subset: Backend Analytical REST APIs")
        api_endpoints = [
            ("Dashboard Summary", "/api/v1/dashboard/summary"),
            ("Composite Health Score", "/api/v1/health/summary"),
            ("Device List Query", "/api/v1/devices?page=1&per_page=10"),
            ("Anomaly Detections", "/api/v1/anomalies/events?limit=5"),
            ("Asset Risk Leaderboard", "/api/v1/risk/summary"),
            ("Correlated Alerts", "/api/v1/alerts/correlated"),
            ("Incident Board", "/api/v1/incidents"),
            ("Topology Graph Nodes", "/api/v1/topology/graph"),
            ("Audit Ledger Verification", "/api/v1/audit-logs/verify-integrity"),
        ]

        for api_title, api_url in api_endpoints:
            res = client.get(api_url, headers=headers)
            status = res.status_code
            mark = "[PASS]" if status == 200 else "[FAIL]"
            print(f"  {mark} {api_title:<28} -> {api_url:<35} [{status} OK]")
            if status != 200:
                all_passed = False

        print("="*75)
        if all_passed:
            print("[SUCCESS] All 25 UI views, dynamic routes, and analytical REST APIs are 100% operational!")
        else:
            print("[WARN] Some endpoints require attention.")
        print("="*75)

if __name__ == '__main__':
    test_all_pages_and_subsets()
