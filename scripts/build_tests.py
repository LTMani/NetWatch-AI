import sys
sys.path.insert(0, '.')
from scripts.writer import write

# conftest.py
conftest_code = '''import pytest
from app import create_app
from app.models.base import db
from app.models.user import User, Role
from app.models.organization import Organization, Department, NetworkSite, Subnet
from app.utils.crypto import hash_password, generate_jwt_token

@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        # Seed basic test fixture
        org = Organization(name='Test Org', domain='test.local')
        db.session.add(org)
        db.session.flush()

        role = Role(name='super_admin', display_name='Super Admin', is_system_role=True)
        db.session.add(role)
        db.session.flush()

        user = User(
            organization_id=org.id,
            username='testadmin',
            email='admin@test.local',
            password_hash=hash_password('Password123!'),
            full_name='Test Admin'
        )
        user.roles.append(role)
        db.session.add(user)
        db.session.commit()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_headers(app):
    with app.app_context():
        user = User.query.filter_by(username='testadmin').first()
        token = generate_jwt_token(user.id, user.email, 'super_admin')
        return {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
'''
write('tests/conftest.py', conftest_code)

# unit/test_crypto.py
test_crypto = '''import pytest
from app.utils.crypto import hash_password, verify_password, calculate_sha256, generate_api_key

def test_password_hashing():
    pwd = 'SecurePassword2026!'
    hashed = hash_password(pwd)
    assert hashed != pwd
    assert verify_password(pwd, hashed) is True
    assert verify_password('WrongPassword!', hashed) is False

def test_password_too_short():
    with pytest.raises(ValueError):
        hash_password('short')

def test_sha256_calculation():
    h = calculate_sha256('netwatch-ai')
    assert len(h) == 64

def test_api_key_generation():
    key = generate_api_key('nw_live_')
    assert key.startswith('nw_live_')
    assert len(key) > 30
'''
write('tests/unit/test_crypto.py', test_crypto)

# unit/test_ip_utils.py
test_ip = '''import pytest
from app.utils.ip_utils import is_valid_ipv4, is_valid_mac, normalize_mac, is_private_ip, get_subnet_broadcast

def test_ip_validation():
    assert is_valid_ipv4('192.168.1.1') is True
    assert is_valid_ipv4('10.0.0.254') is True
    assert is_valid_ipv4('999.999.999.999') is False
    assert is_valid_ipv4('not-an-ip') is False

def test_mac_normalization():
    assert normalize_mac('00-50-56-AB-CD-EF') == '00:50:56:ab:cd:ef'
    assert is_valid_mac('00:50:56:ab:cd:ef') is True

def test_private_ip_detection():
    assert is_private_ip('192.168.1.5') is True
    assert is_private_ip('10.0.10.1') is True
    assert is_private_ip('172.16.0.1') is True
    assert is_private_ip('8.8.8.8') is False
'''
write('tests/unit/test_ip_utils.py', test_ip)

# unit/test_network_math.py
test_math = '''import pytest
from app.utils.network_math import calculate_mean, calculate_stddev, calculate_z_score, calculate_ewma, format_bytes, format_bits_per_second

def test_mean_and_stddev():
    vals = [10.0, 20.0, 30.0, 40.0, 50.0]
    assert calculate_mean(vals) == 30.0
    assert round(calculate_stddev(vals), 2) == 14.14

def test_z_score():
    z = calculate_z_score(50.0, 30.0, 10.0)
    assert z == 2.0

def test_byte_formatting():
    assert format_bytes(1024) == '1.00 KB'
    assert format_bytes(1048576) == '1.00 MB'
    assert format_bytes(1073741824) == '1.00 GB'
'''
write('tests/unit/test_network_math.py', test_math)

# unit/test_domain_engine.py
test_dom = '''import pytest
from app.services.domain_engine import DomainClassificationEngine

def test_domain_classification():
    engine = DomainClassificationEngine()
    cat, score, mal, reason = engine.classify_domain('github.com')
    assert cat == 'Development'
    assert score >= 90
    assert mal is False

def test_subdomain_inheritance():
    engine = DomainClassificationEngine()
    cat, score, mal, reason = engine.classify_domain('api.github.com')
    assert cat == 'Development'

def test_malicious_keyword_heuristic():
    engine = DomainClassificationEngine()
    cat, score, mal, reason = engine.classify_domain('c2-beacon-exploit.xyz')
    assert mal is True
'''
write('tests/unit/test_domain_engine.py', test_dom)

# integration/test_auth_api.py
test_auth = '''import pytest

def test_login_success(client):
    res = client.post('/api/v1/auth/login', json={
        'identifier': 'admin@test.local',
        'password': 'Password123!'
    })
    assert res.status_code == 200
    data = res.get_json()
    assert data['status'] == 'success'
    assert 'access_token' in data['data']

def test_login_bad_password(client):
    res = client.post('/api/v1/auth/login', json={
        'identifier': 'admin@test.local',
        'password': 'WrongPassword!'
    })
    assert res.status_code == 401
'''
write('tests/integration/test_auth_api.py', test_auth)

# integration/test_devices_api.py
test_devices = '''import pytest

def test_create_and_list_device(client, auth_headers):
    # 1. Create Device
    create_res = client.post('/api/v1/devices', headers=auth_headers, json={
        'name': 'TEST-LAPTOP-99',
        'ip_address': '10.0.10.99',
        'mac_address': '00:50:56:99:88:77',
        'device_type': 'laptop',
        'operating_system': 'Linux'
    })
    assert create_res.status_code == 201
    dev_id = create_res.get_json()['data']['id']

    # 2. List Devices
    list_res = client.get('/api/v1/devices', headers=auth_headers)
    assert list_res.status_code == 200
    items = list_res.get_json()['data']['items']
    assert any(d['id'] == dev_id for d in items)

    # 3. Quarantine Toggle
    q_res = client.post(f'/api/v1/devices/{dev_id}/quarantine', headers=auth_headers, json={'quarantine': True})
    assert q_res.status_code == 200
    assert q_res.get_json()['data']['is_quarantined'] is True
'''
write('tests/integration/test_devices_api.py', test_devices)

# integration/test_copilot_api.py
test_copilot = '''import pytest

def test_copilot_query_grounding(client, auth_headers):
    res = client.post('/api/v1/copilot/ask', headers=auth_headers, json={
        'query': 'Why is the network slow today?'
    })
    assert res.status_code == 200
    data = res.get_json()['data']
    assert data['intent'] == 'NETWORK_HEALTH_DIAGNOSIS'
    assert 'health_score' in data['metrics']
    assert len(data['actions']) > 0
'''
write('tests/integration/test_copilot_api.py', test_copilot)

# e2e/test_full_workflow.py
test_e2e = '''import pytest

def test_complete_platform_lifecycle(client, auth_headers):
    # 1. Dashboard summary
    dash_res = client.get('/api/v1/dashboard/summary', headers=auth_headers)
    assert dash_res.status_code == 200

    # 2. Run Slow Network Diagnostic Wizard
    diag_res = client.post('/api/v1/diagnostics/run', headers=auth_headers, json={'scope': 'Core Gateway'})
    assert diag_res.status_code == 201
    assert len(diag_res.get_json()['data']['steps']) == 7

    # 3. Open Incident
    inc_res = client.post('/api/v1/incidents', headers=auth_headers, json={
        'title': 'Automated Test Incident',
        'severity': 'sev2_high',
        'category': 'Performance',
        'summary': 'Generated during E2E verification.'
    })
    assert inc_res.status_code == 201
    inc_id = inc_res.get_json()['data']['id']

    # 4. Update Incident Status
    status_res = client.patch(f'/api/v1/incidents/{inc_id}/status', headers=auth_headers, json={'status': 'resolved'})
    assert status_res.status_code == 200

    # 5. Verify Audit Ledger Integrity
    audit_res = client.get('/api/v1/audit-logs/verify', headers=auth_headers)
    assert audit_res.status_code == 200
    assert audit_res.get_json()['data']['is_tamper_free'] is True
'''
write('tests/e2e/test_full_workflow.py', test_e2e)

print('Automated test suite (Unit, Integration, E2E) generated.')
