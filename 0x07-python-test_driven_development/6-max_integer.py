#!/usr/bin/python3
""" Module to find the maximum integer in a list
"""


def max_integer(my_list=[]):
    """ returns the max integer in a list

    Args:
        list: a list
    Returns:
        TypeError: if argument is not a list
        TypeError: if all elements of a list are not int
    """
    if not isinstance(my_list, list) or not all(my_list):
        raise TypeError("list must be a list")
    if len(my_list) == 0:
        return (None)
    highest = 0
    for i in my_list:
        if i > highest:
            highest = i
    return (highest)
