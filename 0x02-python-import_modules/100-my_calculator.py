#!/usr/bin/python3

import sys
import calculator_1 as calc

if __name__ == "__main__":
    long = len(sys.argv)
    operator = ["+", "/", "*", "-"]
    argc = sys.argv
    if long != 4 and argc[2] != "*":
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif not(sys.argv[2] in operator):
        print("Unknown operator. Available operators: +, -, * and / ")
        exit(1)
    else:
        clac = ([calc.add, calc.div, calc.mul, calc.sub])
        selct = 0
        for op in operator:
            if op == sys.argv[2]:
                result = clac[selct](int(sys.argv[1]), int(sys.argv[3]))
                print("{} + {} = {}".format(sys.argv[1], sys.argv[3], result))
                exit(0)
            selct += 1
