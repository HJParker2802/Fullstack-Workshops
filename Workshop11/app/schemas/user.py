#app/schemas/user.py
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    """UserBase is a Pydantic model that defines the base attributes for a user."""
    email: EmailStr
    name: str

class UserCreate(UserBase):
    """UserCreate is a Pydantic model that extends UserBase and adds a password field for user creation."""
    pass

class User(UserBase):
    """User is a Pydantic model that extends UserBase and adds an id field for representing a user in the database."""
    id: int

    class Config:
        orm_mode = True

