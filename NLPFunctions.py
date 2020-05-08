import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

class Functions:
    def __init__(self):
        pass

    # takes sentences as input and returns dictionary of frequency of words
    def FrequencyWords(self, data):
        dict = {}
        for i in data:
            for j in i:
                if (j not in dict):
                    dict[j] = 1
                else:
                    dict[j] += 1
        sortedList=[(dict[key], key) for key in dict]
        sortedList.sort()
        sortedList.reverse()
        return sortedList

    #removes unneccesary texts and symboles
    def FilterSentences(self,data):
        filtered=re.subn('[^a-zA-Z0-9\.\,\s(\<br\>)][\xa0\r\n(\)]*',' ',data)
        return filtered[0]

    #returns word tokens
    def WordTokenize(self,data):
        words = [word_tokenize(sent) for sent in data]
        return words

    def pos_tags_removal(self,data):
        temp=[]
        words_tag = [nltk.pos_tag(word) for word in data]
        print(words_tag)
        input()
        """
        to keep: JJS
        to remove: VBD, IN, DT,
        lockdown
        """
        for j in words_tag:
            for name, tag in j:
                #if (tag == "NNP" or tag == "NN" or tag == "NNS"):
                if (tag == "NNS"):
                    print(name+" "+tag)
                    # temp.append(name)
                else:
                    pass
                    # temp.append(name)
        print(temp)
    # takes sentences as input and returns a list of list of stop-words
    def StopWords(self, data):
        stop_words = set(stopwords.words("english"))

        words=self.WordTokenize(data)
        filtered_lists = []
        for i in words:
            temp = []
            for w in i:
                if w not in stop_words:
                    temp.append(w)
            filtered_lists.append(temp)
        return filtered_lists

    def remove_keys(self,data):
        list=[',','.','number','rate',')','(','?','also','new','in','total','as','a','non','one','says','without','way',
              'toll','tally','days','far','li','last','fresh','set','rose','per','open','month','hours']