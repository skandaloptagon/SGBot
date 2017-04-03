import json
import os
import praw
import requests
import re

class RedditManager(object):

    def __init__(self, clientID, secretKey):
        self.reddit = praw.Reddit(client_id=clientID,
                     client_secret=secretKey,
                     user_agent='Linux:SeGB:0.1 (by /u/SeGBot)')

    def check_for_bot_requests(self, sub):


        posts_replied_to = []
        if os.path.isfile("posts_replied_to.txt"):
            with open("posts_replied_to.txt", "r") as f:
                posts_replied_to = f.read()
                posts_replied_to = posts_replied_to.split("\n")
                posts_replied_to = list(filter(None, posts_replied_to))

        subreddit = self.reddit.subreddit(sub)
        for submission in subreddit.hot(limit=5):
            if submission.id not in posts_replied_to:
                if re.search("i love python", submission.title, re.IGNORECASE):
                    print("Bot replying to : ", submission.title)
                    posts_replied_to.append(submission.id)
            

class SGManager(object):

    def __init__(self, clientID, secretKey):
        self.clientID = clientID
        self.secretKey = secretKey

    def getTicketPrices(self, artist):
        r = requests.get('https://api.seatgeek.com/2/events?q={}&client_id={}&client_secret={}'.format(artist,self.clientID,self.secretKey))
        response_json = json.loads(r.text)

        ticketInfo = ""

        for thing in response_json['events']:
            title = thing['title']
            url = thing['url']
            tickets = thing['stats']['listing_count']
            avg_price = thing['stats']['average_price']
            line = '({})[{}]\n\t{} tickets listed at an average price of ${}\n'.format(title,url,tickets,avg_price)
            
            ticketInfo += line
            #print json.dumps(thing, indent=4, separators=(',', ': '))

        return ticketInfo

class SGBot(object):

    def __init__(self):
        with open("manifest.json","r") as manifest:
            manifest = json.loads(manifest.read().replace('\n',''))

            self.reddit = RedditManager(manifest['Reddit']['clientID'],
                                            manifest['Reddit']['secretKey'])
            self.sg = SGManager(manifest['SG']['clientID'],
                                            manifest['SG']['secretKey'])

if __name__ == "__main__":
    bot = SGBot()
    print bot.sg.getTicketPrices("boston+celtics")
    bot.reddit.check_for_bot_requests("pythonforengineers")
