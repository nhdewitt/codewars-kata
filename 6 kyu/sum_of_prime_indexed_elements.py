"""
In this Kata, you will be given an integer array and your task is to return the sum of elements occupying prime-numbered indices.

The first element of the array is at index 0.

Good luck!

If you like this Kata, try:

Dominant primes. It takes this idea a step further.

Consonant value

https://www.codewars.com/kata/59f38b033640ce9fc700015b/train/python
"""

import math

def isprime(n):
    if n == 0 or n == 1:
        return False
    limit = int(math.sqrt(n))
    for i in range(2, limit + 1):
        if str(i)[-1] in [0,2,4,5,6,8]:
            continue
        if (n % i) == 0:
            return False
    return True

def total(arr):
    return sum(a for i, a in enumerate(arr) if isprime(i))