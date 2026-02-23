# app/models/driverslicense.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class DriversLicense(Base):
    __tablename__ = "tbl_DriversLicense"

    DriversLicenseID = Column(Integer, primary_key=True, index=True)
    LicenseNum = Column(String(20))

    # string reference to Person
    persons = relationship("Person", back_populates="license")





# app/models/officer.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Officer(Base):
    __tablename__ = "tbl_Officers"

    OfficerID = Column(Integer, primary_key=True, index=True)
    PersonID = Column(Integer, ForeignKey("tbl_Person.PersonID"))
    ViolationsRecorded = Column(Integer)

    person = relationship("Person")





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
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base

class VehicleMake(Base):
    __tablename__ = "tbl_VehicleMake"

    VehicleMakeID = Column(Integer, primary_key=True, index=True)
    VehicleName = Column(String(50))
    DriveType = Column(String(3))
    VehicleManual = Column(Boolean)
    VehicleBrand = Column(String(50))
    CarWeight = Column(Integer)
    VehicleYear = Column(Integer)

    vehicles = relationship("Vehicle", back_populates="make")



# app/models/vehicle.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Vehicle(Base):
    __tablename__ = "tbl_Vehicles"

    VIN = Column(Integer, primary_key=True, index=True)

    VehicleLicense = Column(String(50))
    VehicleState = Column(String(50))
    VehicleColour = Column(String(35))
    VehicleMakeID = Column(Integer, ForeignKey("tbl_VehicleMake.VehicleMakeID"))
    VehicleAddress = Column(String(50))
    VehicleOwner = Column(Integer, ForeignKey("tbl_Person.PersonID"))

    make = relationship("VehicleMake", back_populates="vehicles")
    owner = relationship("Person")




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

class DriversLicenseBase(BaseModel):
    Origin: str

class DriversLicenseCreate(DriversLicenseBase):
    pass

class DriversLicense(DriversLicenseBase):
    DriversLicenseID: int

    class Config:
        orm_mode = True




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

from app.schemas.person import PersonBase

class VehicleBase(BaseModel):
    VehicleLicense: str
    VehicleState: str
    VehicleColour: str
    VehicleMakeID: int 
    VehicleAddress: str
    VehicleOwnerID: int  

class VehicleCreate(VehicleBase):
    DriversLicenseID: Optional[int]

class VehicleOut(VehicleBase):
    VIN: int # Vehicle ID is VIN
    owner: PersonBase  

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




#app/db/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:SEPS@127.0.0.1:3306/FullstackDevelopment_Assignment1"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)



# app/db/init_db.py
from app.db.base import Base
from app.db.session import engine

# import all models here
from app.models.person import Person  # noqa
from app.models.drivers_license import DriversLicense  # noqa

def init_db():
    Base.metadata.create_all(bind=engine)




#app/db/base.py
from sqlalchemy.orm import declarative_base
Base = declarative_base()

# import models here so relationships can be resolved
from app.models import person
from app.models import drivers_license




#app/crud/violation.py
from sqlalchemy.orm import Session
from app.models.violation import Violation as ViolationModel

def get_violations(db: Session):
    return db.query(ViolationModel).all()

def get_violation(db: Session, violation_id: int):
    return db.query(ViolationModel).filter(
        ViolationModel.ViolationsID == violation_id
    ).first()

def create_violation(db: Session, violation_in):
    violation = ViolationModel(**violation_in.dict())
    db.add(violation)
    db.commit()
    db.refresh(violation)
    return violation




#app/crud/violation_type.py
from sqlalchemy.orm import Session
from app.models.violation_type import ViolationType as ViolationTypeModel

def get_violation_types(db: Session):
    return db.query(ViolationTypeModel).all()

def get_violation_type(db: Session, violation_type_id: int):
    return db.query(ViolationTypeModel).filter(
        ViolationTypeModel.ViolationTypeID == violation_type_id
    ).first()

def create_violation_type(db: Session, violation_type_in):
    violation_type = ViolationTypeModel(**violation_type_in.dict())
    db.add(violation_type)
    db.commit()
    db.refresh(violation_type)
    return violation_type




#app/crud/vehicle.py
from sqlalchemy.orm import Session
from app.models.vehicle import Vehicle as VehicleModel

def get_vehicles(db: Session):
    return db.query(VehicleModel).all()

def get_vehicle(db: Session, vin: int):
    return db.query(VehicleModel).filter(
        VehicleModel.VIN == vin
    ).first()

def create_vehicle(db: Session, vehicle_in):
    vehicle = VehicleModel(**vehicle_in.dict())
    db.add(vehicle)
    db.commit()
    db.refresh(vehicle)
    return vehicle





#app/crud/vehicle_make.py
from sqlalchemy.orm import Session
from app.models.vehicle_make import VehicleMake as VehicleMakeModel

def get_vehicle_makes(db: Session):
    return db.query(VehicleMakeModel).all()

def get_vehicle_make(db: Session, make_id: int):
    return db.query(VehicleMakeModel).filter(
        VehicleMakeModel.VehicleMakeID == make_id
    ).first()

def create_vehicle_make(db: Session, make_in):
    make = VehicleMakeModel(**make_in.dict())
    db.add(make)
    db.commit()
    db.refresh(make)
    return make




#app/crud/person.py
from sqlalchemy.orm import Session
from app.models.person import Person as PersonModel


def get_persons(db: Session):
    return db.query(PersonModel).all()

def get_person(db: Session, person_id: int):
    return db.query(PersonModel).filter(
        PersonModel.PersonID == person_id
    ).first()

def create_person(db: Session, person_in):
    person = PersonModel(**person_in.dict())
    db.add(person)
    db.commit()
    db.refresh(person)
    return person



def delete_person(db: Session, person_id: int):
    person = db.query(PersonModel).filter(PersonModel.PersonID == person_id).first()
    if not person:
        return None
    db.delete(person)
    db.commit()
    return person





#app/crud/officer.py
from sqlalchemy.orm import Session
from app.models.officer import Officer as OfficerModel

def get_officers(db: Session):
    return db.query(OfficerModel).all()

def get_officer(db: Session, officer_id: int):
    return db.query(OfficerModel).filter(
        OfficerModel.OfficerID == officer_id
    ).first()

def create_officer(db: Session, officer_in):
    officer = OfficerModel(**officer_in.dict())
    db.add(officer)
    db.commit()
    db.refresh(officer)
    return officer





#app/crud/drivers_license.py
from sqlalchemy.orm import Session
from app.models.drivers_license import DriversLicense as DriversLicenseModel

def get_licenses(db: Session):
    return db.query(DriversLicenseModel).all()

def get_license(db: Session, license_id: int):
    return db.query(DriversLicenseModel).filter(
        DriversLicenseModel.DriversLicenseID == license_id
    ).first()

def create_license(db: Session, license_in):
    license = DriversLicenseModel(**license_in.dict())
    db.add(license)
    db.commit()
    db.refresh(license)
    return license



#app/core/deps.py
from sqlalchemy.orm import Session
from app.db.session import SessionLocal

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()



#app/api/violations.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db

router = APIRouter(prefix="/violations", tags=["Violations"])

@router.get("/")
def get_violations(db: Session = Depends(get_db)):
    return {"message": "List violations"}

@router.get("/{violation_id}")
def get_violation(violation_id: int, db: Session = Depends(get_db)):
    return {"message": f"Get violation {violation_id}"}




#app/api/violation_types.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db

router = APIRouter(prefix="/violation-types", tags=["Violation Types"])

@router.get("/")
def get_violation_types(db: Session = Depends(get_db)):
    return {"message": "List violation types"}

@router.get("/{type_id}")
def get_violation_type(type_id: int, db: Session = Depends(get_db)):
    return {"message": f"Get violation type {type_id}"}




#app/api/vehicles.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db

router = APIRouter(prefix="/vehicles", tags=["Vehicles"])

@router.get("/")
def get_vehicles(db: Session = Depends(get_db)):
    return {"message": "List vehicles"}

@router.get("/{vin}")
def get_vehicle(vin: int, db: Session = Depends(get_db)):
    return {"message": f"Get vehicle {vin}"}





#app/api/vehicle_make.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db

router = APIRouter(prefix="/vehicle-makes", tags=["Vehicle Makes"])

@router.get("/")
def get_vehicle_makes(db: Session = Depends(get_db)):
    return {"message": "List vehicle makes"}

@router.get("/{make_id}")
def get_vehicle_make(make_id: int, db: Session = Depends(get_db)):
    return {"message": f"Get vehicle make {make_id}"}



# app/api/person.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.person import Person, PersonCreate
from app.crud import person as crud_person
from app.core.deps import get_db

router = APIRouter(prefix="/persons", tags=["Persons"])

# GET /persons/ - list all persons
@router.get("/", response_model=List[Person])
def get_persons(db: Session = Depends(get_db)):
    return crud_person.get_persons(db)


# GET /persons/{person_id} - get a single person
@router.get("/{person_id}", response_model=Person)
def get_person(person_id: int, db: Session = Depends(get_db)):
    db_person = crud_person.get_person(db, person_id)
    if not db_person:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person


# POST /persons/ - create a new person
@router.post("/", response_model=Person)
def create_person(person_in: PersonCreate, db: Session = Depends(get_db)):
    return crud_person.create_person(db, person_in)


@router.delete("/{person_id}", response_model=Person)   
def delete_person(person_id: int, db: Session = Depends(get_db)):
    deleted_person = crud_person.delete_person(db, person_id)
    if not deleted_person:
        raise HTTPException(status_code=404, detail="Person not found")
    return deleted_person




#app/api/officers.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db

router = APIRouter(prefix="/officers", tags=["Officers"])

@router.get("/")
def get_officers(db: Session = Depends(get_db)):
    return {"message": "List officers"}

@router.get("/{officer_id}")
def get_officer(officer_id: int, db: Session = Depends(get_db)):
    return {"message": f"Get officer {officer_id}"}




#app/api/drivers_license.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db

router = APIRouter(prefix="/licenses", tags=["Drivers License"])

@router.get("/")
def get_licenses(db: Session = Depends(get_db)):
    return {"message": "List licenses"}

@router.get("/{license_id}")
def get_license(license_id: int, db: Session = Depends(get_db)):
    return {"message": f"Get license {license_id}"}





