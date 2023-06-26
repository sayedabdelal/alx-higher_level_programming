#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(list_length):
        try:
            dev = (my_list_1[i] / my_list_2[i])

        except TypeError:
            print("wrong type")
            dev = 0
        except ZeroDivisionError:
            dev = 0
            print("division by 0")
        except IndexError:
            dev = 0
            print("out of range")
        finally:
            res.append(dev)
    return res
