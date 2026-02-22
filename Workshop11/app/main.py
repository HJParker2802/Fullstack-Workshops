from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional
from db_raw import test_connection
from db_raw import fetch_all_books
from fastapi import HTTPException
from db_raw import fetch_book_by_id
from db_raw import create_book_in_db
from db_raw import update_book_in_db
from db_raw import delete_book_from_db
# from fastapi import FastAPI
# from app.api import books
from app.db.init_db import init_db
# from app.api import books, users 
from app.api import books, users, reviews 
# from app.db.init_db import init_db


app = FastAPI(title="Bookstore API", version="1.0.0") 
init_db()  # create tables at startup if needed 


app.include_router(books.router) 
app.include_router(users.router) 
app.include_router(reviews.router)


#Register the books router with the main app
app.include_router(books.router)

@app.get("/")
def root():
    """Simple health-check endpoint.""" 
    return {"message": "Week 11 app is running"} 


@app.get("/")
def root():
    return {"This is the standard directory, add /yourroute or /test onto the url to be able to see the name and test directory\n /docs, \db-test"}

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

@app.get("/test/{yourname}")
async def test(yourname):
    return {"your name is": yourname }







# #Books stuff (not using DB)
# class Book(BaseModel):
#     id: int
#     title: str
#     author: str

# class BookCreate(BaseModel):
#     title:str
#     author:str
# class BookUpdate(BaseModel):
#     title: Optional[str] = None
#     author: Optional[str] = None


# books_db = [
#     Book(id=1, title="RESTful Web APIs", author="Leonard R., Amundsen M., and Sam R."),
#     Book(id=2, title="Designing Web APIs", author="Brenda J., Saurabh S., and Amir S."),
#     Book(id=3, title="Test book", author="No one"),
# ]




# @app.get("/books")
# async def get_books():
#     return books_db

# @app.get("/books/{book_id}") 
# async def get_book(book_id: int): 
#     for book in books_db: 
#         if book.id == book_id: 
#             return book 
#     return {"error": "Book not found"}


# @app.post("/books", status_code=201)
# async def create_book(new_book: BookCreate):
#     # Generate a new id
#     next_id = max(book.id for book in books_db) + 1 if books_db else 1
#     book = Book(id=next_id, **new_book.dict())
#     books_db.append(book)
#     return book

# @app.put("/books/{book_id}")
# async def update_book(book_id: int, updated: BookCreate):
#     for index, book in enumerate(books_db):
#         if book.id == book_id:
#             updated_book = Book(id=book_id, **updated.dict())
#             books_db[index] = updated_book
#             return updated_book
#         return {"error": "Book not found"}

# @app.patch("/books/{book_id}")
# async def patch_book(book_id: int, partial: BookUpdate):
#     for index, book in enumerate(books_db):
#         if book.id == book_id:
#             book_data = book.dict()
#             update_data = partial.dict(exclude_unset=True)
#             for key, value in update_data.items():
#                 book_data[key] = value
#             updated_book = Book(**book_data)
#             books_db[index] = updated_book
#             return updated_book
#     return {"error": "Book not found"}

# @app.delete("/books/{book_id}")
# async def delete_book(book_id: int):
#     for index, book in enumerate(books_db):
#         if book.id == book_id:
#             deleted_book = books_db.pop(index)
#             return {"message": "Book deleted", "book": deleted_book}
#     return {"error": "Book not found"}
