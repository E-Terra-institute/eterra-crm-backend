from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app.schemas import RequestCreate
from app.models import Request as DBRequest
from app.database import SessionLocal
import json

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/webhook/telegram")
async def telegram_webhook(req: Request, db: Session = Depends(get_db)):
    data = await req.json()
    message_text = data.get("message", {}).get("text", "")
    sender = data.get("message", {}).get("from", {}).get("username", "unknown")
    
    new_req = DBRequest(
        name=sender,
        message=message_text,
        platform="telegram"
    )
    db.add(new_req)
    db.commit()
    db.refresh(new_req)

    return {"status": "saved", "id": new_req.id}
