

exports.connect=function(dbName, collectionName){
    var jsonFile=[]
    console.log('reached here')
    const MongoClient = require('mongodb').MongoClient;
    const uri = "mongodb+srv://root:root@news-jaoot.mongodb.net/test?retryWrites=true&w=majority";
    const client = new MongoClient(uri, { useNewUrlParser: true });
    
    
    client.connect(err => {
        const collection = client.db(dbName).collection(collectionName);
        collection.find({}).toArray(function(err,todos){  
            // console.log(todos)
          jsonFile = todos
          })
        client.close();
      });
      console.log(jsonFile)
      return jsonFile
}
