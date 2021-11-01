
def test_history_endpoint(client):
    res = client.get('/history')
    assert res.status_code == 200, 'history endpoint failed'
