#!/usr/bin/python3
def roman_to_int(roman_string):
	num_roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
	val = 0
	for letter in range(len(roman_string)):
		if roman_string[letter] in num_roman:
			val += num_roman[roman_string[letter]]
		elif roman_string[letter - 1] and num_roman[roman_string[letter - 1]] < num_roman[roman_string[letter]]:
			val -= num_roman[roman_string[letter - 1]] * 2
	return val