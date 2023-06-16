#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_delet = []
    for k, v in a_dictionary.items():
        if v == value:
            key_delet.append(k)

    for i in key_delet:
        del a_dictionary[i]
    return a_dictionary
