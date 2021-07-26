from pydantic import BaseModel


class User(BaseModel):
    name : str
    email : str
    password : str
    
class UserInDB(User):
    id : int
    rating : int 
    paid : bool
    class Config:
        orm_mode = True

class ShowUser(BaseModel):
    id : int
    name : str
    email : str
    paid : bool
    class Config:
        orm_mode = True
    