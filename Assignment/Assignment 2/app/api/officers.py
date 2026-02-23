#app/api/officers.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.crud import officer as crud
from app.core.deps import get_db
from app.schemas.officer import OfficerOut, OfficerCreate, OfficerUpdate


router = APIRouter(prefix="/officers", tags=["Officers"])


@router.get("/", response_model=List[OfficerOut])
def list_officers(db: Session = Depends(get_db)):
    return crud.get_officers(db)


@router.get("/{officer_id}", response_model=OfficerOut)
def get_officer(officer_id: int, db: Session = Depends(get_db)):
    db_officer = crud.get_officer(db, officer_id)
    if not db_officer:
        raise HTTPException(status_code=404, detail="Officer not found")
    return db_officer


@router.post("/", response_model=OfficerOut)
def create_officer(officer_in: OfficerCreate, db: Session = Depends(get_db)):
    return crud.create_officer(db, officer_in)



@router.put("/{officer_id}", response_model=OfficerOut)
def update_officer(officer_id: int, officer_in: OfficerUpdate, db: Session = Depends(get_db)):
    db_officer = crud.get_officer(db, officer_id)
    if not db_officer:
        raise HTTPException(status_code=404, detail="Officer not found")
    return crud.update_officer(db, db_officer, officer_in)


@router.delete("/{officer_id}", response_model=OfficerOut)
def delete_officer(officer_id: int, db: Session = Depends(get_db)):
    db_officer = crud.delete_officer(db, officer_id)
    if not db_officer:
        raise HTTPException(status_code=404, detail="Officer not found")
    return db_officer