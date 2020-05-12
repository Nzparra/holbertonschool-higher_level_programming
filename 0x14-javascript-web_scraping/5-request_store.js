#!/usr/bin/node
const rqs = require('request');
const fs = require('fs');
rqs(process.argv[2], function (err, responsei, body) {
  if (err == null) {
    fs.writeFileSync(process.argv[3], body);
  }
});
