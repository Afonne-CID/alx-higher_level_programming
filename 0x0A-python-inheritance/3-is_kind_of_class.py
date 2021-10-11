#!/usr/bin/python3
"""Defines a class checking function"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of subclass of a_class

    Args:
        obj: An instance of an object in Python
        a_class: A Class
    """
    return (isinstance(obj, a_class))
