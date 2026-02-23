#app/api/person.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db

router = APIRouter(prefix="/persons", tags=["Persons"])

@router.get("/")
def get_persons(db: Session = Depends(get_db)):
    return {"message": "List persons"}

@router.get("/{person_id}")
def get_person(person_id: int, db: Session = Depends(get_db)):
    return {"message": f"Get person {person_id}"}