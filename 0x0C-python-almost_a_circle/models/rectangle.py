#!/usr/bin/python3
"""Defines a Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle

    Inherits from the Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor

        Args:
            width (int): Rectangle's width
            height (int): Rectangle's height
            x (int): instance attribute x
            y (int): instance attribute y
            id (int): Rectangle's identity

        Raises:
            TypeError: If height or width is not an int
            TypeError: If either x or y is not an int
            ValueError: If height or width is <= 0
            ValueError: If either x or y is under 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves Rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of Rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves Rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of Rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        for i in range(self.height):
            print(self.width * "{}".format('#'))
