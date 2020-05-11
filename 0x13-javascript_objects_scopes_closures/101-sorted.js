#!/usr/bin/node
const dic = require('./101-data').dict;
const newd = {};
Object.keys(dic).map(function (key, index) {
  if (newd[dic[key]] === undefined) {
    newd[dic[key]] = [];
  }
  newd[dic[key]].push(key);
});
console.log(newd);
