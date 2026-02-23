#app/api/violation_types.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db

router = APIRouter(prefix="/violation-types", tags=["Violation Types"])

@router.get("/")
def get_violation_types(db: Session = Depends(get_db)):
    return {"message": "List violation types"}

@router.get("/{type_id}")
def get_violation_type(type_id: int, db: Session = Depends(get_db)):
    return {"message": f"Get violation type {type_id}"}
