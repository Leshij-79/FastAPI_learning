from datetime import datetime
from decimal import Decimal


from pydantic import BaseModel, Field, EmailStr, PositiveInt, NonNegativeInt


class User(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Имя пользователя",
    )
    email: EmailStr = Field(
        ...,
        description="Электронная почта пользователя",
    )
    is_active: bool = Field(
        default=True,
        description="Статус активности пользователя",
    )


class Task(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Название задачи",
    )
    description: str | None = Field(
        default=None,
        max_length=500,
        description="Описание задачи",
    )
    is_completed: bool = Field(
        default=False,
        description="Статус завершения задачи",
    )


class Order(BaseModel):
    order_id: PositiveInt = Field(
        description="Уникальный идентификатор заказа",
    )
    user_id: PositiveInt = Field(
        description="Идентификатор пользователя, сделавшего заказ",
    )
    total_amount: Decimal = Field(
        ge=0,
        description="Общая сумма заказа",
    )
    created_at: datetime = Field(
        description="Дата и время создания заказа",
    )


class Address(BaseModel):
    user_id: PositiveInt = Field(
        description="Идентификатор пользователя",
    )
    city: str = Field(
        min_length=2,
        max_length=100,
        description="Город",
    )
    street: str = Field(
        min_length=2,
        max_length=200,
        description="Улица",
    )
    postal_code: PositiveInt = Field(
        ge=101000,
        le=999999,
        description="Почтовый индекс",
    )


class Product(BaseModel):
    product_slug: str = Field(
        min_length=3,
        max_length=120,
        pattern=r"^[A-Za-z0-9_-]+$",
        description="Слаг продукта",
    )
    name: str = Field(
        min_length=3,
        max_length=100,
        description="Название продукта",
    )
    price: Decimal = Field(
        gt=0,
        description="Цена продукта",
    )
    stock: NonNegativeInt = Field(
        default=0,
        description="Количество продукта на складе",
    )
