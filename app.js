const express = require('express');
var cors = require('cors')
const app = express();

const tags = require('./routes/tags');

app.use(cors());
app.use('/tags',tags);

// app.use(express.static(__dirname + '/Frontend/NewsWebsite/dist/NewsWebsite'));

// app.get('/',(req,res,next)=>{
//     res.sendFile(path.join(__dirname + '/Frontend/NewsWebsite/dist/NewsWebsite/index.html'));
// });

module.exports = app;