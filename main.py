from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import db
from app.routes import user, chat_service

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],    
)
@app.get("/")
async def root():
    return {"message": "Welcome to Mini ChatGPT API"}

app.include_router(user.authentication_router, prefix="/auth", tags=["auth"])
app.include_router(chat_service.chat_service_router, prefix="/chat", tags=["chat"])