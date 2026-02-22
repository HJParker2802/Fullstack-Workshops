#app/models/Review.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Review(Base):
    """Review model representing the 'reviews' table in the database."""
    __tablename__ = 'reviews'
    
    id = Column(Integer, primary_key=True, index=True)
    bookid = Column(Integer, ForeignKey('books.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String(500), nullable=True)
    #Relationship to the Book model (Book.reviews gives all reviews for book).
    book = relationship("Book", backref="reviews")
