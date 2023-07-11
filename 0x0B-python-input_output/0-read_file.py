#!/usr/bin/python3
""" This module defines a text file-reading function """


def read_file(filename=""):
    """ This Read text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
