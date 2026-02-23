#app/main.py
from fastapi import FastAPI

from app.api import person
from app.api import officers
from app.api import vehicles
from app.api import violations
from app.api import violation_types
from app.api import drivers_license

app = FastAPI(
    title="Traffic Violations API",
    description="Full Stack Development Assignment 2 - Harry Parker",
    version="1.0.0"
)

app.include_router(person.router)
app.include_router(officers.router)
app.include_router(vehicles.router)
app.include_router(violations.router)
app.include_router(violation_types.router)
app.include_router(drivers_license.router)