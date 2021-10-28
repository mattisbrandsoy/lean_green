from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class VesselBase(BaseModel):
    name: str
    date_created: Optional[datetime] = None
    is_active: bool

class VesselCreate(VesselBase):
    pass

class Vessel(VesselBase):
    id: int
    class Config:
        orm_mode = True
