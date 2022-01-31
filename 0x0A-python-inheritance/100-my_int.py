#!/usr/bin/python3
""" class int :::"""


class MyInt(int):
    """ class int ::::"""

    def __eq__(self, l):
        """:::validation instance"""
        return super().__ne__(l)

    def __ne__(self, l):
        """validation inverted"""
        return super().__eq__(l)
