from fastapi import APIRouter, status, HTTPException, Depends
from pydantic import BaseModel
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy import select, delete
from models import Artists

class ArtistsModel(BaseModel):
    ArtistName : str

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

router = APIRouter(
    prefix="/artists",
    tags=["artists"]
)

@router.get("/all")
async def get_all_artists(db : db_dependency):
    stmt = select(Artists)
    artists = db.scalars(stmt).all()
    for a in artists:
        print(a)
    return artists

@router.post("/new_artist")
async def create_new_artist(db : db_dependency, artist : ArtistsModel, status_code = status.HTTP_201_CREATED):
    new_artist = Artists(**artist.model_dump())
    db.add(new_artist)
    db.commit()

@router.delete("/delete_artist/{artistId}")
async def delete_artist(db : db_dependency, artistId : int):
    stmt = delete(Artists).where(Artists.ArtistId == artistId)
    db.execute(stmt)
    db.commit()