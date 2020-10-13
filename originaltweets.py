'''
* Finds most recent 3200 tweets from a specified twitter user and checks if they are
tweets that they posted

* Creates an individual Tweet object for each tweet using Tweet.py 
which stores values of the tweets: id, likes, and text

* Puts all tweets into a list

* Makes an ordered list from most liked

* Displays top specified number of most liked tweets with their text 
and then provides the links of each tweet in the list
'''

import tweepy
import sys
import model
import tweet

class OriginalTweets:

   def __init__(self, api):

      self.api = api
      file = open("tweets.txt", "w")
      file.write("-------------------DATA GENERATED FROM ORIGINALTWEETS.PY-------------------\n\n")
      file.close()

      print("")
      print("")
      print("")
      print("Launching Most Popular Tweet Finder ")
      print("")

   def run(self, screenName):
      #Getting model class for functions
      m = model.Model()
      #Variables------
      #@username
      ##screenName = "elonmusk"

      #number of tweets gathered on one call (default = 200)
      count = 200

      #Instantiating and Adding Most Recent Original Tweets (0 through 'count')
      allTweets = [] #all original tweets posted by user
      orderedTweets = [] #original tweets ordered from most liked to least liked
      totalTweetNum = 0 #total Number of Tweets Searched
      currentHighestFav = 0

      #Program Start
      newTweets = self.api.user_timeline(screenName, count=count, tweet_mode="extended")
      
      totalTweetNum += len(newTweets)
      oldestID = newTweets[-1].id -1

      print("")
      print(f"Finding original tweets from @{screenName}...")
      print("")

      m.GetOriginalTweets(allTweets, newTweets)

      print("Tweets added!")
      print("")

      #Search through tweets after the most recent (after 'count' amount)
      while(len(newTweets)>0):

         #print(f"getting tweets before {oldestID}")

         newTweets = self.api.user_timeline(screenName, count=count, max_id=oldestID, tweet_mode="extended")
         totalTweetNum += len(newTweets)
         
         print(f"{totalTweetNum} total tweets searched")

         m.GetOriginalTweets(allTweets, newTweets)

         try:
            oldestID = newTweets[-1].id -1
            print(f"{len(allTweets)} original tweets added so far")
         except:
            print("Max Limit Reached")

         
         print("")

      for tweet in range(len(allTweets)):
         #tweetID = list(allTweets[tweet].keys())[0]

         #tweetLikes = list(allTweets[tweet].keys())[1]
         tweetLikes = allTweets[tweet].likes

         #tweetLikes = api.get_status(tweetID).favorite_count

         if(tweetLikes > currentHighestFav):
            currentHighestFav = tweetLikes
            orderedTweets.insert(0, allTweets[tweet])
         else:
            orderedTweets.append(allTweets[tweet])

      #Top Tweets Menu and List
      for top in range(3):
         m.TweetToFile(top, orderedTweets, False)

      #Ordered Tweets Menu and List
      file = open("tweets.txt", "a")
      file.write("\n\n")
      file.write("------------------ORDERED TWEETS------------------\n")
      file.write("(Most liked to least liked)\n\n")
      file.close()

      for x in range(len(orderedTweets)):
         m.TweetToFile(x, orderedTweets, True)

      print("Finished!")