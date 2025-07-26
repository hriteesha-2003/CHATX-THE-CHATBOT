from datetime import datetime
from app.chat_service_ai.ai_engine import chat_with_ai  
from database.db import message_collection

async def start_chat(request, user):
    prompt = request.prompt
    user_id = user

    
    previous_messages = list(
        message_collection.find({"user_id": user_id})
        .sort("timestamp", -1)
        .limit(5)
    )
    
    
    context = ""
    for msg in reversed(previous_messages):  
        context += f"User: {msg['prompt']}\nAI: {msg['response']}\n"
    context += f"User: {prompt}\nAI:"

    # Get AI response
    response = await chat_with_ai(context)

    
    chat_message = {
        "user_id": user_id,
        "prompt": prompt,
        "response": response,
        "timestamp": datetime.now()
    }
    message_collection.insert_one(chat_message)

    return {"response": response}
