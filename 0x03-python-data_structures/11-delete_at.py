#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    long = len(my_list)
    if long == 0:
        return my_list
    elif idx > long - 1 or idx < 0:
        return my_list
    del my_list[idx]
    return my_list
