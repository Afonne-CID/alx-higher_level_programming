#!/usr/bin/python3
"""Defines a Rectangle class
"""


class Rectangle:
    """Represents a Rectagle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instance of a rectangle

        Args:
            width (int): Width of new rectangle
            height (int): Height of new rectangle
        """
        type(self).number_of_instances += 1
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
            [new.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                new.append("\n")
        return ("".join(new))

    def __repr__(self):
        """Returns the __str__ representation"""
        str_1 = str(self.__width)
        str_2 = str(self.__height)
        new = "Rectangle(" + str_1 + ", " + str_2 + ")"
        return (new)

    def __del__(self):
        """indicates deletion and decrement instance count"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area

        Args:
            rect_1 (Rectangle): First Rectangle
            rect_2 (Rectangle): Second Rectangle

        Raises:
            TypeError: if rect_1 not a Rectangle
            TypeError: if rect_2 not a Rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be na instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
