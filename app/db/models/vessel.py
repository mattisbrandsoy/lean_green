from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, String, DateTime, Boolean, func
from ..base_class import Base

class Vessel(Base):
    __tablename__ = "vessels"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean(), default=True)