# app/api/books.py 
from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.schemas.book import Book
from app.crud import book as crud_book

router = APIRouter(prefix="/books", tags=["books"])
@router.get("/", response_model=List[Book])

def list_books(db: Session = Depends(get_db)):
    return crud_book.get_books(db)

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int, db: Session = Depends(get_db)): 
    book = crud_book.get_book(db, book_id) 
    if not book: 
        raise HTTPException(status_code=404, detail="Book not found") 
    return book

