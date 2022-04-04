#!/usr/bin/node

const { argv } = require('process');

let newAr = [];
if (argv.length <= 3) {
  console.log(0);
} else {
  newAr = argv.slice(2).map(Number).sort();

  newAr.pop();
  console.log(newAr.pop());
}
