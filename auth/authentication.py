from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from auth import oauth2
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import models
from db.hash import Hash

router = APIRouter(prefix='', tags=['authentication'])

@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.DbUser).filter(models.DbUser.user_username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid credentials')
    if not Hash.verify(user.user_password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect password')
    
    access_token = oauth2.create_access_token(data={'sub': user.user_username})

    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'user_id': user.user_id,
        'username': user.user_username
    }