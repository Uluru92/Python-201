'''
Using tweepy, create a script that programmatically tweets to your twitter account.

Create a JSON file that includes a number of tweets you want to post.
Your script should read from that JSON file, select some text and tweet it
whenever you run the script.

BONUS: Look into CRON jobs to automate your tweets to go out at scheduled times.
       E.g.: "Don't start without me, I'm nearly there!" every weekday at 9:14... ;P
'''

import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

client = tweepy.Client(
    consumer_key=os.getenv("API_tweepy_consumer_key"),
    consumer_secret=os.getenv("API_tweepy_consumer_secret"),
    access_token=os.getenv("API_tweepy_access_token"),
    access_token_secret=os.getenv("API_tweepy_access_token_secret")
)

try:
    tweet_text = "Hellow World! This tweet was posted using Tweepy + X API Free Tier @CodingNomads #PythonLearning"
    response = client.create_tweet(text=tweet_text)
    tweet_id = response.data['id']
    print(f"🔗 Enlace al tuit: https://twitter.com/user/status/{tweet_id}")
except tweepy.TweepyException as e:
    print("❌ Error al publicar el tuit:", e)
