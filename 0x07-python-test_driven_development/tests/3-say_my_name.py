#!/usr/bin/python3
"""
The ``3-say_my_name.py`` module
===============================

``3-say_my_name`` supplies two functions, say_my_name().
"""


def say_my_name(first_name, last_name=""):
    """ Returns the concatenated value of supplied arguments

    Args:
        first_name: First name in string format
        last_name: Lastmanme in string format

    Raises:
        TypeError: if fist_name is not a string
        TypeError: if last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    full_name = "My name is " + first_name + " " + last_name
    print(full_name, end="")
    print("")
