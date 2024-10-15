import csv
import psycopg2
import os

DATABASE_URL = "dbname='library' user='postgres' password='admin' host='localhost'"

def init_db():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            author VARCHAR(255),
            average_rating FLOAT,
            isbn VARCHAR(13),
            original_publication_year FLOAT
        );
    """)
    conn.commit()
    
    
    insert_books(cursor, conn, 'books.csv')

    cursor.close()
    conn.close()

def insert_books(cursor, conn, csv_file):
    
    csv_file_path = os.path.join(os.path.dirname(__file__), csv_file)
    
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            book_id = row['book_id']
            title = row['title']
            authors = row['authors']
            average_rating = row['average_rating']
            isbn = row['isbn']
            original_publication_year = row['original_publication_year']

            if title:
                cursor.execute("""
                    INSERT INTO books (id, title, author, average_rating, isbn, original_publication_year) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (id) DO NOTHING;
                """, (book_id, title, authors, average_rating, isbn, original_publication_year))

    conn.commit()

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn
