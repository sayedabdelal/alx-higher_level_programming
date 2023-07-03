#!/usr/bin/python3
""" This module represents a rectangle """


class Rectangle:
    """Aepresents a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """create this rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is != integer
            ValueError: if size is < zero
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height attribute"""
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
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """Represet rectangle with the character class."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rct = []
        for c in range(self.__height):
            for r in range(self.__width):
                try:
                    rct.append(str(self.print_symbol))
                except Exception:
                    rct.append(type(self).print_symbol)
            if c < self.__height - 1:
                rct.append("\n")
        return "".join(rct)

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print the message when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
