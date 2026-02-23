#app/crud/person.py
from sqlalchemy.orm import Session
from app.models.person import Person as PersonModel

def get_persons(db: Session):
    return db.query(PersonModel).all()

def get_person(db: Session, person_id: int):
    return db.query(PersonModel).filter(
        PersonModel.PersonID == person_id
    ).first()

def create_person(db: Session, person_in):
    person = PersonModel(**person_in.dict())
    db.add(person)
    db.commit()
    db.refresh(person)
    return person