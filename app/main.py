from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine
import os

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/albums/{album_id}")
def read_album(album_id: int, db: Session = Depends(get_db)):
    album = crud.get_album(db, album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album


@app.get("/albums")
def read_albums(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    albums = crud.get_albums(db, skip=skip, limit=limit)
    return albums


@app.post("/albums")
def create_album(album: schemas.AlbumCreate, db: Session = Depends(get_db)):
    return create_album(db, album)


@app.put("/albums/{album_id}")
def update_album(album_id: int, updates: schemas.AlbumUpdate, db: Session = Depends(get_db)):
    album = crud.get_album(db, album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return update_album(db, album, updates)


@app.delete("/albums/{album_id}")
def delete_album(album_id: int, db: Session = Depends(get_db)):
    album = delete_album(db, album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album
