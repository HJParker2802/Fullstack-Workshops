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

class Person(PersonBase):
    PersonID: int
    DriversLicenseID: int

    class Config:
        orm_mode = True
