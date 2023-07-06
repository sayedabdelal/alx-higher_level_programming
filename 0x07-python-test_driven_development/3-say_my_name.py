#!/usr/bin/python3
"""
This is a module that print my name

"""


def say_my_name(first_name, last_name=""):
    """This is function print name


    Args:
        first_name: This is string that has a frist name
        last_name: This is string that has a last name
    
    Raises:
        TypeError if frist name or last name not string

    """

    if not isinstance(first_name, str) :
            raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
