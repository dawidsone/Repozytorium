import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, MovieModel, LinkModel, RatingModel, TagModel, init_db
import schemas

app = FastAPI()

init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ==================== MOVIES ====================
@app.get("/movies", response_model=List[schemas.MovieResponse])
def get_movies(db: Session = Depends(get_db)):
    return db.query(MovieModel).all()

@app.get("/movies/{movie_id}", response_model=schemas.MovieResponse)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(MovieModel).filter(MovieModel.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@app.post("/movies", response_model=schemas.MovieResponse, status_code=status.HTTP_201_CREATED)
def create_movie(movie_data: schemas.MovieCreate, db: Session = Depends(get_db)):
    movie = MovieModel(**movie_data.model_dump())
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie

@app.put("/movies/{movie_id}", response_model=schemas.MovieResponse)
def update_movie(movie_id: int, movie_data: schemas.MovieCreate, db: Session = Depends(get_db)):
    movie = db.query(MovieModel).filter(MovieModel.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    movie.title = movie_data.title
    movie.genres = movie_data.genres
    db.commit()
    db.refresh(movie)
    return movie

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(MovieModel).filter(MovieModel.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    db.delete(movie)
    db.commit()
    return {"message": "Movie deleted successfully"}

# ==================== LINKS ====================
@app.get("/links", response_model=List[schemas.LinkResponse])
def get_links(db: Session = Depends(get_db)):
    return db.query(LinkModel).all()

@app.get("/links/{movie_id}", response_model=schemas.LinkResponse)
def get_link(movie_id: int, db: Session = Depends(get_db)):
    link = db.query(LinkModel).filter(LinkModel.movie_id == movie_id).first()
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    return link

@app.post("/links", response_model=schemas.LinkResponse, status_code=status.HTTP_201_CREATED)
def create_link(link_data: schemas.LinkCreate, db: Session = Depends(get_db)):
    link = LinkModel(**link_data.model_dump())
    db.add(link)
    db.commit()
    db.refresh(link)
    return link

@app.put("/links/{movie_id}", response_model=schemas.LinkResponse)
def update_link(movie_id: int, link_data: schemas.LinkCreate, db: Session = Depends(get_db)):
    link = db.query(LinkModel).filter(LinkModel.movie_id == movie_id).first()
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    link.imdb_id = link_data.imdb_id
    link.tmdb_id = link_data.tmdb_id
    db.commit()
    db.refresh(link)
    return link

@app.delete("/links/{movie_id}")
def delete_link(movie_id: int, db: Session = Depends(get_db)):
    link = db.query(LinkModel).filter(LinkModel.movie_id == movie_id).first()
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    db.delete(link)
    db.commit()
    return {"message": "Link deleted successfully"}

# ==================== RATINGS ====================
@app.get("/ratings", response_model=List[schemas.RatingResponse])
def get_ratings(db: Session = Depends(get_db)):
    return db.query(RatingModel).all()

@app.get("/ratings/{rating_id}", response_model=schemas.RatingResponse)
def get_rating(rating_id: int, db: Session = Depends(get_db)):
    rating = db.query(RatingModel).filter(RatingModel.id == rating_id).first()
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    return rating

@app.post("/ratings", response_model=schemas.RatingResponse, status_code=status.HTTP_201_CREATED)
def create_rating(rating_data: schemas.RatingCreate, db: Session = Depends(get_db)):
    rating = RatingModel(**rating_data.model_dump())
    db.add(rating)
    db.commit()
    db.refresh(rating)
    return rating

@app.put("/ratings/{rating_id}", response_model=schemas.RatingResponse)
def update_rating(rating_id: int, rating_data: schemas.RatingCreate, db: Session = Depends(get_db)):
    rating = db.query(RatingModel).filter(RatingModel.id == rating_id).first()
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    rating.user_id = rating_data.user_id
    rating.movie_id = rating_data.movie_id
    rating.rating = rating_data.rating
    rating.timestamp = rating_data.timestamp
    db.commit()
    db.refresh(rating)
    return rating

@app.delete("/ratings/{rating_id}")
def delete_rating(rating_id: int, db: Session = Depends(get_db)):
    rating = db.query(RatingModel).filter(RatingModel.id == rating_id).first()
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    db.delete(rating)
    db.commit()
    return {"message": "Rating deleted successfully"}

# ==================== TAGS ====================
@app.get("/tags", response_model=List[schemas.TagResponse])
def get_tags(db: Session = Depends(get_db)):
    return db.query(TagModel).all()

@app.get("/tags/{tag_id}", response_model=schemas.TagResponse)
def get_tag(tag_id: int, db: Session = Depends(get_db)):
    tag = db.query(TagModel).filter(TagModel.id == tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag

@app.post("/tags", response_model=schemas.TagResponse, status_code=status.HTTP_201_CREATED)
def create_tag(tag_data: schemas.TagCreate, db: Session = Depends(get_db)):
    tag = TagModel(**tag_data.model_dump())
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag

@app.put("/tags/{tag_id}", response_model=schemas.TagResponse)
def update_tag(tag_id: int, tag_data: schemas.TagCreate, db: Session = Depends(get_db)):
    tag = db.query(TagModel).filter(TagModel.id == tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    tag.user_id = tag_data.user_id
    tag.movie_id = tag_data.movie_id
    tag.tag = tag_data.tag
    tag.timestamp = tag_data.timestamp
    db.commit()
    db.refresh(tag)
    return tag

@app.delete("/tags/{tag_id}")
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    tag = db.query(TagModel).filter(TagModel.id == tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    db.delete(tag)
    db.commit()
    return {"message": "Tag deleted successfully"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)