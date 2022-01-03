#!/usr/bin/python3
def max_integer(my_list=[]):
    long = len(my_list)
    if long > 0:
        maX = my_list[0]
        for i in my_list:
            if i > maX:
                maX = i
    elif long == 0:
        return 0
    return maX
