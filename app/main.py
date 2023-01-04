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

# newuser (moet uniek zijn) #newalbum OK (enkel als het nog niet in de db zit) #newgenre ok (enkel als het nog niet in de db zit)
# getalbum OK #getallalbums OK #getrandomalbum
# delete album ok
# edit album ok


@app.get("/albums/{album_id}", response_model=schemas.Album)
def read_album(album_id: int, db: Session = Depends(get_db)):
    album = crud.get_album(db, album_id=album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album


@app.get("/albums", response_model=list[schemas.Album])
def read_albums(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    albums = crud.get_albums(db=db, skip=skip, limit=limit)
    return albums


@app.post("/albums", response_model=schemas.Album)
def create_album(album: schemas.AlbumCreate, db: Session = Depends(get_db)):
    existing_album = (
        db.query(models.Album)
        .filter(models.Album.title == album.title, models.Album.user_id == album.user_id)
        .first()
    )
    if existing_album:
        raise HTTPException(
            status_code=400,
            detail=f"An album with title '{album.title}' already exists for this user.",
        )
    return crud.create_album(db=db, album=album)


@app.put("/albums/{album_id}", response_model=schemas.Album)
def update_album(album_id: int, updates: schemas.AlbumUpdate, db: Session = Depends(get_db)):
    album = crud.get_album(db, album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return crud.update_album(db=db, album=album, updates=updates)


@app.delete("/albums/{album_id}", response_model=schemas.Album)
def delete_album(album_id: int, db: Session = Depends(get_db)):
    album = crud.delete_album(db=db, album_id=album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album


@app.post("/genres", response_model=schemas.Genre)
def create_genre(genre: schemas.GenreCreate, db: Session = Depends(get_db)):
    existing_genre = db.query(models.Genre).filter(
        models.Genre.name == genre.name).first()
    if existing_genre:
        raise HTTPException(
            status_code=400,
            detail=f"A genre with name '{genre.name}' already exists.",
        )
    return crud.create_genre(db=db, genre=genre)


@app.get("/genres", response_model=list[schemas.Genre])
def read_genres(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    genres = crud.get_genres(db, skip=skip, limit=limit)
    return genres


@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(
        models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail=f"A user with email '{user.email}' already exists.",
        )
    return crud.create_user(db=db, user=user)
