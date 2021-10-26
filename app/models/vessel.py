from sqlalchemy import Column, Integer, String
from app.database import Base


class Vessel(Base):
    __tablename__ = "vessels"
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
