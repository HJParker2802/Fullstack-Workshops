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

def update_vehicle(db: Session, db_vehicle, vehicle_in):
    update_data = vehicle_in.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_vehicle, field, value)

    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle


def delete_vehicle(db: Session, vin: int):
    vehicle = db.query(VehicleModel).filter(
        VehicleModel.VIN == vin
    ).first()

    if not vehicle:
        return None

    db.delete(vehicle)
    db.commit()
    return vehicle