"""
Create a function that receives a string consists of only digit characters ('0' to '9'), and returns the lowest product of 4 consecutive digits within that string.

This should only work if the number has 4 digits or more. If not, return "Number is too small" instead.

Example
"123456789" --> 24    // 1*2*3*4
"35" --> "Number is too small"

https://www.codewars.com/kata/554e52e7232cdd05650000a0/train/python
"""

from math import prod

def lowest_product(num):
    if len(num) < 4:
        return "Number is too small"
    smallest = float("inf")
    for i in range(len(num) - 3):                           # sliding window, compare to smallest, change if lower
        p = prod(list(map(int, num[i:i + 4])))
        if p < smallest:
            smallest = p
    
    return smallest