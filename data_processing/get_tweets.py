import tweepy
from textblob import TextBlob
import pandas as pd
from .tweets_sentiment import connect, getTweets, preprocessTweet, stem, sentiment

def fetch_tweets(input):
    api=connect()
    tweets=[]

    try:
    # Fetches the tweets using the api
        fetched_data = getTweets(api, input)
        for tweet in fetched_data:
            print(tweet.full_text)
            txt = tweet.full_text
            clean_txt = preprocessTweet(txt) # Cleans the tweet
            stem_txt = TextBlob(stem(clean_txt)) # Stems the tweet
            sent = sentiment(stem_txt) # Gets the sentiment from the tweet
            tweets.append((txt, clean_txt, sent))

        df = pd.DataFrame(tweets, columns= ['tweets', 'clean_tweets','sentiment'])
        df = df.drop_duplicates(subset='clean_tweets')
        df.to_csv('data.csv', index= False)
        return df

    except tweepy.errors.TweepyException as e:
        print("Error : " + str(e))
        exit(1)

   


def get_percentage(df, tweets):
    list=[]; 
    # 0->positive, 1->Negative 2-> Neutral
    ptweets = df[df['sentiment'] == 'positive']
    p_perc = 100 * len(ptweets)/len(tweets)
    list.append(p_perc) 
    ntweets = df[df['sentiment'] == 'negative']
    n_perc = 100 * len(ntweets)/len(tweets)
    list.append(n_perc)

    list.append(100 - p_perc - n_perc)

    print(f'Positive tweets {p_perc} %')
    print(f'Neutral tweets {100 - p_perc - n_perc} %')
    print(f'Negative tweets {n_perc} %')

    return list






    






