#app/api/drivers_license.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db

router = APIRouter(prefix="/licenses", tags=["Drivers License"])

@router.get("/")
def get_licenses(db: Session = Depends(get_db)):
    return {"message": "List licenses"}

@router.get("/{license_id}")
def get_license(license_id: int, db: Session = Depends(get_db)):
    return {"message": f"Get license {license_id}"}