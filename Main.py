'''
* Run program from this class
    
TO-DO:
-Add a menu
'''

from OriginalTweets import OriginalTweets
from Config import api

class Main:

    def __init__(self):

        self.version = "v1.0"
        print("Unnamed Twitter Tool " + self.version)


    if __name__ == "__main__":
        
        og = OriginalTweets(api)
        og.run("jessekoolkid321")