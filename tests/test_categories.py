import pytest
from bookstore_automation.utils.api_client import APIClient

@pytest.mark.category
def test_create_category():
    """Test creating a category"""
    response = APIClient.create_category("Fiction")
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    response_data = response.json()
    assert response_data["name"] == "Fiction"

@pytest.mark.category
def test_get_category():
    """Test retrieving a category by ID"""
    create_response = APIClient.create_category("Science")
    assert create_response.status_code == 201
    category_id = create_response.json()["id"]

    get_response = APIClient.get_category(category_id)
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Science"
 
