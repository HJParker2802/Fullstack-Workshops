# app/api/violations.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.violation import ViolationOut, ViolationCreate
from app.crud import violation as crud
from app.core.deps import get_db

router = APIRouter(prefix="/violations", tags=["Violations"])

@router.get("/", response_model=List[ViolationOut])
def list_violations(db: Session = Depends(get_db)):
    return crud.get_violations(db)

@router.get("/{violation_id}", response_model=ViolationOut)
def get_violation(violation_id: int, db: Session = Depends(get_db)):
    db_violation = crud.get_violation(db, violation_id)
    if not db_violation:
        raise HTTPException(status_code=404, detail="Violation not found")
    return db_violation

@router.post("/", response_model=ViolationOut)
def create_violation(violation_in: ViolationCreate, db: Session = Depends(get_db)):
    return crud.create_violation(db, violation_in)

@router.put("/{violation_id}", response_model=ViolationOut)
def update_violation(violation_id: int, violation_in: ViolationCreate, db: Session = Depends(get_db)):
    db_violation = crud.update_violation(db, violation_id, violation_in)
    if not db_violation:
        raise HTTPException(status_code=404, detail="Violation not found")
    return db_violation

@router.delete("/{violation_id}", response_model=ViolationOut)
def delete_violation(violation_id: int, db: Session = Depends(get_db)):
    db_violation = crud.delete_violation(db, violation_id)
    if not db_violation:
        raise HTTPException(status_code=404, detail="Violation not found")
    return db_violation