from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional
from db_raw import test_connection
from app.db.init_db import init_db
from app.api import books, users, reviews 

app = FastAPI(title="Bookstore API", version="1.0.0") 
init_db()  # create tables at startup if needed 


app.include_router(books.router) 
app.include_router(users.router) 
app.include_router(reviews.router)


#Register the books router with the main app
app.include_router(books.router)

@app.get("/")
def root():
    return {"This is the standard directory, add /yourroute or /test onto the url to be able to see the name and test directory\n For example, add /test/yourname to the url to see your name in the response."}

@app.get("/db-test")
async def db_test():
    print("DB test route called")  

    try:
        count = test_connection()
        print("DB returned:", count)
        return {"book_count": count}

    except Exception as e:
        print("DB ERROR:", repr(e))
        return {"error": str(e)}

@app.get("/test")
async def test():
    return {"You need to add / and whatever your name is"}

@app.get("/test2/{yourname}")
async def test2(yourname):
    return {"your name is": yourname }
