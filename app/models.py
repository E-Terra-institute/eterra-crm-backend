from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    message = Column(String, nullable=False)
    platform = Column(String, default="telegram")
    created_at = Column(DateTime, default=datetime.utcnow)
