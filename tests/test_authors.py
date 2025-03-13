import pytest
from bookstore_automation.utils.api_client import APIClient

@pytest.mark.author
def test_create_author():
    """Test creating an author"""
    response = APIClient.create_author("John Doe")
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    response_data = response.json()
    assert response_data["name"] == "John Doe"

@pytest.mark.author
def test_get_author():
    """Test retrieving an author by ID"""
    create_response = APIClient.create_author("Jane Smith")
    assert create_response.status_code == 201
    author_id = create_response.json()["id"]

    get_response = APIClient.get_author(author_id)
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Jane Smith"
 
