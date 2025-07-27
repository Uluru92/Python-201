'''
Create an API that serves textual information.

What topic your API is about is your own choice,
however it needs to fulfill the following specs:
* ingest API data from at least 1 external source
* combine (and/or manipulate) the received data in a meaningful way
* store your altered data in a Postgres database
* serve the data at an endpoint (e.g. using sandman2)

TIP: consider using data from twitter or slack (but anything goes)!
'''

import os
import tweepy
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")
print(f"Conectando a: {database_url}")

# --- Autenticación con Twitter (X) ---
auth = tweepy.OAuth1UserHandler(
    os.getenv("API_tweepy_consumer_key"),
    os.getenv("API_tweepy_consumer_secret"),
    os.getenv("API_tweepy_access_token"),
    os.getenv("API_tweepy_access_token_secret")
)
api = tweepy.API(auth)

# --- Obtener últimos 3 tuits de CodingNomads ---
tweets = api.user_timeline(
    screen_name="CodingNomads",
    count=3,
    tweet_mode="extended"
)

# --- Conexión MySQL ---
conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    port=os.getenv("MYSQL_PORT"),
    database=os.getenv("MYSQL_DB_text"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD")
)
cur = conn.cursor()

# --- Crear tabla si no existe ---
cur.execute("""
CREATE TABLE IF NOT EXISTS codingnomads_tweets (
    id VARCHAR(100) PRIMARY KEY,
    text TEXT,
    created_at DATETIME,
    likes INT,
    retweets INT
)
""")

# --- Insertar o actualizar tuits ---
for t in tweets:
    cur.execute("""
        INSERT INTO codingnomads_tweets (id, text, created_at, likes, retweets)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            text = VALUES(text),
            likes = VALUES(likes),
            retweets = VALUES(retweets)
    """, (
        t.id_str,
        t.full_text.replace("\n", " ").strip(),
        t.created_at,
        t.favorite_count,
        t.retweet_count
    ))

conn.commit()
cur.close()
conn.close()

print("✅ Tuits actualizados en MySQL")

