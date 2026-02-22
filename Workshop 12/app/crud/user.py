# app/crud/user.py 
from sqlalchemy.orm import Session 
from app import db
from app.models import user
from app.models.user import User as UserModel 
from app.schemas import user
from app.schemas.user import UserCreate
from app.core.security import hash_password

def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()

def create_user(db: Session, user_in: UserCreate): 
    user = UserModel( 
                     name=user_in.name,
                     email=user_in.email,
                     password_hash=hash_password(user_in.password),
                     role=user_in.role or "user",
    ) 
    db.add(user)
    db.commit()
    db.refresh(user) 
    return user

