# test_api_posts.py
import requests
import pytest
from data.config import BASE_URL



def test_get_all_posts():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_single_post():
    response = requests.get(f"{BASE_URL}/1")
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1

def test_create_post():
    new_post = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(BASE_URL, json=new_post)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "foo"

def test_update_post():
    updated_data = {"title": "updated title"}
    response = requests.put(f"{BASE_URL}/1", json=updated_data)
    assert response.status_code == 200

def test_delete_post():
    response = requests.delete(f"{BASE_URL}/1")
    assert response.status_code == 200
