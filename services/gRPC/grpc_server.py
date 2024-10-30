import grpc
from concurrent import futures
import requests
import logging
from generated import books_pb2, books_pb2_grpc

class BookServiceServicer(books_pb2_grpc.BookServiceServicer):
    def GetBook(self, request, context):
        logging.info("GetBook called with id: %s", request.id)
        try:
            response = requests.get(f"http://localhost:8000/books/{request.id}")
            response.raise_for_status()
            book_data = response.json()
            return books_pb2.Book(
                id=book_data["id"],
                title=book_data["title"],
                author=book_data["author"],
                isbn=book_data["isbn"],
                average_rating=book_data["average_rating"]
            )
        except requests.exceptions.HTTPError as e:
            context.set_details(f"Error fetching book: {str(e)}")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return books_pb2.BookResponse()

    def GetAllBooks(self, request, context):
        logging.info("GetAllBooks called")
        try:
            response = requests.get("http://localhost:8000/books/")
            response.raise_for_status()
            books_data = response.json()
            books_response = books_pb2.BooksResponse()
            for book in books_data:
                books_response.books.add(
                    id=book["id"],
                    title=book["title"],
                    author=book["author"],
                    isbn=book["isbn"],
                    average_rating=book["average_rating"]
                )
            return books_response
        except requests.exceptions.HTTPError as e:
            context.set_details(f"Error fetching books: {str(e)}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return books_pb2.BooksResponse()

def serve():
    logging.basicConfig(level=logging.INFO)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    books_pb2_grpc.add_BookServiceServicer_to_server(BookServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logging.info("gRPC server running on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()