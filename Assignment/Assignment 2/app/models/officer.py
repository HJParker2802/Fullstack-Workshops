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
