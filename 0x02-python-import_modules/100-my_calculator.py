#!/usr/bin/python3

import sys
import calculator_1 as calc

if __name__ == "__main__":
    long = len(sys.argv)
    operator = {"+": calc.add, "/": calc.div, "*": calc.mul, "-": calc.sub}
    argc = sys.argv
    if long != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif not(sys.argv[2] in operator):
        print("Unknown operator. Available operators: +, -, * and / ")
        exit(1)
    else:
        result = operator[sys.argv[2]](int(sys.argv[1]), int(sys.argv[3]))
        a = sys.argv[1]
        op = sys.argv[2]
        print("{} {} {} = {}".format(a, op, sys.argv[3], result))
        exit(0)
