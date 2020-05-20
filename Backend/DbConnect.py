from pymongo import MongoClient

#class used to connect to database
class Database():
    def __init__(self):
        print()
    def connectMongo(self):
        connection = MongoClient(
            "mongodb://root:root@news-shard-00-00-jaoot.mongodb.net:27017,news-shard-00-01-jaoot.mongodb.net:27017,news-shard-00-02-jaoot.mongodb.net:27017/test?ssl=true&replicaSet=News-shard-0&authSource=admin&retryWrites=true&w=majority")
        database = connection.news
        return database, connection

    def showMongo(self,collection):
        mongo_object,connection = self.connectMongo()
        mongo_object = mongo_object[str(collection)]
        for x in mongo_object.find():
            print(x)
        connection.close()
