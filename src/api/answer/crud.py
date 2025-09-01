from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select, func
from models.models import Answer, Question
from api.questions.schemas import QuestionBase
from api.answer.schemas import AnswerBase
from typing import List
from fastapi.exceptions import HTTPException
from fastapi import status

async def add_answer(
        id: int,
        session: AsyncSession,
        answer_in: AnswerBase
):
    result: Result = await session.execute(select(Question).where(Question.id==id))

    if result.scalar_one_or_none():

        answer = Answer(**answer_in.model_dump())

        answer.question_id = id
        session.add(answer)

        await session.commit()
        await session.refresh(answer)

        return answer

    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='question not found'
        )

async def get_answer(
        id: int,
        session: AsyncSession
):
    result: Result = await session.execute(select(Answer.text).where(Answer.id==id))

    if (answer := result.scalar_one_or_none()):
        return answer
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='answer not found'
        )


async def delete_answer(
        id: int,
        session: AsyncSession
):
    result: Result = await  session.execute(select(Answer).where(Answer.id==id))

    if (answer := result.scalar_one_or_none()):

        await session.delete(answer)
        await session.commit()

        return {"delete": answer}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='answer not found'
        )

