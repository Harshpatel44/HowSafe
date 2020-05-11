import DbConnect
from NLPFunctions import Functions as func


import datetime
class NltkProcessing():
    def __init__(self):
        self.count=0
        self.dict={}

    # preparing data for language processing. Creating dictionary of different tags.
    def prepareData(self):
        tags,mongo_object,connection=self.findTags()
        for i in tags:
            temp = ""
            for j in mongo_object.find({"tag": i,
                                        "$or":
                                             [
                                                 {"content.date_stamp": str(datetime.datetime.now().date())},
                                                 {"content.date_stamp": str(datetime.datetime.now().date() - datetime.timedelta(days=1))},

                                            ]
                                        }):
                #for k in j:
                for k in j['content']:
                    temp+=str(k['description'])+"<br>"
            self.dict[i]=temp
        connection.close()
        print("PrepareData complete")

    # language processing on prepared data
    def infoExtract(self):
        print("Information Extraction start")
        """
                        Information architecture first 3 steps:
                            1. Sentence tokenization
                            2. Word tokenization
                            3. Pos tag for each word
        """
        mongo_object, connection = DbConnect.Database.connectMongo(DbConnect.Database())
        mongo_object = mongo_object["processedTags"]
        for i in self.dict:
            data=self.dict[i]

            # removed unwanted symbols
            filtered=func.filterSentences(func(),data)

            # split the files
            sentences =filtered.split("<br>")

            twoGrams=func.twoGrams(func(),sentences)


            input()
            # removed stopwords
            stopwords=func.stopWords(func(),sentences)

            # find frequency of words
            frequency = func.oneGrams(func(), stopwords)

            # remove unwanted words
            cleanWords=func.unwantedWordsRemoval(func(),frequency[:70])
            print(cleanWords)

            if(mongo_object.find({"tag":i,"date_stamp":str(datetime.datetime.now().date())}).count()!=0):
                mongo_object.remove({"tag":i,"date_stamp": str(datetime.datetime.now().date())})
                print("data already exists for today, removed")

            mongo_object.insert({"tag":i,"content":repr(cleanWords),"date_stamp":str(datetime.datetime.now().date())})
            print(str(i)+"complete")

    #get all the source tags
    def findTags(self):
        mongo_object, connection = DbConnect.Database.connectMongo(DbConnect.Database())
        mongo_object = mongo_object["data"]
        tags=mongo_object.distinct('tag')
        return tags,mongo_object,connection

nltk_processing=NltkProcessing()
nltk_processing.prepareData()
nltk_processing.infoExtract()

