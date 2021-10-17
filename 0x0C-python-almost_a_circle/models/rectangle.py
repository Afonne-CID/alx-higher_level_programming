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
        """Print the Rectangle using the "#" character"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            print(self.width * "{}".format('#'))

    def update(self, *args, **kwargs):
        """Assigns an argument to each atrribute of Rectangle

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represents height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            *kwargs (dict): New key/value pairs of attributes
        """
        if args and len(args) != 0:
            cnt = 0
            for arg in args:
                if cnt == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif cnt == 1:
                    self.width = arg
                elif cnt == 2:
                    self.height = arg
                elif cnt == 3:
                    self.x = arg
                elif cnt == 4:
                    self.y = arg
                cnt += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def __str__(self):
        return ("[Rectangle] " + "({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height))
