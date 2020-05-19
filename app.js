const express = require('express');
const app = express();

const tags = require('./routes/tags');

app.use('/tags',tags);

// app.use(express.static(__dirname + '/Frontend/NewsWebsite/dist/NewsWebsite'));

// app.get('/',(req,res,next)=>{
//     res.sendFile(path.join(__dirname + '/Frontend/NewsWebsite/dist/NewsWebsite/index.html'));
// });

module.exports = app;