from pymongo import MongoClient

class Database():
    def __init__(self):
        print()
    def ConnectMongo(self):
        connection = MongoClient('localhost', 27017)
        database = connection["news"]
        return database, connection
    def ShowMongo(self,collection):
        mongo_object,connection = self.ConnectMongo()
        mongo_object = mongo_object[str(collection)]
        for x in mongo_object.find():
            print(x)
        connection.close()
