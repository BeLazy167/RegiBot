import pymongo


class Oauth():

    def __init__(self):
        self.TOKEN = 'ODI1MjYyMzU2NDU1MjI3NDAy.YF7Xdg.hCdAd8g694JAMqkuPjJpaXi7q1k'
        self.OWNER_IDS = ['252353540327079936', '669518518777282561','440858271000035328']
        
        #database token
        self.db_link = "mongodb+srv://BeLazy:BeLazy@cluster0.csr3d.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        self.client = pymongo.MongoClient(self.db_link)
        


    def discordTOKEN(self):
        return self.TOKEN , self.OWNER_IDS

    def databaseTOKEN(self):
        return self.client



