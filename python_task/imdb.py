import os
import requests
from dotenv import load_dotenv
from main import add_to_airtable

load_dotenv()


def get_movie_info(api_key, movie_title):
    url = 'http://www.omdbapi.com/'
    params = {
        'apikey': api_key,
        't': movie_title,
        'plot': 'short',
        'r': 'json'
    }
    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200 and data.get('Response') == 'True':
        movie_info = {
            'Title': data['Title'],
            'Year': data['Year'],
            'Director': data['Director'],
            'Writer': data['Writer'],
            'Released': data['Released'],
            'Plot': data['Plot']
        }
        return movie_info
    else:
        print(f"Ошибка при запросе к API: {data.get('Error', 'Неизвестная ошибка')}")
        return None


def get_movie_list(api_key, num_movies=10):
    url = 'http://www.omdbapi.com/'
    params = {
        'apikey': api_key,
        'type': 'movie',
        's': "any",
        'r': 'json'
    }
    response = requests.get(url, params=params)
    data = response.json()

    if (response.status_code == 200) and ('Search' in data):
        movie_list = data['Search'][:num_movies]

        for movie in movie_list:
            movie_info = get_movie_info(api_key, movie['Title'])
            if movie_info:
                movie.update(movie_info)

        return movie_list
    else:
        error_message = data.get("Error", "Неизвестная ошибка")
        print(response.status_code, error_message)
        return None


api_key_imdb = os.getenv("api_key_imdb")
movie_list = get_movie_list(api_key_imdb, num_movies=10)

if movie_list:
    add_to_airtable(movie_list)
else:
    print("Фильмы не найдены.")
