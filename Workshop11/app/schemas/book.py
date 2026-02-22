# app/schemas/book.py 
from pydantic import BaseModel 
from typing import Optional 

# Base class with fields shared by multiple book schemas. 
class BookBase(BaseModel): 
    """BookBase defines the common fields for book-related schemas."""
    title: str 
    author: str
    year_published: Optional[int] = None
    publisher: Optional[str] = None

# Used when creating or fully updating a book via the API. 
class BookCreate(BookBase): 
    """BookCreate is used for creating new book records via the API."""
    pass

# Used when returning a book from the API (includes the ID). 
class Book(BookBase): 
    """Book is the schema used for returning book data from the API, including the ID."""
    id: int 

class Config: 
    """Config class for Pydantic models to enable ORM mode."""
    # orm_mode=True allows Pydantic to work with SQLAlchemy models. 
    orm_mode = True   
