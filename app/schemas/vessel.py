from pydantic import BaseModel


class VesselCreate(BaseModel):
    name: str


class Vessel(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
