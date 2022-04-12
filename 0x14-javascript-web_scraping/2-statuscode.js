#!/usr/bin/node

const request = require('request');
const { argv } = require('process');

request(argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  }
  console.log('code: ' + response.statusCode);
});
