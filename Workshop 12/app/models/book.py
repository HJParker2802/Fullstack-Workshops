# app/models/book.py
from sqlalchemy import Column, Integer, String 
from app.db.base import Base 

class Book(Base): 
    __tablename__ = "books" 
    id = Column(Integer, primary_key=True, index=True) 
    title = Column(String(255), nullable=False) 
    author = Column(String(255), nullable=False) 
    year_published = Column(Integer, nullable=True) 
    publisher = Column(String(255), nullable=True) 

