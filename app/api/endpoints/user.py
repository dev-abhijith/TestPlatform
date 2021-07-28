
from app.crud import CRUDusers
from fastapi import APIRouter,Depends
from sqlalchemy.orm.session import Session
from app.schemas import user
from app.api.deps import get_db, get_current_user
from typing import List
from app.models import models

router = APIRouter(
    prefix= "/user"
)

@router.get("/",response_model=List[user.ShowUser])
def show_all(db:Session = Depends(get_db), current_user: models.Users = Depends(get_current_user) ):
    return CRUDusers.get_all(db)

@router.post("/", status_code= 201)
def create_user( request: user.User, db: Session = Depends(get_db) ):
    return CRUDusers.create_user(request, db)

@router.delete("/{id}",status_code=204)
def delete_user( id: int, db:Session = Depends(get_db)):
    return CRUDusers.delete(id,db)

@router.put("/{id}",status_code=202)
def update_user(id: int,request: user.User, db:Session = Depends(get_db)):
    return CRUDusers.update_user(id,request, db)

@router.get("/{id}", response_model= user.ShowUser)
def get_user( id: int, db:Session = Depends(get_db)):
    return CRUDusers.get_user(id, db)