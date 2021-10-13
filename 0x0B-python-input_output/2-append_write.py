#!/usr/bin/python3
"""Defines a function that appends a string to a text file"""


def append_write(filename="", text=""):
    """Appends text to filename and returns number of
       characters read

    Args:
        filename (str): The file to append to
        text (str): The text to append
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
