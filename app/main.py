from fastapi import FastAPI
from .api import router
from .database import Base, engine
from . import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Backend Service API", version="1.0.0", description="Layered REST API portfolio project")

@app.get("/health", tags=["system"])
def health():
    return {"status": "ok"}

app.include_router(router)
