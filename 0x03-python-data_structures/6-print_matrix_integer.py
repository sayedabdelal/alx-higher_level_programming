#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, colum in enumerate(row):
            print("{:d}".format(colum), end="")
            if i < (len(row) - 1):
                print(" ", end="")
        print()
