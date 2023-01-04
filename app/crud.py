from sqlalchemy.orm import Session

import models
import schemas


def get_album(db, album_id: int):
    return db.query(models.Album).filter(models.Album.id == album_id).first()


def get_albums(db, skip: int = 0, limit: int = 100):
    return db.query(models.Album).offset(skip).limit(limit).all()


def create_album(db, album: schemas.AlbumCreate):
    db_album = models.Album(**album.dict())
    db.add(db_album)
    db.commit()
    db.refresh(db_album)
    return db_album


def update_album(db, album: schemas.Album, updates: schemas.AlbumUpdate):
    for field, value in updates.dict(exclude_unset=True).items():
        setattr(album, field, value)
    db.add(album)
    db.commit()
    db.refresh(album)
    return album


def delete_album(db, album_id: int):
    album = db.query(models.Album).filter(models.Album.id == album_id).first()
    if not album:
        return None
    db.delete(album)
    db.commit()
    return album
