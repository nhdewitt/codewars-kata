"""
We need a function prime_bef_aft() that gives the largest prime below a certain given value n,

befPrime or bef_prime (depending on the language),

and the smallest prime larger than this value,

aftPrime/aft_prime (depending on the language).

The result should be output in a list like the following:

prime_bef_aft(n) == [befPrime, aftPrime]
If n is a prime number it will give two primes, n will not be included in the result.

Let's see some cases:

prime_bef_aft(100) == [97, 101]

prime_bef_aft(97) == [89, 101]

prime_bef_aft(101) == [97, 103]
Range for the random tests: 1000 <= n <= 200000

(The extreme and special case n = 2 will not be considered for the tests. Thanks Blind4Basics)

Happy coding!!

https://www.codewars.com/kata/560b8d7106ede725dd0000e2/train/python
"""

import math
import bisect

class Sieve:
    def __init__(self, limit):
        self.limit = limit
        self.is_composite = [False] * (self.limit + 1)
        self.primes = []
        
        limit = int(math.sqrt(self.limit))
        
        for i in range(2, limit + 1):
            if self.is_composite[i]:
                continue
            for j in range(i * i, self.limit + 1, i):
                self.is_composite[j] = True
                
        for i in range(2, self.limit + 1):
            if not self.is_composite[i]:
                self.primes.append(i)
    
    def is_prime(self, n):
        return not self.is_composite[n]
    
    def neighbors(self, n):
        idx = bisect.bisect_left(self.primes, n)
        lower, upper = 0, 0
        if (idx > 0) and (self.primes[idx - 1] < n):
            lower = self.primes[idx - 1]
        if (idx < len(self.primes)):
            if self.primes[idx] == n:
                upper = self.primes[idx + 1]
            else:
                upper = self.primes[idx]
        return [lower, upper]

def prime_bef_aft(num):
    s = Sieve(200_000)
    return s.neighbors(num)