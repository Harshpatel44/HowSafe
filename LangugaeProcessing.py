import DbConnect
from NLPFunctions import Functions as func


import datetime
class NltkProcessing():
    def __init__(self):
        self.count=0
        self.dict={}

    # preparing data for language processing. Creating dictionary of different tags.
    def PrepareData(self):
        tags,mongo_object,connection=self.FindTags()

        for i in tags:
            temp = ""
            for j in mongo_object.find({"tag": i})[0]["content"]:
                temp+=str(j['description'])+"<br>"
            self.dict[i]=temp
        connection.close()
        print("PrepareData complete")

    # language processing on prepared data
    def InfoExtract(self):
        print("Information Extraction start")
        """
                        Information architecture first 3 steps:
                            1. Sentence tokenization
                            2. Word tokenization
                            3. Pos tag for each word
        """
        mongo_object, connection = DbConnect.Database.ConnectMongo(DbConnect.Database())
        mongo_object = mongo_object["processedTags"]
        for i in self.dict:
            data=self.dict[i]

            #removed unwanted symbols
            filtered=func.FilterSentences(func(),data)

            #split the files
            sentences =filtered.split("<br>")

            #removed stopwords
            stopwords=func.StopWords(func(),sentences)

            # find frequency of words
            frequency = func.FrequencyWords(func(), stopwords)

            #remove unwanted words
            cleanWords=func.unwantedWordsRemoval(func(),frequency[:70])
            print(cleanWords)


            if(mongo_object.find({"tag":i,"date_stamp":str(datetime.datetime.now().date())}).count()!=0):
                print("data already exists for today")
                mongo_object.remove({"tag":i,"date_stamp": str(datetime.datetime.now().date())})
                print("removed")

            mongo_object.insert({"tag":i,"content":cleanWords,"date_stamp":str(datetime.datetime.now().date())})
            print(str(i)+"complete")

        # connection.close()
        # print("Information Extraction complete")

    #get all the source tags
    def FindTags(self):
        mongo_object, connection = DbConnect.Database.ConnectMongo(DbConnect.Database())
        mongo_object = mongo_object["data"]
        tags=mongo_object.distinct('tag')
        return tags,mongo_object,connection

nltk_processing=NltkProcessing()
nltk_processing.PrepareData()
nltk_processing.InfoExtract()
#print(process_data.count)

