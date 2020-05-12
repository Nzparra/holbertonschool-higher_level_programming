#!/usr/bin/node
const rqs = require('request');
let n = 0;
rqs(process.argv[2], function (err, responsei, body) {
  if (err == null) {
    const json = JSON.parse(body);
    const results = json.results;
    for (let i = 0; i < results.length; i++) {
      const char = results[i].characters;
      for (let j = 0; j < char.length; j++) {
        if (char[j].search('18') > 0) {
          n++;
        }
      }
    }
    console.log(n);
  }
});
