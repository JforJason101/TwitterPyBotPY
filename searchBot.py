import tweepy
import logging
import time

print("Hi! This is the first iteration of the Twitter Bot!")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

consumer_key = "v7IYdMEWVFEQQ3mWpVicChW5G"
consumer_secret = "PAsIyVvRL63jwEDzj6Yg8utwYQNKWp1jlm1xTvadDVjyLzmlOu"
key = "1342268696425758722-iE39zyqh1sB5eHwk6D9vLwBoavt2db"
secret = "TdgmGcEpQijYML7o6PyyoUq7Dy5vFcT8TyQNR44JlE6m5"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
try:
    api.verify_credentials()
except Exception as e:
    logger.error("Error during authentication", exc_info=True)
    raise e
logger.info("Authenticated")

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

hashtag = "#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


def search_bot():
    # While it retrieves tweets
    print("Searching for tweets...")
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
            api.create_favorite(last_fav_tweet)
            print("Liked!", flush=True)

            # Stores the ID in the text file...
            store_last_seen(FILE_NAME, tweet.id)

        except tweepy.TweepError as e:
            print("Already Replied! More info in the next line:", flush=True)
            print(e.reason)


while True:
    search_bot()
    time.sleep(15)
