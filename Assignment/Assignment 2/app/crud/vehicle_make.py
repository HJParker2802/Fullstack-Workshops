#app/crud/vehicle_make.py
from sqlalchemy.orm import Session
from app.models.vehicle_make import VehicleMake as VehicleMakeModel

def get_vehicle_makes(db: Session):
    return db.query(VehicleMakeModel).all()

def get_vehicle_make(db: Session, make_id: int):
    return db.query(VehicleMakeModel).filter(
        VehicleMakeModel.VehicleMakeID == make_id
    ).first()

def create_vehicle_make(db: Session, make_in):
    make = VehicleMakeModel(**make_in.dict())
    db.add(make)
    db.commit()
    db.refresh(make)
    return make

def update_vehicle_make(db: Session, db_make, make_in):
    update_data = make_in.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_make, field, value)

    db.commit()
    db.refresh(db_make)
    return db_make


def delete_vehicle_make(db: Session, make_id: int):
    make = db.query(VehicleMakeModel).filter(
        VehicleMakeModel.VehicleMakeID == make_id
    ).first()

    if not make:
        return None

    db.delete(make)
    db.commit()
    return make