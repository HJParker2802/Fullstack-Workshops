#app/crud/book.py

from sqlalchemy.orm import Session 
from app.models.book import Book as BookModel 
from app.schemas.book import BookCreate

def get_books(db: Session):
    """Return all book records from the database"""
    return db.query(BookModel).all()


def get_book(db: Session, book_id: int):
    """Return a single book record by its ID"""
    return db.query(BookModel).filter(BookModel.id == book_id).first()


def create_book(db: Session, book_in: BookCreate):
    """Create a new book record in the database"""
    book = BookModel( 
                     title=book_in.title, 
                     author=book_in.author, 
                     year_published=book_in.year_published, 
                     publisher=book_in.publisher, 
                     )
    db.add(book) 
    db.commit()
    db.refresh(book) # load generated ID and any defaults 
    return book

def update_book(db: Session, book_id: int, book_in: BookCreate):
    """Update an existing book record in the database"""
    book = get_book(db, book_id) 
    if not book: 
        return None 

    book.title = book_in.title
    book.author = book_in.author 
    book.year_published = book_in.year_published 
    book.publisher = book_in.publisher 
    db.commit()
    db.refresh(book) 
    return book

def delete_book(db: Session, book_id: int): 
    """Delete a book record from the database"""
    book = get_book(db, book_id) 
    if not book: 
        return None 
    db.delete(book) 
    db.commit()
    return book
