#!/usr/bin/node

const request = require('request');
const { argv } = require('process');

if (argv[2]) {
  const url = 'https://swapi-api.hbtn.io/api/films/';
  request(url, (err, response, body) => {
    if (err) console.log(err);

    const date = JSON.parse(body);

    (date.results[argv[2] - 1].characters).forEach(element => {
      request(element, (err, response, body) => {
        if (err) console.log(err);
        const character = JSON.parse(body);
        console.log(character.name);
      });
    });
  });
}
