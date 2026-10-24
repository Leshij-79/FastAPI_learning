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


@app.get("/users")
async def users(name : str = "Undefined", age: int = 18) -> dict:
    return {"user_name": name, "user_age": age}


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
