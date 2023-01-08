from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Boolean
from database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    albums = relationship("Album", back_populates="user")


class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    artist = Column(String, index=True)
    genre_id = Column(Integer, ForeignKey("genres.id"), index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)

    user = relationship("User", back_populates="albums")


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
