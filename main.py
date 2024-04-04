import tweepy
from textblob import TextBlob
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get('API_KEY')
api_key_secret = os.environ.get('API_KEY_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
search_query = input('What would you like to search?')
public_tweets = api.search_tweets(search_query)

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis)