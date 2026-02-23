#app/api/vehicle_make.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.vehicle_make import VehicleMake, VehicleMakeCreate
from app.crud import vehicle_make as crud
from app.core.deps import get_db

router = APIRouter(prefix="/vehicle-makes", tags=["Vehicle Makes"])


@router.get("/", response_model=List[VehicleMake])
def list_vehicle_makes(db: Session = Depends(get_db)):
    return crud.get_vehicle_makes(db)


@router.get("/{make_id}", response_model=VehicleMake)
def get_vehicle_make(make_id: int, db: Session = Depends(get_db)):
    db_make = crud.get_vehicle_make(db, make_id)
    if not db_make:
        raise HTTPException(status_code=404, detail="Vehicle make not found")
    return db_make


@router.post("/", response_model=VehicleMake)
def create_vehicle_make(make_in: VehicleMakeCreate, db: Session = Depends(get_db)):
    return crud.create_vehicle_make(db, make_in)


@router.put("/{make_id}", response_model=VehicleMake)
def update_vehicle_make(make_id: int, make_in: VehicleMakeCreate, db: Session = Depends(get_db)):
    db_make = crud.get_vehicle_make(db, make_id)
    if not db_make:
        raise HTTPException(status_code=404, detail="Vehicle make not found")
    return crud.update_vehicle_make(db, db_make, make_in)


@router.delete("/{make_id}", response_model=VehicleMake)
def delete_vehicle_make(make_id: int, db: Session = Depends(get_db)):
    db_make = crud.delete_vehicle_make(db, make_id)
    if not db_make:
        raise HTTPException(status_code=404, detail="Vehicle make not found")
    return db_make