 
# 📚 Bookstore Automation Testing

This project is an **automated test framework** for a **Bookstore Management API**.  
It automates **Books, Authors, and Categories API** testing using **Selenium, Python, and pytest**.

---

## 🛠️ **Project Features**
✅ Automated API testing using **Selenium + Python + pytest**  
✅ Test coverage includes **Books, Authors, and Categories** API  
✅ **GitHub Actions CI/CD** integration for continuous testing  
✅ Supports **creating, retrieving, updating, and deleting books**  
✅ Well-structured and modular framework  

---

## 📂 **Project Structure**

bookstore_automation/ │── tests/ # Contains all test scripts │ ├── test_books.py # Books API tests │ ├── test_authors.py # Authors API tests │ ├── test_categories.py # Categories API tests │ ├── utils/ # Utility functions │ ├── api_client.py # Handles API requests │ ├── .github/workflows/ # CI/CD setup for GitHub Actions │ ├── test.yml # GitHub Actions workflow │ ├── requirements.txt # Dependencies ├── pytest.ini # pytest configuration ├── README.md # Documentation


---

## ⚙️ **Setup Instructions**
### **1️⃣ Clone the Repository**
```bash
2️⃣ Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

🧪 How to Run the Tests
Run All Tests

pytest tests --disable-warnings -v

Run a Specific Test

pytest tests/test_books.py -v

✅ Expected Output:

===================== 3 passed in 0.60s =====================

🔗 API Endpoints Used
Feature	Endpoint	Method
Create Book	/books	POST
Get Book	/books/{book_id}	GET
Update Book	/books/{book_id}	PUT
Delete Book	/books/{book_id}	DELETE
Create Author	/authors	POST
Get Author	/authors/{author_id}	GET
Create Category	/categories	POST
Get Category	/categories/{category_id}	GET




📌 Base API URL:

BASE_URL = "https://your-api-url.com"

(Replace with the actual API URL.)



🚀 GitHub Actions (CI/CD)
How It Works

    Every push or pull request to main triggers GitHub Actions.
    The workflow installs dependencies, runs tests, and reports results.

Trigger GitHub Actions Manually

git commit --allow-empty -m "Trigger GitHub Actions"
git push origin main




✅ Test Coverage

    Books API: ✅ Create, Retrieve, Update, Delete
    Authors API: ✅ Create, Retrieve
    Categories API: ✅ Create, Retrieve