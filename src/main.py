from fastapi import FastAPI
from api.questions.views import api_router as questions_router

app = FastAPI()

app.include_router(
    router=questions_router
)

@app.get('/')
async def root():
    return {"message": "hello world"}
