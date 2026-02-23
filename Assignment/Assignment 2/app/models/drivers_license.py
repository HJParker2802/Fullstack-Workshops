# app/models/driverslicense.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class DriversLicense(Base):
    __tablename__ = "tbl_DriversLicense"

    DriversLicenseID = Column(Integer, primary_key=True, index=True)
    LicenseNum = Column(String(20))

    # string reference to Person
    persons = relationship("Person", back_populates="license")