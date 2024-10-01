import sys
sys.path.append("services/REST/app")
from data.book_repository import Book, BookRepository


class BookService:
    def __init__(self):
        self.repository = BookRepository()

    def get_all_books(self):
        return self.repository.get_all_books()

    def get_book(self, book_id):
        return self.repository.get_book(book_id)