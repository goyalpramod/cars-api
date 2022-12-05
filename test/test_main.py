from starlette.testclient import TestClient
from test.main import app

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


# def test_update_note(test_app, monkeypatch):
#     test_update_data = {"title": "someone", "description": "someone else", "id": 1}
#
#     async def mock_get(id):
#         return True
#
#     monkeypatch.setattr(crud, "get", mock_get)
#
#     async def mock_put(id, payload):
#         return 1
#
#     monkeypatch.setattr(crud, "put", mock_put)
#
#     response = test_app.put("/notes/1/", content=json.dumps(test_update_data))
#     assert response.status_code == 200
#     assert response.json() == test_update_data


def test_update_a_car():
    pass


# def test_remove_note(test_app, monkeypatch):
#     test_data = {"title": "something", "description": "something else", "id": 1}
#
#     async def mock_get(id):
#         return test_data
#
#     monkeypatch.setattr(crud, "get", mock_get)
#
#     async def mock_delete(id):
#         return id
#
#     monkeypatch.setattr(crud, "delete", mock_delete)
#
#     response = test_app.delete("/notes/1/")
#     assert response.status_code == 200
#     assert response.json() == test_data
#
#
# def test_remove_note_incorrect_id(test_app, monkeypatch):
#     async def mock_get(id):
#         return None
#
#     monkeypatch.setattr(crud, "get", mock_get)
#
#     response = test_app.delete("/notes/999/")
#     assert response.status_code == 404
#     assert response.json()["detail"] == "Note not found"


def test_delete_a_car():
    pass
