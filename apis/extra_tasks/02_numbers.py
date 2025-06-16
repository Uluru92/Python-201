'''
Create an API that serves numerical information.

What topic your API is about is your own choice,
however it needs to fulfill the following specs:
* ingest API data from at least 1 external source
* combine (and/or manipulate) the received data in a meaningful way
* store your altered data in a Postgres database
* serve the data at an endpoint (e.g. using sandman2)

TIP: consider using a cryptocurrency API such as coinmarketcap (but anything goes)!
'''

#FIRST STEP: ingest API data from at least 1 external source
import requests
from pprint import pprint

base_ = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5000&convert=USD"
base_url = "https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
base_url_names = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"

headers = {
    "X-CMC_PRO_API_KEY": "d8b8630f-dc62-4cd7-86d8-d4c7f7189bd1"
}

response0 = requests.get(base_, headers=headers)
response1 = requests.get(base_url, headers=headers)
response2 = requests.get(base_url_names, headers=headers)

if response1.status_code == 200:
    data = response1.json()
    data2 = response2.json()

    print("\nDATA:\n")
    pprint(data)
    print(" ")
    
    USD_price = data["data"][0]["quote"]["USD"]["price"]
    BTC_price = data["data"][1]["quote"]["BTC"]["volume_24h"]
    
    name_1 = data2["data"][0]["name"]
    name_2 = data2["data"][1]["name"]
    name_3 = data2["data"][2]["name"]
    print(f"Crytocurrency names:\n-{name_1}\n-{name_2}\n-{name_3}")
    
    print(" ")
    print(f"BTC price: {BTC_price}")
    print(f"BTC price: {BTC_price}")
    print(f"BTC price: {BTC_price}")

else:
    print(f"Error: {response1.status_code}")
    print(response1.json())