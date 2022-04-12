#!/usr/bin/node

const request = require('request');
const { argv } = require('process');
const url = argv[2];
if (url) {
  request(url, (err, response, body) => {
    if (err) {
      console.log(err);
    }
    const date = JSON.parse(body);
    const count = { character18: 0 };
    const id = '18';
    for (let x = 0; x < (date.results).length; x++) {
      const num = (date.results[x].characters).map((char) => { return char.indexOf(id); });
      if (num.filter((char) => { return char >= 0; }).length > 0) {
        ++count.character18;
      }
    }
    console.log(parseInt(count.character18));
  });
}
