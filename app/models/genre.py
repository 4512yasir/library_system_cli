from sqlalchemy import Column,String,Integer
from .base import Base

class Genre(Base):
    __tablename__ = "genres"


    id = Column(Integer, primary_key= True)
    name = Column(String)