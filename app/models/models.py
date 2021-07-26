from sqlalchemy.sql.sqltypes import Boolean
from app.db.database import Base
from sqlalchemy import Column, Integer, String

class Questions(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    exam = Column(String)
    year = Column(Integer)
    subject = Column(String)
    section = Column(String)
    question = Column(String)
    answer = Column(String)
    option1 = Column(String)
    option2 = Column(String)
    option3 = Column(String)
    solution = Column(String)
    difficulty = Column(Integer)

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    hashed_password = Column(String)
    rating = Column(Integer)
    paid = Column(Boolean)