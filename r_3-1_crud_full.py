from fastapi import FastAPI, HTTPException, status, Body

app = FastAPI()

comments_db = {0: "First comment in FastAPI"}


@app.get("/comments")
async def read_comments() -> dict:
    return comments_db


@app.get("/comments/{comment_id}")
async def read_comment(comment_id: int) -> str:
    try:
        return comments_db[comment_id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")


@app.post("/comments", status_code=status.HTTP_201_CREATED)
async def create_comment(comment: str = Body(...)) -> str:
    current_index = max(comments_db.keys()) + 1 if len(comments_db) > 0 else 0
    comments_db[current_index] = comment
    return "Comment created!"


@app.put("/comments/{comment_id}")
async def update_comment(comment_id: int, comment: str = Body(...)) -> str:
    if comment_id in comments_db:
        comments_db[comment_id] = comment
        return "Comment updated!"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")


@app.delete("/comments/{comment_id}")
async def delete_comment(comment_id: int) -> str:
    if comment_id in comments_db:
        comments_db.pop(comment_id)
        return "Comment deleted!"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")