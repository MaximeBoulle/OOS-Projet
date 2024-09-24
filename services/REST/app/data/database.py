import psycopg2
from psycopg2 import sql

DATABASE_URL = "dbname='library' user='postgres' password='admin' host='localhost'"

def init_db():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255),
            average_rating DECIMAL,
            isbn VARCHAR(20),
            original_publication_year DECIMAL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn
