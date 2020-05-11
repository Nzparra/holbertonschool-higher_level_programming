#!/usr/bin/node
const list = require('./100-data').list;
const newl = list.map(function (num, index) {
  return index * num;
});
console.log(list);
console.log(newl);
