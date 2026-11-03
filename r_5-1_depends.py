from fastapi import FastAPI, Depends

app = FastAPI()

async def get_message():
    return "Hello from dependency!"


@app.get("/welcome")
async def welcome(message: str = Depends(get_message)):
    return {"message": message}