#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for ele in my_list:
            if count == x:
                break
            if isinstance(ele, int):
                print("{:d}".format(ele), end="")
                count += 1
    except (TypeError, ValueError):
        pass
    finally:
        print()
        return count
