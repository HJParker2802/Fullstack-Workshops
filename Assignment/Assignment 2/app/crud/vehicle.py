#app/crud/vehicle.py
from sqlalchemy.orm import Session
from app.models.vehicle import Vehicle as VehicleModel

def get_vehicles(db: Session):
    return db.query(VehicleModel).all()

def get_vehicle(db: Session, vin: int):
    return db.query(VehicleModel).filter(
        VehicleModel.VIN == vin
    ).first()

def create_vehicle(db: Session, vehicle_in):
    vehicle = VehicleModel(**vehicle_in.dict())
    db.add(vehicle)
    db.commit()
    db.refresh(vehicle)
    return vehicle