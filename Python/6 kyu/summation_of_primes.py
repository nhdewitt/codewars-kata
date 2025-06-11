"""
Summation Of Primes
The sum of the primes below or equal to 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below or equal to the number passed in.

https://www.codewars.com/kata/59ab0ca4243eae9fec000088/train/python
"""

import math

def sieve(n):
    is_composite = [False] * (n + 1)
    limit = int(math.sqrt(n))
    primes = []
    
    for i in range(2, limit + 1):
        if is_composite[i]:
            continue
        for j in range(i * i, n + 1, i):
            is_composite[j] = True

    for i in range(2, n + 1):
        if not is_composite[i]:
            primes.append(i)
    
    return primes

def summation_of_primes(primes):
    return sum(sieve(primes))           # sieve up to and including primes and return the sum