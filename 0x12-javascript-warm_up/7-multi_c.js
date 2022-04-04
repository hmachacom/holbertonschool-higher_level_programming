#!/usr/bin/node

const { argv } = require('process');

// print process.argv
if (argv[2] && !(isNaN(parseInt(argv[2])))) {
  let num = parseInt(argv[2]);
  for (; num; num--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
