#app/db/base.py
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import ALL models so SQLAlchemy registers them
from app.models.person import Person
from app.models.officer import Officer
from app.models.vehicle import Vehicle
from app.models.vehicle_make import VehicleMake
from app.models.violation import Violation
from app.models.violation_type import ViolationType
from app.models.drivers_license import DriversLicense