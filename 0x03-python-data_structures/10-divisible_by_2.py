#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    long = len(my_list)
    new_list = []
    if long == 0:
        return new_list
    for i in range(0, long):
        if my_list[i] % 2:
            new_list.append(False)
        else:
            new_list.append(True)
    return new_list
