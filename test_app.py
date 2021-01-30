""""""
from travis_test.app import app
import pytest

@pytest.fixture()
def client():
    with app.test_client() as c:
        yield c


def test_main(client):
    rv = client.get('/')
    assert b'Assert will fail' in rv.data
