# app/models/violation_type.py
from sqlalchemy import Column, Integer, String
from app.db.base import Base

class ViolationType(Base):
    __tablename__ = "tbl_ViolationTypes"

    ViolationTypeID = Column(Integer, primary_key=True, index=True)
    ViolationName = Column(String(100))
    ViolationClass = Column(String(10))