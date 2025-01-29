from typing import Optional
from pydantic import BaseModel,Field

class TaskCreateModel(BaseModel):
    title:str=Field(example="Spring Homework")
    description:str=Field(example="I should do my spring homework with authentication")
    is_done:bool=Field(default=False)

class TaskUpdateModel(BaseModel):
    title:Optional[str]=Field(example="")
    description:Optional[str]=Field(example="I should do my spring homework with authentication")
    is_done:Optional[bool]=Field(default=False)

class TaskModel(BaseModel):
    id:str
    title:str
    description:str
    is_done:bool

    class Config:
        orm_mode=True
