#!/usr/bin/node

const list = require('./100-main').list;

console.log(list);

const newList = list.map(function (x, idx){
	return x * idx;
})

console.log(newList);