#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lst_cpy = my_list.copy()
    if idx < 0 or idx > (len(my_list) - 1):
        return (lst_cpy)
    else:
        lst_cpy[idx] = element
        return (lst_cpy)
