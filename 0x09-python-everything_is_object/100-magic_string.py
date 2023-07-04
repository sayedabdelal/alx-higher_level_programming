#!/usr/bin/python3
def magic_string():
    magic_string.num = getattr(magic_string, 'num', 0) + 1
    return ", ".join(["BestSchool" for n in range(magic_string.num)])
