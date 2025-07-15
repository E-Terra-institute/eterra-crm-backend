from pydantic import BaseModel
from datetime import datetime

class RequestCreate(BaseModel):
    name: str | None
    message: str
    platform: str = "telegram"

class RequestOut(RequestCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
