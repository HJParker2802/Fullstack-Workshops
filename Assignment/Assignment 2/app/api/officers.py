#app/api/officers.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db

router = APIRouter(prefix="/officers", tags=["Officers"])

@router.get("/")
def get_officers(db: Session = Depends(get_db)):
    return {"message": "List officers"}

@router.get("/{officer_id}")
def get_officer(officer_id: int, db: Session = Depends(get_db)):
    return {"message": f"Get officer {officer_id}"}