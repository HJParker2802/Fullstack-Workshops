#app/schemas/violation.py
from pydantic import BaseModel
from typing import Optional
 
from app.schemas.person import PersonBase
from app.schemas.officer import OfficerBase
from app.schemas.violation_type import ViolationTypeBase

class ViolationBase(BaseModel):
    ViolationDate: str
    ViolationTime: str
    PersonID: int          
    OfficerID: int         
    ViolationTypeID: int   
    Notes: Optional[str] = None

class ViolationCreate(ViolationBase):
    pass  

class ViolationOut(ViolationBase):
    ViolationID: int
    person: PersonBase            
    officer: OfficerBase          
    violation_type: ViolationTypeBase  

    class Config:
        orm_mode = True
