from fastapi import FastAPI
import telegram

app = FastAPI()

app.include_router(telegram.router)

@app.get("/")
def root():
    return {"message": "ETERRA CRM Backend is running"}
