from fastapi import APIRouter, Depends
from app.schemas import question
from sqlalchemy.orm.session import Session
from app.db.database import get_db
from app.crud import CRUDquestions
from typing import List

router = APIRouter(
    prefix="/questions",
    tags=['Questions']
)

@router.get("/", response_model=List[question.ShowQuestion])
def show_questions(db: Session = Depends(get_db)):
    return CRUDquestions.get_all(db)

@router.post("/", status_code=201)
def enter_question(request: question.Question, db: Session = Depends(get_db)):
    return CRUDquestions.create_question(request, db)

@router.delete("/{id}", status_code=204)
def delete(id: int, db:Session= Depends(get_db)):
    return CRUDquestions.delete(id, db)

@router.get("/{id}", response_model=question.ShowQuestion)
def show(id: int, db: Session = Depends(get_db)):
    return CRUDquestions.show(id, db)

@router.put("/{id}", status_code=202)
def update(id: int, request:question.Question, db:Session = Depends(get_db)):
    return CRUDquestions.update_question(id,request, db)