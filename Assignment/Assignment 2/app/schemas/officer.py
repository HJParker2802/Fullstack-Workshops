#app/schemas/officer.py
from pydantic import BaseModel
from typing import Optional

from app.schemas.person import PersonBase

class OfficerBase(BaseModel):
    personID: int
    ViolationsRecorded: Optional[int]

class OfficerCreate(OfficerBase):
    pass  

class OfficerOut(OfficerBase):
    OfficerID: int
    person: PersonBase

    class Config:
        orm_mode = True
