#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """Create a student."""
    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name : The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets a dictionary representation of the Student"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
