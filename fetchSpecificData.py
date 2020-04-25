from pymongo import MongoClient
def ConnectMongo():
    connection = MongoClient('localhost', 27017)
    database = connection["news"]
    data=database['data']
    for i in data.find({"time_stamp": "GoogleNews"}):
        #print(i['content'])
        #input()
        print(i['content'][0]['title'])
    return database, connection

ConnectMongo()