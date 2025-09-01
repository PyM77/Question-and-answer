from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.questions.schemas import QuestionBase
from db.database import get_async_session
from api.questions import crud

api_router = APIRouter(tags=['questions'], prefix='/questions')


@api_router.get('/')
async def get_questions(
    session: AsyncSession = Depends(get_async_session)
):
    questions = await crud.get_questions(session)

    return questions

@api_router.post('/')
async def post_questions(
        question: QuestionBase,
        session: AsyncSession = Depends(get_async_session),
):

    question_create = await crud.add_questions(session, question)

    return {"question_create": question_create}


@api_router.get('/{id}')
async def get_question(
        id: int,
        session: AsyncSession = Depends(get_async_session)
):
    question_and_answers = await crud.get_question_and_answers(id, session)

    return question_and_answers




@api_router.delete('/{id}')
async def delete_question(id: int):
    ...

