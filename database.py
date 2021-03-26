import re
import config
import pymongo
clientObj = config.Oauth()
client = clientObj.databaseTOKEN()


def addServerInfo(serverID, serverName, textChannels, Admin, roles):
    """
  Bot connections database creation.
  @params - Discord parameters from client.
  
  """

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
  event = dataBase[eventName]
  return event

def passcodeGen():
	dataBase = client[serverID]
  event = dataBase['passcodes']
	
def teamNameCheck(event,teamName):
		if event.find_one({"_id":teamName}) is None:
    datatoEnter = {
			"_id":teamName
			# 'passcode': 0000
			}
		event.insert_one(datatoEnter)
		event.update_one({"_id": teamName}, {"$set": {'passcode': $floor:{ $multiply: [ { $rand: {} }, 1000 ] }}})
		passcode = event['passcode']
		x = 0
		dataEvent = event.find_one({'_id':teamName})
		return x,passcode,dataEvent
	else:
		x = 1
		return event['teamName']

def emailCheck(email):
  checkedEmail = []

  for emails in email:
      if re.match('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', emails):
          checkedEmail.append(emails)
      else:
          return None
  return checkedEmail

def mainTemplate(serverID,eventName,teamName,discordID,name,age,emailID,passcode = None):

	availableEvents = dataBase.list_collection_names()
	if eventName is not in availableEvents:
		tag = 'no such event found'
		return tag
	event = createEvent(serverID , eventName)
	if emailCheck(emailID) is None:
		tag = 'some error in email'
		return tag
	x,passcode,dataEvent = teamNameCheck(event,teamName)
	if x == 0:
		event.update_one({"_id": teamName}, {"$set": {
			"discordID":discordID,
			"name":name1,
			"age":age,
			"email":emailID	
		}})
		return teamName,passcode

	else:
		if passcode == None:
			tag = 'enter passcode or team is present'
			return tag
		if dataEvent['_id'] == teamName and dataEvent['passcode'] == passcode:
			event.update({'_id': teamName}, {'$push': {'discordID':discordID,'name':name,'age':age,'email':emailID }}
		else:
			tag = 'check teamname or password'
			return tag