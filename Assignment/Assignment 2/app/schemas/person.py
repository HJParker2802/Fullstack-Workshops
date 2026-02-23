#app/schemas/person.py
from pydantic import BaseModel
from typing import Optional

class PersonBase(BaseModel):
    Forename: str
    Surname: str
    Address: str
    State: str
    ZipCode: str
    City: str
    DOB: str
    Height: float
    Weight: float
    EyeColour: str
    PhoneNum: str

class PersonCreate(PersonBase):
    DriversLicenseID: int

class PersonUpdate(BaseModel):
    Forename: Optional[str]
    Surname: Optional[str]
    Address: Optional[str]
    State: Optional[str]
    ZipCode: Optional[str]
    City: Optional[str]
    DOB: Optional[str]
    Height: Optional[float]
    Weight: Optional[float]
    EyeColour: Optional[str]
    PhoneNum: Optional[str]
    DriversLicenseID: Optional[int]



class Person(PersonBase):
    PersonID: int
    DriversLicenseID: int

    class Config:
        orm_mode = True
