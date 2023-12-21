from db.models import DbArticle
from schemas import ArticleBase
from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status
from exceptions import StoryException

def create_article(db: Session, request: ArticleBase):
    if request.article_content.startswith('Once upon a time'):
        raise StoryException('No stories please')
    new_article = DbArticle(
        article_title = request.article_title,
        article_content = request.article_content,
        article_published = request.article_published, 
        user_id = request.user_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

def get_article(db: Session, id: int):
    article = db.query(DbArticle).filter(DbArticle.article_id == id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Article with id {id} not found')
    return article