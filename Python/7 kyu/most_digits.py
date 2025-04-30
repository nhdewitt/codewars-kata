"""
Find the number with the most digits.

If two numbers in the argument array have the same number of digits, return the first one in the array.

https://www.codewars.com/kata/58daa7617332e59593000006/train/python
"""

def find_longest(arr):
    longest_size = [str(a) for a in arr]
    longest = len(sorted(longest_size, key=len)[-1])
    for _, v in enumerate(arr):
        if len(str(v)) == longest:
            return v