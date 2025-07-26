#for user
from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    username: str
    password: str
    email: str
    is_admin: bool = False

class UserLogin(BaseModel):
    email: str= Field(..., description="User's email address")
    password: str= Field(..., description="User's password")
   
class usersignup(BaseModel):
    username: str= Field(..., description="User's username")
    email: str= Field(..., description="User's email address")
    password: str= Field(..., description="User's password")
    confirm_password: str= Field(..., description="User's confirm password")