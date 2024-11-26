from pydantic import BaseModel, conlist
from enum import Enum

class Answer(str,Enum):
    a="a"
    b="b"
    c="c"
    d="d"

class Choices(BaseModel):
    a:str
    b:str
    c:str
    d:str

class Question(BaseModel):
    ques: str
    choices: Choices
    ans: Answer

class QuestionSet(BaseModel):
    quiz: list[Question] = conlist(Question,min_length=10,max_length=10)

class QuizRequest(BaseModel):
    topic: str