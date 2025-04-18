"""
You have two arrays in this kata, every array contains unique elements only. Your task is to calculate number of elements in the first array which are also present in the second array.

https://www.codewars.com/kata/561046a9f629a8aac000001d/train/python
"""

def match_arrays(v, r):
    return len(set(v) & set(r))