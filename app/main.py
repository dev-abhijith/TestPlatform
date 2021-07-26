from fastapi import FastAPI
from app.api.api import api_router
from app.models import models
from app.db.database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)
app.include_router(api_router, prefix="/api")