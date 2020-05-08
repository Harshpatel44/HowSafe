import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

# This class contains functions required for language processing.
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
        filtered=re.subn('[^a-zA-Z\.\,\s<>][\xa0\r\n]*',' ',data)
        filtered=re.subn('[\.]',' . ',filtered[0])
        filtered = re.subn('<br>', ' <br> ', filtered[0])
        d=re.findall("\(",filtered[0])
        return filtered[0]


    #returns word tokens
    def WordTokenize(self,data):
        words = [word_tokenize(sent) for sent in data]
        return words


    #to return a specific pos words
    def posWords(self,data,pos_tag):
        # removing frequencies
        data=[word for freq,word in data]
        #pos_tagging
        words_tag = nltk.pos_tag(data)

        temp=[]
        for j in words_tag:
            name,tag = j
            if (tag == pos_tag):
                temp.append(name)
        return temp


    # removing unwanted words from the data
    def unwantedWordsRemoval(self, data):
        # we will create a set of all the words that are unwanted and then will subtract from main set.

        # adding all the words from the text file to the unwanted_words set.
        unwanted_words=set()
        for i in ["JJ","NN","NNS","others"]:
            with open("NLPFiles/"+str(i)+".txt") as f:
                # pos_words=self.posWords(data, str(i))
                unwanted_words.update(f.read().split())

        # adding some POS_TAG words to the unwanted_words set.
        for i in ["VBD", "IN", "DT"]:
            pos_words = self.posWords(data, str(i))
            unwanted_words.update(pos_words)

        #creating set of main data
        main_set=set()
        for freq,name in data:
            main_set.add(name)
        # Now we subtract it from the main set.
        clean_words = main_set - unwanted_words
        return clean_words


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


# string="India News  The home ministry on Friday permitted all shops in residential and market complexes outside municipal limits and all neighbourhood, standalone shops a.<br>Maharashtra, which is witnessing the fastest spread of the Coronavirus disease in India, has doubled its number of positive cases in the last one week."
# print(Functions.FilterSentences(Functions(),string))