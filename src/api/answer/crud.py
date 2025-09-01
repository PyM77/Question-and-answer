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
    query_id: Result = await session.execute(select(Question).where(Question.id==id))

    if query_id.scalar_one_or_none():

        answer = Answer(**answer_in.model_dump())

        answer.question_id = id
        session.add(answer)

        await session.commit()
        await session.refresh(answer)

        return answer

    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='detail not found'
        )

