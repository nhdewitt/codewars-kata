"""
Find the sum of the digits of all the numbers from 1 to N (both ends included).

Examples
# N = 4
1 + 2 + 3 + 4 = 10

# N = 10
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) = 46

# N = 12
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) + (1 + 1) + (1 + 2) = 51


https://www.codewars.com/kata/527e4141bb2ea5ea4f00072f/train/python
"""

def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def compute_sum(n):
    total = 0
    while n >= 10:
        total += digit_sum(n)
        n -= 1
    return total + (n * (n + 1) // 2)