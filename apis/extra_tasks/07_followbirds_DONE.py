'''
Using the tweepy package, build a script that separates twitter handles
into different groups according to the number of their followers.

The classes can be whatever you like (e.g. I used ASCII art birds ;)

CHALLENGE: Also fetch the number of their friends and display the ratio
between followers and friends in an interesting way.
'''

import tweepy
from dotenv import load_dotenv
import os

load_dotenv()
bearer_token = os.getenv("API_tweepy_bearer_token")
client = tweepy.Client(bearer_token=bearer_token)

handles = ["elonmusk", "CodingNomads","JorddyCastroAra"]

def classify_user(followers):
    if followers > 10_000_000:
        return "🦅 Mega Bird"
    elif followers > 1_000_000:
        return "🕊️ Big Bird"
    elif followers > 10_000:
        return "🐤 Medium Bird"
    else:
        return "🐣 Tiny Chick"

for username in handles:
    try:
        user = client.get_user(username=username, user_fields=["public_metrics"]).data
        metrics = user.public_metrics
        followers = metrics["followers_count"]
        following = metrics["following_count"]
        ratio = round(followers / following, 2) if following else "∞"
        label = classify_user(followers)

        print(f"@{username} → {label}")
        print(f"   Followers: {followers}, Following: {following}, Ratio: {ratio}\n")

    except Exception as e:
        print(f"Error fetching {username}: {e}")