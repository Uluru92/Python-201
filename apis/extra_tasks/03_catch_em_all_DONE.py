'''
Using the PokéAPI https://pokeapi.co/docs/v2#pokemon-section
fetch the name and height of all 151 Pokémon of the main series.

Create a text document that describes each Pokémon using the information
available in the JSON response.
NOTE: only using 'height' is enough, but if you want more, go crazy.

BONUS: Using your script, create a folder and download the main 'front_default'
       sprites for each Pokémon using requests into that folder.
       Name the files appropriately using the name data from your response.
'''
import requests
from pprint import pprint
import os

url = "https://pokeapi.co/api/v2/pokemon/?limit=151"
response = requests.get(url)
data = response.json()

first_151_pokemons = {}

for index, pokemon in enumerate(data['results']):
    name = pokemon['name']
    id = index + 1

    url_single_pokemon = pokemon['url']
    response_single_pokemon = requests.get(url_single_pokemon)
    data_single_pokemon = response_single_pokemon.json()

    weight = int(data_single_pokemon['weight'])
    height = int(data_single_pokemon['height'])
    body_mass_index = (weight / (height ** 2))

    first_151_pokemons[name] = {
        'id': id,
        'name': name,
        'weight': weight,
        'height': height,
        'body_mass_index': body_mass_index
    }

    #BONUS:
    images_folder = r"C:\Users\jordd\Documents\Repositorios Github\Python-201\apis\extra_tasks\03_catch_em_all"
    os.makedirs(images_folder, exist_ok=True)
    
    front_default_url = data_single_pokemon['sprites']['front_default']
    img_data = requests.get(front_default_url).content
    file_path = os.path.join(images_folder, f"{name}.png")
    with open(file_path, "wb") as f:
        f.write(img_data)

with open(r"C:\Users\jordd\Documents\Repositorios Github\Python-201\apis\extra_tasks\03_catch_em_all.txt", "w", encoding="utf-8") as file:
    for pokemon in sorted(first_151_pokemons.values(), key=lambda p: p['id']):
        description = (
            f"ID: {pokemon['id']:03}\n"
            f"Name: {pokemon['name'].capitalize()}\n"
            f"Weight: {pokemon['weight']} (decagrams)\n"
            f"Height: {pokemon['height']} (decimetres)\n"
            f"Body Mass Index (BMI): {pokemon['body_mass_index']:.2f}\n"
            "---------------------------------------------\n"
        )
        file.write(description)

