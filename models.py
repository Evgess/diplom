from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

class TodoItem(Base):
    __tablename__ = "todo_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    completed = Column(Integer, default=0)  # 0 - не завершено, 1 - завершено
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="todo_items")

User.todo_items = relationship("TodoItem", order_by=TodoItem.id, back_populates="user")
