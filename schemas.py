from pydantic import BaseModel

# --- MOVIES ---
class MovieCreate(BaseModel):
    title: str
    genres: str

class MovieResponse(MovieCreate):
    id: int

    class Config:
        from_attributes = True

# --- LINKS ---
class LinkCreate(BaseModel):
    movie_id: int
    imdb_id: str
    tmdb_id: str

class LinkResponse(LinkCreate):
    class Config:
        from_attributes = True

# --- RATINGS ---
class RatingCreate(BaseModel):
    user_id: int
    movie_id: int
    rating: float
    timestamp: int

class RatingResponse(RatingCreate):
    id: int

    class Config:
        from_attributes = True

# --- TAGS ---
class TagCreate(BaseModel):
    user_id: int
    movie_id: int
    tag: str
    timestamp: int

class TagResponse(TagCreate):
    id: int

    class Config:
        from_attributes = True