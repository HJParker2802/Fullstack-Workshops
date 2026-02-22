#app/models/book.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped
from app.db.base import Base

class Book(Base):
    """SQLAlchemy ORM Model for the 'boosks' table"""
    __tablename__="books"
    
    id = Column(Integer, primary_key=True, index=True) 
    title = Column(String(200), nullable=False) 
    author = Column(String(200), nullable=False) 
    year_published = Column(Integer, nullable=True) 
    publisher = Column(String(200), nullable=True) 
