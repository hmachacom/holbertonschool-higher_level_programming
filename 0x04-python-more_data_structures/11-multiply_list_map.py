#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda a, b: number * a, my_list, my_list))
