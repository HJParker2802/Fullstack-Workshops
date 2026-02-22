# app/schemas/review.py 
from pydantic import BaseModel
from typing import Optional 

class ReviewCreate(BaseModel):
    book_id: int 
    rating: int
    comment: Optional[str] = None 

class Review(ReviewCreate):
    id: int
    user_id: int

class Config:
    orm_mode = True 