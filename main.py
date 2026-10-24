from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/products/{product_id}")
async def detail_view(product_id: int) -> dict:
    return {"product": f"Stock number {product_id}"}


# Закомментировано, тк ниже есть такая же точка входа
#
# @app.get("/users")
# async def users(name : str = "Undefined", age: int = 18) -> dict:
#     return {"user_name": name, "user_age": age}


@app.get("/country/{country}")
async def list_cities(country: str, limit: int) -> dict:
    country_dict = {
        'Russia': ['Moscow', 'St. Petersburg', 'Novosibirsk', 'Ekaterinburg', 'Kazan'],
        'USA': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia'],
    }

    return {"country": country, "cities": country_dict[country][:limit]}

@app.get("/users/{user}")
async def get_user(user: str = Path(min_length=4, max_length=20, description="Enter your name")) -> dict:
    return {"user_name": user}


@app.get("/category/{category_id}/products")
async def category(category_id: Annotated[int, Path(gt=0, description="Category ID")],
                   page: Annotated[int, Query()]) -> dict:
    return {"category_id": category_id, "page": page}


@app.get("/users")
async def retrieve_user_profile(
        username: Annotated[str, Query(min_length=2, max_length=50, description='Имя пользователя')]
) -> dict:
    profiles_dict = {
        'alex': {'name': 'Александр', 'age': 33, 'phone': '+79463456789', 'email': 'alex@my-site.com'},
    }
    # if username in profiles_dict:
    #     return profiles_dict[username]
    # else:
    #     return {"message": f"Пользователь {username} не найден."}
    return profiles_dict.get(username, {'message': f'Пользователь {username} не найден.'})
