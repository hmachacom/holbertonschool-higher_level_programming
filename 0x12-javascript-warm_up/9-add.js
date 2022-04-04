#!/usr/bin/node

const { argv } = require('process');

// print process.argv
function add (a, b) {
  return a + b;
}
if (argv[2] && argv[3]) {
  console.log(add(parseInt(argv[2]), parseInt(argv[3])));
} else {
  console.log('NaN');
}
