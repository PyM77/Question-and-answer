from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select, func
from models.models import Question
from api.questions.schemas import QuestionBase
from typing import List




async def get_questions(session: AsyncSession) -> list[Question.text]:
    questions_query = select(Question.text).order_by(Question.id)

    result: Result = await session.execute(questions_query)

    questions = result.scalars().all()

    return list(questions)

# async def get_question(session: AsyncSession) ->

async def add_questions(session: AsyncSession, question_in: QuestionBase):

    question = Question(**question_in.model_dump())

    session.add(question)

    await session.commit()
    await session.refresh(question)

    return question
