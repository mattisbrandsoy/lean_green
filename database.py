from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///vessel.db")

Base = declarative_base()

