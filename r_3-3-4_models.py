from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class UserUpdate(BaseModel):
    name: str = Field()
    age: int = Field(
        gt=0,
    )


class User(BaseModel):
    id: int = Field()
    name: str = Field()
    age: int = Field(
        gt=0,
    )


users = [
    User(id=1, name="Алексей", age=25),
    User(id=2, name="Мария", age=30),
    User(id=3, name="Иван", age=22),
    User(id=4, name="Елена", age=28),
    User(id=5, name="Дмитрий", age=35)
]


@app.put("/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
async def update_user(user_id: int, create_user: UserUpdate) -> User:
    for i, user in enumerate(users):
        if user.id == user_id:
            update_user = User(id=user_id, name=create_user.name, age=create_user.age)
            users[i] = update_user
            return update_user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
