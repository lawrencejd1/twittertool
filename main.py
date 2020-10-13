'''
* Run program from this class
    
TO-DO:
-Add a menu
'''

from originaltweets import OriginalTweets
from config import api

class Main:

    def __init__(self):

        self.version = "v1.0"
        print("Unnamed Twitter Tool " + self.version)


    if __name__ == "__main__":
        userName = ""
        og = OriginalTweets(api)
        og.run(userName)