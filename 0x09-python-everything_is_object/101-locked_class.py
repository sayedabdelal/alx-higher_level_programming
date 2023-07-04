#!/usr/bin/python3
"""This defines a locked class"""


class LockedClass:
    """
    Prevents user from dynamically creating only attribute is called first_name
    """

    __slots__ = ["first_name"]
