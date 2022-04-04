#!/usr/bin/node

const { argv } = require('process');

// print process.argv
if (argv[2] && !(isNaN(parseInt(argv[2])))) {
  const x = parseInt(argv[2]);
  for (let index = 0; index <= x; index++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
