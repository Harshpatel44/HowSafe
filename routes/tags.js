const express = require('express');
const router = express.Router();

const path = require('path');


router.route('/').get((req, res) => {
  res.json(
      [{"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'ko', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},]
  )
})














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



module.exports = router;