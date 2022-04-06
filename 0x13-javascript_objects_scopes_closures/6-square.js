#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      let num = this.height;
      for (; num; num--) {
        console.log(`${c}`.repeat(this.width));
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
