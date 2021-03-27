import pymongo
import pandas as pd
from pymongo import MongoClient
def mongotoCsv(serverID,eventName):
    db_link = "mongodb+srv://BeLazy:BeLazy@cluster0.csr3d.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    client = pymongo.MongoClient(db_link)
    dataBase = client[serverID]
    collection = dataBase[eventName]
    cursor = collection.find({'defId':"1"})
    df = pd.DataFrame(list(cursor))
    return df
