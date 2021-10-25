from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///vessel.db", echo=True, future=True)

SessionLocal = sessionmaker(engine)

Base = declarative_base()

