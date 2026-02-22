# app/api/users.py 
from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy.orm import Session
from app.db.session import get_db 
from app.schemas.user import User, UserCreate
from app.crud import user as crud_user 

router = APIRouter(prefix="/users", tags=["users"]) 
@router.post("/", response_model=User, status_code=201) 
def register(user_in: UserCreate, db: Session = Depends(get_db)): 
    existing = crud_user.get_user_by_email(db, user_in.email) 
    if existing: 
        raise HTTPException(status_code=400, detail="Email already registered") 
    return crud_user.create_user(db, user_in)

