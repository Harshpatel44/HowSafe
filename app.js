const express = require('express');
var cors = require('cors')

const app = express();
app.use(cors())

const tags = require('./routes/tags')
const news = require('./routes/news')
const categories = require('./routes/categories')

app.use('/tags',tags)
app.use('/news',news)
app.use('/categories',categories)

const MongoClient = require('mongodb').MongoClient;
const uri = "mongodb+srv://root:root@news-jaoot.mongodb.net/test?retryWrites=true&w=majority";
const client = new MongoClient(uri, { useNewUrlParser: true });
client.connect(err => {
  const collection = client.db("news").collection("dataSources");
  
  collection.find({}).toArray(function(err,todos){  
      console.log(todos)
    //   todos.forEach(function(todo){
    //     console.log(todo)
    //   });
  })
  
  client.close();
});


// app.use(express.static(__dirname + '/Frontend/NewsWebsite/dist/NewsWebsite'));

// app.get('/',(req,res,next)=>{
//     res.sendFile(path.join(__dirname + '/Frontend/NewsWebsite/dist/NewsWebsite/index.html'));
// });

module.exports = app;