#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  let len = list.length - 1;
  while (len >= 0) {
    newList.push(list[len]);
    len--;
  }
  return newList;
};
