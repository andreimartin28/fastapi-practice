from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    user_username: str
    user_email: str
    user_password: str

#Article inside UserDisplay
class Article(BaseModel):
    article_title: str
    article_content: str 
    article_published: bool
    class Config():
        from_attributes = True

class UserDisplay(BaseModel):
    user_username : str
    user_email: str
    items: List[Article] = []
    class Config():
        from_attributes = True

#-----------------------------------#

class ArticleBase(BaseModel):
    article_title : str
    article_content: str
    article_published: bool
    user_id : int

#User inside Article Display
class User(BaseModel):
    user_id: int 
    user_username: str
    class Config():
        from_attributes = True

class ArticleDisplay(BaseModel):
    article_title: str
    article_content: str
    article_published: bool
    user: User
    class Config():
        from_attributes = True   