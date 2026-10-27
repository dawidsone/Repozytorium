import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, MovieModel, init_db

app = FastAPI()

# Inicjalizacja bazy przy starcie
init_db()

# Dependency - zarządzanie połączeniem z bazą
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Zrefaktorowany endpoint /movies
@app.get("/movies")
def get_movies(db: Session = Depends(get_db)):
    # Pobieramy wszystkie obiekty z tabeli 'movies' z bazy SQLite
    movies = db.query(MovieModel).all()
    
    # FastAPI automatycznie serializuje obiekty ORM SQLAlchemy na JSON
    return movies

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)