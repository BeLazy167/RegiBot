import re
import random
from cogs import configbot
import pymongo
import string

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

clientObj = Oauth()
client = clientObj.databaseTOKEN()

def random_string_generator():
	#to generate random team name for one time  
	allowed_chars = string.ascii_letters
	return ''.join(random.choice(allowed_chars) for _ in range(10))

def addServerInfo(serverID, serverName, textChannels, Admin, roles):
	#to add all the serverinfo when the bot is addded to the server for 1st time
    dataBase = client[serverID]
    serverInfo = dataBase['serverInfo']
    serverData = {
        "server_id": serverID,
        "server_name": serverName,
        "text_channels": textChannels,
        "roles": roles,
        "Admin": Admin
    }
    serverInfo.insert_one(serverData)


def removeServerInfo(serverID):
	#to delete all server info when the bot is kicked from the server
	client.drop_database(serverID)
	
def eventCheck(serverID,eventName):
	#to check that the event is present for user to register refer maintemplate function
	dataBase = client[serverID]
	availableEvents = dataBase.list_collection_names()
	if eventName in availableEvents:
		event = dataBase[eventName]
		return event,dataBase
	else:
	#if no scuh event is found it returns the tag
		tag = 1
		return tag , None

def createEventAdmin(serverID, eventName):
	#this is called when the admin has created the event for the first time it will store 1 temp value and delete it so the collection is not removed (if we create one collection and dont enter any data it does not sticks)
	dataBase = client[serverID]
	availableEvents = dataBase.list_collection_names()
	if eventName not in availableEvents :
		event = dataBase[eventName]
		datatoEnter = {
			"_id":str(random_string_generator()),
			"passcode":0000,
			"discordID":"discordID",
			"name":"name",
			"age":"age",
			"email":"emailID"
			}
		event.insert_one(datatoEnter)
		event.delete_one({"passcode":0000})
		return event ,dataBase
	elif eventName in availableEvents:
		#if event is already there then then it will return the tag 
		event = dataBase[eventName]
		tag = 'same event is already present'
		return tag,dataBase
	

	
def teamNameCheck(event,teamName):
	#this function checks that if the team name is already there or not ,if not it creates the team and returns the passcode
	if event.find_one({"_id":teamName}) is None:
		datatoEnter = {
				"_id":teamName,
				'defId':"1"
			}
		event.insert_one(datatoEnter)
		event.update_one({"_id": teamName}, {"$set": {'passcode': random.randint(1000,9999)}})
		dataEvent = event.find_one({"_id":teamName})
		passcode = dataEvent['passcode']
		x = 0
		dataEvent = event.find_one({'_id':teamName})
		return x,passcode,dataEvent
	else:
		#returns the team data id present 
		x = 1
		dataEvent = event.find_one({'_id':teamName})
		return x,None,dataEvent


def mainTemplate(serverID,eventName,teamName,discordID,name,age,emailID,passcode = None):
	event,dataBase = eventCheck(serverID,eventName)
	if event == 1 :
		tag = 'no such event found'
		return tag ,None

	x,passcode1,dataEvent = teamNameCheck(event,teamName)
	
	if x == 0:
		#after creating team for 1st time the user who created the team will be registerd
		event.update_one({"_id": teamName}, {"$push": {
			"discordID":discordID,
			"name":name,
			"age":age,
			"email":emailID	
		}})
		return teamName,passcode1

	else:
		#if the other memeber of the team enters teamname && passcode they will be registerd in the team 
		if passcode == None:
			tag = 'enter passcode'
			return tag,None
		
		if dataEvent['_id'] == teamName and dataEvent['passcode'] == passcode:
			event.update_many({'_id': teamName}, {'$push': {'discordID':discordID,'name':name,'age':age,'email':emailID }})
			tag = 'registration done'
			return tag,None
		else:
			tag = 'check teamname or passcode'
			return tag, None


# serverID = "669168139061166120"
# eventName = 'hcaks2021'
# teamName = 'lazix2'
# discordID = '660518518777282561'
# name = 'JDDdday'
# age = '25'
# emailID = 'JadaDADAdayP@gmail.com'
# passcode = 7235
# print(mainTemplate(serverID,eventName,teamName,discordID,name,age,emailID,passcode))



# def emailCheck(email):
# 	checkedEmail = []
# 	for emails in email:
		
# 		if re.match('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', emails):
# 				checkedEmail.append(emails)
# 		else:
# 				return None
# 	return checkedEmail