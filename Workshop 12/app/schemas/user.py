# app/schemas/user.py 
from pydantic import BaseModel 
from typing import Optional 

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase): 
    password: str
    role: Optional[str] = "user"
    
class User(UserBase):
    id: int
    role: str

class Config:
    orm_mode = True 

