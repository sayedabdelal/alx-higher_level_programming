#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    unq = list(set(my_list))
    # sum all list
    for i in unq:
        sum += i
    return sum
