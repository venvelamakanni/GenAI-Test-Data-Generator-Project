```python
import pytest
import requests
import json

@pytest.fixture
def base_url():
    return "http://127.0.0.1:8000"

@pytest.fixture
def headers():
    return {"Content-Type": "application/json"}

@pytest.mark.positive
def test_create_user_success(base_url, headers):
    """
    Test case for successful user creation.
    """
    url = f"{base_url}/users"  # Assuming the endpoint is /users
    payload = {
        "username": "newuser",
        "email": "newuser@example.com",
        "password": "securepass123",
        "full_name": "New User"
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    assert response.status_code == 201
    response_json = response.json()
    assert "id" in response_json
    assert response_json["username"] == "newuser"
    assert response_json["email"] == "newuser@example.com"
    assert response_json["full_name"] == "New User"
    assert "created_at" in response_json

@pytest.mark.negative
def test_create_user_duplicate_username(base_url, headers):
    """
    Test case for creating a user with a duplicate username (should fail).
    """
    url = f"{base_url}/users"  # Assuming the endpoint is /users
    payload = {
        "username": "newuser",  # Assuming "newuser" already exists from the positive test
        "email": "anotheruser@example.com",
        "password": "anothersecurepass",
        "full_name": "Another User"
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    assert response.status_code == 400  # Or another appropriate error code
    response_json = response.json()
    assert "username" in response_json  # Assuming the error message contains the field with the error
    #assert "This username already exists." in response_json["username"] # Example error message assertion

@pytest.mark.negative
def test_create_user_invalid_email(base_url, headers):
    """
    Test case for creating a user with an invalid email format.
    """
    url = f"{base_url}/users"
    payload = {
        "username": "invalidemailuser",
        "email": "invalid-email",
        "password": "securepass123",
        "full_name": "Invalid Email User"
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    assert response.status_code == 400
    response_json = response.json()
    assert "email" in response_json
    #assert "Enter a valid email address." in response_json["email"]
```