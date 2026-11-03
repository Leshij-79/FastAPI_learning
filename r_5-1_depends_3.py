from fastapi import FastAPI, Depends, HTTPException, status

app = FastAPI()

async def check_auth(token: str) -> bool:
    if token == "secret":
        return True
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")


@app.get("/profile")
async def get_profile(token: str = Depends(check_auth)) -> str:
    return "User is authorized"