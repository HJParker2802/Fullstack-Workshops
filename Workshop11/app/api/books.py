# app/api/books.py

#FastAPI Imports:
from app.schemas.book import Book, BookCreate
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.crud import book as crud_book 

router = APIRouter( 
                   prefix="/books",
                   tags=["books"],
                   )

@router.get("/", response_model=List[Book], summary="Get all books") 
async def list_books(db: Session = Depends(get_db)): 
    books = crud_book.get_books(db) 
    return books 

@router.get("/{book_id}", response_model=Book)
async def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud_book.get_book(db, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book

@router.post("/", response_model=Book)
async def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return crud_book.create_book(db, book)

@router.delete("/{book_id}")
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    success = crud_book.delete_book(db, book_id)

    if not success:
        raise HTTPException(status_code=404, detail="Book not found")

    return {"message": "Book deleted"}

