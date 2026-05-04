from fastapi import FastAPI
#import models
#from routers import concerts, artists, venues

#from database import engine


app = FastAPI(
    docs_url=None, 
    redoc_url=None, 
    openapi_url=None
)


#models.Base.metadata.create_all(bind=engine)

#app.include_router(venues.router)
#app.include_router(concerts.router)
#app.include_router(artists.router)

@app.get("/health_check")
async def get_health_check():
    return {"Status" : "healthy"}