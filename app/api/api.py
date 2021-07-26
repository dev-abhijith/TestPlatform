from fastapi import APIRouter
from app.api.endpoints import login, user, questions

api_router = APIRouter()

api_router.include_router(login.router, tags=['Login'])
api_router.include_router(user.router, tags=['User'])
api_router.include_router(questions.router, tags=['Questions'])
