#!/usr/bin/python3
"""Defines a Rectangle class
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
        if value < 0:
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
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of our Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter of our Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2*(self.__width + self.__height))

    def __str__(self):
        """Returns the area in place of #"""
        if self.__width == 0 or self.__height == 0:
            return ""

        new = []
        for i in range(self.__height):
            [new.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                new.append("\n")
        return ("".join(new))
