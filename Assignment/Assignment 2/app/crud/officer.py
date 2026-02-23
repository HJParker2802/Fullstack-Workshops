#app/crud/officer.py
from sqlalchemy.orm import Session
from app.models.officer import Officer as OfficerModel

def get_officers(db: Session):
    return db.query(OfficerModel).all()

def get_officer(db: Session, officer_id: int):
    return db.query(OfficerModel).filter(
        OfficerModel.OfficerID == officer_id
    ).first()

def create_officer(db: Session, officer_in):
    officer = OfficerModel(**officer_in.dict())
    db.add(officer)
    db.commit()
    db.refresh(officer)
    return officer