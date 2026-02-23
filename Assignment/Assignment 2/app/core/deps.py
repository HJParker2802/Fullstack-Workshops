#app/core/deps.py
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from app.core.security import SECRET_KEY, ALGORITHM
from app.crud import person as crud_person  # adjust if your users are elsewhere




def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    """Validate JWT and return current user."""

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: Optional[str] = payload.get("sub")

        if email is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = crud_person.get_person_by_email(db, email)

    if user is None:
        raise credentials_exception

    return user