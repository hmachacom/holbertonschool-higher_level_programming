#!/usr/bin/python3
def roman_to_int(roman_string):
    num_roman = 0
    if roman_string and isinstance(roman_string, str):
        values = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev = 0
        for i in roman_string[::-1]:
            value2 = values[i]
            if value2 >= prev:
                num_roman += value2
            else:
                num_roman -= value2
            prev = value2
    return num_roman
