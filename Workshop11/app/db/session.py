#app/db/session.py
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, Session 
SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:SEPS@localhost:3306/bookstore"

engine = create_engine( 
                       SQLALCHEMY_DATABASE_URL, 
                       pool_pre_ping=True, 
                       )  
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
def get_db(): 
    """Dependency that provides a database session to FastAPI endpoints.""" 
    db: Session = SessionLocal() 
    try: 
        yield db 
    finally: 
        db.close() 