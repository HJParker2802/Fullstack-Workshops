# app/api/reviews.py
from fastapi import APIRouter 
router = APIRouter(
    prefix="/reviews",
    tags=["reviews"], 
    )

@router.get("/book/{book_id}", summary="List reviews for a book (placeholder)") 
async def list_reviews_for_book(book_id: int): 
    """Temporary hard-coded reviews. Will be replaced with DB-backed implementation later.""" 
    return [ 
            {"book_id": book_id, "review_id": 1, "rating": 5, "comment": "Excellent!"}, 
            {"book_id": book_id, "review_id": 2, "rating": 4, "comment": "Very good."}, 
            ]
 