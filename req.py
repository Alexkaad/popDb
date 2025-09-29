from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_KEY = "600ec0e1d08c0a3daefabbcf24858c1e"  # Remplace par ta clé API
BASE_URL = "https://api.themoviedb.org/3"

@app.route('/films/<int:page>/popular', methods=['GET'])
def get_films(page):
    url = f"{BASE_URL}/movie/popular"
    params = {
        "api_key": API_KEY,
        "language": "fr-FR",
        "page": page
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        films = data.get("results", [])
       
        # On renvoie les 10 premiers films
        return jsonify([
            {
                "title": film['title'],
                "release_date": film['release_date'],
                "vote_average": film['vote_average'],
                "poster_path": film.get('poster_path'),
                "id": film.get('id')
            } for film in films

        ])

    else:
        return jsonify({"error": f"Erreur {response.status_code}"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)








