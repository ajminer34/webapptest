from fastapi import APIRouter

router = APIRouter(
    prefix = "/concerts",
    tags=["concerts"]
)

artist_list = {
    "artist1" : "song1",
    "artist2" : "song2",
    "artist3" : "song3",
}

@router.get("/artist/{artist}")
async def get_artist(artist : str):
    return artist_list[artist]