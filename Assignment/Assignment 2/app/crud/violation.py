#app/crud/violation.py
from sqlalchemy.orm import Session
from app.models.violation import Violation
from app.schemas.violation import ViolationCreate

def get_violations(db: Session):
    return db.query(Violation).all()

def get_violation(db: Session, violation_id: int):
    return db.query(Violation).filter(Violation.ViolationsID == violation_id).first()

def create_violation(db: Session, violation_in: ViolationCreate):
    db_violation = Violation(**violation_in.dict())
    db.add(db_violation)
    db.commit()
    db.refresh(db_violation)
    return db_violation

def update_violation(db: Session, violation_id: int, violation_in: ViolationCreate):
    db_violation = get_violation(db, violation_id)
    if not db_violation:
        return None
    for key, value in violation_in.dict().items():
        setattr(db_violation, key, value)
    db.commit()
    db.refresh(db_violation)
    return db_violation

def delete_violation(db: Session, violation_id: int):
    db_violation = get_violation(db, violation_id)
    if not db_violation:
        return None
    db.delete(db_violation)
    db.commit()
    return db_violation