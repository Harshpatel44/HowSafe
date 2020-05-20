import DbConnect

key="0fc0e9b54d5d4389b807d66a86fcee50"

sources_list=[
    ["http://newsapi.org/v2/top-headlines?country=in&apiKey=0fc0e9b54d5d4389b807d66a86fcee50","Top20"],
    ["http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=0fc0e9b54d5d4389b807d66a86fcee50","GoogleNews"],
    ["http://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=0fc0e9b54d5d4389b807d66a86fcee50","GeneralNews"],
    ["http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=0fc0e9b54d5d4389b807d66a86fcee50","BusinessNews"],
    ["http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=0fc0e9b54d5d4389b807d66a86fcee50","ScienceNews"],
    ["http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=0fc0e9b54d5d4389b807d66a86fcee50","SportsNews"],
    ["http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=0fc0e9b54d5d4389b807d66a86fcee50","TechnologyNews"],
    ["http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=0fc0e9b54d5d4389b807d66a86fcee50","EntertainmentNews"],
    ["http://newsapi.org/v2/top-headlines?sources=financial-times&apiKey=0fc0e9b54d5d4389b807d66a86fcee50","FinanceNews"]
]

#Sources class is used to add sources, show sources links.
class Sources():
    def __init__(self):
        pass

    #add sources to mongo
    def SourcesAdd(self, source, tag):
        mongo_object, connection = DbConnect.Database.connectMongo(DbConnect.Database())
        mongo_object = mongo_object['dataSources']
        mongo_object.insert({"tag": tag, "url": source})
        connection.close()

    #print sources
    def ShowCollection(self,collection):
        DbConnect.Database.showMongo(DbConnect.Database(),collection)


sources=Sources()
for i in sources_list:
    sources.SourcesAdd(i[0],i[1])

sources.ShowCollection("dataSources")