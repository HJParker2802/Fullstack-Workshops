#app/schemas/drivers_license.py
from pydantic import BaseModel

from pydantic import BaseModel

class DriversLicenseBase(BaseModel):
    DriversLicenseOrigin: str

class DriversLicenseCreate(BaseModel):
    DriversLicenseID: int
    DriversLicenseOrigin: str
    
class DriversLicense(DriversLicenseBase):
    DriversLicenseID: int

    class Config:
        orm_mode = True