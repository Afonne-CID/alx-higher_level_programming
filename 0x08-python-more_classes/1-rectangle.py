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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.width = width
        self.height = height

        @property
        def width(self):
            return self._width

        @width.setter
        def width(self, value):
            self._value = value

        @property
        def height(self):
            return self._height

        @height.setter
        def height(self, value):
            self._value = value
