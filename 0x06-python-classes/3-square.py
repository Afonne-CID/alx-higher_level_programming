#!/usr/bin/python3
"""Writing a class that defines a square"""


class Square:
    """A class to represent a square"""
    def __init__(self, size=0):
        """Defining a private instance attribute, size

        Args:
            size(int): the size of our square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """A public instance area that returns the current square area"""
        return (self.__size ** 2)
