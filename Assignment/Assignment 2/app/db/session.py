from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.deps import get_db

SQLALCHEMY_DATABASE_URL = "mysql+mysqlclient://root:SEPS@127.0.0.1:3306/FullstackDevelopment_Assignment1"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)