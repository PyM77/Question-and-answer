from pydantic import BaseModel, ConfigDict

class QuestionBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    text: str
