from fastapi import FastAPI
from routers.concerts import router as concerts_router

app = FastAPI()

app.include_router(concerts_router)

@app.get("/health_check")
async def get_health_check():
    return {"Status" : "healthy"}