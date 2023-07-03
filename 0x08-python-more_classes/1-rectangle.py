#!/usr/bin/python3
"""
This module represents a rectangle.
"""

class Rectangle:
    """
    Represents a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is negative.
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """
        Get the height attribute of the rectangle.
        """
        return self.__height


    @height.setter
    def height(self, value):
        """
        Set the height attribute of the rectangle.

        Args:
            value (int): The value to set as the height.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        
    @property
    def width(self):
        """
        Get the width attribute of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width attribute of the rectangle.

        Args:
            value (int): The value to set as the width.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
