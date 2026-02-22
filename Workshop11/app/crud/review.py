#app/crud/Review.py
from sqlalchemy.orm import Session
from app.models.review import Review as ReviewModel
from app.schemas.review import ReviewCreate

def get_reviews(db: Session, book_id: int):
    """Return all reviews for a given book"""
    return db.query(ReviewModel).filter(ReviewModel.book_id == book_id).all()

def create_review(db: Session, review_in: ReviewCreate):
    """Create a new review for a book."""
    review = ReviewModel(
        book =review_in.book_id,
        rating = review_in.rating,
        comment = review_in.comment,
        )
    db.add(review)
    db.commit()
    db.refresh(review)
    return review

