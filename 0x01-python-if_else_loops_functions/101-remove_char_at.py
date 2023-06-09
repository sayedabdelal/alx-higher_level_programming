#!/usr/bin/python3
def remove_char_at(str, n):
    # copy of list
    c_str = str[:]
    if n >= 0:
        c_str = c_str[:n] + c_str[n+1:]
        return (c_str)
    else:
        return (c_str)
