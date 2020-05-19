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

// app.use(express.static(__dirname + '/Frontend/NewsWebsite/dist/NewsWebsite'));

// app.get('/',(req,res,next)=>{
//     res.sendFile(path.join(__dirname + '/Frontend/NewsWebsite/dist/NewsWebsite/index.html'));
// });

module.exports = app;