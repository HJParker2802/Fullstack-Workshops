# app/models/vehicle.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Vehicle(Base):
    __tablename__ = "tbl_Vehicles"

    VIN = Column(Integer, primary_key=True, index=True)

    VehicleLicense = Column(String(50))
    VehicleState = Column(String(50))
    VehicleColour = Column(String(35))
    VehicleMakeID = Column(Integer, ForeignKey("tbl_VehicleMake.VehicleMakeID"))
    VehicleAddress = Column(String(50))
    VehicleOwner = Column(Integer, ForeignKey("tbl_Person.PersonID"))

    make = relationship("VehicleMake", back_populates="vehicles")
    owner = relationship("Person")