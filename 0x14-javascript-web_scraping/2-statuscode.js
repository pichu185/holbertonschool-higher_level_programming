#!/usr/bin/node

const req = require('request');
req(process.argv[2], function (err, response) {
        if (err) console.log(err);
        else console.log('code: ' + response.statusCode);
});
