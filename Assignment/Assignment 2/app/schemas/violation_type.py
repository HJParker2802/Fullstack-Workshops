#app/schemas/violation_type.py
from pydantic import BaseModel
from typing import Optional

class ViolationTypeBase(BaseModel):
    ViolationName: str
    ViolationClass: str

class ViolationTypeCreate(ViolationTypeBase):
    pass  

class ViolationType(ViolationTypeBase):
    ViolationTypeID: int

    class Config:
        orm_mode = True
