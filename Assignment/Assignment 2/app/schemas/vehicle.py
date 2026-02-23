#app/schemas/vehicle.py
from pydantic import BaseModel
from typing import Optional

from app.schemas.person import PersonBase

class VehicleBase(BaseModel):
    VehicleLicense: str
    VehicleState: str
    VehicleColour: str
    VehicleMakeID: int 
    VehicleAddress: str
    VehicleOwnerID: int  

class VehicleCreate(VehicleBase):
    DriversLicenseID: Optional[int]

class VehicleOut(VehicleBase):
    VIN: int # Vehicle ID is VIN
    owner: PersonBase  

    class Config:
        orm_mode = True
