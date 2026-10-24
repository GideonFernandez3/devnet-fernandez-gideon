import requests
import random
import json

pokemon_list = ["metapod", "weedle", "charmander", "squirtle", "bulbasaur"]
PokeAPI_URL = "https://pokeapi.co/api/v2/pokemon/"
def get_random_pokemon():
    random_pokemon = random.choice(pokemon_list)
    response = requests.get(f"{PokeAPI_URL}/{random_pokemon}")
    return response.json()

print(get_random_pokemon())
