import requests

BASE_URL = "http://localhost:5000"

def test_create_book_happy_path():
    payload = {"title": "The Hobbit", "author": "J.R.R. Tolkien"}
    response = requests.post(f"{BASE_URL}/books", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "The Hobbit"
    assert data["author"] == "J.R.R. Tolkien"
    assert "id" in data

def test_create_book_missing_title_returns_400():
    payload = {"author": "J.R.R. Tolkien"}
    response = requests.post(f"{BASE_URL}/books", json=payload)
    assert response.status_code == 400
    data = response.json()
    assert "error" in data

def test_delete_nonexistent_book_returns_404():
    response = requests.delete(f"{BASE_URL}/books/99999")
    assert response.status_code == 404
    data = response.json()
    assert "error" in data