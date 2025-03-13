import requests

# Base URL of the API (Replace with the actual API endpoint)
BASE_URL = "https://api.example.com"

class APIClient:
    """A class to interact with the Bookstore API."""

    @staticmethod
    def create_book(title, author_id, category_id):
        """Creates a new book in the system."""
        payload = {
            "title": title,
            "author_id": author_id,
            "category_id": category_id
        }
        response = requests.post(f"{BASE_URL}/books", json=payload)
        return response

    @staticmethod
    def get_book(book_id):
        """Retrieves book details by ID."""
        response = requests.get(f"{BASE_URL}/books/{book_id}")
        return response

    @staticmethod
    def update_book(book_id, title=None, author_id=None, category_id=None):
        """Updates book details."""
        payload = {}
        if title:
            payload["title"] = title
        if author_id:
            payload["author_id"] = author_id
        if category_id:
            payload["category_id"] = category_id

        response = requests.put(f"{BASE_URL}/books/{book_id}", json=payload)
        return response

    @staticmethod
    def delete_book(book_id):
        """Deletes a book from the system."""
        response = requests.delete(f"{BASE_URL}/books/{book_id}")
        return response

    @staticmethod
    def create_author(name):
        """Creates a new author."""
        payload = {"name": name}
        response = requests.post(f"{BASE_URL}/authors", json=payload)
        return response

    @staticmethod
    def get_author(author_id):
        """Retrieves author details by ID."""
        response = requests.get(f"{BASE_URL}/authors/{author_id}")
        return response

    @staticmethod
    def create_category(name):
        """Creates a new category."""
        payload = {"name": name}
        response = requests.post(f"{BASE_URL}/categories", json=payload)
        return response

    @staticmethod
    def get_category(category_id):
        """Retrieves category details by ID."""
        response = requests.get(f"{BASE_URL}/categories/{category_id}")
        return response
 
