"""
Write a function that given an integer n >= 0, returns an array of n ascending length subarrays, all filled with 1s.

0 => [ ]
1 => [ [1] ]
2 => [ [1], [1, 1] ]
3 => [ [1], [1, 1], [1, 1, 1] ]


https://www.codewars.com/kata/515f51d438015969f7000013/train/python
"""

def pyramid(n):
    res = list()
    for i in range(1, n + 1):
        res.append([1] * i)
    return res