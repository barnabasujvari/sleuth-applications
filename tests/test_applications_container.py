from applications_container import __version__
from applications_container.applications_container import get_app
from tests.test_comments import *
import pytest
import json
import base64
import os
import urllib


@pytest.fixture(scope="module")
def client():
    with get_app().app.test_client() as c:
        yield c


def test_no_ticker(client):
    query = {
        'comment': get_comment_no_ticker()
    }
    response = client.get(
        f"/applications_container/get_ticker/{urllib.parse.urlencode(query)}")
    expected_response = []

    assert response.status_code == 200
    assert response.json == expected_response

def test_gme_ticker(client):
    query = {
        'comment': get_comment_gme_ticker()
    }
    response = client.get(
        f"/applications_container/get_ticker/{urllib.parse.urlencode(query)}")
    expected_response = ["GME"]

    assert response.status_code == 200
    assert response.json == expected_response

def test_invalid_ticker(client):
    query = {
        'comment': get_comment_invalid_ticker()
    }
    response = client.get(
        f"/applications_container/get_ticker/{urllib.parse.urlencode(query)}")
    expected_response = []

    assert response.status_code == 200
    assert response.json == expected_response

def test_aapl_ticker(client):
    query = {
        'comment': get_comment_aapl_ticker()
    }
    response = client.get(
        f"/applications_container/get_ticker/{urllib.parse.urlencode(query)}")
    expected_response = ["AAPL"]

    assert response.status_code == 200
    assert response.json == expected_response

def test_uwmc_ticker(client):
    query = {
        'comment': get_comment_uwmc_ticker()
    }
    response = client.get(
        f"/applications_container/get_ticker/{urllib.parse.urlencode(query)}")
    expected_response = ["UWMC"]

    assert response.status_code == 200
    assert response.json == expected_response