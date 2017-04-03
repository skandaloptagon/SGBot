import json
import praw
import requests

class RedditManager(object):

    def __init__(self, clientID, secretKey):
        self.reddit = praw.Reddit(client_id=clientID,
                     client_secret=secretKey,
                     user_agent='Linux:SeGBot:0.1 (by /u/SeGBot)')

class SGManager(object):

    def __init__(self, clientID, secretKey):
        self.clientID = clientID
        self.secretKey = secretKey

    def getTicketPrices(artist):
        ticketInfo = ""

        return ticketInfo

class SGBot(object):

    def __init__(self):
        with open("manifest.json","r") as manifest:
            manifest = json.loads(manifest.read().replace('\n',''))
            self.reddit = RedditManager(manifest['Reddit']['clientID'],
                                            manifest['Reddit']['secretKey'])

if __name__ == "__main__":
    bot = SGBot()
