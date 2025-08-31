from fastapi import APIRouter

app = APIRouter(tags=['answer'])

@app.post('/questions/{id}/answers/')
async def answer_to_question(id: int):
    ...

@app.get('/answer/{id}')
async def get_answer(id: int):
    ...

@app.delete('/answer/{id}')
async def delete_answer(id: int):
    ...

