# app/api/persons.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.person import Person, PersonCreate, PersonUpdate
from app.crud import person as crud
from app.core.deps import get_db

router = APIRouter(prefix="/persons", tags=["Persons"])

@router.get("/", response_model=List[Person])
def list_persons(db: Session = Depends(get_db)):
    return crud.get_persons(db)

@router.get("/{person_id}", response_model=Person)
def get_person(person_id: int, db: Session = Depends(get_db)):
    db_person = crud.get_person(db, person_id)
    if not db_person:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person

@router.post("/", response_model=Person)
def create_person(person_in: PersonCreate, db: Session = Depends(get_db)):
    return crud.create_person(db, person_in)

@router.put("/{person_id}", response_model=Person)
def update_person(person_id: int, person_in: PersonUpdate, db: Session = Depends(get_db)):
    db_person = crud.get_person(db, person_id)
    if not db_person:
        raise HTTPException(status_code=404, detail="Person not found")
    return crud.update_person(db, db_person, person_in)

@router.delete("/{person_id}", response_model=Person)
def delete_person(person_id: int, db: Session = Depends(get_db)):
    db_person = crud.delete_person(db, person_id)
    if not db_person:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person