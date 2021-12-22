#!/usr/bin/python3
def remove_char_at(str, n):
    cpstr = ""
    if len(str) >= n and n >= 0:
        for i in str:
            if i != str[n]:
                cpstr += i
    else:
        cpstr = str
    return cpstr
