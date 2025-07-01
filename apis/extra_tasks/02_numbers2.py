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

# Solution
#   Pseudocode
#       Topic: Currencies
#       GET: extract all the symbols from API

#FIRST STEP: ingest API data from at least 1 external source

import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_FINNHUB")

url = f"https://finnhub.io/api/v1/stock/recommendation?symbol=GWH&token={api_key}"

data_finnhub = requests.get(url).json()

pprint(data_finnhub)