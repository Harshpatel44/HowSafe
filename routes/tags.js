const express = require('express')
const router = express.Router()

const path = require('path')
var dbConnect = require('../databaseConnect')

router.route('/').get((req, res) => {
  res.json(
      dbConnect.connect('news','data')
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
    )
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



