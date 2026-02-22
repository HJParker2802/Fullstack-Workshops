# app/api/reviews.py 
from fastapi import APIRouter, Depends 
from sqlalchemy.orm import Session 
from typing import List 
from app.db.session import get_db 
from app.schemas.review import Review, ReviewCreate 
from app.crud import review as crud_review 

router = APIRouter( prefix="/reviews", tags=["reviews"], ) 

@router.get("/book/{book_id}", response_model=List[Review], summary="List reviews for a book") 
async def list_reviews_for_book(book_id: int, db: Session = Depends(get_db)): 
    return crud_review.get_reviews(db, book_id)


@router.post("/", response_model=Review, status_code=201, summary="Create a review") 
async def create_review(review_in: ReviewCreate, db: Session = Depends(get_db)): 
    return crud_review.create_review(db, review_in)