from fastapi import FastAPI
from app.api.api import api_router
from app.models import models
from app.db.database import engine
from app.core.config import settings

app = FastAPI()

models.Base.metadata.create_all(engine)
app.include_router(api_router, prefix=settings.API_STR)