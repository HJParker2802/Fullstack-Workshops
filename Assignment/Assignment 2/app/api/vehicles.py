#app/api/vehicles.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db

router = APIRouter(prefix="/vehicles", tags=["Vehicles"])

@router.get("/")
def get_vehicles(db: Session = Depends(get_db)):
    return {"message": "List vehicles"}

@router.get("/{vin}")
def get_vehicle(vin: int, db: Session = Depends(get_db)):
    return {"message": f"Get vehicle {vin}"}