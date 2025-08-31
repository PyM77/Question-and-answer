from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import text, ForeignKey, String



class Question(Base):
    text: Mapped[str] = mapped_column(String, nullable=False)

    answers: Mapped["Answer"] = relationship(back_populates='questions')


class Answer(Base):
    question_id: Mapped[int] = mapped_column(ForeignKey('questions.id'))
    user_id: Mapped[str]
    text: Mapped[str]


    questions: Mapped["Question"] = relationship(back_populates='answers')
