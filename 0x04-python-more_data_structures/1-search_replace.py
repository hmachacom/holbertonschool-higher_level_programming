#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if search in my_list:
        new_list = []
        for i in my_list:
            if search == i:
                new_list.append(replace)
            else:
                new_list.append(i)
    else:
        new_list = my_list
    return new_list
