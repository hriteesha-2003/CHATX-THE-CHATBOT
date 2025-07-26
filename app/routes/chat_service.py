from fastapi import APIRouter, Depends
from datetime import datetime
from app.models.chat import ChatRequest, ChatResponse
from database.db import message_collection
from app.chat_service_ai.ai_engine import chat_with_ai 
from app.utils import get_current_user
from app.controllers.chat import start_chat

chat_service_router = APIRouter()

@chat_service_router.post("/chat")
async def chat(request: ChatRequest, user=Depends(get_current_user)):
    return await start_chat(request, user)

