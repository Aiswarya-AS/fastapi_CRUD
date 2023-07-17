from fastapi import FastAPI
import model
from router import router
from config import engine

model.Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(router, prefix="/book", tags=["book"])


@app.get("/")
async def Home():
    return "welcom home"
