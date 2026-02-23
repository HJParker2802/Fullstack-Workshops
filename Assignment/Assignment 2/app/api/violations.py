#app/api/violations.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db

router = APIRouter(prefix="/violations", tags=["Violations"])

@router.get("/")
def get_violations(db: Session = Depends(get_db)):
    return {"message": "List violations"}

@router.get("/{violation_id}")
def get_violation(violation_id: int, db: Session = Depends(get_db)):
    return {"message": f"Get violation {violation_id}"}