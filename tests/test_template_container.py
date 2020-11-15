from template_container import __version__, get_app
import pytest
import json

@pytest.fixture(scope='module')
def client():
    with get_app().app.test_client() as c:
        yield c

def test_version():
    assert __version__ == '0.1.0'

def test_hello_world_get(client):
    response = client.get('/template_container/hello_world')
    assert response.status_code == 200

def test_hello_world_put(client):
    response = client.put('/template_container/hello_world', json={"hello_message": "some_message"})
    assert response.status_code == 200
    assert response.json == {
        'hello-world-response': 'you sent: some_message'
    }