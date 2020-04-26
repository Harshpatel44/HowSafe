from wordcloud import WordCloud,STOPWORDS
import DbConnect
import matplotlib

matplotlib.use('Agg')

#class used to generate wordcloud
class Cloud():
    def __init__(self):
        self.title=""
    def PrepareData(self):
        mongo_object, connection=DbConnect.Database.ConnectMongo(DbConnect.Database())
        mongo_object=mongo_object["data"]

        for i in mongo_object.find():
            for j in i["content"]:
                self.title+=j["description"]
        connection.close()
    def generate_graph(self):
        stopwords = set(STOPWORDS)
        wordcloud = WordCloud(width = 1300, height = 600,
                        background_color ='black',
                        stopwords = stopwords,
                        min_font_size = 15).generate(self.title)
        matplotlib.pyplot.figure(figsize = (100, 100), facecolor = None,frameon=False)
        matplotlib.pyplot.imshow(wordcloud)
        matplotlib.pyplot.axis("off")
        matplotlib.pyplot.tight_layout(pad = 0)
        matplotlib.pyplot.savefig('discription.PNG')

cloud=Cloud()
cloud.PrepareData()
cloud.generate_graph()