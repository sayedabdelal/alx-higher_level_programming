#!/usr/bin/python3
class Rectangle:
    """this represents a rectangle"""
    """Initializing
        Args:
            width: Know the width of the rectangle
            height: Know the height of the rectangle
        Raises:
            TypeError: if size != int
            ValueError: if size is <0
        """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """retrse width attribute"""
        return self.__width

    @property
    def height(self):
        """ Set width attr"""
        return self.__height

    @width.setter
    def width(self, value):
        """retrse height attr"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return the the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if [self.__width, self.__height] == [0, 0]:
            return 0
        return (self.__height + self.__width) * 2
