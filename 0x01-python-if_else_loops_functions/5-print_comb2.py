#!/usr/bin/python3
for abc in range(0, 100):
    if abc < 10:
        aux = "0"
    if abc < 99:
        print("{}{:d}".format(aux, abc), end=", ")
    else:
        print("{:d}".format(abc))
    aux = ""
