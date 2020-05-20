

exports.connect=function(dbName, collectionName){
    jsonFile=[]
    const MongoClient = require('mongodb').MongoClient;
    const uri = "mongodb+srv://root:root@news-jaoot.mongodb.net/test?retryWrites=true&w=majority";
    const client = new MongoClient(uri, { useNewUrlParser: true });
    const collection = client.db("news").collection("dataSources");
    
    client.connect(err => {
        collection.find({}).toArray(function(err,todos){  
          jsonFile = todos
          })
        client.close();
      });
    return jsonFile
}
