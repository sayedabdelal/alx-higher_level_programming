#!/usr/bin/python3
def max_integer(my_list=[]):
    le_n = len(my_list)
    if le_n == 0:
        return "None"
    else:
        big = my_list[0]  # Initialize big with the first element
        for i in range(1, le_n):
            if my_list[i] > my_list[i + 1]:
                big = my_list[i]

            return (big)
