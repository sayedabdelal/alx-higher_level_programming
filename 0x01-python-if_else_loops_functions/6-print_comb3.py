#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if j == 9 and i == 8:
            print("{}{}".format(i, j))
        elif j > i and i != j:
            print("{}{}, ".format(i, j), end="")
