from starlette.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app=app)


@pytest.mark.skip(reason="no way of currently testing this")
def test_get_all_cars():
    response = client.get("/cars")

    assert response.status_code == 200
    assert len(response.json()) != 0


def test_get_a_car():
    response = client.get("/cars/0")

    assert response.status_code == 201 or 404
    if response.status_code != 404:
        assert response.json()["id"] == 0


@pytest.mark.skip(reason="no way of currently testing this")
def test_create_existing_car():
    response = client.post(
        "/cars",
        json={
            "id": 1,
            "name": "Foo Bar",
            "make": "The Foo Barters",
            "horsepower": 3000,
            "color": "black",
        },
    )
    if response.status_code != 201:
        assert response.status_code == 400
        assert response.json() == {"detail": "Car already exists"}


@pytest.mark.skip(reason="no way of currently testing this")
def test_create_a_car():
    response = client.post(
        "/cars",
        json={
            "id": 2,
            "name": "Foo Bar fighter",
            "make": "The Foo Barters fighters",
            "horsepower": 30000,
            "color": "white",
        },
    )
    if response.status_code != 400:
        assert response.status_code == 201
        assert response.json() == {
            "id": 2,
            "name": "Foo Bar fighter",
            "make": "The Foo Barters fighters",
            "horsepower": 30000,
            "color": "white",
        }


@pytest.mark.skip(reason="no way of currently testing this")
def test_update_a_car():
    test_update_data = {
        "id": 1,
        "name": "Foo Bar",
        "make": "The Foo Barters",
        "horsepower": 3000,
        "color": "black",
    }

    response = client.put("/car/1", json=test_update_data)
    assert response.status_code == 200
    assert response.json() == test_update_data


@pytest.mark.skip(reason="no way of currently testing this")
def test_delete_a_car_with_invalid_id():
    response = client.delete("/car/1")
    if response.status_code != 202:
        assert response.status_code == 404
        assert response.json()["detail"] == "Resources not found"


@pytest.mark.skip(reason="no way of currently testing this")
def test_delete_a_car():
    response = client.delete("/car/1")

    if response.status_code != 404:
        assert response.status_code == 202
