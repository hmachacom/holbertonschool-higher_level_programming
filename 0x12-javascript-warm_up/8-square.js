#!/usr/bin/node

const { argv } = require('process');

// print process.argv
if (argv[2] && !(isNaN(parseInt(argv[2])))) {
  let num = parseInt(argv[2]);
  for (; num; num--) {
    console.log('X'.repeat(parseInt(argv[2])));
  }
} else {
  console.log('Missing size');
}
