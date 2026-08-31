import pytest

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
