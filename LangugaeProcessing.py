import DbConnect
class ProcessData():
    def __init__(self):
        self.count=0
    #perform processing on each tag
    def task(self):
        tags,mongo_object,connection=self.FindTags()

        for i in tags:
            for j in mongo_object.find({"tag": i})[0]["content"]:
                print(j['description'])

            input()
    #get all the source tags
    def FindTags(self):
        mongo_object, connection = DbConnect.Database.ConnectMongo(DbConnect.Database())
        mongo_object = mongo_object["data"]
        tags=mongo_object.distinct('tag')
        return tags,mongo_object,connection
process_data=ProcessData()
process_data.task()
#print(process_data.count)

