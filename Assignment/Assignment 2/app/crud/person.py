# app/crud/persons.py
from sqlalchemy.orm import Session
from app.models.person import Person as PersonModel

def get_persons(db: Session):
    return db.query(PersonModel).all()

def get_person(db: Session, person_id: int):
    return db.query(PersonModel).filter(PersonModel.PersonID == person_id).first()

def create_person(db: Session, person_in):
    person = PersonModel(**person_in.dict())
    db.add(person)
    db.commit()
    db.refresh(person)
    return person

def update_person(db: Session, db_person, person_in):
    update_data = person_in.dict(exclude_unset=True)  # only provided fields
    for field, value in update_data.items():
        setattr(db_person, field, value)

    db.commit()
    db.refresh(db_person)
    return db_person

def delete_person(db: Session, person_id: int):
    person = db.query(PersonModel).filter(PersonModel.PersonID == person_id).first()
    if not person:
        return None
    db.delete(person)
    db.commit()
    return person

def get_person_by_email(db: Session, email: str):
    return db.query(PersonModel).filter(PersonModel.email == email).first()