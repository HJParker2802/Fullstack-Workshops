#app/api/violation_types.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.violation_type import ViolationTypeOut, ViolationTypeCreate
from app.crud import violation_type as crud
from app.core.deps import get_db

router = APIRouter(prefix="/violation_types", tags=["Violation Types"])

@router.get("/", response_model=List[ViolationTypeOut])
def list_violation_types(db: Session = Depends(get_db)):
    return crud.get_violation_types(db)

@router.get("/{violation_type_id}", response_model=ViolationTypeOut)
def get_violation_type(violation_type_id: int, db: Session = Depends(get_db)):
    db_type = crud.get_violation_type(db, violation_type_id)
    if not db_type:
        raise HTTPException(status_code=404, detail="ViolationType not found")
    return db_type

@router.post("/", response_model=ViolationTypeOut)
def create_violation_type(violation_type_in: ViolationTypeCreate, db: Session = Depends(get_db)):
    return crud.create_violation_type(db, violation_type_in)

@router.put("/{violation_type_id}", response_model=ViolationTypeOut)
def update_violation_type(violation_type_id: int, violation_type_in: ViolationTypeCreate, db: Session = Depends(get_db)):
    db_type = crud.update_violation_type(db, violation_type_id, violation_type_in)
    if not db_type:
        raise HTTPException(status_code=404, detail="ViolationType not found")
    return db_type

@router.delete("/{violation_type_id}", response_model=ViolationTypeOut)
def delete_violation_type(violation_type_id: int, db: Session = Depends(get_db)):
    db_type = crud.delete_violation_type(db, violation_type_id)
    if not db_type:
        raise HTTPException(status_code=404, detail="ViolationType not found")
    return db_type