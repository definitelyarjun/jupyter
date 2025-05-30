from db import Base
from sqlalchemy import Column, Integer, String, Text

class ChatHistory(Base):
    __tablename__ = "Chat_History"
    id = Column(Integer, primary_key=True, index=True)
    query = Column(Text)
    response = Column(Text)

    class config:
        from_attribute = True

