import tweepy
import os
import requests

bearer_token = "AAAAAAAAAAAAAAAAAAAAAKVsbgEAAAAAx%2BIlwGEstd7pTJpyqcZzVjjViFU%3D676SIt5xyGfCA9o14DV0QPHCauteZ5oRyiJvqY32pznuX9DxJE"
api_key_public = "hLu0UQu7yVurEJzf8L9AAxElE"
api_key_secret = "yyhTrQDaCiJizHIWTTTKRjBoTkqFgPZWJSfnd4cqi6YhMcwiU1"
client_id = "dVJYcFV4SmZIUnR5dTEyYzhLeEU6MTpjaQ"
client_secret = "aPJdFRXC19eW-b2WGn8CLpNOWMe2cMIW2zHuucHyWZWKLa1W_I"

client = tweepy.Client(bearer_token, return_type = requests.Response)

def return_user_id(screen_name):
    # Add public username to pull tweets from
    twitter_id_request = client.get_user(username=screen_name)
    user_id = (int(twitter_id_request.json()['data']['id']))
    return user_id

# Pull in tweets and public data
def return_tweets_and_public_metrics(screen_name):
    user_id = return_user_id(screen_name)
    tweets = client.get_users_tweets(user_id, tweet_fields = ['public_metrics'])
    tweets = tweets.json()['data']
    out_data = []
    for tweet in tweets:
        tweet_id = tweet['id']
        tweet_text = tweet['text']
        like_count = tweet['public_metrics']['like_count']
        retweet_count = tweet['public_metrics']['retweet_count']
        reply_count = tweet['public_metrics']['reply_count']
        quote_count = tweet['public_metrics']['quote_count']
        out_tweet_dict = {'id': tweet_id, 
                        'text': tweet_text, 
                        'like_count': like_count,
                        'retweet_count': retweet_count,
                        'reply_count': reply_count,
                        'quote_count': quote_count}
        out_data.append(out_tweet_dict)
    return out_data
        
