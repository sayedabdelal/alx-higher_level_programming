#!/usr/bin/python3
"""This module contains a class to serve as base for other classes"""


class Base:
    """Represents base of all classes created """

    __nb_objects = 0

    def __init__(self, id=None):
        """Manage id attribute in all your future classes """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
