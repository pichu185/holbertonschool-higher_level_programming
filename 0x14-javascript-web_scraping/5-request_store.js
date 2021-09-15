#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const path = process.argv[2];
request(path, function (err, res, body) {
  if (err) console.log(err);
  else {
    fs.writeFile(process.argv[3], body, 'utf-8', function (err) {
      if (err) console.log(err);
    });
  }
});
