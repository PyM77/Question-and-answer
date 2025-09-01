from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import text, ForeignKey, String
import uuid
from sqlalchemy.dialects.postgresql import UUID as PG_UUID


class Question(Base):
    text: Mapped[str] = mapped_column(String, nullable=False)

    answers: Mapped["Answer"] = relationship(back_populates='questions')


class Answer(Base):
    question_id: Mapped[int] = mapped_column(ForeignKey('questions.id'))
    user_id: Mapped[uuid.UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    text: Mapped[str]


    questions: Mapped["Question"] = relationship(back_populates='answers')
