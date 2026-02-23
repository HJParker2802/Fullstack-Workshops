#app/schemas/violation.py
from pydantic import BaseModel
from typing import Optional

class ViolationBase(BaseModel):
    OfficerID: int
    ViolationTypeID: int
    Location: str
    District: str
    ViolationDate: str
    ViolationTime: str
    ViolatorID: int

class ViolationCreate(ViolationBase):
    pass

class ViolationOut(ViolationBase):
    ViolationsID: int

    class Config:
        orm_mode = True