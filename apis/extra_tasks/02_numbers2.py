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
#       GET: extract company's symbols, API https://finnhub.io/api/v1/stock/symbol?exchange=US&token={api_key}
#       GET: extract recomendations for every company, API https://finnhub.io/api/v1/stock/recommendation?symbol=GWH&token={api_key}
#
# FIRST STEP: ingest API data from at least 1 external source

import requests
import os
from pprint import pprint
from dotenv import load_dotenv

# API resources:
load_dotenv()
api_key = os.getenv("API_FINNHUB")
url_companies = f"https://finnhub.io/api/v1/stock/symbol?exchange=US&token={api_key}"
url_recomendations = f"https://finnhub.io/api/v1/stock/recommendation?symbol=GWH&token={api_key}"

# Data received:
data_finnhub_companies = requests.get(url_companies).json()

# Create a list of every company's symbol. This is a REQUIRED argument to get latest analyst recommendation trends for a company.
symbols = [item["displaySymbol"] for item in data_finnhub_companies]

# Use our required argument list, to ingest API data
for index, company in enumerate(data_finnhub_companies):
    symbol = company["displaySymbol"]
    if symbol in symbols:
        print(f"{index}: Procesando {symbol} - {company['description']}")

