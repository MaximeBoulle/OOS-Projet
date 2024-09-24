import csv
import psycopg2

DATABASE_URL = "dbname='library' user='postgres' password='admin' host='localhost'"

def insert_books_from_large_csv(csv_file):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    with open(csv_file, 'r', encoding='utf-8') as file:
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
                    VALUES (%s, %s, %s, %s, %s, %s);
                """, (book_id, title, authors, average_rating, isbn, original_publication_year))
    
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    insert_books_from_large_csv('books.csv')
