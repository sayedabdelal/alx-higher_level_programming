#!/usr/bin/env python3
def no_c(my_string):
    new_string = ""
    for i in my_string:
        if i.lower() != 'c':
            new_string += i
        else:
            continue

    return (new_string)
