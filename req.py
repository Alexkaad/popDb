import requests

API_KEY = "600ec0e1d08c0a3daefabbcf24858c1e"  # Remplace par ta clé API
BASE_URL = "https://api.themoviedb.org/3"

url = f"https://api.themoviedb.org/3/movie/popular"
params = {
    "api_key": API_KEY,
    "language": "fr-FR",
    "page": 1  # tu peux changer de page (1, 2, 3...)
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    films = data["results"]

    print("📌 Films populaires :")
    for film in films:  # affiche les 10 premiers
        print(f"🎬 {film['title']} ({film['release_date']}) - ⭐ {film['vote_average']}")
else:
    print("Erreur:", response.status_code)








