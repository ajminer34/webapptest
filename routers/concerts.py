from fastapi import APIRouter, status, HTTPException, Depends
from pydantic import BaseModel
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

class ConcertModel(BaseModel):
    artist_name : str
    city : str
    state : str
    venue_address : str
    venue : str
    date : str
    doors_open : str
    ticket_price : int


router = APIRouter(
    prefix = "/concerts",
    tags=["concerts"]
)

concert_list = [
    {"artist" : "artist1",
     "city" : "Denver",
     "state" : "CO",
     "venue_address" : "red_rocks_address",
     "venue" : "Red Rocks",
     "date" : "01/01/2027",
     "doors_open" : "18:00",
     "ticket_price" : 50},
    {"artist" : "artist2",
     "city" : "Chicago",
     "state" : "IL",
     "venue_address" : "vic_theater_address",
     "venue" : "Vic Theater",
     "date" : "01/02/2027",
     "doors_open" : "18:00",
     "ticket_price" : 60}
]

@router.get("/by-artist/{artist}")
async def get_concert_by_artist(db : db_dependency, artist : str, status_code = status.HTTP_200_OK):
    for concert in concert_list:
        if concert.get("artist").casefold() == artist.casefold():
            return concert
    raise HTTPException(status_code = 404, detail = f"Concert not found with artist: {artist}")
    
@router.get("/by-venue/{venue}")
async def get_concert_by_venue(db : db_dependency, venue : str, status_code = status.HTTP_200_OK):
    for concert in concert_list:
        if concert.get("venue").casefold() == venue.casefold():
            return concert
    raise HTTPException(status_code=404, detail = f"Concert not found by venue: {venue} ")