from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel



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
async def get_concert_by_artist(artist : str, status_code = status.HTTP_200_OK):
    for concert in concert_list:
        if concert.get("artist").casefold() == artist.casefold():
            return concert
    raise HTTPException(status_code = 404, detail = f"Concert not found with artist: {artist}")
    
@router.get("/by-venue/{venue}")
async def get_concert_by_venue(venue : str, status_code = status.HTTP_200_OK):
    for concert in concert_list:
        if concert.get("venue").casefold() == venue.casefold():
            return concert
    raise HTTPException(status_code=404, detail = f"Concert not found by venue: {venue} ")
"""@router.post("/artist/")
async def create_artist(song_model : SongModel, status_code = status.HTTP_201_CREATED):
    song_list[song_model.artist_name] = song_model.song_name

@router.put("/aritst/")
async def update_song(song_model : SongModel, status_code = status.HTTP_204_NO_CONTENT):
    if not song_model.artist_name in song_list.keys():
        return status.HTTP_404_NOT_FOUND
    song_list[song_model.artist_name] = song_model.song_name"""