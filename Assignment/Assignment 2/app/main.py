#app/main.py
from fastapi import FastAPI

from app.api import person, drivers_license, officers, vehicles, vehicle_make, violations, violation_types

app = FastAPI(
    title="Traffic Violations API",
    description="Full Stack Development Assignment 2 - Harry Parker",
    version="1.0.0"
)

@app.get("/", )
def root_message():
    return "Traffic Violations API   Visit /docs to see the API documentation           This was written by Harry Parker for Fullstack Development Assignment 2."

app.include_router(person.router)
app.include_router(drivers_license.router)
app.include_router(officers.router)
app.include_router(vehicles.router)
app.include_router(vehicle_make.router)
app.include_router(violations.router)
app.include_router(violation_types.router)