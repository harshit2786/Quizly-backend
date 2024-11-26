from fastapi import FastAPI
from routers import quiz

app = FastAPI()

app.include_router(quiz.router)