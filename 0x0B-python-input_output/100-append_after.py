#!/usr/bin/python3
"""This module defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line to string
    """
    n_text = ""
    with open(filename) as r:
        for line in r:
           n_ text += line
            if search_string in line:
                n_text += new_string
    with open(filename, "w") as w:
        w.write(n_text)
