# app/schemas/book.py 
from pydantic import BaseModel 
from typing import Optional 

class BookBase(BaseModel):
    title: str 
    author: str
    year_published: Optional[int] = None
    publisher: Optional[str] = None

class Book(BookBase):
    id: int
    
class Config:
    orm_mode = True


 