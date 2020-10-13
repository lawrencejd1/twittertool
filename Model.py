'''
* Class used for storing functions
'''

import tweepy
import sys
from Tweet import Tweet
from Config import api

class Model:

    def __init__(self):
        self.link = "https://twitter.com/twitter/statuses/"

    #Takes tweets from api.user_timeline and returns
    def GetOriginalTweets(self, allTweets, newTweets,):
        
        for x in range(len(newTweets)):

            #tweet = api.get_status(newTweets[x].id, tweet_mode="extended")
            tweet = newTweets[x]
            #print(tweet)

            if(not tweet.retweeted) and ('RT' not in tweet.full_text) and ('@' not in tweet.full_text):
                
                singleTweet = Tweet(tweet.id, tweet.favorite_count, tweet.full_text)
                # tweetID = tweet.id
                # numOfLikes = tweet.favorite_count
                # tweetText = tweet.full_text

                allTweets.append(singleTweet)

    def TweetToFile(self, interval, tweetList, linkOnly):
        self.file = open("tweets.txt", "a")
        if(linkOnly == False):
            try:
                tweet = tweetList[interval]
                tweetLink = self.link + str(tweet.id)
                self.file.write("------------------\n")
                self.file.write("Top Tweet #" + str(interval + 1) + ": \n")
                self.file.write(tweet.text + "\n")
                self.file.write("Link: " + tweetLink + "\n")
                self.file.write("------------------\n")
            except Exception as e:
                print(e)
                print("No original tweets found within the number of tweets")
        else:
            try:
                tweet = tweetList[interval]
                tweetLink = self.link + str(tweet.id)
                self.file.write("--------------\n")
                self.file.write("Tweet #" + str(interval + 1) + " ")
                self.file.write("Link: " + tweetLink + "\n")
                self.file.write("--------------\n")
                self.file.write("")
            except Exception as e:
                print(e)
                print("No original tweets found within the number of tweets")

        self.file.close()