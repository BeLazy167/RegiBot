import pymongo
import pandas as pd
from pymongo import MongoClient
from pymongo import cursor
def main(serverID,eventName):
    db_link = "mongodb+srv://BeLazy:BeLazy@cluster0.csr3d.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    client = pymongo.MongoClient(db_link)
    dataBase = client[serverID]
    collection = dataBase[eventName]
    cursor = collection.find({'defId':"1"})
    return cursor
    
def mongoToCsv(serverID,eventName):
    cursor = main(serverID,eventName)
    df = pd.DataFrame(list(cursor))
    df.to_csv(f'{eventName}.csv')
    return f'{eventName}.csv'

def totalParticipant(serverID,eventName):
    cursor = main(serverID,eventName)
    lenx = 0
    for obj in cursor:
        lenx = lenx + len(obj['discordID'])
    return lenx


