"""
I love Fibonacci numbers in general, but I must admit I love some more than others.

I would like for you to write me a function that, when given a number n (n >= 1 ), returns the nth number in the Fibonacci Sequence.

For example:

   nth_fib(4) == 2
Because 2 is the 4th number in the Fibonacci Sequence.

For reference, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two.

https://www.codewars.com/kata/522551eee9abb932420004a0/train/python
"""

from math import sqrt

def nth_fib(n):
    n -= 1                                          # Adjust n to be 0-indexed
    phi = (1 + sqrt(5)) / 2                         # Golden ratio
    psi = (1 - sqrt(5)) / 2                         # Conjugate of the golden ratio      
    return int((phi ** n - psi ** n) // sqrt(5))    # Binet's formula for Fibonacci numbers cast to int