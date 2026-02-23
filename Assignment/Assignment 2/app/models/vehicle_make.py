# app/models/vehicle_make.py
from sqlalchemy import Column, Integer, String
from app.db.base import Base

class VehicleMake(Base):
    __tablename__ = "tbl_VehicleMake"

    VehicleMakeID = Column(Integer, primary_key=True)
    VehicleName = Column(String)
    DriveType = Column(String)
    VehicleManual = Column(Integer)  # 0 or 1
    VehicleBrand = Column(String)
    CarWeight = Column(Integer)
    VehicleYear = Column(Integer)