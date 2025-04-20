"""
Given an array containing only integers, add all the elements and return the binary equivalent of that sum.

If the array contains any non-integer element (e.g. an object, a float, a string and so on), return false.

Note: The sum of an empty array is zero.

[1, 2]      --> "11"
[1, "a", 2] --> false / False (depending on the language)

https://www.codewars.com/kata/559576d984d6962f8c00003c/train/python
"""

def arr2bin(arr):
    if not all(isinstance(a, int) and not isinstance(a, bool) for a in arr):
        return False
    return bin(sum(a for a in arr))[2:]