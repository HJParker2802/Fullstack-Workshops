#app/schemas/Review.py
from pydantic import BaseModel
from typing import Optional

class ReviewBase(BaseModel):
    book_id: int
    rating: int
    comment: str

class ReviewCreate(ReviewBase): 
    """Schema for creating a new review.""" 
    pass 

class Review(ReviewBase): 
    """Schema returned by the API for a review.""" 
    id: int 

class Config: 
    orm_mode = True 