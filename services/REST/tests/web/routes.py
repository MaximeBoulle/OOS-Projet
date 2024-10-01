import unittest
from fastapi.testclient import TestClient
import sys
sys.path.append("services/REST")
from app.main import app

client = TestClient(app)

class TestBookRoutes(unittest.TestCase):
    
    def test_get_books(self):
        response = client.get("/books/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
    
    def test_get_book(self):
        response = client.get("/books/1")
        if response.status_code == 200:
            self.assertIsInstance(response.json(), dict)
        else:
            self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
