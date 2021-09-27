#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
        else:
            raise TypeError
    except TypeError:
        return (False)
    return (True)
