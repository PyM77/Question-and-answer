import uuid

from pydantic import BaseModel, ConfigDict

class AnswerBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: uuid.UUID
    text: str


