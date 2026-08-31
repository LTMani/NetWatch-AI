import pytest

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
