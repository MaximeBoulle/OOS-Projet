import unittest
from app.service.book_service import BookService

class TestBookService(unittest.TestCase):
    
    def setUp(self):
        self.service = BookService()

    def test_get_all_books(self):
        books = self.service.get_all_books()
        self.assertIsInstance(books, list)

    def test_get_book(self):
        book = self.service.get_book(1)
        if book:
            self.assertIsInstance(book, dict)
        else:
            self.assertIsNone(book)

if __name__ == "__main__":
    unittest.main()
