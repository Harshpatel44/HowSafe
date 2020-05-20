const express = require('express')
const router = express.Router()

const path = require('path')
// var dbConnect = require('../databaseConnect')
console.log('in tag file')
router.get('/',function(req, res,next){
  
  var list=[]
  const MongoClient = require('mongodb').MongoClient;
  const uri = "mongodb+srv://root:root@news-jaoot.mongodb.net/test?retryWrites=true&w=majority";
  const client = new MongoClient(uri, { useNewUrlParser: true });

  client.connect(err => {
      const collection = client.db('news').collection('processedTags');
      collection.find({tag:"GeneralNews"}).forEach(function(todo,err){
            //  console.log(todo)
              list.push(todo.content)
           }, function(){
            client.close();
            console.log(JSON.parse(list[0]))
            
            res.json(JSON.parse(list[0]))
           
           })
    });
  
  // res.json(

  //     dbConnect.connect('news','data')
      
      // [
      //   {"name":'ko', "url":""}, 
      //   {"name":'virat', "url":""},
      //   {"name":'kohli', "url":""}, 
      //   {"name":'virat', "url":""},
      //   {"name":'kohli', "url":""}, 
      //   {"name":'virat', "url":""},
      //   {"name":'kohli', "url":""}, 
      //   {"name":'virat', "url":""},
      //   {"name":'kohli', "url":""}, 
      //   {"name":'virat', "url":""},
      //   {"name":'kohli', "url":""}, 
      //   {"name":'virat', "url":""},
      //   {"name":'kohli', "url":""}, 
      //   {"name":'virat', "url":""},
      //   {"name":'kohli', "url":""}, 
      //   {"name":'virat', "url":""},
      //   {"name":'kohli', "url":""}, 
      //   {"name":'virat', "url":""},
      //   {"name":'kohli', "url":""}, 
      //   {"name":'virat', "url":""},
      //   {"name":'kohli', "url":""}, 
      //   {"name":'virat', "url":""},
      //   {"name":'kohli', "url":""}, 
      //   {"name":'virat', "url":""},
      //   {"name":'kohli', "url":""}, 
      //   {"name":'virat', "url":""},
      //   {"name":'kohli', "url":""}, 
      //   {"name":'virat', "url":""},
      //   {"name":'kohli', "url":""}, 
      //   {"name":'virat', "url":""},
      //   {"name":'ko', "url":""}, 
      //   {"name":'virat', "url":""},
      //   {"name":'kohli', "url":""}, 
      //   {"name":'virat', "url":""},
      //   {"name":'kohli', "url":""}, 
      //   {"name":'virat', "url":""},
      // ]
//     )
})

module.exports = router













// router.get('/',(req,res,next)=>{
//   res.send({
//     cats: [{ name: 'lilly' }, { name: 'lucy' }],
//   })
//     console.log('tags post');
//     // res.status(200).json({
//     //     message: "tags recieved get"
//     //     });
// });


// router.post('/',(req,res,next)=>{
//   res.send({
//     cats: [{ name: 'lilly' }, { name: 'lucy' }],
//   })
//     console.log('tags post');
    // res.status(200).json({
    //     message: "tags recieved post"
    // });
// });



