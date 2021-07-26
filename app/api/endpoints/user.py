from fastapi import APIRouter

router = APIRouter()

@router.post("/user")
def login():
    return "Great Hello from login"