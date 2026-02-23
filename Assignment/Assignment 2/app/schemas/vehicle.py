# app/schemas/vehicle.py
from pydantic import BaseModel
from typing import Optional

class VehicleBase(BaseModel):
    VehicleLicense: str
    VehicleState: str
    VehicleColour: str
    VehicleMakeID: int
    VehicleAddress: str
    VehicleOwner: int

class VehicleCreate(VehicleBase):
    pass  

class VehicleOut(VehicleBase):
    VIN: int

    class Config:
        orm_mode = True