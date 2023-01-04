from typing import List
from pydantic import BaseModel


class AlbumBase(BaseModel):
    title: str
    artist: str


class AlbumCreate(AlbumBase):
    pass


class Album(AlbumBase):
    id: int

    class Config:
        orm_mode = True


class AlbumUpdate(BaseModel):
    title: str = None
    artist: str = None
