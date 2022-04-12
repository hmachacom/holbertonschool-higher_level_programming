#!/usr/bin/node

const fs = require("fs");
const { argv } = require('process');


dat1 = fs.open(argv[2], "r", (err, file) => {
   if (err) throw err;
	 fs.readFile(file, (err, data) => {
	   if (err) throw err;
	  const dat1 = data.toString();
	});
	
});

console.log(dat1);
let dat2;
fs.open(argv[3], "r", (err, file) => {
	if (err) throw err;
	fs.readFile(file, (err, data) => {
		if (err) throw err;
		dat2 = data.toString();
	});
});
console.log(dat2);