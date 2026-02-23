#app/schemas/violation_type.py
from pydantic import BaseModel

class ViolationTypeBase(BaseModel):
    ViolationName: str
    ViolationClass: str

class ViolationTypeCreate(ViolationTypeBase):
    pass

class ViolationTypeOut(ViolationTypeBase):
    ViolationTypeID: int

    class Config:
        orm_mode = True