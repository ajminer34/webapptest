from fastapi import APIRouter, status, HTTPException, Depends
from pydantic import BaseModel, Field
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy import select
from models import Venues


router = APIRouter(
    prefix= "/venues",
    tags = ["Venues"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class VenueModel(BaseModel):
    VenueName : str
    VenueAddress : str
    VenueCity : str
    VenueState : str = Field(max_length = 3)
    VenueZip : str

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/by-venueId/{venue_id}")
async def get_venue_by_id(db : db_dependency, venue_id : int):

    try:
        stmt = select(Venues).where(Venues.VenueId == venue_id)
        result = db.execute(stmt).scalars().first()
        return result
    except Exception as e:
        print(e)
        raise HTTPException(status_code=403, detail = f"Failed due to exception {e}")

@router.post("/new_venue", status_code = status.HTTP_201_CREATED)
async def create_new_venue(db : db_dependency, venue : VenueModel):
    new_venue = Venues(
        VenueName = venue.VenueName,
        VenueAddress = venue.VenueAddress,
        VenueCity = venue.VenueCity,
        VenueState = venue.VenueState,
        VenueZip = venue.VenueZip
    )
    db.add(new_venue)
    db.commit()