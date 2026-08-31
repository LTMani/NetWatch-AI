import pytest

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
