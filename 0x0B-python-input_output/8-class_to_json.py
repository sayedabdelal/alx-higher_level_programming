#!/usr/bin/python3
"""This module defines a Python class-to-JSON function"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure"""
    return obj.__dict__
