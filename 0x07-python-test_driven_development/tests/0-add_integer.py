#!/usr/bin/python3
"""
This is the 0-add_integer module.

The 0-add_integer module supplies one function, add_integer(). For example,
"""


def add_integer(a, b=98):
    """ Returns the sum of a and b.

    a must be an integer or float, and,
    b must be an integer or float.

    when float is supplied for either both or one of the parameters,
    we must type cast to integer.

    E.g:
    >>> add_integer(10, 7)
    17
    """
    if (not isinstance(a, int) and isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
