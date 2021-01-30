from travis_test.app import app
import pytest

@pytest.fixture()
def client():
    with app.test_client() as c:
        yield c


def test_main(client):
    rv = client.get('/')
    assert b'Hello World!' in rv.data

