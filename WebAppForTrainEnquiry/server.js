// app.js
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const myapikey = 'uhl4cf3b5y'
app.use(bodyParser.urlencoded({ extended: false }));
var request = require('request');

app.get('/', (request, response) =>  response.sendFile(`${__dirname}/index.html`));

app.post('/api/data', (request, response) => {
  const postBody = request.body;
  trainNo = postBody.data[0];
  sourceSC = postBody.data[1];
  destSC = postBody.data[2];
  date  =  postBody.data[3];
  pref = postBody.data[4];
  quota = postBody.data[5];

    url = 'https://api.railwayapi.com/v2/check-seat/train/'+trainNo+'/source/'+sourceSC+'/dest/'+destSC+'/date/'+date+'/pref/'+pref+'/quota/'+quota+'/apikey/'+myapikey+'/';
request(url ,{json:true},(err,res,body) => {
	if (err) {return console.log(err);}
  console.log(body.url);
  console.log(body.explanation);
	
}); 
   


response.send(postBody);
});

app.listen(3000, () => console.info('Application running on port 3000'));

