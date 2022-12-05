from starlette.testclient import TestClient
from app.main import app

client = TestClient(app=app)


def test_get_all_cars():
    response = client.get("/cars")

    assert response.status_code == 200
    assert len(response.json()) != 0


def test_get_a_car():
    response = client.get("/cars/0", json={})

    assert response.status_code == 201 or 404
    if response.status_code != 404:
        assert response.json()["id"] == 0


def test_create_existing_item():
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
    assert response.status_code == 400
    assert response.json() == {"detail": "Car already exists"}


def test_create_a_car():
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
    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "name": "Foo Bar",
        "make": "The Foo Barters",
        "horsepower": 3000,
        "color": "black",
    }


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


# def test_remove_note(test_app, monkeypatch):
#     test_data = {"title": "something", "description": "something else", "id": 1}
#     response = test_app.delete("/notes/1/")
#     assert response.status_code == 200
#     assert response.json() == test_data

def test_delete_a_car_with_invalid_id():
    response = client.delete("/car/1")

    assert response.status_code == 404
    assert response.json()["detail"] == "Resources not found"

def test_delete_a_car():
    response = client.delete("/car/1")

    if response.status_code != 404:
        assert response.status_code == 202
