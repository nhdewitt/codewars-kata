"""
Implement a function that receives two integers m and n and generates a sorted list of pairs (a, b) such that m <= a <= b <= n.

The input m will always be smaller than or equal to n (e.g., m <= n)

Example
m = 2
n = 4

result = [(2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

https://www.codewars.com/kata/588e2a1ad1140d31cb00008c/train/python
"""

def generate_pairs(m, n):
    return [(i, j) for i in range(m, n + 1) for j in range(i, n + 1)]