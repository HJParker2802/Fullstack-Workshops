# app/db/init_db.py
from app.db.base import Base
from app.db.session import engine

# import all models here
from app.models.person import Person  # noqa
from app.models.drivers_license import DriversLicense  # noqa

def init_db():
    Base.metadata.create_all(bind=engine)