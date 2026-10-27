import csv
from fastapi import FastAPI

app = FastAPI()
#Zadanie 1
@app.get("/")
def helloworld():
    return {"hello": "world"}
#Zadanie 2
# Krok 2: Stworzenie klasy Movie (model danych)
class Movie:
    def __init__(self, id, title, genres):
        self.id = id
        self.title = title
        self.genres = genres

@app.get("/movies")
def get_movies():
    try:
        with open('plikiCsv/movies.csv', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader) 
            return [Movie(row[0], row[1], row[2]).__dict__ for row in reader if len(row) >= 3]
            
    except FileNotFoundError:
        return {"error": "Brak pliku movies.csv"}
    #Zadanie 3
@app.get("/links")
def get_links():
    try:
        with open('plikiCsv/links.csv', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader) 
            return [{"movieId": row[0], "imdbId": row[1], "tmdbId": row[2]} for row in reader if len(row) >= 3]
                
    except FileNotFoundError:
        return {"error": "Brak pliku links.csv"}
@app.get("/ratings")
def get_ratings():
    try:
        with open('plikiCsv/ratings.csv', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader) 
            return [{"userId": row[0], "movieId": row[1], "rating": row[2], "timestamp": row[3]} for row in reader if len(row) >= 4]
    except FileNotFoundError:
        return {"error": "Brak pliku ratings.csv"}

@app.get("/tags")
def get_tags():
    try:
        with open('plikiCsv/tags.csv', encoding= 'utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            return [{"userId": row[0], "movieId": row[1], "tag": row[2], "timestamp": row[3]} for row in reader if len(row) >= 4]
    except FileNotFoundError:
        return {"error": "Brak pliku tags.csv"}

