#!/usr/bin/python3
import config
import threading
from time import time
from threading import Timer
import tweepy

interval_number = 60.0 * 60.0 * 5.0
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)

def tweet(text):
    api.update_status(text[:140])

def tweet_with_media(filename, text):
    api.update_status(filename, text[:140])

def interval_func():
    tweet("Testing the interval function " + str(time()))
    Timer(interval_number, interval_func).start()

Timer(interval_number, interval_func).start()

#monday - wholesome memes
#tuesday - cats
#wednesday - temp: wholesome memes
#thursday - dogs
#friday - fortunes
#saturday - temp: wholesome memes
