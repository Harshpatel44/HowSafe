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
        filtered=re.subn('[^a-zA-Z\.\,\s(\<br\>)][\xa0\r\n(\)]*',' ',data)
        filtered=re.subn('\.',' . ',filtered[0])
        filtered = re.subn('<br>', ' <br> ', filtered[0])
        return filtered[0]

    #returns word tokens
    def WordTokenize(self,data):
        words = [word_tokenize(sent) for sent in data]
        return words

    #to return a specific pos words
    def posWords(self,data,pos_tag):
        temp=[]
        words_tag = [nltk.pos_tag(word) for word in data]
        
        for j in words_tag:
            for name, tag in j:
                if (tag == pos_tag):
                    temp.append(name)
                else:
                    pass
        return temp
    def unwantedWordsRemoval(self, data):
        # we will create a set of all the words that are unwanted and then will subtract from main list.

        # adding all the words from the text file to the set.
        unwanted_words=set()
        for i in ["JJ","NN","NNS"]:
            with open("NLPFiles/"+str(i)+".txt") as f:
                # pos_words=self.posWords(data, str(i))
                unwanted_words.update(f.read().split())

        # adding some POS_TAG words to the set.
        for i in ["VBD", "IN", "DT"]:
            pos_words = self.posWords(data, str(i))
            unwanted_words.update(pos_words)

        print(len(data))
        print(len(unwanted_words))
        # Now we subtract it from the main set.
        clean_words = set(data) - unwanted_words
        print(len(clean_words))
        print(clean_words)
        input()




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

# string="India News  The home ministry on Friday permitted all shops in residential and market complexes outside municipal limits and all neighbourhood, standalone shops a.<br>Maharashtra, which is witnessing the fastest spread of the Coronavirus disease in India, has doubled its number of positive cases in the last one week."
# print(Functions.FilterSentences(Functions(),string))