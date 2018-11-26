// app.js
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const myapikey = 'uhl4cf3b5y'
app.use(bodyParser.urlencoded({ extended: false }));
var req = require('request');

app.get('/', (request, response) =>  response.sendFile(`${__dirname}/index.html`));

app.post('/api/data', (request, response) => {
console.log(request);
  const postBody = request.body;
  trainNo = postBody.data[0];
  sourceSC = postBody.data[1];
  destSC = postBody.data[2];
  date  =  postBody.data[3];
  pref = postBody.data[4];
  quota = postBody.data[5];

URL = 'https://api.railwayapi.com/v2/check-seat/train/'+trainNo+'/source/'+sourceSC+'/dest/'+destSC+'/date/'+date+'/pref/'+pref+'/quota/'+quota+'/apikey/'+myapikey+'/';

 var options = {
    url: URL,
    method: 'GET'
  };  

req(options, function(err, res, body) {
    if (err) console.error(err);
    else {
      data = JSON.parse(body);
	console.log(data);
response.json({Data:data});
    }
  });

//response.json(postBody);
});

app.listen(3000, () => console.info('Application running on port 3000'));

