# app/db/init_db.py 
from app.db.base import Base 
from app.db.session import engine 
from app.models.book import Book  # noqa 
from app.models.user import User  # noqa 
from app.models.review import Review  # noqa 

def init_db(): 
    Base.metadata.create_all(bind=engine)