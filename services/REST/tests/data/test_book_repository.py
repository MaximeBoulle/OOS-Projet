import unittest
from app.data.book_repository import BookRepository

class TestBookRepository(unittest.TestCase):
    
    def setUp(self):
        self.repo = BookRepository()

    def test_get_all_books(self):
        books = self.repo.get_all_books()
        self.assertIsInstance(books, list)
    
    def test_get_book(self):
        book = self.repo.get_book(1)
        if book:
            self.assertIsInstance(book, dict)
        else:
            self.assertIsNone(book)

if __name__ == "__main__":
    unittest.main()
