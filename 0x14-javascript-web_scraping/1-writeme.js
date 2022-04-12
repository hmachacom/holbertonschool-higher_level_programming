#!/usr/bin/node

const fs = require('fs');
const { argv } = require('process');
if (argv[2]) {
  try {
    fs.writeFileSync(argv[2], argv[3]);
  } catch (err) {
    console.log(err);
  }
}
