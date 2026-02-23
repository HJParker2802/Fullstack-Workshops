# app/models/vehicle_make.py
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base

class VehicleMake(Base):
    __tablename__ = "tbl_VehicleMake"

    VehicleMakeID = Column(Integer, primary_key=True, index=True)
    VehicleName = Column(String(50))
    DriveType = Column(String(3))
    VehicleManual = Column(Boolean)
    VehicleBrand = Column(String(50))
    CarWeight = Column(Integer)
    VehicleYear = Column(Integer)

    vehicles = relationship("Vehicle", back_populates="make")