from sqlalchemy import Column, Integer, String
from .database import Base
from passlib.context import CryptContext

psw_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer,primary_key=True, index=True)
    title = Column(String)
    body = Column(String)

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    password = Column(String)

    def verify_password(self,plain_password):
        return pwd_context.verify(plain_password, self.password)
    def set_password(self, plain_password):
        self.password = psw_context.hash(plain_password)