#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lst_n = number % 10
else:
    lst_n = number % -10
if lst_n > 5:
    print(f"Last digit of {number} is {lst_n} and is greater than 5")
elif lst_n < 6 and lst_n != 0:
    print(f"Last digit of {number} is {lst_n} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {lst_n} and is 0")
