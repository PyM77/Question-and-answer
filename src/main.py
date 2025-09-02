from fastapi import FastAPI
from api.questions.views import api_router as questions_router
from api.answer.views import api_router as answer_router
import uvicorn

app = FastAPI()

app.include_router(
    router=questions_router
)

app.include_router(
    router=answer_router
)

@app.get('/')
async def root():
    return {"message": "hello world"}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)