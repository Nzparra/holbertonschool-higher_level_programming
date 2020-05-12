#!/usr/bin/node
const rqs = require('request');
rqs(process.argv[2], function (err, response, body) {
  if (err == null) {
    const json = JSON.parse(body);
    const task = {};
    for (let i = 0; i < json.length; i++) {
      if (json[i].completed === true) {
        if (task[json[i].userId] === undefined) {
          task[json[i].userId] = 0;
        }
        task[json[i].userId]++;
      }
    }
    console.log(task);
  }
});
