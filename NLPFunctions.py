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

