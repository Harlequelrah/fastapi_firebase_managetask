from typing import Optional
from pydantic import BaseModel, Field






class UserModel(BaseModel):
    id:str
    email: str
    password: str

class UserCreateModel(BaseModel):
    email: str = Field(example="user@example.com", pattern=r"[^@]+@[^@]+\.[^@]+")
    password: str = Field(example="motdepasse",max_length=100)

class UserUpdateModel(BaseModel):
    email: Optional[str] = Field(example="user@example.com", pattern=r"[^@]+@[^@]+\.[^@]+")
    password: Optional[str] = Field(default=None,example="motdepasse",max_length=100)
