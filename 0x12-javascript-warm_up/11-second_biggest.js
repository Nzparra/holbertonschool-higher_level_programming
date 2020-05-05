#!/usr/bin/node
const numbers = [];
let n = 0; let i;
for (i = 2; i < process.argv.length; i++) {
  if (Number.isNaN(parseInt(process.argv[i])) === false) {
    numbers[i - 2] = parseInt(process.argv[i]);
  }
}
if (numbers.length > 1) {
  n = Math.max.apply(null, numbers);
  i = numbers.indexOf(n);
  numbers.splice(i, 1);
  n = Math.max.apply(null, numbers);
}
console.log(n);
