# app/api/reviews.py 
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from app.db.session import get_db
from app.schemas.review import Review, ReviewCreate
from app.crud import review as crud_review 
from app.core.deps import get_current_user 

router = APIRouter(prefix="/reviews", tags=["reviews"])
@router.post("/", response_model=Review, status_code=201) 

def create_review(review_in: ReviewCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)): 
    return crud_review.create_review(db, review_in, user_id=current_user.id)

