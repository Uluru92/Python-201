'''
Using tweepy, create a script that programmatically tweets to your twitter account.

Create a JSON file that includes a number of tweets you want to post.
Your script should read from that JSON file, select some text and tweet it
whenever you run the script.

BONUS: Look into CRON jobs to automate your tweets to go out at scheduled times.
       E.g.: "Don't start without me, I'm nearly there!" every weekday at 9:14... ;P

'''

import tweepy
import json
import random
from dotenv import load_dotenv
import os

load_dotenv()

client = tweepy.Client(
    consumer_key=os.getenv("API_tweepy_consumer_key"),
    consumer_secret=os.getenv("API_tweepy_consumer_secret"),
    access_token=os.getenv("API_tweepy_access_token"),
    access_token_secret=os.getenv("API_tweepy_access_token_secret")
)

def post_random_tweet():
    with open(, "r", encoding="utf-8") as f:
        tweets = json.load(f)
    tweet = random.choice(tweets)

    try:
        client.create_tweet(text=tweet)
        print(f"✅ Tweet posted: {tweet}")
    except Exception as e:
        print(f"❌ Error posting tweet: {e}")

if __name__ == "__main__":
    post_random_tweet()