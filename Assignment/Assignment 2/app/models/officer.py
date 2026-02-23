# app/models/officer.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Officer(Base):
    __tablename__ = "tbl_Officers"

    OfficerID = Column(Integer, primary_key=True, index=True)
    personID = Column(Integer, ForeignKey("tbl_Person.PersonID"), nullable=False)
    ViolationsRecorded = Column(Integer, default=0)