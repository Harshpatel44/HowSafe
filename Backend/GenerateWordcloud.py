from wordcloud import WordCloud,STOPWORDS
import DbConnect
import datetime
import matplotlib
matplotlib.use('Agg')

#class used to generate wordcloud
class Cloud():
    def __init__(self):
        self.tag=[]
        self.content=[]

    #preparing data for wordcloud
    def prepareData(self):
        mongo_object, connection=DbConnect.Database.ConnectMongo(DbConnect.Database())
        mongo_object=mongo_object["processedTags"]

        for i in mongo_object.find():
            self.tag.append(i["tag"])
            self.content.append(i["content"])
        connection.close()

    #generating wordcloud
    def generateGraph(self):
        stopwords = set(STOPWORDS)
        for i in zip(self.tag,self.content):
            if(i[1]!=""):
                wordcloud = WordCloud(width = 600, height = 600,
                                background_color ='black',
                                stopwords = stopwords,
                                min_font_size = 15).generate(i[1])
                matplotlib.pyplot.figure(figsize = (50, 50), facecolor = None,frameon=False)
                matplotlib.pyplot.imshow(wordcloud)
                matplotlib.pyplot.axis("off")
                matplotlib.pyplot.tight_layout(pad = 0)
                matplotlib.pyplot.savefig("wordclouds/"+str(i[0])+str(datetime.datetime.now().date())+'.PNG')
                del wordcloud
            print(str(i[0])+" wordcloud complete")

cloud=Cloud()
cloud.prepareData()
cloud.generateGraph()