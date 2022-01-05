#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    my_dic = a_dictionary.copy()
    for i in my_dic:
        if my_dic[i] == value:
            del a_dictionary[i]
    return a_dictionary
