#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number > 0:
    la = number % 10
    nu = number
else:
    la = (((number * (- 1)) % 10) * -1)
    nu = number

if la == 0:
    print("Last digit of {} is {} and is 0".format(number, la))
elif la > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, la))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(nu, la))
