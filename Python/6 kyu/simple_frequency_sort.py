"""
In this kata, you will sort elements in an array by decreasing frequency of elements. If two elements have the same frequency, sort them by increasing value.

solve([2,3,5,3,7,9,5,3,7]) = [3,3,3,5,5,7,7,2,9]
-- We sort by highest frequency to lowest frequency.
-- If two elements have same frequency, we sort by increasing value.
More examples in test cases.

Good luck!


https://www.codewars.com/kata/5a8d2bf60025e9163c0000bc/train/python
"""

from collections import Counter

def solve(arr):
    a = Counter(arr)
    res = []
    a = sorted(a.most_common(), key=lambda x: (-x[1], x[0]))
    for i, v in a:
        for _ in range(v):
            res.append(i)
    return res