#app/crud/violation_type.py
from sqlalchemy.orm import Session
from app.models.violation_type import ViolationType
from app.schemas.violation_type import ViolationTypeCreate

def get_violation_types(db: Session):
    return db.query(ViolationType).all()

def get_violation_type(db: Session, violation_type_id: int):
    return db.query(ViolationType).filter(ViolationType.ViolationTypeID == violation_type_id).first()

def create_violation_type(db: Session, violation_type_in: ViolationTypeCreate):
    db_type = ViolationType(**violation_type_in.dict())
    db.add(db_type)
    db.commit()
    db.refresh(db_type)
    return db_type

def update_violation_type(db: Session, violation_type_id: int, violation_type_in: ViolationTypeCreate):
    db_type = get_violation_type(db, violation_type_id)
    if not db_type:
        return None
    for key, value in violation_type_in.dict().items():
        setattr(db_type, key, value)
    db.commit()
    db.refresh(db_type)
    return db_type

def delete_violation_type(db: Session, violation_type_id: int):
    db_type = get_violation_type(db, violation_type_id)
    if not db_type:
        return None
    db.delete(db_type)
    db.commit()
    return db_type