#!/usr/bin/python3
"""
The ``4-print_square.py`` module
================================

``4-print_square`` supplies one function, print_square()
"""


def print_square(size):
    """ Prints a square with the character '#'

    Args:
        size: the size length of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
        TypeError: if size is a float and is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size, end="")
        print("")
