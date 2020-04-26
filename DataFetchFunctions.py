__author__ = 'harsh'
import requests
import json
import datetime
import time
import DbConnect


## Fetch class is to fetch the data from the sources and store it to mongodb
class Fetch():
    #constructor
    def __init__(self):
        self.flag=True

    #print sources
    def ShowCollection(self,collection):
        DbConnect.Database.ShowMongo(DbConnect.Database(),collection)

    #storing data to mongodb
    def dataAdd(self,list):
        mongo_object,connection=DbConnect.Database.ConnectMongo(DbConnect.Database())
        mongo_object = mongo_object['data']

        """list is the current fetched data. this is to check if the current fetched data already exists in the db. if it exists
           then, we will not store it. we will match current news title with all the news titles of the same day.
        """

        if (mongo_object.count() == 0): #checks if it is empty or not.
            mongo_object.insert(list)
            print("found count=0, all news inserted")
        else:  #does not allow duplicate news to be stored.
            for i1 in list:
                if(mongo_object.count({"tag":i1['tag']})==0):
                    mongo_object.insert(i1)
                    print("new tag news found, all news inserted")
                else:
                    for j1 in mongo_object.find({ "$or":[{"content.date_stamp": str(datetime.datetime.now().date())},{"content.date_stamp": str(datetime.datetime.now().date() - datetime.timedelta(days=1))}],"tag":i1['tag']}):
                        for i2 in i1['content']:
                            flag=True
                            for j2 in j1['content']:
                                if(i2['title'] == j2['title']):
                                    flag=False
                            if(flag==True):
                                print(i1['tag'])
                                mongo_object.update({'tag': i1['tag']}, {'$push': {'content': i2}})
                                print('added news: ',i2['title'])
        connection.close()
        return 'data updated'

    #main program which handles fetching sources, fetching data from sources, storing in mongo
    def RunEngine(self):
        mongo_object,connection=DbConnect.Database.ConnectMongo(DbConnect.Database())
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
        #print(data['articles'][1]['title'])
        try:
            for i in data['articles']:
                data_dictionary = {}
                data_dictionary['title']=i['title']
                data_dictionary['content']=i['content']
                data_dictionary['description']=i['description']
                data_dictionary['author']=i['author']
                data_dictionary['publishedAt']=i['publishedAt']
                data_dictionary['url']=i['url']
                data_dictionary['urlToImage']=i['urlToImage']
                data_dictionary['date_stamp']=str(datetime.datetime.now().date())
                data_dictionary['time_stamp']=str(datetime.datetime.now().time())
                list.append(data_dictionary)
        except:
            pass
        return {"tag":url[0],"content":list}


fetch = Fetch()
while 1:
    print(fetch.RunEngine())
    time.sleep(300)


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

