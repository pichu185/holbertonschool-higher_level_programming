#!/usr/bin/node

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const request = require('request');
request(url, function (err, response, body) {
  if (err) console.log(err);
  else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
