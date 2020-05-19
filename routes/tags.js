const express = require('express');
const router = express.Router();

const path = require('path');

router.get('/',(req,res,next)=>{
    res.send('tags recieved get')
    console.log('tags post');
    res.status(200).json({
        message: "tags recieved get"
        });
});

router.route('/cats').get((req, res) => {
    res.send({
      cats: [{ name: 'lilly' }, { name: 'lucy' }],
    })
  })

router.post('/',(req,res,next)=>{
    res.send('tags recieved get')
    console.log('tags post');
    res.status(200).json({
        message: "tags recieved post"
    });
});



module.exports = router;