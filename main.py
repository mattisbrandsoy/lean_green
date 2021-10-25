from typing import List
from fastapi import FastAPI, status, HTTPException, Depends
from database import Base, SessionLocal, engine
from sqlalchemy.orm import Session
import models
import schemas

Base.metadata.create_all(engine)

app = FastAPI()

def get_session():
  session = SessionLocal()
  try:
    yield session
  finally:
    session.close()

@app.get("/")
def root():
  return "I am root"



@app.post("/vessel", response_model=schemas.Vessel, status_code=status.HTTP_201_CREATED)
def create_vessel(vessel: schemas.VesselCreate, session: Session = Depends(get_session)):

  vesseldb = models.Vessel(name = vessel.name)
  
  session.add(vesseldb)
  session.commit()
  session.refresh(vesseldb)

  return vesseldb



@app.get("/vessel/{id}", response_model=schemas.Vessel)
def read_vessel(id: int, session: Session = Depends(get_session)):

  vessel = session.query(models.Vessel).get(id)
  
  if not vessel:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Vessel with id {id} not found")

  return vessel



@app.put("/vessel/{id}", response_model=schemas.Vessel)
def update_vessel(id: int, name: str, session: Session = Depends(get_session)):

  vessel = session.query(models.Vessel).get(id)

  if vessel:
    vessel.name = name
    session.commit()
  
  if not vessel:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Vessel with id: {id} not found")
  
  return vessel




@app.delete("/vessel/{id}")
def delete_vessel(id: int, session: Session = Depends(get_session)):

  vessel = session.query(models.Vessel).get(id)

  if vessel:
    session.delete(vessel)
    session.commit()
  else:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Vessel with id: {id} not found")
  
  return None




@app.get("/vessel", response_model = List[schemas.Vessel])
def read_vessel_list(session: Session = Depends(get_session)):
  
  vessel_list = session.query(models.Vessel).all()
  
  return vessel_list