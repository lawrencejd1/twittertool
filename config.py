import tweepy
from tweepy import OAuthHandler

#Twitter API Keys and Tokens
consumer_key = ''
consumer_secret = ''

access_token = ''
access_secret = ''

#Authorization
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

