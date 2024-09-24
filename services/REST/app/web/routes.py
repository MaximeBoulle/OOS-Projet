from fastapi import APIRouter, HTTPException
from service.book_service import BookService

router = APIRouter()

book_service = BookService()

@router.get("/books/", response_model=list)
async def get_books():
    books = book_service.get_all_books()
    return books

@router.get("/books/{book_id}", response_model=dict)
async def get_book(book_id: int):
    book = book_service.get_book(book_id)
    if book:
        return book
    raise HTTPException(status_code=404, detail="Book not found")

