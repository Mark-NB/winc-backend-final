import pytest

from main import app


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_redirect(client):
    response = client.get("/home")
    assert response.status_code == 302
    assert response.location == "http://188.166.40.219/"


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"<title>WINC backend CL Assignment</title>" in response.data


def test_about(client):
    response = client.get("/contact")
    assert response.status_code == 200
    assert b"<title>Contact</title>" in response.data


# Guaranteed fail test to test github action to stop before deployment
# def test_about(client):
#     response = client.get("/contact")
#     assert response.status_code == 200
#     assert b"<title>THIS SHOULD READ CONTENT BUT IT DOESNT</title>" in response.data
