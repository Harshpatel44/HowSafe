import DbConnect
import nltk
from nltk.tokenize import word_tokenize

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
        for i in self.dict:
            data=self.dict[i]
            sentences = data.split("<br>")
            words = [word_tokenize(sent) for sent in sentences]
            words_tag = [nltk.pos_tag(word) for word in words]

            temp=""
            #pos tagging
            for j in words_tag:
                for name, tag in j:
                    if (tag == "NNP" or tag == "NN" or tag == "NNS"):
                        temp += str(name) + " "

            mongo_object, connection = DbConnect.Database.ConnectMongo(DbConnect.Database())
            mongo_object = mongo_object["processed_data"]
            mongo_object.insert({"tag":i,"content":temp})
            print(str(i)+"complete")
        print("Information Extraction complete")
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

