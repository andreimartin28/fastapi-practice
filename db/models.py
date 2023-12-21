from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

class DbUser(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    user_username = Column(String)
    user_email = Column(String)
    user_password = Column(String)
    items = relationship("DbArticle", back_populates='user')

class DbArticle(Base):
    __tablename__ = 'articles'
    article_id = Column(Integer, primary_key=True, index=True)
    article_title = Column(String)
    article_content = Column(String)
    article_published = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    user = relationship("DbUser", back_populates='items')
