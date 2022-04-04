#!/usr/bin/node

const { argv } = require('process');

// print process.argv
if (!argv[2] || argv.length === 3) {
  console.log(0);
} else {
  const newAr = argv.slice(2).sort();
  newAr.pop();
  console.log(parseInt(newAr[newAr.length - 1]));
}
