#!/usr/bin/python3
roman_num = {
    'I': 1,
    'V': 5,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000
}


def roman_to_int(roman_string):
    # isinstance check string or not
    if isinstance(roman_string, str) or roman_string is None:
        return 0

    sum = 0
    nums = [roman_num[i] for i in roman_string for k in roman_num if k == i]

    for i in range(len(nums) - 1):
        if nums[i] >= nums[i + 1]:
            sum += nums[i]
        else:
            sum -= nums[i]
    # Add the value of the last numeral
    sum += nums[-1]
    return sum
