#!/usr/bin/python3
def weight_average(my_list=[]):
    numerator = 0
    denominator = 0

    for item in my_list:
        a, b = item
        numerator += a * b
        denominator += b
    if denominator == 0:
        return 0
    else:
        return numerator / denominator
