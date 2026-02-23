#app/api/drivers_license.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.drivers_license import DriversLicense, DriversLicenseCreate
from app.crud import drivers_license as crud
from app.core.deps import get_db

router = APIRouter(prefix="/licenses", tags=["Drivers License"])


@router.get("/", response_model=List[DriversLicense])
def list_licenses(db: Session = Depends(get_db)):
    return crud.get_licenses(db)


@router.get("/{license_id}", response_model=DriversLicense)
def get_license(license_id: int, db: Session = Depends(get_db)):
    db_license = crud.get_license(db, license_id)
    if not db_license:
        raise HTTPException(status_code=404, detail="License not found")
    return db_license


@router.post("/", response_model=DriversLicense)
def create_license(license_in: DriversLicenseCreate, db: Session = Depends(get_db)):
    return crud.create_license(db, license_in)


@router.put("/{license_id}", response_model=DriversLicense)
def update_license(license_id: int, license_in: DriversLicenseCreate, db: Session = Depends(get_db)):
    db_license = crud.get_license(db, license_id)
    if not db_license:
        raise HTTPException(status_code=404, detail="License not found")
    return crud.update_license(db, db_license, license_in)


@router.delete("/{license_id}", response_model=DriversLicense)
def delete_license(license_id: int, db: Session = Depends(get_db)):
    db_license = crud.delete_license(db, license_id)
    if not db_license:
        raise HTTPException(status_code=404, detail="License not found")
    return db_license