#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_lis = []
    for i in my_list:
        if i not in new_lis:
            new_lis.append(i)
    return sum(new_lis)
