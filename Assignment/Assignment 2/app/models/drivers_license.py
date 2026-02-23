# app/models/drivers_license.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class DriversLicense(Base):
    __tablename__ = "tbl_DriversLicense"

    DriversLicenseID = Column(Integer, primary_key=True, index=True)
    DriversLicenseOrigin = Column(String(50))

    persons = relationship("Person", back_populates="license")
