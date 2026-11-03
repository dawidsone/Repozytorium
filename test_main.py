import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from main import app, get_db
from database import Base, MovieModel, LinkModel, RatingModel, TagModel

# Konfiguracja bazy w pamięci RAM do celów testowych
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Fixtura tworząca bazę oraz zasilająca ją wstępnymi danymi
@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    
    # Przykładowe fixtury danych testowych
    movie = MovieModel(id=1, title="Test Movie", genres="Action|Sci-Fi")
    link = LinkModel(movie_id=1, imdb_id="0111161", tmdb_id="550")
    rating = RatingModel(id=1, user_id=1, movie_id=1, rating=4.5, timestamp=12345678)
    tag = TagModel(id=1, user_id=1, movie_id=1, tag="cool", timestamp=12345678)
    
    db.add_all([movie, link, rating, tag])
    db.commit()
    
    yield db
    
    db.close()
    Base.metadata.drop_all(bind=engine)

# Fixtura nadpisująca bazę danych aplikacji na bazę testową
@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()

# ==================== TESTY INTEGRACYJNE MOVIES ====================
def test_get_movies_list(client):
    response = client.get("/movies")
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_get_movie_by_id_success(client):
    response = client.get("/movies/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Movie"

def test_get_movie_by_id_not_found(client):
    response = client.get("/movies/999")
    assert response.status_code == 404

def test_create_movie(client):
    payload = {"title": "New Movie", "genres": "Drama"}
    response = client.post("/movies", json=payload)
    assert response.status_code == 201
    assert response.json()["id"] is not None
    assert response.json()["title"] == "New Movie"

def test_update_movie(client):
    payload = {"title": "Updated Title", "genres": "Comedy"}
    response = client.put("/movies/1", json=payload)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"

def test_delete_movie(client):
    response = client.delete("/movies/1")
    assert response.status_code == 200
    
    # Weryfikacja, że element zniknął z bazy
    get_res = client.get("/movies/1")
    assert get_res.status_code == 404

# ==================== TESTY INTEGRACYJNE LINKS ====================
def test_get_links_list(client):
    response = client.get("/links")
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_create_link(client):
    payload = {"movie_id": 2, "imdb_id": "999999", "tmdb_id": "8888"}
    response = client.post("/links", json=payload)
    assert response.status_code == 201
    assert response.json()["imdb_id"] == "999999"

# ==================== TESTY INTEGRACYJNE RATINGS ====================
def test_get_ratings_list(client):
    response = client.get("/ratings")
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_create_rating(client):
    payload = {"user_id": 1, "movie_id": 1, "rating": 5.0, "timestamp": 12345}
    response = client.post("/ratings", json=payload)
    assert response.status_code == 201
    assert response.json()["rating"] == 5.0

# ==================== TESTY INTEGRACYJNE TAGS ====================
def test_get_tags_list(client):
    response = client.get("/tags")
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_delete_tag(client):
    response = client.delete("/tags/1")
    assert response.status_code == 200