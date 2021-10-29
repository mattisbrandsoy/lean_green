from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class VesselBase(BaseModel):
    name: str
    created_at: datetime
    updated_at: datetime
    is_active: bool

class VesselCreate(VesselBase):
    pass

class Vessel(VesselBase):
    id: int
    class Config:
        orm_mode = True
