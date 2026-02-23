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