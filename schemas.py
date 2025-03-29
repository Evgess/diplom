from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class User(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True


class TodoItemCreate(BaseModel):
    title: str

class TodoItem(BaseModel):
    id: int
    title: str
    completed: int
    user_id: int

    class Config:
        from_attributes = True

