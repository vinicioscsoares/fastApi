from pydantic import BaseModel

class Blog(BaseModel):
    title:str
    body:str

class UserCreate(BaseModel):
    username:str
    name:str
    email: str
    password:str