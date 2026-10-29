from datetime import datetime
from decimal import Decimal
from typing import List

from pydantic import BaseModel, Field, EmailStr, PositiveInt, NonNegativeInt, SecretStr


class User(BaseModel):
    username: str = Field(
        ...,
        min_length=5,
        max_length=20,
        description="Пользовательское имя, от 5 до 20 символов",
    )
    password: SecretStr = Field(
        ...,
        min_length=8,
        max_length=50,
        description="Пароль, от 8 до 50 символов",
    )
    email: EmailStr = Field(
        ...,
        description="Электронная почта",
    )
    first_name: str | None = Field(
        min_length=2,
        max_length=30,
        default=None,
        description="Имя, от 2 до 30 символов",
    )
    last_name: str | None = Field(
        min_length=2,
        max_length=30,
        default=None,
        description="Фамилия, от 2 до 30 символов",
    )
    is_active: bool = Field(
        default=True,
        description="Учётная запись активна",
    )
    is_staff: bool = Field(
        default=False,
        description="Является служебным пользователем",
    )
    is_superuser: bool = Field(
        default=False,
        description="Является суперпользователем",
    )
    date_joined: datetime = Field(
        default_factory=datetime.now,
        description="Зарегистрирован",
    )
    last_login: datetime | None = Field(
        default=None,
        description="Последнее посещение",
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


class Post(BaseModel):
    author_id: PositiveInt = Field(
        description="Идентификатор автора",
    )
    title: str = Field(
        ...,
        max_length=100,
        description="Заголовок записи, не более 100 символов",
    )
    description: str | None = Field(
        default=None,
        max_length=250,
        description="Описание записи, не более 250 символов",
    )
    content: str = Field(
        ...,
        description="Контент записи",
    )
    created_at: datetime = Field(
        default_factory=datetime.now,
        description="Запись создана",
    )
    updated_at: datetime | None= Field(
        default=None,
        description="Запись обновлена",
    )
    is_published: bool = Field(
        default=False,
        description="Запись опубликована",
    )
    tags: List[str] = Field(
        default=[],
        description="Теги записи",
    )
