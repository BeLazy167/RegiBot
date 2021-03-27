import re
import random
from pymongo import database
import config
import string

clientObj = config.Oauth()
client = clientObj.databaseTOKEN()

def random_string_generator():
	allowed_chars = string.ascii_letters
	return ''.join(random.choice(allowed_chars) for x in range(10))

def addServerInfo(serverID, serverName, textChannels, Admin, roles):

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
	client.drop_database(serverID)


def createEvent(serverID, eventName):
	
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
	else:
		event = dataBase[eventName]
		return event,dataBase

	
def teamNameCheck(event,teamName):
	if event.find_one({"_id":teamName}) is None:
		datatoEnter = {
				"_id":teamName
			}
		event.insert_one(datatoEnter)
		event.update_one({"_id": teamName}, {"$set": {'passcode': random.randint(1000,9999)}})
		dataEvent = event.find_one({"_id":teamName})
		passcode = dataEvent['passcode']
		x = 0
		dataEvent = event.find_one({'_id':teamName})
		return x,passcode,dataEvent
	else:
		x = 1
		dataEvent = event.find_one({'_id':teamName})
		return x,None,dataEvent


def mainTemplate(serverID,eventName,teamName,discordID,name,age,emailID,passcode = None):
	passcode
	event,dataBase = createEvent(serverID,eventName)
	availableEvents = dataBase.list_collection_names()
	if eventName not in availableEvents :
		tag = 'no such event found'
		return tag ,None

	x,passcode1,dataEvent = teamNameCheck(event,teamName)
	if x == 0:
		event.update_one({"_id": teamName}, {"$push": {
			"discordID":discordID,
			"name":name,
			"age":age,
			"email":emailID	
		}})
		return teamName,passcode1

	else:
		if passcode == None:
			tag = 'enter passcode or team is present'
			return tag
		
		if dataEvent['_id'] == teamName and dataEvent['passcode'] == passcode:
			event.update_many({'_id': teamName}, {'$push': {'discordID':discordID,'name':name,'age':age,'email':emailID }})
		else:
			tag = 'check teamname or password'
			return tag


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