#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (Number.isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    let box = '';
    for (let j = 0; j < num; j++) {
      box += 'X';
    }
    console.log(box);
  }
}
