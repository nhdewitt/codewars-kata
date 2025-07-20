"""
Given a list of random integers, return the integer used to initialize the random number generator (the "seed") (0 <= n < 10000)

The input list is comprised of the first 10 random integers between 0 and 100 (inclusive) produced after initializing the random number generator from the random module.

Examples
input: [17, 72, 97, 8, 32, 15, 63, 97, 57, 60]
expected: 1

input: [99, 56, 14, 0, 11, 74, 4, 85, 88, 10]
expected: 1234

https://www.codewars.com/kata/5a106ce7ffe75f4c200000f7/train/python
"""

import random

def find_random_seed(lst):
    for i in range(10000):
        check = []
        random.seed(i)
        for _ in range(10):
            check.append(random.randint(0, 100))
        if check == lst:
            return i