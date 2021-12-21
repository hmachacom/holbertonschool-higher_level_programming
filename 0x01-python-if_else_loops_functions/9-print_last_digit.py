#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        pnum = number % 10
    else:
        pnum = (number * (- 1)) % 10
    print("{:d}".format(pnum), end="")
    return pnum
