#!/usr/bin/python3

# Import Tweepy, sleep, datetime, creds.py
import tweepy
import datetime
import logging
from time import sleep
from creds import *
import signal

logging.basicConfig(filename='tweet.log', filemode='w', level=logging.INFO)
logger = logging.getLogger(__name__)

def retweeter(query):
    start = datetime.date.today()
    logging.info('Start time: ' + str(start))
    # Access and authorize our Twitter credentials from credentials.py
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # For loop to iterate over tweets with NY Isles
    # for tweet in tweepy.Cursor(api.search, q=query, since=start, until=end, lang='en').items():
    for tweet in tweepy.Cursor(api.search, tweet_mode = 'extended', q = query, since = start, rpp = 100, lang ='en').items():
        try:
            logging.info('Tweet by: @' + tweet.user.screen_name)
            logging.info('Created: ' + str(tweet.created_at))
            # Retweet tweets as they are found
            tweet.retweet()
            logging.info('Retweeted the tweet ' + str(start))
            logging.info('Sleep within Cursor')
            sleep(180)
        except tweepy.RateLimitError:
            time.sleep(15 * 60)
        except tweepy.TweepError as e:
            logging.warning(e.reason)
        except StopIteration:
            break


if __name__ == '__main__':
    while True:
         try:
            logging.info('Starting while true statement')
            retweeter("'New York Islanders' AND -giving")
            # when the cursor page is complete, it will come out and hit the below
            logging.info('sleeping within the while true')
            sleep (60)
         except KeyboardInterrupt:
            logging.info('Bye')
            sys.exit()
