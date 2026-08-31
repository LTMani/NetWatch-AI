import pytest

def test_copilot_query_grounding(client, auth_headers):
    res = client.post('/api/v1/copilot/ask', headers=auth_headers, json={
        'query': 'Why is the network slow today?'
    })
    assert res.status_code == 200
    data = res.get_json()['data']
    assert data['intent'] == 'NETWORK_HEALTH_DIAGNOSIS'
    assert 'health_score' in data['metrics']
    assert len(data['actions']) > 0
