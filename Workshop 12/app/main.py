# app/main.py 
#$env:SECRET_KEY="week12-demo-secret-key" 
from fastapi import FastAPI 
from app.api import auth, books, users, reviews
from app.db.init_db import init_db 

app = FastAPI(title="Bookstore API (Week 12)", version="1.0.0")


init_db() 

app.include_router(auth.router)

app.include_router(books.router)

app.include_router(users.router)

app.include_router(reviews.router)

@app.get("/")
def root():
    return {"message": "Bookstore API is running"}