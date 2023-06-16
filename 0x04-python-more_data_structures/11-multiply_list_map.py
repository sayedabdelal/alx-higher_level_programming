#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    mul = map(lambda a: a*number, my_list)
    return list(mul)
