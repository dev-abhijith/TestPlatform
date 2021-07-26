
from sqlalchemy.orm.session import Session
from app.models import models
from fastapi.exceptions import HTTPException

def get_all(db:Session):
    users = db.query(models.Users).all()
    return users

def create_user(request, db:Session):
    new_user = models.Users(
        name = request.name,
        email = request.email,
        password = request.password,
        rating = 1500,
        paid = False
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def delete(id: int, db:Session):
    db.query(models.Users).filter(models.Users.id == id).delete(synchronize_session=False)
    db.commit()
    return 'Deleted'

def update_user(id: int, request, db:Session):
    user = db.query(models.Users).filter(models.Users.id == id)

    if not user.first():
        raise HTTPException(status_code= 404, detail=f'The user with id {id} not found')
    else:
        user.update({
            'name': request.name,
            'password': request.password,
            'email': request.email
        })
        db.commit()
    return 'Updated User'

def get_user(id: int, db:Session):
    user = db.query(models.Users).filter(models.Users.id == id).first()
    if not user:
        raise HTTPException(status_code = 404, detail=f'The user with id {id} is not available')
    return user