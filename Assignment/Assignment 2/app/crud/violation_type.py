#app/crud/violation_type.py
from sqlalchemy.orm import Session
from app.models.violation_type import ViolationType as ViolationTypeModel

def get_violation_types(db: Session):
    return db.query(ViolationTypeModel).all()

def get_violation_type(db: Session, violation_type_id: int):
    return db.query(ViolationTypeModel).filter(
        ViolationTypeModel.ViolationTypeID == violation_type_id
    ).first()

def create_violation_type(db: Session, violation_type_in):
    violation_type = ViolationTypeModel(**violation_type_in.dict())
    db.add(violation_type)
    db.commit()
    db.refresh(violation_type)
    return violation_type