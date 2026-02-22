# app/crud/book.py 
from sqlalchemy.orm import Session
from app.models.book import Book as BookModel 

def get_books(db: Session):
    return db.query(BookModel).all()

def get_book(db: Session, book_id: int):
    return db.query(BookModel).filter(BookModel.id == book_id).first()

