"""
Find the sum of the odd numbers within an array, after cubing the initial integers. The function should return undefined/None/nil/NULL if any of the values aren't numbers.

Note: Booleans should not be considered as numbers.

https://www.codewars.com/kata/580dda86c40fa6c45f00028a/train/python
"""

def cube_odd(arr):
    if not all(type(x) is int for x in arr):
        return None
    return sum(x ** 3 for x in arr if x % 2 != 0)