#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
let occurrences;
for (occurrences in dict) {
  newDict[[dict[occurrences]]] = [];
}
for (occurrences in dict) {
  newDict[[dict[occurrences]]].push(occurrences);
}
console.log(newDict);
