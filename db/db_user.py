from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from db.hash import Hash
from fastapi import HTTPException, status

def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        user_username = request.user_username,
        user_email = request.user_email,
        user_password = Hash.bcrypt(request.user_password)
    )     
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db: Session):
    return db.query(DbUser).all()

def get_user(db: Session, id: int):
    # Handle any exceptions
    user = db.query(DbUser).filter(DbUser.user_id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} not found')
    return 

def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.user_id == id)
    # Handle any exceptions
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} not found')
    user.update({
        DbUser.user_username: request.user_username,
        DbUser.user_email: request.user_email,
        DbUser.user_password: Hash.bcrypt(request.user_password)
    })
    db.commit()
    return {'message': 'updated user'}

def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.user_id == id).first()
    # Handle any exceptions
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} not found')
    db.delete(user)
    db.commit()
    return {'message': 'deleted user'}
