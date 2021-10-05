#!/usr/bin/python3
"""This is the ``0-rectangle`` module
which defines a Rectangle class
"""


class Rectangle:
    """Represents a Rectagle class"""

    def __init__(self, width=0, height=0):
        """Instance of a rectangle

        Args:
            width (int): Width of new rectangle
            height (int): Height of new rectangle
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """gets and sets the width of our Rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """height attribute getter and setter"""
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
