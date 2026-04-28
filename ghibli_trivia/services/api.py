import requests

API_URL = "https://ghibliapi.dev/films"

def obtener_peliculas():
    response = requests.get(API_URL)
    return response.json()