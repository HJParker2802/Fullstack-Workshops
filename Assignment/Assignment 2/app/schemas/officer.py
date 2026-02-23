# app/schemas/officer.py
from pydantic import BaseModel
from typing import Optional

class OfficerBase(BaseModel):
    personID: int
    ViolationsRecorded: Optional[int] = 0

class OfficerCreate(OfficerBase):
    pass  

class OfficerUpdate(BaseModel):
    ViolationsRecorded: Optional[int] = None

class OfficerOut(OfficerBase):
    OfficerID: int

    class Config:
        orm_mode = True