#!/usr/bin/node
const fs = require('fs');

const aArg = fs.readFileSync(process.argv[2]).toString();
const bArg = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], aArg + bArg);
