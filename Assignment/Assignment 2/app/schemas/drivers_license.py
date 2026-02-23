#app/schemas/drivers_license.py
from pydantic import BaseModel

class DriversLicenseBase(BaseModel):
    Origin: str

class DriversLicenseCreate(DriversLicenseBase):
    pass

class DriversLicense(DriversLicenseBase):
    DriversLicenseID: int

    class Config:
        orm_mode = True
