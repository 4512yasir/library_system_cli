from .base import Base
from sqlalchemy import Integer,String,Column



class Member(Base):
    __tablename__="members"

    id= Column(Integer,primary_key=True)
    _name = Column("name",String)
    _email =Column("email",String)
    membership_no =Column(Integer)


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value:str):
        if len(value) < 4 or len(value) > 25:
            raise ValueError ("Name should be more than 3 or 25")
        else:
            self._name = value

