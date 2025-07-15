from fastapi import FastAPI
from app import telegram

app = FastAPI()

app.include_router(telegram.router)

@app.get("/")
def root():
    return {"message": "ETERRA CRM Backend is running"}
