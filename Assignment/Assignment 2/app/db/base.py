#app/db/base.py
from sqlalchemy.orm import declarative_base
Base = declarative_base()

# import models here so relationships can be resolved
from app.models import person
from app.models import drivers_license