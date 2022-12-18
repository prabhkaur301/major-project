import re 
import tweepy 
import nltk
import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from textblob import TextBlob


def connect():
  # Replace the xxxxx with your twitter api keys
    api_key= 'Skeo5Fb5WA1GduHS00LPmTysi'
    api_key_secret ='xAi0zxRjGiDbbErtCTM7PbQKOwRwG1l2d6ZhzGx24hEAsEa7rZ'
    access_token='1572951053997580288-P7TlFQ6aGjnTv0pexl6MojJ4tiLzsB'
    access_token_secret='iRQzZhjTcNe1goSFHN4aXYBMxdFkIvvlo7TNVeK1Hcx7g'
    try:
        auth_handler= tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
        auth_handler.set_access_token(access_token, access_token_secret)
        api= tweepy.API(auth_handler)
        return api
    except:
        print("Error")
        exit(1)


def getTweets(api, query):
    tweet_amount=20
    query_res= tweepy.Cursor(api.search_tweets, q=query, lang='en', tweet_mode='extended').items(tweet_amount)
    return query_res

def preprocessTweet(tweet):
    tweet = tweet.lower()
    # Removes all mentions (@username) from the tweet since it is of no use to us
    tweet = re.sub(r'(@[A-Za-z0-9_]+)', '', tweet)
    # Removes any link in the text
    tweet = re.sub('http://\S+|https://\S+', '', tweet)
    # Only considers the part of the string with char between a to z or digits and whitespace characters
    # Basically removes punctuation
    tweet = re.sub(r'[^\w\s]', '', tweet)
    # Removes stop words that have no use in sentiment analysis 
    tweet_tokens = word_tokenize(tweet)
    tweet = [word for word in tweet_tokens if not word in stopwords.words()]

    tweet = ' '.join(tweet)
    return tweet


def stem(tweet):
  # This function is used to stem the given sentence
  porter = PorterStemmer()
  token_words = word_tokenize(tweet)
  stem_sentence = []
  for word in token_words:
    stem_sentence.append(porter.stem(word))
  return " ".join(stem_sentence)
    

def sentiment(cleaned_text):
  # Returns the sentiment based on the polarity of the input TextBlob object
  if cleaned_text.sentiment.polarity > 0:
    return 'positive'
  elif cleaned_text.sentiment.polarity < 0:
    return 'negative'
  else:
    return 'neutral'










