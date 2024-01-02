from fastapi import FastAPI, Request, status
from controllers import blog_get, blog_post, user, article, product, file
from auth import authentication
from db import models
from db.database import engine
from exceptions import StoryException
from templates import templates
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from client import html
from fastapi.websockets import WebSocket

app = FastAPI()
app.include_router(templates.router)
app.include_router(file.router)
app.include_router(authentication.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)

@app.get('/hello')
def index():
    return {'message': 'Hello World!'}

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(status_code=status.HTTP_418_IM_A_TEAPOT,
                        content={'detail': exc.name})

@app.get("/")
async def get():
    return HTMLResponse(html)

clients = []

@app.websocket('/chat')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    while True:
        data = await websocket.receive_text()
        for client in clients:
            await client.send_text(data)

# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc:StoryException):
#     return PlainTextResponse(str(exc),
#                                 status_code=status.HTTP_400_BAD_REQUEST)

models.Base.metadata.create_all(engine)

app.mount('/files', StaticFiles(directory='files/'), name='files')
app.mount('/templates/static', 
            StaticFiles(directory="templates/static"),
            name= "static"
        )