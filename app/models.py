from sqlalchemy import create_engine, Column, Integer, String, DateTime
from database import Base
from sqlalchemy.orm import relationship


class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    artist = Column(String, index=True)
