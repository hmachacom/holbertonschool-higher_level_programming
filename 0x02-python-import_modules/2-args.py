#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    long = len(argv)
    if long == 1:
        print("0 arguments.")
    elif long > 1:
        if long == 2:
            print("{} argument:".format(long - 1))
        else:
            print("{} arguments:".format(long - 1))
        for argc in range(1, long):
            print("{}: {}".format(argc, argv[argc]))
