#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_len = len(tuple_a)
    b_len = len(tuple_b)

    if a_len >= 2:
        a = tuple_a[0]
        b = tuple_a[1]
    elif a_len == 1:
        a = tuple_a[0]
        b = 0
    else:
        a = 0
        b = 0

    if b_len >= 2:
        c = tuple_b[0]
        d = tuple_b[1]
    elif b_len == 1:
        c = tuple_b[0]
        d = 0
    else:
        c = 0
        d = 0

    new_tuple = (a+c, b+d)
    return new_tuple
