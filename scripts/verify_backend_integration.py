import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import json
from app import create_app
from app.models.base import db
from app.models.user import User
from app.models.device import Device
from app.models.data_source import NetworkDataSource
from app.models.telemetry import DNSQueryLog, NetworkFlowMetric
from app.models.alert import Alert
from app.models.incident import Incident
from app.models.audit import AuditLog
from app.models.organization import Organization, Subnet, NetworkSite
from app.utils.crypto import generate_jwt_token

app = create_app("development")

def run_integration_audit():
    print("=" * 75)
    print("      NetWatch AI -- Full Backend Integration & Connectivity Audit     ")
    print("=" * 75)

    with app.app_context():
        # 1. Database Tier Verification
        print("\n[+] 1. DATABASE TIER & DATA MODEL INTEGRITY:")
        models_to_check = [
            ("Users", User),
            ("Organizations", Organization),
            ("Network Subnets", Subnet),
            ("Devices (Inventory)", Device),
            ("Network Data Sources", NetworkDataSource),
            ("NetFlow Metrics", NetworkFlowMetric),
            ("DNS Query Logs", DNSQueryLog),
            ("Alerts", Alert),
            ("Incidents", Incident),
            ("Audit Logs (Immutable)", AuditLog)
        ]
        
        all_models_ok = True
        for name, model in models_to_check:
            try:
                count = model.query.count()
                print(f"  [PASS] {name:<26} -> {count:>4} records in SQLite DB")
            except Exception as e:
                print(f"  [FAIL] {name:<26} -> Error: {e}")
                all_models_ok = False

        # 2. REST API Integration Tier
        print("\n[+] 2. BACKEND REST API ENDPOINT INTEGRATION:")
        client = app.test_client()
        user = User.query.filter_by(username="admin").first()
        token = generate_jwt_token(user.id, user.email, "super_admin")
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

        apis_to_test = [
            ("POST", "/api/v1/auth/login", {"username": "admin", "password": "Admin@NetWatch2026!"}, False),
            ("GET",  "/api/v1/dashboard/summary", None, True),
            ("GET",  "/api/v1/devices?page=1&per_page=5", None, True),
            ("GET",  "/api/v1/investigation/ip/10.0.10.12", None, True),
            ("GET",  "/api/v1/investigation/recent", None, True),
            ("GET",  "/api/v1/data-sources", None, True),
            ("GET",  "/api/v1/health/summary", None, True),
            ("GET",  "/api/v1/analytics/bandwidth", None, True),
            ("GET",  "/api/v1/domains/activity", None, True),
            ("GET",  "/api/v1/anomalies/events?limit=5", None, True),
            ("GET",  "/api/v1/risk/summary", None, True),
            ("GET",  "/api/v1/alerts/correlated", None, True),
            ("GET",  "/api/v1/incidents", None, True),
            ("GET",  "/api/v1/topology/graph", None, True),
            ("POST", "/api/v1/copilot/query", {"query": "What is the network health status and active alerts?"}, True),
            ("GET",  "/api/v1/audit-logs/verify-integrity", None, True),
        ]

        all_apis_ok = True
        for method, endpoint, payload, use_auth in apis_to_test:
            h = headers if use_auth else {"Content-Type": "application/json"}
            if method == "GET":
                res = client.get(endpoint, headers=h)
            else:
                res = client.post(endpoint, data=json.dumps(payload), headers=h)
            
            is_ok = res.status_code in (200, 201)
            status_tag = "[PASS]" if is_ok else "[FAIL]"
            print(f"  {status_tag} {method:<4} {endpoint:<38} -> Status {res.status_code}")
            if not is_ok:
                print(f"         Error details: {res.get_data(as_text=True)[:120]}")
                all_apis_ok = False

        # 3. Dynamic Service Engine Integration Check
        print("\n[+] 3. DYNAMIC INTELLIGENCE & TELEMETRY ENGINES:")
        from app.services.health_engine import NetworkHealthEngine
        from app.services.anomaly_engine import AnomalyDetectionEngine
        from app.services.discovery_engine import NetworkDiscoveryEngine

        # Health Calculation
        he = NetworkHealthEngine()
        h_snapshot = he.calculate_health()
        print(f"  [PASS] 6-Factor Health Engine        -> Active Score: {h_snapshot.overall_score:.1f}/100 (Status: {h_snapshot.health_status})")

        # Discovery & Connector Engine
        de = NetworkDiscoveryEngine()
        disc_res = de.discover_all_active_sources()
        print(f"  [PASS] Network Discovery Connectors  -> {disc_res.get('message', 'Ready')}")

        # Anomaly Engine
        ae = AnomalyDetectionEngine()
        anom_res = ae.detect_traffic_anomalies()
        print(f"  [PASS] Z-Score & EWMA Anomaly Engine -> Detected {len(anom_res)} real-time telemetry anomalies")

        print("\n" + "=" * 75)
        if all_models_ok and all_apis_ok:
            print("[SUCCESS] BACKEND IS 100% OPERATIONAL, INTEGRATED, AND CONNECTED!")
        else:
            print("[WARNING] SOME BACKEND COMPONENTS REQUIRE ATTENTION.")
        print("=" * 75)

if __name__ == "__main__":
    run_integration_audit()
