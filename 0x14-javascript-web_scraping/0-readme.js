#!/usr/bin/node

const fs = require('fs');
const { argv } = require('process');

if (argv[2]) {
  try {
    const date = fs.readFileSync(argv[2], 'utf-8');
    console.log(date);
  } catch (err) {
    console.log(err);
  }
}

/*
if (argv[2]) {
  fs.open(argv[2], 'r', function (err, data) {
    if (err) {
      return console.log(err);
    }
      const buffer = Buffer.alloc();
    fs.read(data, buffer, 0, buffer.length, 0, function (error, date) {
      if (err) {
        return console.log(error);
      }
      console.log(buffer.toString());
    });
    fs.close(data, function (err) {
      if (err) {
        console.log(err);
      }
    });
  });
}
 */
