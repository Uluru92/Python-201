'''
Sign up for an API key with the coinmarketcap API.

Using their documentation, fetch all listed cryptocurrencies.
From the result, create a new JSON file that includes the following:
* cmc_rank
* name
* symbol
* platform
* quote

Save that info to a file.
'''

# When try to sign up coinmarketcap API: "An internal server error occurred" every time.
# For this exercise I am going to use Coinlayer API http://api.coinlayer.com/
# API coin layer endpoint: https://api.coinlayer.com/api/list
# For this exercise please activate the venv called venv_coincap

import os
import requests
import json

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_COINLAYER")
url_coinlayer = f"http://api.coinlayer.com/api/list?access_key={api_key}"

try:
    response = requests.get(url_coinlayer)
    data = response.json()

    if data.get("success"):
        crypto_data = data.get("crypto", {})
        cleaned_data = []

        for symbol, info in crypto_data.items():
            cleaned_entry = {
                "symbol": info.get("symbol"),
                "name": info.get("name"),
                "max_supply": info.get("max_supply"),
                "icon_url": info.get("icon_url")   
            }
            cleaned_data.append(cleaned_entry)

        # Save as JSON file
        with open(r"C:\Users\jordd\Documents\Repositorios Github\Python-201\apis\extra_tasks\10_coincryptos.json", "w", encoding="utf-8") as f:
            json.dump(cleaned_data, f, indent=4, ensure_ascii=False)
    else:
        print("The request to Coinlayer failed:", data)

except Exception as e:
    print("Error:", e)