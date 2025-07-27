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

# Solution:  activate virtual enviroment venv37 path: \apis\extra_tasks\venv37 with command: venv37\Scripts\activate
# while venv active run: python -m sandman2 "mysql+pymysql://user:pasword@localhost/stocks_db" with root as user and password as.... cant tell because this file is going to github 
# while running go to: http://localhost:5000/recommendations/
# Topic: Currencies
#       GET: extract company's symbols, API https://finnhub.io/api/v1/stock/symbol?exchange=US&token={api_key}
#       GET: extract recomendations for every company, API https://finnhub.io/api/v1/stock/recommendation?symbol=GWH&token={api_key}
#
# FIRST STEP: ingest API data from at least 1 external source

import requests
import os
from dotenv import load_dotenv
import mysql.connector

# API resources:
load_dotenv()
api_key = os.getenv("API_FINNHUB")
url_companies = f"https://finnhub.io/api/v1/stock/symbol?exchange=US&token={api_key}"


# Data received:
data_finnhub_companies = requests.get(url_companies).json()

# Create a list of every company's symbol. This is a REQUIRED argument to get latest analyst recommendation trends for a company.
data_finnhub_companies_sorted = sorted(data_finnhub_companies, key=lambda x: x["displaySymbol"])
symbol_to_company = {
    item["displaySymbol"]: item["description"]
    for item in data_finnhub_companies_sorted[:100]
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

        # save the data calculated in a list
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

# For the next step, I am using MySQL Workbench, Let's connect:
connection = mysql.connector.connect(
    host= os.getenv("MYSQL_HOST"),
    user= os.getenv("MYSQL_USER"),
    password= os.getenv("MYSQL_PASSWORD"),
    database= os.getenv("MYSQL_DATABASE")
)

cursor = connection.cursor()

# Conection verify 
if connection.is_connected():
    print("✅ Conenection activated.")
else:
    print("❌ Connection error.")

create_table_query = """
CREATE TABLE IF NOT EXISTS recommendations (
    id INT NOT NULL AUTO_INCREMENT,
    symbol VARCHAR(10) NOT NULL,
    company VARCHAR(255),
    strongBuy FLOAT,
    buy FLOAT,
    hold FLOAT,
    sell FLOAT,
    strongSell FLOAT,
    sentiment_score FLOAT,
    PRIMARY KEY (id),
    UNIQUE KEY unique_symbol (symbol)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
"""

cursor.execute(create_table_query)
connection.commit()

# save our API data in the db 
insert_or_update_query = """
    INSERT INTO recommendations 
    (symbol, company, strongBuy, buy, hold, sell, strongSell, sentiment_score)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE 
        company = VALUES(company),
        strongBuy = VALUES(strongBuy),
        buy = VALUES(buy),
        hold = VALUES(hold),
        sell = VALUES(sell),
        strongSell = VALUES(strongSell),
        sentiment_score = VALUES(sentiment_score)
"""

for item in recommendation_data:
    values = (
        item["symbol"],
        item["company"],
        item["strongBuy"],
        item["buy"],
        item["hold"],
        item["sell"],
        item["strongSell"],
        int(item["sentiment_score"])
    )
    cursor.execute(insert_or_update_query, values)

# Make a query to explore data
cursor.execute("SELECT * FROM recommendations")
rows = cursor.fetchall()

# show each row from select all query
for row in rows:
    print(row)

# Using sandman2 execute the API
url_api_recomendations = "http://localhost:5000/recommendations"
data_recommendations = requests.get(url_api_recomendations).json()

print("\nTop 10 sentiment score, data from sandman2:\n")
top_10 = sorted(data_recommendations["resources"], key=lambda x: x["sentiment_score"], reverse=True)[:10]

for index, entry in enumerate(top_10):
    print(f"TOP {index + 1}: Symbol: {entry['symbol']}, Company: {entry['company']}, sentiment score: {entry['sentiment_score']}")

connection.commit()
cursor.close()
connection.close()