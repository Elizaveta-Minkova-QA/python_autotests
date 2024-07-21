import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'be1880559a4d64e0627621a25db08df7'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_pokemons = {
    "name": "generate",
    "photo_id": -1
}

body_update = {
    "pokemon_id": "44474",
    "name": "Бог Грома",
    "photo_id": -1
}

body_pokeball = {
    "pokemon_id": "44475"
}


response_pokemons = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
print(response_pokemons.text)

pokemon_id = response_pokemons.json()['id']
print(pokemon_id)

response_update = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_update)
print(response_update.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)

