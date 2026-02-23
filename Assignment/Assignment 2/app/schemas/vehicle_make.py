# app/schemas/vehicle_make.py
from pydantic import BaseModel
from typing import Optional

class VehicleMakeBase(BaseModel):
    VehicleName: str
    DriveType: str
    VehicleManual: bool
    VehicleBrand: str
    CarWeight: int
    VehicleYear: int
    Country: str

class VehicleMakeCreate(VehicleMakeBase):
    pass  # nothing extra needed for creation

class VehicleMake(VehicleMakeBase):
    VehicleMakeID: int

    class Config:
        orm_mode = True
