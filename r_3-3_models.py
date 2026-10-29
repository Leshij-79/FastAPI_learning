from fastapi import FastAPI, status
from pydantic import BaseModel, Field

app = FastAPI()


class Task(BaseModel):
    id: int = Field()
    title: str = Field()
    completed: bool = Field()


class UserCreate(BaseModel):
    name: str = Field()
    age: int = Field(
        ge=18,
    )


class User(BaseModel):
    id: int = Field()
    name: str = Field()
    age: int = Field(
        ge=18,
    )


tasks = [
    Task(id=1, title="Купить молоко", completed=False),
    Task(id=2, title="Позвонить другу", completed=True),
    Task(id=3, title="Сделать домашку", completed=False),
    Task(id=4, title="Погулять с собакой", completed=True),
    Task(id=5, title="Записаться на тренировку", completed=False)
]

users=[]


@app.get("/tasks")
async def get_tasks() -> list[Task]:
    return tasks


@app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate) -> User:
    next_id = max((u.id for u in users), default=-1) + 1
    new_user = User(id=next_id, name=user.name, age=user.age)
    users.append(new_user)
    return new_user
