import pytest
from bookstore_automation.utils.api_client import APIClient

@pytest.mark.book
def test_create_book():
    """Test creating a book"""
    response = APIClient.create_book("Automation Book", 1, 2)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    response_data = response.json()
    assert response_data["title"] == "Automation Book"

@pytest.mark.book
def test_get_book():
    """Test retrieving a book by ID"""
    create_response = APIClient.create_book("Retrieve Book", 1, 2)
    assert create_response.status_code == 201
    book_id = create_response.json()["id"]

    get_response = APIClient.get_book(book_id)
    assert get_response.status_code == 200
    assert get_response.json()["title"] == "Retrieve Book"

@pytest.mark.book
def test_update_book():
    """Test updating a book"""
    create_response = APIClient.create_book("Old Title", 1, 2)
    assert create_response.status_code == 201
    book_id = create_response.json()["id"]

    update_response = APIClient.update_book(book_id, title="Updated Title")
    assert update_response.status_code == 200

    get_response = APIClient.get_book(book_id)
    assert get_response.status_code == 200
    assert get_response.json()["title"] == "Updated Title"

@pytest.mark.book
def test_delete_book():
    """Test deleting a book"""
    create_response = APIClient.create_book("Delete Book", 1, 2)
    assert create_response.status_code == 201
    book_id = create_response.json()["id"]

    delete_response = APIClient.delete_book(book_id)
    assert delete_response.status_code == 204  # Usually, delete returns 204 (No Content)

    get_response = APIClient.get_book(book_id)
    assert get_response.status_code == 404  # The book should no longer exist
 
