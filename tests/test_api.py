import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_user_by_id():
    response = requests.get(
        f"{BASE_URL}/users/1",
        timeout=10
    )

    assert response.status_code == 200

    user = response.json()

    assert user["id"] == 1
    assert user["name"] == "Leanne Graham"
    assert "email" in user
def test_get_nonexistent_user():
    response = requests.get(
        f"{BASE_URL}/users/9999",
        timeout=10
    )

    assert response.status_code == 404


def test_create_user():
    payload = {
        "name": "Chaymae",
        "username": "chaymae_qa",
        "email": "chaymae@example.com"
    }

    response = requests.post(
        f"{BASE_URL}/users",
        json=payload,
        timeout=10
    )

    assert response.status_code == 201

    created_user = response.json()

    assert created_user["name"] == payload["name"]
    assert created_user["username"] == payload["username"]
    assert created_user["email"] == payload["email"]
    assert "id" in created_user


def test_get_users_list():
    response = requests.get(
        f"{BASE_URL}/users",
        timeout=10
    )

    assert response.status_code == 200

    users = response.json()

    assert isinstance(users, list)
    assert len(users) > 0
    assert "id" in users[0]
    assert "name" in users[0]
    assert "email" in users[0]