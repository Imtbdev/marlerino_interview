from dotenv import load_dotenv
from pyairtable import Api
import os

load_dotenv()

def add_to_airtable(movie_list):
    api_key = os.getenv("api_key_air")
    base_id = os.getenv("base_id")
    table_name = os.getenv("table_name")

    api = Api(api_key)
    table = api.get_table(base_id, table_name)

    if movie_list:
        for movie in movie_list:
            table.create({
                "Название": movie['Title'],
                "Режиссер": movie['Director'],
                "Сценарист": movie['Writer'],
                "Дата выхода": movie['Released'],
                "Краткий сюжет": movie["Plot"],
                "Обложка": [{'url': movie['Poster']}]
            })
    else:
        print("Произошла ошибка")
