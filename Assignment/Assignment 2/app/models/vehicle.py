# app/models/vehicle.py
from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Vehicle(Base):
    __tablename__ = "tbl_Vehicles"

    VIN = Column(Integer, primary_key=True, autoincrement=True, index=True) 
    VehicleLicense = Column(String)
    VehicleState = Column(String)
    VehicleColour = Column(String)
    VehicleMakeID = Column(Integer)
    VehicleAddress = Column(String)
    VehicleOwner = Column(Integer)