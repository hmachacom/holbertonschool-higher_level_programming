#!/usr/bin/node
module.exports = function (x, theFunction) {
	console.log(x);
	while (x) {
		theFunction();
		console.log(x);
		x--;
	}
}