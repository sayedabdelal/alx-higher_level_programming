#!/usr/bin/python3
"""This module defines a file-writing function."""


def append_write(filename="", text=""):
    """append a string to a text file and return number of chr """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
