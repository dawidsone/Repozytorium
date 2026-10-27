import csv
from database import engine, SessionLocal, init_db, MovieModel, LinkModel, RatingModel, TagModel

def load_data():
    init_db()
    db = SessionLocal()

    # 1. Ładowanie filmów (movies.csv)
    try:
        with open("plikiCsv/movies.csv", mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                movie = MovieModel(
                    id=int(row["movieId"]),
                    title=row["title"],
                    genres=row["genres"]
                )
                db.add(movie)
        print("Zapisano filmy...")
    except FileNotFoundError:
        print("Nie znaleziono pliku plikiCsv/movies.csv")

    # 2. Ładowanie linków (links.csv)
    try:
        with open("plikiCsv/links.csv", mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                link = LinkModel(
                    movie_id=int(row["movieId"]),
                    imdb_id=row["imdbId"],
                    tmdb_id=row["tmdbId"]
                )
                db.add(link)
        print("Zapisano linki...")
    except FileNotFoundError:
        print("Nie znaleziono pliku plikiCsv/links.csv")

    # 3. Ładowanie ocen (ratings.csv)
    try:
        with open("plikiCsv/ratings.csv", mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rating = RatingModel(
                    user_id=int(row["userId"]),
                    movie_id=int(row["movieId"]),
                    rating=float(row["rating"]),
                    timestamp=int(row["timestamp"])
                )
                db.add(rating)
        print("Zapisano oceny...")
    except FileNotFoundError:
        print("Nie znaleziono pliku plikiCsv/ratings.csv")

    # 4. Ładowanie tagów (tags.csv)
    try:
        with open("plikiCsv/tags.csv", mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                tag = TagModel(
                    user_id=int(row["userId"]),
                    movie_id=int(row["movieId"]),
                    tag=row["tag"],
                    timestamp=int(row["timestamp"])
                )
                db.add(tag)
        print("Zapisano tagi...")
    except FileNotFoundError:
        print("Nie znaleziono pliku plikiCsv/tags.csv")

    db.commit()
    db.close()
    print("Baza danych została pomyślnie utworzona i zasilona danymi!")

if __name__ == "__main__":
    load_data()