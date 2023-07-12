#!/usr/bin/python3
"""
    This module returns the list of available attributes
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return dir(obj)
