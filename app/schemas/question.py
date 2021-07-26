
from pydantic import BaseModel

class Question(BaseModel):
    year: int
    exam: str
    subject: str
    section: str
    question: str
    answer: str
    option1: str
    option2: str
    option3: str
    solution: str

class ShowQuestion(Question):
    id: int
    difficulty: int
    class Config:
        orm_mode= True
