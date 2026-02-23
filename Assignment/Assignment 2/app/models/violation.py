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