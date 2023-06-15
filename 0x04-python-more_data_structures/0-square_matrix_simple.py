#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr2 = []
    for i in matrix:
        sqr1 = []
        for x in i:
            sqr1.append(x * x)
        sqr2.append(sqr1)
    return sqr2
