import tweepy
import keys
import sys



def tweet(message):
    try:
        auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
        auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        api.update_status(message)
    except tweepy.TweepError as e:
        # TODO: Add logging
        print("Duplicate Tweet")
