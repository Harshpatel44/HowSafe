const express = require('express');
const path  =  require('path');
const port = process.env.PORT || 3000;

const app = require('./app');

app.listen(port,function(){
    console.log('Server started')
});






// const express = require('express');
// const path  =  require('path');
// const app1 = express();
// app1.use(express.static(__dirname + '/Frontend/NewsWebsite/dist/NewsWebsite'));

// app1.get('/',(req,res,next)=>{
//     res.sendFile(path.join(__dirname + '/Frontend/NewsWebsite/dist/NewsWebsite/index.html'));
// });

// // const server = http.createServer(app);

// app1.listen(3000,function(){
//     console.log('started')
// });
