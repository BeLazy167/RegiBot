import pymongo


class Oauth():

    def __init__(self):
        self.TOKEN = 'YOUR DISCORD BOT PUBLIC KEY HERE'
        self.OWNER_IDS = ['YOUR USER ID HERE']
        
        #database token
        self.db_link = "your Mongo database link here"
        self.client = pymongo.MongoClient(self.db_link)
        


    def discordTOKEN(self):
        return self.TOKEN , self.OWNER_IDS

    def databaseTOKEN(self):
        return self.client



