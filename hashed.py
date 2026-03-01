from typing_extensions import deprecated

from passlib.context import CryptContext

pwd_hashed = CryptContext(schemes=["bcrypt"],deprecated = "auto")

class hashed():
    def bcrypt(password :str):
        return pwd_hashed.hash(password)
