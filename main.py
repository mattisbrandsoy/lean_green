from fastapi import FastAPI, status, HTTPException
from database import Base, engine
from sqlalchemy.orm import Session
import models
import schemas


Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/")
def root():
  return "root"

@app.post("/vessel", status_code=status.HTTP_201_CREATED)
def create_vessel(vessel: schemas.Vessel):

  session = Session(bind=engine, expire_on_commit=False)
  vesseldb = models.Vessel(name = vessel.name)
  session.add(vesseldb)
  session.commit()
  id = vesseldb.id
  session.close()

  return f"Created vessel with id : {id}"

@app.get("/vessel/{id}")
def read_vessel(id: int):

  session = Session(bind=engine, expire_on_commit=False)
  vessel = session.query(models.Vessel).get(id)
  session.close()

  if not vessel:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Vessel with id {id} not found")

  return vessel


@app.put("/vessel/{id}")
def update_vessel(id: int, name: str):

  session = Session(bind=engine, expire_on_commit=False)
  vessel = session.query(models.Vessel).get(id)

  if vessel:
    vessel.name = vessel
    session.commit()
  session.close()

  if not vessel:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Vessel with id: {id} not found")
  
  return vessel

@app.delete("/vessel/{id}")
def delete_vessel(id: int):

  session = Session(bind=engine, expire_on_commit=False)
  vessel = session.query(models.Vessel).get(id)

  if vessel:
    session.delete(vessel)
    session.commit()
    session.close()
  else:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Vessel with id: {id} not found")
  
  return None


@app.get("/vessel")
def read_all_vessels():
  
  session = Session(bind=engine, expire_on_commit=False)
  vessel_list = session.query(models.Vessel).all()
  session.close()
  
  return vessel_list