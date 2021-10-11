#!/usr/bin/python3
"""2-is_same_class module"""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class

    Args:
        obj: an instance of an object in Python
        a_class: A class in Python
    """
    return (type(obj) == a_class)
