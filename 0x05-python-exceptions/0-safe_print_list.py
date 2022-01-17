#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    long = 0
    for i in my_list:
        long += 1
    try:
        for inten in range(x):
            my_list[inten]
        for inten in range(x):
            print("{}".format(my_list[inten]), end="")
        print()
        return x
    except IndexError:
        for inten in range(long):
            print("{}".format(my_list[inten]), end="")
        print()
        return long
