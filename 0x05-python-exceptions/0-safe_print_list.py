#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # know the len of the list
    length = 0
    for _ in my_list:
        length += 1
    try:
        for i in range(0, x):
            print(my_list[i], end="")
    except IndexError:
        x = length
    finally:
        print()
        return x
