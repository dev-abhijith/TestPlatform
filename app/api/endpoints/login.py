from datetime import timedelta
from typing import Any

from app.api.deps import get_db
from app.schemas import token_schema
from app.crud import CRUDusers
from app.core.config import settings
from app.core import security
from app.models import models

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm.session import Session
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter()

@router.post("/login/access-token", response_model= token_schema.Token)
def login_access_token( db:Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    
    """
    OAuth2 compatible token login, get an access token for future requests
    """

    user = CRUDusers.authenticate( db, username= form_data.username, password = form_data.password )
    if not user:
      raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return{
        "access_token": security.create_access_token(user.id, expires_delta=access_token_expires),
        "token_type": "bearer",
    }