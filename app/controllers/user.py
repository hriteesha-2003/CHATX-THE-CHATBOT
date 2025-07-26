from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from database.db import user_collection
from app.models.user import User, UserLogin, usersignup
from app.utils import get_hashed_password, verify_password, create_JWT_token

async def login(user):
    user_data = user_collection.find_one({"email": user.email})
    if not user_data or not verify_password(user.password, user_data["password"]):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    token = create_JWT_token({"user_id": str(user_data["_id"])})
    return {"access_token": token, 
            "token_type": "bearer",
            "user": {"id": str(user_data["_id"]),
                    "username": user_data.get("username")}}


async def signup(user: usersignup):
    if user.password != user.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")
    
    existing_user = user_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_hashed_password(user.password)
    new_user = User(username=user.username, email=user.email, password=hashed_password)
    
    user_dict = new_user.model_dump()
    result = user_collection.insert_one(user_dict)
    user_collection.update_one({"_id": result.inserted_id}, {"$set": {"user_id": str(result.inserted_id)}})
    if not result.acknowledged:
        raise HTTPException(status_code=500, detail="User creation failed")

    return {"message": "User created successfully",
            "user_id": str(result.inserted_id),
            "username": user.username}
