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

# Pseudocode

# 1. Retrieve the user ID of @CodingNomads
# 2. Get their latest tweets
# 3. Extract the ID of the most recent tweet
# 4. Transform the tweet data:
#    - Get tweet text and creation date
#    - Calculate text length
#    - Check if it mentions the word "python"
# 5. Store the transformed data in a MySQL database called MYSQL_DB_text
# 6. Serve the stored data using Sandman2:
#    python -m sandman2 "mysql+pymysql://root:<your_password>@localhost/MYSQL_DB_text"
#    (Note: I don't include the password here because this code will be uploaded to GitHub)
#    In the navegator go to: http://127.0.0.1:5000/codingnomads_last_tweet and look at the data at this endpoint!

import tweepy
import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()
bearer_token = os.getenv("API_tweepy_bearer_token")

client = tweepy.Client(bearer_token=bearer_token)

# 1. Get the user ID of @CodingNomads
user_response = client.get_user(username="CodingNomads")
user_id = user_response.data.id
print(f"User ID for CodingNomads: {user_id}")

# 2. Get latest tweets
tweets_response = client.get_users_tweets(
    id=user_id,
    max_results=5,
    tweet_fields=["created_at", "public_metrics"]
)

# 3. Get the most recent tweet
latest_tweet = tweets_response.data[0] if tweets_response.data else None

if latest_tweet:
    print(f"Latest tweet ID: {latest_tweet.id}")
    print(f"Text: {latest_tweet.text}")
else:
    print("No tweets found.")
    exit()

# 4. Function to transform tweet (receives Tweepy Tweet object)
def transform_tweet(tweet_data):
    text = tweet_data.text
    date = tweet_data.created_at  # datetime.datetime object
    length = len(text)
    contains_python = "python" in text.lower()

    return {
        "tweet_id": str(tweet_data.id),
        "text": text,
        "date": date,
        "length": length,
        "contains_python": contains_python
    }

tweet = transform_tweet(latest_tweet)
print("Transformed tweet:", tweet)

# 5. Insert into MySQL database
conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    port = int(os.getenv("MYSQL_PORT")),
    database=os.getenv("MYSQL_DB_TEXT"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD")
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS codingnomads_last_tweet (
    tweet_id VARCHAR(100) PRIMARY KEY,
    text TEXT,
    date DATETIME,
    length INT,
    contains_python BOOLEAN
)
""")



for tweet_data in tweets_response.data:
    tweet = transform_tweet(tweet_data)
    print("Insertando tweet:", tweet["tweet_id"])

    cur.execute("""
        INSERT INTO codingnomads_last_tweet (tweet_id, text, date, length, contains_python)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            text = VALUES(text),
            date = VALUES(date),
            length = VALUES(length),
            contains_python = VALUES(contains_python)
    """, (
        tweet["tweet_id"],
        tweet["text"],
        tweet["date"],
        tweet["length"],
        tweet["contains_python"]
    ))
    
conn.commit()
cur.close()
conn.close()