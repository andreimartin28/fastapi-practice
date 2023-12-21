from fastapi import FastAPI, Request, status
from controllers import blog_get, blog_post, user, article, product
from db import models
from db.database import engine
from exceptions import StoryException
from fastapi.responses import JSONResponse, PlainTextResponse

app = FastAPI()
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

# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc:StoryException):
#     return PlainTextResponse(str(exc),
#                                 status_code=status.HTTP_400_BAD_REQUEST)

models.Base.metadata.create_all(engine)