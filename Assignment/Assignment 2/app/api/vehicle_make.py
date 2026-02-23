#app/api/vehicle_make.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db

router = APIRouter(prefix="/vehicle-makes", tags=["Vehicle Makes"])

@router.get("/")
def get_vehicle_makes(db: Session = Depends(get_db)):
    return {"message": "List vehicle makes"}

@router.get("/{make_id}")
def get_vehicle_make(make_id: int, db: Session = Depends(get_db)):
    return {"message": f"Get vehicle make {make_id}"}