from starlette.testclient import TestClient
from main import app

client=TestClient(app=app)

def test_something():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {}

def test_post():
    response = client.post('/{insert teh specific route}',json={})

    assert response.status_code == 201
    assert response.json() == {}