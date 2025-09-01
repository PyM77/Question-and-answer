from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.questions.schemas import QuestionBase
from models.models import Question, Answer


async def get_questions(session: AsyncSession) -> list[Question.text]:
    questions_query = select(Question.text).order_by(Question.id)

    result: Result = await session.execute(questions_query)

    questions = result.scalars().all()

    return list(questions)


# async def get_question(session: AsyncSession) ->

async def add_questions(session: AsyncSession,
                        question_in:
                        QuestionBase
                        ):
    question = Question(**question_in.model_dump())

    session.add(question)

    await session.commit()
    await session.refresh(question)

    return question


async def get_question_and_answers(
        id: int,
        session: AsyncSession
):
    question_query = select(Question.text).where(Question.id == id)
    answers_query = select(Answer.text).where(Answer.question_id == id)

    result: Result = await session.execute(question_query)

    if (question := result.scalar_one_or_none()):
        result: Result = await session.execute(answers_query)

        if (answers := result.scalars().all()):

            return {"question": question, "answers": answers}

        return {"question": question}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="detail not found"
    )

async def delete_question_and_answers(
        id: int,
        session: AsyncSession
):
    result: Result = await session.execute(select(Question).where(Question.id==id))

    if (question:= result.scalar_one_or_none()):

        await session.delete(question)
        await session.commit()

        return {"delete": question}
    else:
        HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='detail not found'
        )


