#app/crud/violation.py
from sqlalchemy.orm import Session
from app.models.violation import Violation as ViolationModel

def get_violations(db: Session):
    return db.query(ViolationModel).all()

def get_violation(db: Session, violation_id: int):
    return db.query(ViolationModel).filter(
        ViolationModel.ViolationsID == violation_id
    ).first()

def create_violation(db: Session, violation_in):
    violation = ViolationModel(**violation_in.dict())
    db.add(violation)
    db.commit()
    db.refresh(violation)
    return violation