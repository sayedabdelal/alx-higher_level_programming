#!/usr/bin/python3
"""This module defines a file-writing function."""


def write_file(filename="", text=""):
    """write a string to a text file and return number of chr """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
