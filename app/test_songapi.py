import requests
from fastapi.testclient import TestClient
from pydantic import BaseModel
import json

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}


tokenrequest = requests.post(
    "http://localhost:8000/token", data={
        "grant_type": "password",
        "username": "test@test.be",
        "password": "test123",
    }, auth=("client-id", "client-secret"))

print(tokenrequest.text)

# extracting the token that came with the response
access_token = tokenrequest.json()["access_token"]

# Using the token in the headers of a secured endpoint
headerswithtoken = {
    "accept": "application/json",
    "Authorization": f'Bearer {access_token}'
}


def test_create_user():
    """Test the POST /users endpoint."""
    # send a POST request to the /users endpoint with a new user object
    user = {"email": "test@example.com", "password": "password"}
    response = requests.post("http://127.0.0.1:8000/users", json=user)

    # check that the response status code is 201 (Created)
    assert response.status_code == 201

    # check that the response body is the created user object
    created_user = response.json()
    assert isinstance(created_user, dict)
    assert created_user["email"] == user["email"]


def test_create_album():
    """Test the POST /albums endpoint."""
    # create a new user and genre
    user_id = 3
    genre_id = 2

    # send a POST request to the /albums endpoint with a new album object
    album = {"title": "Test Album 3", "artist": "Test Artist",
             "genre_id": genre_id, "user_id": user_id}
    response = requests.post("http://127.0.0.1:8000/albums", json=album)

    # check that the response status code is 201 (Created)
    assert response.status_code == 200

    # check that the response body is the created album object
    created_album = response.json()
    assert isinstance(created_album, dict)
    assert created_album["title"] == album["title"]


def test_create_genre():
    """Test the POST /genres endpoint."""
    # send a POST request to the /genres endpoint with a new genre object
    genre = {"name": "Metal"}
    response = requests.post("http://127.0.0.1:8000/genres", json=genre)

    # check that the response status code is 201 (Created)
    assert response.status_code == 200

    # check that the response body is the created genre object
    created_genre = response.json()
    assert isinstance(created_genre, dict)
    assert created_genre["name"] == genre["name"]


def test_get_genres():
    """Test the GET /genres endpoint."""
    # send a GET request to the /genres endpoint
    response = requests.get(
        "http://127.0.0.1:8000/genres", headers=headerswithtoken)

    # check that the response status code is 200 (OK)
    assert response.status_code == 200

    # check that the response body is a list of genres
    genres = response.json()
    assert isinstance(genres, list)
    assert all(isinstance(genre, dict) for genre in genres)


def test_get_albums():
    """Test the GET /albums endpoint."""
    # send a GET request to the /albums endpoint
    response = requests.get(
        "http://127.0.0.1:8000/albums", headers=headerswithtoken)

    # check that the response status code is 200 (OK)
    assert response.status_code == 200

    # check that the response body is a list of albums
    albums = response.json()
    assert isinstance(albums, list)
    assert all(isinstance(album, dict) for album in albums)


def test_get_album():
    """Test the GET /albums/{id} endpoint."""

    # send a GET request to the /albums/{id} endpoint
    response = requests.get(
        "http://127.0.0.1:8000/albums/3", headers=headerswithtoken)

    # check that the response status code is 200 (OK)
    assert response.status_code == 200

    # check that the response body is the album object
    album = response.json()
    assert isinstance(album, dict)


def test_update_album():
    """Test the PUT /albums/{id} endpoint."""
    user_id = 3
    genre_id = 2

    # send a PUT request to the /albums/{id} endpoint with an updated album object
    album = {"title": "Test Album 2", "artist": "Test Artist 2",
             "genre_id": genre_id, "user_id": user_id}
    response = requests.put(
        "http://127.0.0.1:8000/albums/4", json=album)

    # check that the response status code is 200 (OK)
    assert response.status_code == 200

    # check that the response body is the updated album object
    updated_album = response.json()
    assert isinstance(updated_album, dict)
    assert updated_album["title"] == album["title"]


def test_delete_album():
    """Test the DELETE /albums/{id} endpoint."""

    # send a DELETE request to the /albums/{id} endpoint
    response = requests.delete("http://127.0.0.1:8000/albums/4")

    # check that the response status code is 204 (No Content)
    assert response.status_code == 200
