import tweepy
from bs4 import BeautifulSoup
import requests


def pokemon_tweet(numOfPosts):
    auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")
    auth.set_access_token("access_token", "access_token_secret")

    api = tweepy.API(auth)
    messages = set()
    page = "pokemon"
    while True:
        tweets = api.user_timeline(
            screen_name=page, count=200, include_rts=False, tweet_mode="extended"
        )
        if tweets:
            for tweet in tweets[:numOfPosts]:
                message = tweet.full_text.replace("\n", " ").strip()
                if message not in messages:
                    return message
                messages.add(message)
        else:
            print("List is empty/account name not found.")


numOfPosts = 1

pokemon_tweet(numOfPosts)
