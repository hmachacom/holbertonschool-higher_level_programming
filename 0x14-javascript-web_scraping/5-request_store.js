#!/usr/bin/node

const request = require('request');
const { argv } = require('process');
const fs = require('fs');

if (argv[2] && argv[3]) {
  const url = argv[2];
  const file = argv[3];
  request(url, (err, response, body) => {
    if (err) {
      console.log(err);
    }
    try {
      fs.writeFileSync(file, body);
    } catch (err) {
      console.log(err);
    }
  });
}
