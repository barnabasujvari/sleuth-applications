from template_container import __version__
from template_container.template_container import get_app
import pytest
import json
import base64
import os

test_auth = {"Authorization": "Bearer xxxxxxxxxxxxxx"}
os.environ["DISABLE_OAUTH"] = "True"


@pytest.fixture(scope="module")
def client():
    with get_app().app.test_client() as c:
        yield c


def test_hello_world_get(client):
    print(os.getenv("DISABLE_OAUTH"))
    response = client.get("/template_container/hello_world", headers=test_auth)
    assert response.status_code == 200


def test_hello_world_put(client):
    response = client.put(
        "/template_container/hello_world?hello_message=some_message",
        headers=test_auth,
    )
    assert response.status_code == 200
    assert response.json == {"hello-world-response": "you sent: some_message"}
