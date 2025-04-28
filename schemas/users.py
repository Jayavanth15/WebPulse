from pydantic  import BaseModel, EmailStr
from enum import Enum


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class RoleEnum(str, Enum):
    admin = "admin"
    user = "user"

class UserCreate(BaseModel):
    first_name : str
    last_name : str
    email: EmailStr
    password: str
    role : RoleEnum

class UserResponse(BaseModel):
    user_id: int
    first_name : str
    last_name : str
    email: EmailStr
    role : str
    createdBy: int
