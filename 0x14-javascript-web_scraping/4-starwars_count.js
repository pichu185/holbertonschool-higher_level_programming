#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (err, res, body) {
  if (err) console.log(err);
  else if (res.statusCode === 200) {
    const films = JSON.parse(body).results;
    let pichu = 0;
    for (const film in films) {
      const characters = films[film].characters;
      for (const char in characters) {
        if (characters[char].includes('18')) {
          pichu++;
        }
      }
    }
    console.log(pichu);
  }
});
