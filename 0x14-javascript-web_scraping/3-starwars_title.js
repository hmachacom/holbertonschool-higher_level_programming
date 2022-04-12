#!/usr/bin/node

const request = require('request');
const { argv } = require('process');

request('https://swapi-api.hbtn.io/api/films/', (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const date = JSON.parse(body);
  console.log(date.results[argv[2] - 1].title);
});
