# app/crud/officer.py
from sqlalchemy.orm import Session
from app.models.officer import Officer


def get_officers(db: Session):
    return db.query(Officer).all()

def get_officer(db: Session, officer_id: int):
    return db.query(Officer).filter(Officer.OfficerID == officer_id).first()

def create_officer(db: Session, officer_in):
    officer = Officer(**officer_in.dict())
    db.add(officer)
    db.commit()
    db.refresh(officer)
    return officer

def update_officer(db: Session, db_officer, officer_in):
    update_data = officer_in.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_officer, field, value)
    db.commit()
    db.refresh(db_officer)
    return db_officer

def delete_officer(db: Session, officer_id: int):
    officer = db.query(Officer).filter(Officer.OfficerID == officer_id).first()
    if officer:
        db.delete(officer)
        db.commit()
    return officer


def validate_officer_login(db: Session, OfficerID: int, PersonID: int):
    return (
        db.query(Officer)
        .filter(
            Officer.OfficerID == OfficerID,
            Officer.PersonID == PersonID
        )
        .first()
    )