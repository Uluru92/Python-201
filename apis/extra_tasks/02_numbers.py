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

base_url = "https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

headers = {
    'Accepts': 'application/json',
    "X-CMC_PRO_API_KEY": "b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c"
}

response = requests.get(base_url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("\nDATA:\n")
    print(data)
else:
    print(f"Error: {response.status_code}")
    print(response.json())