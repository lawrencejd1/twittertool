# Most Popular Tweet Finder

This is a Python script that finds the most recent 3200 tweets from a specified Twitter user and checks if they are original tweets that they posted. The script creates an individual Tweet object for each tweet using Tweet.py, which stores values of the tweets: id, likes, and text. All tweets are put into a list, and an ordered list is made from most liked. The script displays the top specified number of most liked tweets with their text and provides the links of each tweet in the list.

## Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Create and activate a virtual environment.
4. Install the required packages using pip: `pip install tweepy`

## Usage

To use the script, you will need to have a Twitter API key and access tokens. Once you have those, add them to the script.

You can run the script by calling the run() function and passing in the screenName of the user you want to search for.

```
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    originalTweets = OriginalTweets(api)
    originalTweets.run("elonmusk")
```
The script will display the progress of the search and output the top specified number of most liked tweets with their text and links in a tweets.txt file.
