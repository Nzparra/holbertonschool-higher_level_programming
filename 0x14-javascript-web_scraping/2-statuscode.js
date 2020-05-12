#!/usr/bin/node
const rqs = require('request');
rqs(process.argv[2], function (err, response) {
  if (err == null) {
    console.log('code:' + response.statusCode);
  } else {
    console.log(err);
  }
});
