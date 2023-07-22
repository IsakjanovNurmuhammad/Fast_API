from sqlalchemy import Integer, String, Column
from db import Base


class MsgModel(Base):
    __tablename__ = "msg"
    id = Column(Integer, primary_key=True, index=True)
    msg = Column(String)
