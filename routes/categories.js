const express = require('express')
const router = express.Router()

const path = require('path')

router.route('/').get((req,res)=>{
    res.json(
        [
            {"name":"General News"},
            {"name":"Sports News"},
            {"name":"Entertainment News"},
            {"name":"Technology News"},
            {"name":"Science News"},
            {"name":"Business News"},
        ]
    )
})

module.exports = router