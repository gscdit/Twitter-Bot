import tweepy
import time
from time import sleep
import os
from os import environ

#Enter the keys and Secrets of your account
consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q = ('#DituGoogle OR #DITUniversity OR #gscditu OR #gscdit OR #GSCDITU OR #GSCDIT')).items(5):
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet tweets as they are found !!
        #tweet.retweet()
        #print('Retweeted to : @' + tweet.user.screen_name)

        #like the tweets
        #tweet.favorite()
        #print('Liked the tweet : @' + tweet.user.screen_name)

        # Follow the user who tweeted !!
        tweet.user.follow()
        print('Followed : @' + tweet.user.screen_name)

        # Add sleep method to space tweets by 600 seconds each !!
        sleep(600)

    except tweepy.TweepError as e:
        print(e.reason)



