#!/usr/bin/python3
"""Defines a function ``inherits_from()``"""


def inherits_from(obj, a_class):
    """ Returns True if obj is an instance of a subclass

    Args:
        obj: an instance of an object in Python
        a_class: A Class
    """
    return not(type(obj) == a_class)
