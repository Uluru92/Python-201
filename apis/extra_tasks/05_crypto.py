'''
https://coinmarketcap.com/api/pricing/
Use the CoinMarketCap API, to repeatedly fetch the price of Bitcoin for a duration of 10 minutes.
Store each value in a dictionary that uses the time of query as a key.

After the script stopped running, determine programmatically at what query time the price
was the highest, and when the lowest.

HINTS:
- You can pick a different API from this list: https://github.com/public-apis/public-apis#cryptocurrency
- You may have to request an API key first. If you need one, remember to include it in your queries.
- You can use packages from the standard library, e.g. for time keeping and dates

BONUS: Explore the `logging` package for easier tracking

'''

# SOLUTION
# For this exercise I am going to use Coinlayer API http://api.coinlayer.com/

import requests
import os
from dotenv import load_dotenv
from pprint import pprint

# API resources:
load_dotenv()
api_key = os.getenv("API_COINLAYER")
url_coinlayer = f"http://api.coinlayer.com/live?access_key={api_key}"
data_coinlayer = requests.get(url_coinlayer).json()

pprint(data_coinlayer)