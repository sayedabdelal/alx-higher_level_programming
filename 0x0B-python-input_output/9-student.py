#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """Create a student."""
    def __init__(self, first_name, last_name, age):
        """Create a new student"""
        first_name = self.first_name
        last_name = self.last_name
        age = self.age

    def to_json(self):
        """Gets a dictionary representation of the Student"""
        self.__dict__
