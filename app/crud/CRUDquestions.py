from sqlalchemy.orm.session import Session
from app.models import models
from fastapi.exceptions import HTTPException


def get_all(db:Session):
    questions = db.query(models.Questions).all()
    return questions

def create_question(request, db:Session):
    new_question = models.Questions(
        exam = request.exam,
        year = request.year,
        subject = request.subject,
        section = request.section,
        question = request.question,
        answer = request.answer,
        option1 = request.option1,
        option2 = request.option2,
        option3 = request.option3,
        solution = request.solution,
        difficulty = 1500
    )
    db.add(new_question)
    db.commit()
    db.refresh(new_question)
    return new_question

def delete(id: int, db:Session):
    db.query(models.Questions).filter(models.Questions.id == id).delete(synchronize_session=False)
    db.commit()
    return 'Deleted'

def update_question(id: int, request, db:Session):
    question = db.query(models.Questions).filter(models.Questions.id == id)
    if not question.first():
        raise HTTPException(status_code= 404, detail=f'The question with id {id} not found')
    else:
        question.update({
            'year' : request.year,
            'exam' : request.exam,
            'subject' : request.subject,
            'section' : request.section,
            'question' : request.question,
            'answer' : request.answer,
            'option1' : request.option1,
            'option2' : request.option2,
            'option3' : request.option3,
            'solution' : request.solution
            },
            synchronize_session=False)
    db.commit()
    return 'Updated'

def show(id: int, db:Session):
    question = db.query(models.Questions).filter(models.Questions.id == id).first()
    if not question:
        raise HTTPException(status_code = 404, detail=f'The question with id {id} is not available')
    return question

