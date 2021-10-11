#!/usr/bin/python3
"""Defines a class MyList that inherits from ``list``"""


class MyList(list):
    """Inherits and extends ``list``"""
    def print_sorted(self):
        """Prints a list in sorted (ascending) order"""
        print(sorted(self))
