
from sqlalchemy.orm.session import Session
from app.models import models
from fastapi.exceptions import HTTPException
from app.core.security import get_password_hash, verify_password

def get_all(db:Session):
    users = db.query(models.Users).all()
    return users

def create_user(request, db:Session):
    new_user = models.Users(
        name = request.name,
        email = request.email,
        password = get_password_hash(request.password),
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

# Change fetching user (add a get by email function instead of db query) after adding email verification

def authenticate( db:Session, username:str, password: str ):
    user = db.query(models.Users).filter(models.Users.email == username).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user