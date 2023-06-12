#!/usr/bin/python3
def element_at(my_list, idx):
    len_lst = len(my_list)
    if idx > len_lst or idx < 0:
        return None
    else:
        return (my_list[idx])
