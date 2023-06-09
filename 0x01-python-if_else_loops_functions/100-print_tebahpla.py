#!/usr/bin/python3
set = 0
for i in range(ord('z'), ord('a')-1, -1):
    if set == 0:
        print("{:c}".format(i), end="")
        set = 1
    else:
        print("{:c}".format(i - 32), end="")
        set = 0
