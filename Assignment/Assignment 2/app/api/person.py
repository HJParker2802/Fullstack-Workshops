# app/api/person.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.person import Person, PersonCreate
from app.crud import person as crud_person
from app.core.deps import get_db

router = APIRouter(prefix="/persons", tags=["Persons"])

# GET /persons/ - list all persons
@router.get("/", response_model=List[Person])
def get_persons(db: Session = Depends(get_db)):
    return crud_person.get_persons(db)


# GET /persons/{person_id} - get a single person
@router.get("/{person_id}", response_model=Person)
def get_person(person_id: int, db: Session = Depends(get_db)):
    db_person = crud_person.get_person(db, person_id)
    if not db_person:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person


# POST /persons/ - create a new person
@router.post("/", response_model=Person)
def create_person(person_in: PersonCreate, db: Session = Depends(get_db)):
    return crud_person.create_person(db, person_in)


@router.delete("/{person_id}", response_model=Person)   
def delete_person(person_id: int, db: Session = Depends(get_db)):
    deleted_person = crud_person.delete_person(db, person_id)
    if not deleted_person:
        raise HTTPException(status_code=404, detail="Person not found")
    return deleted_person