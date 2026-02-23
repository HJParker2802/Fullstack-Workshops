# app/models/person.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Person(Base):
    __tablename__ = "tbl_Person"

    PersonID = Column(Integer, primary_key=True, index=True)
    DriversLicenseID = Column(Integer, ForeignKey("tbl_DriversLicense.DriversLicenseID"))

    Forename = Column(String(50))
    Surname = Column(String(50))
    Address = Column(String(100))
    State = Column(String(100))
    ZipCode = Column(String(5))
    City = Column(String(50))
    DOB = Column(String(10))
    Height = Column(String(5))      # MUST be String
    Weight = Column(String(5))      # MUST be String
    EyeColour = Column(String(6))
    PhoneNum = Column(String(12))

    license = relationship("DriversLicense", back_populates="persons")
