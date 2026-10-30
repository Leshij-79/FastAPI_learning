from fastapi import FastAPI, HTTPException, status, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


app = FastAPI()

# Настройка Jinja2 и статических файлов
templates = Jinja2Templates(directory="templates")
# подключает папку static для обслуживания статических файлов (CSS) по url /static
app.mount("/static", StaticFiles(directory="static"), name="static")


# Модель для входных данных (запросов: создание и обновление)
class MessageCreate(BaseModel):
    content: str


# Модель для ответов и хранения в базе данных
class Message(BaseModel):
    id: int
    content: str


# Инициализируем messages_db как список объектов Message
messages_db: list[Message] = [Message(id=0, content="Первое сообщение в FastAPI")]


@app.get("/web/messages", response_class=HTMLResponse)
async def get_messages_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"messages": messages_db},
    )

# Страница создания сообщения
@app.get("/web/messages/create", response_class=HTMLResponse)
async def get_create_message_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="create.html"
    )

# Обработка формы создания сообщения
@app.post("/web/messages", response_class=HTMLResponse)
async def create_message_form(request: Request, content: str = Form(...)):
    next_id = max((msg.id for msg in messages_db), default=-1) + 1
    new_message = Message(id=next_id, content=content)
    messages_db.append(new_message)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"messages": messages_db},
    )

# Страница одного сообщения
@app.get("/web/messages/{message_id}", response_class=HTMLResponse)
async def get_message_detail_page(request: Request, message_id: int):
    for message in messages_db:
        if message.id == message_id:
            return templates.TemplateResponse(
                request=request,
                name="detail.html",
                context={"message": message},
            )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Сообщение не найдено")
