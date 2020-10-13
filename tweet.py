'''
Turns tweet into a more simpler object to grab specific data from
'''
class Tweet:

    def __init__(self, id, likes, text):
        self.id = id
        self.likes = likes
        self.text = text
