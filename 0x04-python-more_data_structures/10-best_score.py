#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        val = 0
        kye = ""
        for i in a_dictionary:
            if a_dictionary[i]:
                if a_dictionary[i] > val:
                    val = a_dictionary[i]
                    kye = i
        if kye not in a_dictionary:
            return None
        else:
            return kye
