from fastapi.testclient import TestClient 

from main import app

client = TestClient(app)


def test_wiki_ok():
    response = client.get('/wiki/rum')
    assert response.status_code == 200


def test_wiki_half():
    response = client.get('/wiki/rumbellion')
    assert response.status_code == 303


def test_wiki_error():
    response = client.get('/wiki/asdsdfjsd')
    assert response.status_code == 404
    assert response.json() == {'result': None}