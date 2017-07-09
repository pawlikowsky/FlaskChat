from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey

import datetime
from database import Base

class Chat(Base):
    __tablename__ = 'chat'
    __table_args__ = {'extend_existing': True} 
    id = Column(Integer, primary_key=True)
    chat_uid = Column(String(12), unique=True)
    content = Column(String)
    editor = Column(String(12))
    created = Column(DateTime, default=datetime.datetime.now)
    

    def __init__(self, chat_uid=None, content=None, convert_unicode=True):
        self.chat_uid = chat_uid
        self.content = content

    def __repr__(self):
        return '<Chat %r>' % (self.chat_uid)



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(10))
    chat_id = Column(String, ForeignKey('chat.chat_uid'))

    def __init__(self, name=None):
        self.name =  name
        
    
    def __repr__(self):
        return '<User %r>' % (self.name)

