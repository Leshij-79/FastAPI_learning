from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class Task(BaseModel):
    id: int = Field()
    title: str = Field()
    completed: bool = Field()


class UserCreate(BaseModel):
    name: str = Field()
    email: str = Field()


class User(BaseModel):
    id: int = Field()
    name: str = Field()
    email: str = Field()


tasks = [
    Task(id=1, title="Купить молоко", completed=False),
    Task(id=2, title="Позвонить другу", completed=True),
    Task(id=3, title="Сделать домашку", completed=False),
    Task(id=4, title="Погулять с собакой", completed=True),
    Task(id=5, title="Записаться на тренировку", completed=False)
]

users = [
    User(id=1, name="Алексей", email="alexey@example.com"),
    User(id=2, name="Мария", email="maria@example.com"),
    User(id=3, name="Иван", email="ivan@example.com"),
    User(id=4, name="Елена", email="elena@example.com"),
    User(id=5, name="Дмитрий", email="dmitry@example.com")
]


@app.get("/tasks")
async def get_tasks() -> list[Task]:
    return tasks


@app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate) -> User:
    next_id = max((u.id for u in users), default=-1) + 1
    new_user = User(id=next_id, name=user.name, age=user.age, email=user.email)
    users.append(new_user)
    return new_user


@app.get("/users/{user_id}")
async def get_user(user_id: int) -> User:
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
