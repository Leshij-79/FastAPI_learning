from fastapi import FastAPI, HTTPException, status, Body

app = FastAPI()

notes_db = {0: "Study FastAPI", 1: "I like FastAPI"}
tasks_db = {0: "Study FastAPI", 1: "I like FastAPI"}
reminders_db = {}
quotes_db = {0: "FastAPI lets you build APIs fast with type hints",
             1: "Auto docs at /docs and /redoc with OpenAPI",
             2: "Pydantic validates your data",
             3: "Depends gives clean Dependency Injection",
             4: "Use async def and await for concurrency"}
goals_db = {0: "Learn FastAPI basics",
            1: "Build CRUD app",
            2: "Write tests with TestClient",
            3: "Add authentication",
            4: "Deploy to production"}


@app.get("/notes")
async def read_notes() -> dict:
    return notes_db


@app.get("/tasks/{task_id}")
async def read_task(task_id: int) -> str:
    try:
        return tasks_db[task_id]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


@app.post("/reminders", status_code=status.HTTP_201_CREATED)
async def create_reminder(reminder: str = Body(...)) -> str:
    current_index = max(reminders_db) + 1 if reminders_db else 0
    reminders_db[current_index] = reminder
    return "Reminder created!"


@app.put("/quotes/{quote_id}")
async def update_quote(quote_id: int, quote: str = Body(...)) -> str:
    if quote_id in quotes_db:
        quotes_db[quote_id] = quote
        return "Quote updated!"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quote not found")


@app.delete("/goals/{goal_id}")
async def delete_goal(goal_id: int) -> str:
    if goal_id in goals_db:
        goals_db.pop(goal_id)
        return "Goal deleted!"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Goal not found")
