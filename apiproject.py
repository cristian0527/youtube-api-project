#python3 apiproject.py
#will be using themoviedb lib + API 
#pip install tmdbsimple

import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
name = input("Enter pokemon name: ").lower()
response = requests.get(BASE_URL + name)
print("Status of connection: ", response.status_code)
data = response.json()
print(data)