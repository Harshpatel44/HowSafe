__author__ = 'harsh'
import requests
import json
import time
from pymongo import MongoClient

class Fetch():
    #constructor
    def __init__(self):
        self.flag=True

    #adds the sources
    def SourcesAdd(self,source,tag):
        mongo_object,connection=self.ConnectMongo()
        mongo_object = mongo_object['data_sources']
        mongo_object.insert({"tag":tag ,"url":source })
        connection.close()

    #connects to mongo
    def ConnectMongo(self):
        connection = MongoClient('localhost', 27017)
        database = connection["news"]
        return database,connection

    #print sources
    def ShowMongo(self,collection):
        mongo_object,connection = self.ConnectMongo()
        mongo_object = mongo_object[str(collection)]
        for x in mongo_object.find():
            print(x)
        connection.close()

    #storing data to mongodb
    def dataAdd(self,list):
        mongo_object,connection=self.ConnectMongo()
        mongo_object = mongo_object['data']
        mongo_object.insert_many(list)
        connection.close()
        return 'data added'

    #main program which handles fetching sources, fetching data from sources, storing in mongo
    def RunEngine(self):
        mongo_object,connection=self.ConnectMongo()
        mongo_object = mongo_object['data_sources']
        main_list = []
        for x in mongo_object.find():
            main_list.append(self.FetchFromUrl([ x['tag'],x['url'] ]))
        connection.close()
        response=self.dataAdd(main_list)
        return response

    #program to fetch data from sources
    def FetchFromUrl(self,url):
        list=[]
        response = requests.get(url[1])
        data = json.loads(response.text)
        for i in data['articles']:
            data_dictionary = {}
            data_dictionary['title']=i['title']
            data_dictionary['content']=i['content']
            data_dictionary['description']=i['description']
            data_dictionary['author']=i['author']
            data_dictionary['publishedAt']=i['publishedAt']
            data_dictionary['url']=i['url']
            data_dictionary['urlToImage']=i['urlToImage']
            list.append(data_dictionary)
        print(list)
        return {"tag":url[0],"content":list}


fetch = Fetch()
while 1:
    time.sleep(30)
    print(fetch.RunEngine())
#fetch.SourcesAdd("http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=0fc0e9b54d5d4389b807d66a86fcee50","GoogleNews")
#fetch.SourcesAdd("http://newsapi.org/v2/top-headlines?country=in&apiKey=0fc0e9b54d5d4389b807d66a86fcee50","TheHindu")
#fetch.ShowMongo('data')
#fetch.ShowMongo('data_sources')





"""
Accessing the data: 

Its a list of data sources. each item in a list is a data from specific source.
the sources can be accessed by object[0]['GoogleNews']
this dictionary values is a list of data which can be accessed as object[0]['GoogleNews'][0] 
--> each data contains following values: title, content, discription, author, publishedAt, url, urlToImage
"""

