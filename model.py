from sqlalchemy import String , Column , Integer ,ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer , primary_key=True , index=True)
    name = Column(String,nullable=False)
    age = Column(Integer)
    email = Column(String , unique=True)
    password = Column(String)
    post_key = relationship("Post" , back_populates="user_key")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer , primary_key=True , index=True)
    user_id = Column(Integer,ForeignKey(User.id))
    title = Column(String)
    user_key = relationship("User" , back_populates="post_key")
