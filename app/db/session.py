from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

from app.core.config import settings

# # CONNECT TO PG DB
# SQLALCHEMY_DATABASE_URI = settings.DATABASE_URI
# engine = create_engine(SQLALCHEMY_DATABASE_URI)

# CONNECT TO SQLITE
SQLALCHEMY_DATABASE_URI = "sqlite:///./app/db.sqlite3"
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True, future=True, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db() -> Generator:
  try:
    db = SessionLocal()
    yield db
  finally:
    db.close()