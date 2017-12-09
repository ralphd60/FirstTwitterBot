#!/usr/bin/python3

# Import Tweepy, sleep, datetime, creds.py
import tweepy
import datetime
from time import sleep
from creds import *
import signal

def retweeter(query):
    deltatime = datetime.timedelta(days = 1)
    start = datetime.date.today() - deltatime
    end = datetime.date.today()
    print(deltatime)
    print('Start time: ' + str(start))
    print('End time: ' + str(end))
    # Access and authorize our Twitter credentials from credentials.py
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    # For loop to iterate over tweets with NY Isles
    for tweet in tweepy.Cursor(api.search,
                               q = query,
                               since = start,
                               until = end,
                               lang ='en').items():
        #print('This is the object ', tweet)

        if datetime.date.today() != end:
            start = datetime.date.today() - deltatime
            end = datetime.date.today()
        try:
            print('Tweet by: @' + tweet.user.screen_name)
            # Retweet tweets as they are found
            tweet.retweet()
            print('Retweeted the tweet ', start, ' ', end)
            sleep(1440)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

        if datetime.date.today() != end:
            start = datetime.date.today() - deltatime
            end = datetime.date.today()

if __name__ == '__main__':
    while True:
         try:
            print('Starting while true')
            retweeter("'New York Islanders' AND -giving")
            print('sleeping within the while true')
            sleep (60)
         except KeyboardInterrupt:
            print('Bye')
            sys.exit()
