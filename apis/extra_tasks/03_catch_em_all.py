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

all_pokemons = []
pokemon_main_series_list = []

url_total = "https://pokeapi.co/api/v2/pokemon/?limit=1302"
response = requests.get(url_total)
data_total = response.json()
total_pokemon = int(len(data_total['results'])) # total number of pokemons
print(f'There are a total of {total_pokemon}.')
pprint(data_total)

for pokemon in data_total['results']:
    name = pokemon['name']
    print(f"\n🔍 Checking: {name}")

    url_ability = f"https://pokeapi.co/api/v2/ability/{name}"

    try:
        response_pokemon = requests.get(url_ability)
        response_pokemon.raise_for_status()  # lanza excepción si status no es 200

        data_pokemon = response_pokemon.json()

        if data_pokemon.get("is_main_series"):  # usa get por si no existe la key
            print(f"✅ {name} is part of the main series.")
            pokemon_main_series_list.append(name)
        else:
            print(f"ℹ️ {name} is NOT part of the main series.")

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error for '{name}': {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"❌ Request failed for '{name}': {req_err}")
    except ValueError:
        print(f"❌ JSON decode error for '{name}' — no se pudo interpretar respuesta.")
    except Exception as e:
        print(f"❌ Unexpected error for '{name}': {e}")