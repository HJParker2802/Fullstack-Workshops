#app/crud/drivers_license.py
from sqlalchemy.orm import Session
from app.models.drivers_license import DriversLicense as DriversLicenseModel

def get_licenses(db: Session):
    return db.query(DriversLicenseModel).all()

def get_license(db: Session, license_id: int):
    return db.query(DriversLicenseModel).filter(
        DriversLicenseModel.DriversLicenseID == license_id
    ).first()

def create_license(db: Session, license_in):
    license = DriversLicenseModel(**license_in.dict())
    db.add(license)
    db.commit()
    db.refresh(license)
    return license