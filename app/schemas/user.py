from pydantic import BaseModel


    
class User(BaseModel):
    id = int
    name = str
    email = str
    hashed_password = str
    rating = int 
    paid = bool

class PaidUser(BaseModel):
    id = int 
    name = str
    email = str 
    paid = bool

class ShowUser( BaseModel ):
    id = int
    name = str
    email = str
    


