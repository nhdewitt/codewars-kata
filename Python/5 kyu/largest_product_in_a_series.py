"""
Complete the method so that it'll find the greatest product of five consecutive digits in the given string of digits.

For example: the greatest product of five consecutive digits in the string "123834539327238239583" is 3240.

The input string always has more than five digits.

Adapted from Project Euler.

https://www.codewars.com/kata/529872bdd0f550a06b00026e/train/python
"""

import numpy as np

def greatest_product(st):
    highest = 0
    for i in range(9, 0, -1):                                       # starting with 9, find slices of 5 consecutive numbers starting with that digit
        for j, s in enumerate(st):
            if int(s) == i:
                if len(st[j:j + 5]) == 5:                           # make sure it's len(5) and not at the end of the string
                    consec = list(int(s) for s in st[j:j + 5])      # group together the numbers
                    check = np.prod(consec)                         # check the product
                    if check > highest:                             # compare to current largest
                        highest = check
    return highest