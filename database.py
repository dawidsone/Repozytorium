from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./movies.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class MovieModel(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    genres = Column(String)

class LinkModel(Base):
    __tablename__ = "links"
    movie_id = Column(Integer, primary_key=True)
    imdb_id = Column(String)
    tmdb_id = Column(String)

class RatingModel(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    movie_id = Column(Integer)
    rating = Column(Float)
    timestamp = Column(Integer)

class TagModel(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    movie_id = Column(Integer)
    tag = Column(String)
    timestamp = Column(Integer)

def init_db():
    Base.metadata.create_all(bind=engine)