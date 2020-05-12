#!/usr/bin/node
const rqs = require('request');
rqs('https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/', function (err, responsei, body) {
  if (err == null) {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
