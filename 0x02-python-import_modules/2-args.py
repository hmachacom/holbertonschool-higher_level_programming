#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    long = len(sys.argv)
    if long == 1:
        print("0 arguments.")
    elif long > 1:
        print("{} arguments:".format(long - 1))
        for argc in range(1, long):
            print("{:d}: {}".format(argc, sys.argv[argc]))
