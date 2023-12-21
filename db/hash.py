from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes='bcrypt', deprecated = 'auto')

class Hash():
    def bcrypt(user_password: str):
        return pwd_cxt.hash(user_password)

    def verify(hashed_user_password, plain_user_password):
        return pwd_cxt.verify(plain_user_password, hashed_user_password)

