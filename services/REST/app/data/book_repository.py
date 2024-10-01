import psycopg2
import sys
sys.path.append("services/REST/app")
from data.database import get_db_connection

class Book:
    def __init__(self, id, title, author, average_rating=None, isbn=None, original_publication_year=None):
        self.id = id
        self.title = title
        self.author = author
        self.average_rating = average_rating
        self.isbn = isbn
        self.original_publication_year = original_publication_year

class BookRepository:
    def get_all_books(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books;")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        return [Book(*row).__dict__ for row in rows]

    def get_book(self, book_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE id = %s;", (book_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return Book(*row).__dict__ if row else None

