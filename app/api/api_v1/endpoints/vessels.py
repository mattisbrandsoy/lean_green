from fastapi import APIRouter, HTTPException, status, Depends, Query
from typing import Optional
from sqlalchemy.orm import Session

from app.api.deps import get_session
import app.models
from app.schemas.schemas import Vessel, VesselCreate

router = APIRouter(
    prefix="/vessels", tags=["vessels"], responses={status.HTTP_404_NOT_FOUND}
)


@router.post("/", response_model=schemas.Vessel, status_code=status.HTTP_201_CREATED)
async def create_vessel(
    vessel: schemas.VesselCreate, session: Session = Depends(get_session)
):
    """
    Create a new vessel
    """

    vesseldb = app.models.Vessel(name=vessel.name)

    session.add(vesseldb)
    session.commit()
    session.refresh(vesseldb)

    return vesseldb


@router.get("/{item_id}", response_model=schemas.Vessel)
async def read_vessel(item_id: int, session: Session = Depends(get_session)):
    """
    Get vessel by id
    """

    vessel = session.query(app.models.Vessel).get(item_id)

    if not vessel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vessel with item_id {item_id} not found",
        )

    return vessel


@router.put("/{item_id}", response_model=schemas.Vessel)
async def update_vessel(
    item_id: int, name: str, session: Session = Depends(get_session)
):
    """
    Update vessel by id
    """

    vessel = session.query(app.models.Vessel).get(item_id)

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
async def delete_vessel(item_id: int, session: Session = Depends(get_session)):
    """
    Delete vessel by id
    """

    vessel = session.query(app.models.Vessel).get(item_id)

    if vessel:
        session.delete(vessel)
        session.commit()
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vessel with item_id: {item_id} not found",
        )

    return None


@router.get("/", response_model=List[schemas.Vessel])
async def read_vessel_list(session: Session = Depends(get_session)):
    """
    Get all vessels
    """

    vessel_list = session.query(app.models.Vessel).all()

    return vessel_list
