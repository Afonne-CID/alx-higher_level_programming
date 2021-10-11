#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Represents a base geometry"""

    def area(self):
        """Raises an excepton"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an int

        Args:
            name (str): A name
            value (int): An int argument

        Raises:
            TypeError: if value is not an int
            ValueError: if value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
