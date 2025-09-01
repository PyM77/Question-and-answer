from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.answer import crud
from api.answer.schemas import AnswerBase
from db.database import get_async_session

api_router = APIRouter(tags=['answer'])


@api_router.post('/questions/{id}/answers/')
async def answer_to_question(
        id: int,
        answer: AnswerBase,
        session: AsyncSession = Depends(get_async_session)
):
    answer_create = await crud.add_answer(id, session, answer)

    return {"answer_create": answer_create}


@api_router.get('/answer/{id}')
async def get_answer(
        id: int,
        session: AsyncSession = Depends(get_async_session)
):
    return await crud.get_answer(id, session)


@api_router.delete('/answer/{id}')
async def delete_answer(
        id: int,
        session: AsyncSession = Depends(get_async_session)
):
    return await crud.delete_answer(id, session)
