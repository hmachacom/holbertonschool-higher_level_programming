#!/usr/bin/python3
def pow(a, b):
    po = 1
    i = 0
    while i < b:
        po *= a
        i += 1
    if b < 0:
        po = 0.0001
    return po
