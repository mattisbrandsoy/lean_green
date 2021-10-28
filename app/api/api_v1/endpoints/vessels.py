from typing import List

from fastapi import APIRouter, HTTPException, status, Depends, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.db.base import Vessel as ModelVessel
from app.schemas.vessel import Vessel as SchemaVessel
from app.schemas.vessel import VesselCreate as SchemaVesselCreate


router = APIRouter()


@router.get("/", response_model=List[SchemaVessel])
async def read_vessel_list(session: Session = Depends(get_db)):
    """
    Get all vessels
    """

    vessel_list = session.query(ModelVessel).all()

    return vessel_list


@router.post(
    "/", response_model=SchemaVesselCreate, status_code=status.HTTP_201_CREATED
)
async def create_vessel(
    vessel: SchemaVesselCreate, session: Session = Depends(get_db)
):
    """
    Create a new vessel
    """

    vesseldb = ModelVessel(name=vessel.name)
    session.add(vesseldb)
    session.commit()
    session.refresh(vesseldb)

    return vesseldb


@router.get("/{item_id}", response_model=SchemaVessel)
async def read_vessel(item_id: int, session: Session = Depends(get_db)):
    """
    Get vessel by id
    """

    vessel = session.query(ModelVessel).get(item_id)

    if not vessel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vessel with item_id {item_id} not found",
        )

    return vessel


@router.put("/{item_id}", response_model=SchemaVessel)
async def update_vessel(
    item_id: int, name: str, session: Session = Depends(get_db)
):
    """
    Update vessel by id
    """

    vessel = session.query(ModelVessel).get(item_id)

    if vessel:
        vessel.name = name
        session.commit()

    if not vessel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vessel with item_id: {item_id} not found",
        )

    return vessel


@router.delete("/{item_id}")
async def delete_vessel(item_id: int, session: Session = Depends(get_db)):
    """
    Delete vessel by id
    """

    vessel = session.query(ModelVessel).get(item_id)

    if vessel:
        session.delete(vessel)
        session.commit()
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vessel with item_id: {item_id} not found",
        )

    return None
