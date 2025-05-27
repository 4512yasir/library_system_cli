from .base import Base 
from sqlalchemy import Column,Integer,DateTime


class BorrowedBook(Base):
     __tablename__ = "Borrowed_books"


     id = Column(Integer, primary_key=True)
     members_id =Column(Integer)
     books_id =Column(Integer)
     borrowed_date = Column(DateTime ,default=DateTime)
     return_date = Column(DateTime , default=DateTime)
