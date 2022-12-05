from starlette.testclient import TestClient
from test.main import app

client = TestClient(app=app)


def test_get_all_cars():
    response = client.get("/cars")

    assert response.status_code == 200
    assert len(response.json()) != 0


def test_get_a_car():
    response = client.get("cars/0", json={})

    assert response.status_code == 201 or 404
    if response.status_code != 404:
        assert response.json()["id"] == 0

def test_create_a_car():
    pass

def test_update_a_car():
    pass

def test_delete_a_car():
    pass


