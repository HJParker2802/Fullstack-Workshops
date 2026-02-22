#app/db/init+db.py

from app.db.base import Base 
from app.db.session import engine 
from app.models.review import Review  # noqa: F401
from app.models.user import User  # noqa: F401
from app.models.book import Book  # noqa: F401

# Import models so SQLAlchemy knows about them. 
from app.models.book import Book  # noqa: F401 
def init_db(): 
    """Create tables in the database if they do not already exist.""" 
    Base.metadata.create_all(bind=engine) 
