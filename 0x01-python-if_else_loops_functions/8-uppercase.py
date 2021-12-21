#!/usr/bin/env python3
def uppercase(str):
    str2 = ""
    for charter in str:
        charter2 = ord(charter)
        if charter2 in range(97, 123):
            str2 += chr(ord(charter) - 32)
        else:
            str2 += charter
    print("{}".format(str2))
