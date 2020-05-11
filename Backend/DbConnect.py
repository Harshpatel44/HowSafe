from pymongo import MongoClient

#class used to connect to database
class Database():
    def __init__(self):
        print()
    def connectMongo(self):
        connection = MongoClient('localhost', 27017)
        database = connection["news"]
        return database, connection

    def showMongo(self,collection):
        mongo_object,connection = self.connectMongo()
        mongo_object = mongo_object[str(collection)]
        for x in mongo_object.find():
            print(x)
        connection.close()
