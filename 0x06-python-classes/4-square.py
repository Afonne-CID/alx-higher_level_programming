#!/usr/bin/python3
"""Writing a class that defines a square"""


class Square:
    """A class to represent a square"""
    def __init__(self, size=0):
        """Defining a private instance attribute, size

        Args:
            size(int): the size of our square
        """
        self.size = size

    @property
    def size(self):
        """retrieves our size attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the value of our private size attribute,
        having confirmed size is and int and greater than zero,
        otherwise, an error is raised
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """A public instance area that returns the current
        square area
        """
        return (self.__size * self.__size)
