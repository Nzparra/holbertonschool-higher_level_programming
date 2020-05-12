#!/usr/bin/node
const rqs = require('request');
rqs('https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/', function (err, responsei, body) {
  if (err == null) {
    const json = JSON.parse(body);
    const char = json.characters;
    for (let i = 0; i < char.length; i++) {
      rqs(char[i], function (err, response, body) {
        if (err == null) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
