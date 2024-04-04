import tweepy
from textblob import TextBlob
from dotenv import load_dotenv
import os
import csv

load_dotenv()

def get_sentiment_label(sentiment_score):
    if sentiment_score > 0.7:
        return 'Strongly Positive'
    elif sentiment_score > 0.3:
        return 'Positive'
    elif sentiment_score > -0.3:
        return 'Neutral'
    elif sentiment_score > -0.7:
        return 'Negative'
    else:
        return 'Strongly Negative'

api_key = os.environ.get('API_KEY')
api_key_secret = os.environ.get('API_KEY_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
search_query = input('What would you like to search?')
public_tweets = api.search_tweets(search_query)

with open(f'{search_query}_sentiment_analysis.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Tweet Text', 'Sentiment Label'])

    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        sentiment_score = analysis.sentiment.polarity

        sentiment_label = get_sentiment_label(sentiment_score)

        csv_writer.writerow([tweet.text, sentiment_label])
    
    print(f"Sentiment analysis results for search query: {search_query} were saved to {search_query}_sentiment_analysis.csv")