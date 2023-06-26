#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(list_length):
        try:
            if my_list_2[i] == 0:
                res.append(0)
                print("division by 0")
            else:
                res.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            res.append(0)
            print("wrong type")
        except IndexError:
            res.append(0)
            print("out of range")
    return res
