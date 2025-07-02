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


# Data received:
data_finnhub_companies = requests.get(url_companies).json()

# Create a list of every company's symbol. This is a REQUIRED argument to get latest analyst recommendation trends for a company.
symbol_to_company = {
    item["displaySymbol"]: item["description"]
    for item in data_finnhub_companies[:20]  # limit to 20 for testing porpuses
}
symbols = list(symbol_to_company.keys())

recommendation_data = []

for index, symbol in enumerate(symbols):
    url_recommendation = f"https://finnhub.io/api/v1/stock/recommendation?symbol={symbol}&token={api_key}"
    response = requests.get(url_recommendation)
    
    if response.status_code == 200 and response.json():
        all_recommendations = response.json()

        # manipulate data
        total_entries = len(all_recommendations)
        strong_buy = sum(r.get("strongBuy", 0) for r in all_recommendations)/ total_entries
        buy = sum(r.get("buy", 0) for r in all_recommendations)/ total_entries
        hold = sum(r.get("hold", 0) for r in all_recommendations)/ total_entries
        sell = sum(r.get("sell", 0) for r in all_recommendations)/ total_entries
        strong_sell = sum(r.get("strongSell", 0) for r in all_recommendations)/ total_entries

        # calculate a new score based on the last recomendations for each company
        sentiment_score = strong_buy + 0.5 * buy - 0.5 * sell - strong_sell
        description = symbol_to_company.get(symbol, "unknown")

        recommendation_data.append({
            "symbol": symbol,
            "company": description,
            "strongBuy": round(strong_buy, 2),
            "buy": round(buy, 2),
            "hold": round(hold, 2),
            "sell": round(sell, 2),
            "strongSell": round(strong_sell, 2),
            "sentiment_score": round(sentiment_score, 2)
        })

        print(f"{index}: {symbol} procesado con promedio de {total_entries} entradas.")
    else:
        print(f"{index}: {symbol} - sin datos o error ({response.status_code})")

# Mostrar resultados
pprint(recommendation_data)
