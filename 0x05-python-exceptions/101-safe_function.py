#!/usr/bin/python3
def safe_function(fct, *args):

    import sys

    try:
        return fct(*args)
    except (ValueError, TypeError, ZeroDivisionError, IndexError) as a:
        sys.stderr.write("Exception: " + str(a) + "\n")
