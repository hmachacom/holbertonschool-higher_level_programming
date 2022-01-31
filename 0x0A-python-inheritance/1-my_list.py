#!/usr/bin/python3
"""class for inherits from list"""


class MyList(list):
    """ class my list"""

    def print_sorted(self):
        """that prints the list, but sorted (ascending sort)"""
        print(sorted(self))
