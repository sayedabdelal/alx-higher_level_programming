#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_lst = []
    for i in my_list:
        if i != search:
            n_lst.append(i)
        else:
            n_lst.append(replace)
    return n_lst
