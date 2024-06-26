from fastapi import APIRouter, Depends
from schemas import ArticleBase, ArticleDisplay
from sqlalchemy.orm import Session
from schemas import UserBase
from db.database import get_db
from db import db_article
from typing import List
from auth.oauth2 import oauth2_scheme, get_current_user

router = APIRouter(
    prefix='/article',
    tags=['article']
)

# Create article 
@router.post('/', response_model=ArticleDisplay)
def create_article(request:ArticleBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_article.create_article(db, request)

# Get specific article - token method 
# @router.get('/{id}', response_model=ArticleDisplay)
# def get_article(id:int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
#     print(locals())
#     return db_article.get_article(db, id)

@router.get('/{id}')
def get_article(id:int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    print({'locals': locals()})
    print(db_article.get_article(db,id))
    return {'data': db_article.get_article(db, id),
            'current_user': current_user}
