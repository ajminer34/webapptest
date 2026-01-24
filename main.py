from fastapi import FastAPI
import models
from routers import concerts, artists

from database import engine


app = FastAPI()


models.Base.metadata.create_all(bind=engine)

app.include_router(concerts.router)
app.include_router(artists.router)

@app.get("/health_check")
async def get_health_check():
    return {"Status" : "healthy"}