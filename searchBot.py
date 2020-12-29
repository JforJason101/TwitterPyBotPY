import tweepy
import logging
import time
import os
from os import environ

print("Hi! This is the first iteration of the Twitter Bot!")
time.sleep(5)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

consumer_key = "F7h7NoPTabp1XDADhBboO11lX"
consumer_secret = "GoOYoFJ82or7XrKZF5yeN0rLz37QifH5DGilDURZTT34drnatw"
key = "1342268696425758722-l3nuC7FzCTHEAE1gWvwEpfyOoeJjiP"
secret = "gnA638d7G1OIxzKrz0Xh1y9pvoLVIxG3LGc4PAsVqv3nw"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
try:
    api.verify_credentials()
except Exception as e:
    logger.error("Error during authentication", exc_info=True)
    raise e
logger.info(" --> AUTHENTICATED!")

### ID --> READ and WRITE

FILE_NAME = "last_seen.txt"


# READ
def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


# WRITE
def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


### ID --> READ and WRITE

hashtag = "#searchBotTester123"


def search_bot():
    time.sleep(3)
    # While it retrieves tweets
    print("Retrieving...")
    # While it retrieves tweets

    tweets = api.search(hashtag, tweet_mode='extended')

    # FOR-LOOP
    for tweet in reversed(tweets):
        if not tweet:
            return
        try:
            print(str(tweet.id) + ' - ' + tweet.user.screen_name + ' - ' + tweet.full_text, flush=True)
            last_fav_tweet = tweet.id
            api.update_status(f"@{tweet.user.screen_name} hello world!", tweet.id)
            print("Replied!", flush=True)
            time.sleep(2)
            api.create_favorite(last_fav_tweet)
            print("Liked!", flush=True)

            # Stores the ID in the text file...
            store_last_seen(FILE_NAME, tweet.id)

        except tweepy.TweepError as e:
            print("\033[1;36;40m Already Replied! More info in the next line: \033", flush=True)
            print("---------------------------------------------------")
            print(f"\033[1;32;40m {e.reason} \033")


while True:
    search_bot()
    time.sleep(15)
