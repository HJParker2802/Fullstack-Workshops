#app/api/drivers_license.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.drivers_license import DriversLicense, DriversLicenseCreate
from app.crud import drivers_license as crud
from app.core.deps import get_db

router = APIRouter(prefix="/licenses", tags=["Drivers License"])


@router.get("/", response_model=List[DriversLicense])
def list_licenses(db: Session = Depends(get_db)):
    return crud.get_licenses(db)


@router.get("/{license_id}", response_model=DriversLicense)
def get_license(license_id: int, db: Session = Depends(get_db)):
    db_license = crud.get_license(db, license_id)
    if not db_license:
        raise HTTPException(status_code=404, detail="License not found")
    return db_license


@router.post("/", response_model=DriversLicense)
def create_license(license_in: DriversLicenseCreate, db: Session = Depends(get_db)):
    return crud.create_license(db, license_in)


@router.put("/{license_id}", response_model=DriversLicense)
def update_license(license_id: int, license_in: DriversLicenseCreate, db: Session = Depends(get_db)):
    db_license = crud.get_license(db, license_id)
    if not db_license:
        raise HTTPException(status_code=404, detail="License not found")
    return crud.update_license(db, db_license, license_in)


@router.delete("/{license_id}", response_model=DriversLicense)
def delete_license(license_id: int, db: Session = Depends(get_db)):
    db_license = crud.delete_license(db, license_id)
    if not db_license:
        raise HTTPException(status_code=404, detail="License not found")
    return db_license



#app/api/officers.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.crud import officer as crud
from app.core.deps import get_db
from app.schemas.officer import OfficerOut, OfficerCreate, OfficerUpdate


router = APIRouter(prefix="/officers", tags=["Officers"])


@router.get("/", response_model=List[OfficerOut])
def list_officers(db: Session = Depends(get_db)):
    return crud.get_officers(db)


@router.get("/{officer_id}", response_model=OfficerOut)
def get_officer(officer_id: int, db: Session = Depends(get_db)):
    db_officer = crud.get_officer(db, officer_id)
    if not db_officer:
        raise HTTPException(status_code=404, detail="Officer not found")
    return db_officer


@router.post("/", response_model=OfficerOut)
def create_officer(officer_in: OfficerCreate, db: Session = Depends(get_db)):
    return crud.create_officer(db, officer_in)



@router.put("/{officer_id}", response_model=OfficerOut)
def update_officer(officer_id: int, officer_in: OfficerUpdate, db: Session = Depends(get_db)):
    db_officer = crud.get_officer(db, officer_id)
    if not db_officer:
        raise HTTPException(status_code=404, detail="Officer not found")
    return crud.update_officer(db, db_officer, officer_in)


@router.delete("/{officer_id}", response_model=OfficerOut)
def delete_officer(officer_id: int, db: Session = Depends(get_db)):
    db_officer = crud.delete_officer(db, officer_id)
    if not db_officer:
        raise HTTPException(status_code=404, detail="Officer not found")
    return db_officer




# app/models/person.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Person(Base):
    __tablename__ = "tbl_Person"

    PersonID = Column(Integer, primary_key=True, index=True)
    DriversLicenseID = Column(Integer, ForeignKey("tbl_DriversLicense.DriversLicenseID"))

    Forename = Column(String(50))
    Surname = Column(String(50))
    Address = Column(String(100))
    State = Column(String(100))
    ZipCode = Column(String(5))
    City = Column(String(50))
    DOB = Column(String(10))
    Height = Column(Integer)
    Weight = Column(Integer)
    EyeColour = Column(String(6))
    PhoneNum = Column(String(12))

    # use string reference to avoid circular imports
    license = relationship("DriversLicense", back_populates="persons")
    
    
    
    
    
    # app/models/vehicle_make.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class VehicleMake(Base):
    __tablename__ = "tbl_VehicleMake"

    VehicleMakeID = Column(Integer, primary_key=True)
    VehicleName = Column(String)
    DriveType = Column(String)
    VehicleManual = Column(Integer)  # 0 or 1
    VehicleBrand = Column(String)
    CarWeight = Column(Integer)
    VehicleYear = Column(Integer)
    
    
    
    
    # app/models/vehicle.py
from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class Vehicle(Base):
    __tablename__ = "tbl_Vehicles"

    VIN = Column(String, primary_key=True, index=True)
    VehicleLicense = Column(String)
    VehicleState = Column(String)
    VehicleColour = Column(String)
    VehicleMakeID = Column(Integer)
    VehicleAddress = Column(String)
    VehicleOwner = Column(Integer)  # matches your DB
    
    
    
    
    
    
    
    
    # app/models/violation_type.py
from sqlalchemy import Column, Integer, String
from app.db.base import Base

class ViolationType(Base):
    __tablename__ = "tbl_ViolationTypes"

    ViolationTypeID = Column(Integer, primary_key=True, index=True)
    ViolationName = Column(String(100))
    ViolationClass = Column(String(10))




# app/models/violation.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Violation(Base):
    __tablename__ = "tbl_Violations"

    ViolationsID = Column(Integer, primary_key=True, index=True)

    OfficerID = Column(Integer, ForeignKey("tbl_Officers.OfficerID"))
    ViolationTypeID = Column(Integer, ForeignKey("tbl_ViolationTypes.ViolationTypeID"))
    ViolatorID = Column(Integer, ForeignKey("tbl_Person.PersonID"))

    Location = Column(String(100))
    District = Column(String(100))
    ViolationDate = Column(String(10))
    ViolationTime = Column(String(8))

    officer = relationship("Officer")
    violator = relationship("Person")
    violation_type = relationship("ViolationType")
    
    
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



# app/schemas/vehicle_make.py
from pydantic import BaseModel
from typing import Optional

class VehicleMakeBase(BaseModel):
    VehicleName: str
    DriveType: str
    VehicleManual: bool
    VehicleBrand: str
    CarWeight: int
    VehicleYear: int
    Country: str

class VehicleMakeCreate(VehicleMakeBase):
    pass  # nothing extra needed for creation

class VehicleMake(VehicleMakeBase):
    VehicleMakeID: int

    class Config:
        orm_mode = True




#app/schemas/vehicle.py
from pydantic import BaseModel
from typing import Optional

class VehicleBase(BaseModel):
    VehicleLicense: str
    VehicleState: str
    VehicleColour: str
    VehicleMakeID: int
    VehicleAddress: str
    VehicleOwner: int

from pydantic import BaseModel

from pydantic import BaseModel
from typing import Optional

class VehicleCreate(BaseModel):
    VehicleLicense: str
    VehicleState: str
    VehicleColour: str
    VehicleMakeID: int
    VehicleAddress: str
    VehicleOwner: int  # must match DB
    VIN: Optional[str] = None  # optional if you auto-generate


class VehicleOut(VehicleBase):
    VIN: str
    make: Optional[str]  

    class Config:
        orm_mode = True
        
        
        
        
        
        
        
        
        
        
        
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





#app/main.py
from fastapi import FastAPI

from app.api import person, drivers_license, officers, vehicles, vehicle_make, violations, violation_types

app = FastAPI(
    title="Traffic Violations API",
    description="Full Stack Development Assignment 2 - Harry Parker",
    version="1.0.0"
)


app.include_router(person.router)
app.include_router(drivers_license.router)
app.include_router(officers.router)
app.include_router(vehicles.router)
app.include_router(vehicle_make.router)
app.include_router(violations.router)
app.include_router(violation_types.router)




