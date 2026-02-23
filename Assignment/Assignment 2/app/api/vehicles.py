#app/api/vehicles.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import uuid
from app.models.vehicle import Vehicle
from app.schemas.vehicle import VehicleCreate, VehicleOut
from app.crud import vehicle as crud
from app.core.deps import get_db

router = APIRouter(prefix="/vehicles", tags=["Vehicles"])

# List all vehicles
@router.get("/", response_model=List[VehicleOut])
def list_vehicles(db: Session = Depends(get_db)):
    return crud.get_vehicles(db)

# Get vehicle by VIN (str)
@router.get("/{vin}", response_model=VehicleOut)
def get_vehicle(vin: str, db: Session = Depends(get_db)):
    db_vehicle = crud.get_vehicle(db, vin)
    if not db_vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return db_vehicle

@router.post("/", response_model=VehicleOut)
def create_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    # Ensure VIN is generated if not provided

    db_vehicle = Vehicle(
        VehicleLicense=vehicle.VehicleLicense,
        VehicleState=vehicle.VehicleState,
        VehicleColour=vehicle.VehicleColour,
        VehicleMakeID=vehicle.VehicleMakeID,
        VehicleAddress=vehicle.VehicleAddress,
        VehicleOwner=vehicle.VehicleOwner,
    )
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle


# Update vehicle by VIN
@router.put("/{vin}", response_model=VehicleOut)
def update_vehicle(vin: str, vehicle_in: VehicleCreate, db: Session = Depends(get_db)):
    db_vehicle = crud.get_vehicle(db, vin)
    if not db_vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    for field, value in vehicle_in.dict(exclude_unset=True).items():
        setattr(db_vehicle, field, value)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

# Delete vehicle by VIN
@router.delete("/{vin}", response_model=VehicleOut)
def delete_vehicle(vin: str, db: Session = Depends(get_db)):
    db_vehicle = crud.get_vehicle(db, vin)
    if not db_vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    db.delete(db_vehicle)
    db.commit()
    return db_vehicle