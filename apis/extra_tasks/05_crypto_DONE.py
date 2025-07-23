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
# I am going to catch 1 bitcoin value per minute.

import requests
import os
import time
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
api_key = os.getenv("API_COINLAYER")
url_coinlayer = f"http://api.coinlayer.com/live?access_key={api_key}"

btc_history = {}

for lapse in range(10):
    try:
        data_coinlayer = requests.get(url_coinlayer).json()

        if data_coinlayer.get("success"):
            query_time = data_coinlayer['timestamp']
            query_bitcoin = data_coinlayer['rates']['BTC']
            readable_time = datetime.fromtimestamp(query_time).strftime('%Y-%m-%d %H:%M:%S')
            btc_history[readable_time] = query_bitcoin
            
            print(f"{readable_time} → BTC: ${query_bitcoin}")
        
        else:
            print("API Error:", data_coinlayer.get("error", "Unknown error"))

    except Exception as e:
        print("Request failed:", e)

    time.sleep(60)

if btc_history:
    highest_time, highest_price = max(btc_history.items(), key=lambda item: item[1])
    print("\nHighest BTC Price in 10 Minutes:")
    print(f"{highest_time} → ${highest_price}")
else:
    print("No data collected.")