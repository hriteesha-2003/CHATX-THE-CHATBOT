#only routes/user.py
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.models.user import UserLogin, usersignup
from bson import ObjectId
from app.utils import get_hashed_password, verify_password, create_JWT_token
from app.controllers.user import login, signup

authentication_router = APIRouter()

@authentication_router.get("/login")
async def user_login(user: UserLogin):
    return await login(user)



@authentication_router.post("/signup")
async def user_signup(user: usersignup):
    return await signup(user)
