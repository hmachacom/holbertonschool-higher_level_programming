#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    import sys

    long = len(sys.argv)
    count = 0
    if long == 1:
        print("0")
    elif long > 1:
        for argc in range(1, long):
            count += int(argv[argc])
        print("{}".format(count))
