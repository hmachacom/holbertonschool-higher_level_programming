#!/usr/bin/env python3
def uppercase(str):
    for charter in str:
        charter2 = ord(charter)
        if charter2 >= 97 and charter2 <= 122:
            charter2 = chr(ord(charter) - 32)
        else:
            charter2 = charter
        print("{:s}".format(charter2), end="")
    print("")
